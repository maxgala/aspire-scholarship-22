import os
from app import app
from flask import flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
import re
import numpy as np
import cv2
import pytesseract
import difflib
from dictionary import kwlist
from pytesseract import Output
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys

# that path of pytesseract installed
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# formats of images that are acceptable
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

dictionary = []


def allowed_file(filename):
    ''' check the format of image uploaded'''
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

   
# load "upload.html" when the program starts
@app.route('/')
def upload_form():
    return render_template('upload.html')





@app.route('/', methods=['POST'])
def upload_image():
    # uploaded files are stores in request.files
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    # written word in input box can be gotten by request.form
    #WordInHeader = request.form['wordInHeader']
    #wordInBody = request.form['wordInBody']

    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')  
        
        return redirect(request.url)
    # get the name of image that is uploaded and store in filename variable
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # save uploaded image in the path UPLOAD_FOLDER = 'static/uploads/'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # show message to users
        flash('Image successfully uploaded')
        filePath = 'static/uploads/' + filename

        specificWords,outputSearchHeader = main(filePath)
        
        # remove the uploaded image
        # os.remove('static/uploads/' + filename)
       
        # convert the output of api to json and return it
        response=jsonify({ "Header": outputSearchHeader,"Body": specificWords 

                       })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    # if an user uploads the image with the format except png, jpg, jpeg, gif
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)


def createBorder(img):
    '''create a border around the image in order to increase the ocr accuracy'''
    row, col = img.shape[:2]
    bottom = img[row - 2:row, 0:col]
    mean = cv2.mean(bottom)[0]

    bordersize = 20
    border = cv2.copyMakeBorder(
        img,
        top=bordersize,
        bottom=bordersize,
        left=bordersize,
        right=bordersize,
        borderType=cv2.BORDER_CONSTANT,
        value=[mean, mean, mean]
    )

    return img


def removeEmptyStringInList(list2):
    ''' remove " " in a list'''
    # removing empty strings
    list2 = list(filter(None, list2))
    ' '.join(list2).split()
    #while ("" in list):
        #list.remove("")
    return list2 



def SplitNumberText(list):
    ''' split number from text in a string'''
    newList = []
    for i in range(len(list)):
        newList.append(re.split('(\d+)', list[i]))
        newList = removeEmptyStringInList(newList)

    return newList


def listToString(s):
    ''' convert a list to string using join() function '''
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


def flattenNestedList(nestedList):
    ''' Converts a nested list to a flat list '''
    flatList = []
    # Iterate over all the elements in given list
    for elem in nestedList:
        # Check if type of element is list
        if isinstance(elem, list):
            # Extend the flat list by adding contents of this element (list)
            flatList.extend(flattenNestedList(elem))
        else:
            # Append the elemengt to the list
            flatList.append(elem)
    return flatList


def checkSpellWord(list):
    ''' correct inaccurate spelling'''

    processedWord = []
    for x in range(len(list)):
        word = list[x]
        outputSpellChecker = listToString(difflib.get_close_matches(word, kwlist)).split()
        length = len(outputSpellChecker)
        if (length == 0):
            processedWord.append(word)
        if (length == 1):
            processedWord.append(outputSpellChecker)
        if (length > 1):
            for x in range(length):
                if outputSpellChecker[x] == word:
                    processedWord.append(outputSpellChecker[x])
                break

    list = flattenNestedList(processedWord)
    return list


def detectAngleImage(preprocessedImage):
    '''detect the angle of images'''
    osd = pytesseract.image_to_osd(preprocessedImage)
    angleImg = re.search('(?<=Rotate: )\d+', osd).group(0)
    return angleImg


def rotate_bound(image, angle):
    '''rotate the image to be horizontal'''
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))


def resizeImg(img):
    '''resize the image
    Gets the image
    Returns the resized image'''
	#calculate the image size
    width, height = img.shape[0:2]
    h = int(height * 0.6)
    w = int(width * 0.6)
	#resize the image
    resizedImg = cv2.resize(img, (h, w))
    return resizedImg


def convertRGBToGrayImg(img):
    """Convert RGB to Gray image
    Gets the RGB image
    Returns gray image"""
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return grayImg



def convertListToString(org_list, seperator='\n'):
    """ Convert list to string, by joining all item in list with given separator.
    eturns the concatenated string """
    return seperator.join(org_list)


