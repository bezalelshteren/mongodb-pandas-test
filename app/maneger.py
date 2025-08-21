from fecher import cech_data
from prosesor import Prossor


class Maneger:
    def __init__(self):
        self.fech = cech_data()
        self.data = self.fech.connect_and_read()
        self.pros = Prossor(self.data)
        # print(self.data,78978999978)

    def start_all_fanction(self):
        self.pros.to_find_the_rarest_word()
        self.pros.check_the_score()
        self.pros.read_from_txt("../data/weapon_list.txt")
        self.pros.check_if_their_is_wepen()
        print(self.data.to_dict())
        return self.data.to_dict()


# "..data/weapon_list.txt"
# r"C:\Users\User\exe python\mongo-pandas-test\data\weapon_list.txt"
# data/weapon_list.txt