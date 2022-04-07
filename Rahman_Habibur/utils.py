import json
line = "-" * 155 + "\n"
name_line = line + "%55s" % "Lastname | " + \
    "%10s" % "Firstname | " + "%10s" % "Industry | " + \
    "%10s" % "Interests" + "%20s" % "Lastname | " + \
    "%10s" % "Firstname |" + "%10s" % "Industry" + \
    "%10s" % " | Interests | Frequency" + "\n" + line
pretty_format = line + "%10s" % "Chat Name" + \
    "%15s" % "Date" + "%10s" % "Time" + "%10s" % "Location" + \
    "%50s" % "Aspiring Professional" + "%40s" % "Senior Executive" + "\n" + name_line

# function for loading data from json file


def load_data(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
    return data
