import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fecher import cech_data


class Prossor:
    def __init__(self,data):
        self.df = data
        self.weapons = None

    def find_the_rarest(self,filed):
        dict_of_common = {}
        for i in filed.lower().split(" "):
            if i not in dict_of_common:
                dict_of_common[i] = 1
            else:
                dict_of_common[i] += 1
        the_rarest_word = min(dict_of_common, key=dict_of_common.get)
        return the_rarest_word

    def to_find_the_rarest_word(self):
        self.df["rarest_word"] =  self.df["Text"].apply(self.find_the_rarest)



    def is_positive_or_negative(self,tweet):
        # nltk.download('vader_lexicon')
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)["compound"]
        if score >=0.5:
            return "positive"
        if score < -0.5:
            return "negative"
        else:
            return "normal"

    def check_the_score(self):
        self.df["score"] = self.df["Text"].apply(self.is_positive_or_negative)



    def read_from_txt(self,weapon):
        with open(weapon,"r")as file:
            self.weapons = file.read().split("\n")


    def their_is_wepen(self,text):
        for tweet in text:
            for weapon in self.weapons:
                if weapon in tweet:
                    return weapon


    def check_if_their_is_wepen(self):
        self.df["weapons"] = self.df["Text"].apply(self.their_is_wepen)


# cech_data11 = cech_data()
# data = cech_data11.connect_and_read()
# pros = Prossor(data)
# pros.to_find_the_rarest_word()
# # pros.check_the_score()
# # pros.read_from_txt(r"C:\Users\User\exe python\mongo-pandas-test\data\weapon_list.txt")
# # pros.check_if_their_is_wepen()
# # r"C:\Users\User\exe python\mongo-pandas-test\data\weapon_list.txt"
# # "data/weapon_list.txt"