from adem_mohamed.classes.ScoreAnalyzer import ScoreAnalyzer
from adem_mohamed.classes.User import User
from adem_mohamed.classes.UserTypes import UserTypes

mohamed = User(UserTypes.ASPIRING_PROFESSIONAL,
               "Mohamed Adem",
               22,
               "Engineering",
               ["soccer", "chess", "coding"],
               "Montreal",
               "MUN")

ali = User(UserTypes.ASPIRING_PROFESSIONAL,
               "Mohamed Adem",
               25,
               "Engineering",
               ["asd", "coding"],
               "madacasgar",
               "MUN")

analyzer = ScoreAnalyzer(mohamed)

print(analyzer.getScore(ali).score)