#def serachWord(list, serachwordInBody):
    """Search the word
    Gets the list and a word
    Returns all serached words in a list"""
    """specificWords = []
    stringsAfterSemicolon = []
    if len(serachwordInBody) != 0:
        for match in list:
            if serachwordInBody in match:
                specificWords.append(match)
        if len(specificWords) == 0:
            specificWords.append("string is not in this document")
    return specificWords"""




  


def convertImageToWord(readyImageToProcess):
    """onvert preprocessImage to text"""
	#output:string
    d = pytesseract.image_to_data(readyImageToProcess, output_type=Output.DICT, lang="fas")
	
	#output:text
    # d = pytesseract.image_to_strings(readyImageToProcess,lang="fas")
	
    return d['text']


def SearchInHeader(readyImageToProcess):
    d = pytesseract.image_to_data(readyImageToProcess, output_type=Output.DICT, lang="fas")
    keys = list(d.keys())
    n_boxes = len(d['text'])
    specificWords = []
    #full_str = convertListToString(d['text'])
    #printInFile(full_str)
    dic={}
    for i in range(n_boxes):
        if int(d['conf'][i]) > 40:
            text = d['text'][i]
            if ':' in text:
                """(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                (x2, y2, w2, h2) = (d['left'][i + 1], d['top'][i + 1], d['width'][i + 1], d['height'][i + 1])
                img = cv2.rectangle(readyImageToProcess, (x, y), (x + w, y + h), (0, 255, 0), 1)
                img = cv2.rectangle(readyImageToProcess, (x2 - 7, y2), (x2 + w2 + 14, y2 + h2), (0, 255, 0), 1) """
                # print(d['text'][i-1],d['text'][i],d['text'][i + 1])
                # print(d['text'][i-1],d['text'][i],d['text'][i + 1])
                if d['text'][i - 1] == "تاریخ" or "ت ار ی خ" in d['text'][i - 1]:
                    document_date = "date"
                    d_number = d['text'][i + 1]
                    specificWords.append(document_date)
                    specificWords.append( d_number)
                    #print(document_date, ":", d_number)
                elif d['text'][i - 1] == "سند":
                    if d['text'][i - 2] == "شرح":
                        documnet_description = "doc_description"
                        d_description = d['text'][i + 1] + ' ' + d['text'][i + 2] + ' ' + d['text'][i + 3]
                        specificWords.append(documnet_description)
                        specificWords.append(d_description)
                        #print(documnet_description, ":", d_description)
                    elif d['text'][i - 2] == "شماره":
                        document_number = "doc_id"
                        d_number = d['text'][i + 1]
                        specificWords.append(document_number )
                        specificWords.append(d_number )
                        #print(document_number, ":", d_number)
                elif d['text'][i - 1] == "عطف":
                    turning_number = "reference_id"
                    t_number = d['text'][i + 1]
                    specificWords.append(turning_number)
                    specificWords.append( t_number)
                    #print(turning_number, ":", t_number)
    
    dic={specificWords[0]:specificWords[1],specificWords[2]:specificWords[3],specificWords[4]:specificWords[5],specificWords[6]:specificWords[7]}


    return dic


def postprocessImage(readyImageToProcess):

    #ocr pahse
    ListWords = convertImageToWord(readyImageToProcess)
	
	#remove empty strings
    ListWithoutEmptyString = removeEmptyStringInList(ListWords)
   
   #correct misspelled words
    checkedList = checkSpellWord(  ListWithoutEmptyString)
   
    #return importants words in header of image
    wordHeader=SearchInHeader(readyImageToProcess)
    return checkedList,wordHeader


def preprocessImage(preprocessedImage):
    # height, width = calSizeImage(preprocessedImage)
    angleImg = detectAngleImage(preprocessedImage)
    rotatedImg = rotate_bound(preprocessedImage, int(angleImg))
    resizedImg = resizeImg(rotatedImg)
    # borderImage=createBorder(resizedImg)
    grayImg = convertRGBToGrayImg(resizedImg)
    return grayImg


def main(filePath):
    inputImage = cv2.imread(filePath, 2)
    readyImageToProcess = preprocessImage(inputImage)
    specificWords,outputSearchHeader = postprocessImage(readyImageToProcess)
    return specificWords,outputSearchHeader


if __name__ == "__main__":
    
    #running on server
    #app.run('192.168.3.2',port=5000,debug=True)
	
    app.run()
