# noinspection PyMethodMayBeStatic
from adem_mohamed.classes.RoasterResult import RoasterResult
from adem_mohamed.classes.User import User


class ScoreAnalyzer:

    weights = [3,  # industry
               3,  # interests
               1,  # age
               1,  # school
               1]  # location

    def __init__(self, subjectUser):
        self.subjectUser = subjectUser

    def getScore(self, potentialMatch: User) -> RoasterResult:

        industryScore = self.analyzeIndustry(potentialMatch)
        interestsScore = self.analyzeInterests(potentialMatch)
        ageScore = self.analyzeAge(potentialMatch)
        schoolScore = self.analyzeSchool(potentialMatch)
        locationScore = self.analyzeLocation(potentialMatch)

        scores = [industryScore, interestsScore, ageScore, schoolScore, locationScore]
        overallScore = self.getWeightedAverage(scores)

        return mapResult(potentialMatch, overallScore)

    def analyzeIndustry(self, potentialMatch):
        if potentialMatch.industry == self.subjectUser.industry:
            return 100
        else:
            return 0

    def analyzeInterests(self, potentialMatch: User):
        matches = len(set(potentialMatch.interests).intersection(self.subjectUser.interests))

        if matches == 0:
            return 0
        elif matches == 1:
            return 50
        elif matches == 2:
            return 80
        else:
            return 100

    def analyzeAge(self, potentialMatch: User):

        ageDifference = abs(potentialMatch.age - self.subjectUser.age)

        if 0 <= ageDifference <= 3:
            return 100
        elif 3 <= ageDifference <= 8:
            return 70
        elif 8 <= ageDifference <= 30:
            return 50
        else:
            return 0

    def analyzeSchool(self, potentialMatch: User):
        if potentialMatch.school == self.subjectUser.school:
            return 100
        else:
            return 0

    def analyzeLocation(self, potentialMatch: User):
        if potentialMatch.location == self.subjectUser.location:
            return 100
        else:
            return 0

    def getWeightedAverage(self, scores):
        numerator = 0
        for i in range(5):
            numerator = numerator + scores[i] * self.weights[i]

        return numerator / sum(self.weights)


def mapResult(potentialMatch: User, overallScore):
    return RoasterResult(potentialMatch.userType,
                         potentialMatch.name,
                         potentialMatch.age,
                         potentialMatch.industry,
                         potentialMatch.interests,
                         potentialMatch.location,
                         potentialMatch.school,
                         0,
                         overallScore)
