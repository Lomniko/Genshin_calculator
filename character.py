

class Character:
    max_level = 90
    ch_list = dict()

    def __init__(self, name, asc_gem=None, boss_material=None, common_material=None, specialty_material=None):
        self.name = name
        self.asc_gem = asc_gem
        self.boss_material = boss_material
        self.common_material = common_material
        self.speciality_material = specialty_material
        Character.ch_list[name] = self

    def print_parameters(self):
        data = self.name, self.asc_gem, self.boss_material, self.common_material, self.speciality_material
        my_str = ""
        for element in data:
            my_str += str(element) + " | "
        print(my_str)

    def get_parameters(self):
        return self.name, self.asc_gem, self.boss_material, self.common_material, self.speciality_material


    # def save_changes(self):
    #     with open('characters.txt', 'a') as f:
    #         f.write(self.print_parameters() + "\n")
    #         print("Wrote to file successfully!")

    @classmethod
    def get_ch_list(cls):
        return cls.ch_list


beidou = Character("Beidou", "amethyst", "lightning prism", "treasure hoarder insignia", "noctilucous jade")
xingqiu = Character("Xingqiu", "lazurite", "cleansing heart", "damaged mask", "silk flower")
albedo = Character("Albedo", "topaz", "basalt pillar", "divining scroll", "cecilia")
razor = Character("Razor", "amethyst", "lightning prism", "damaged mask", "wolfhook")


if __name__ == "__main__":
    print(Character.ch_list["Beidou"].name)
    print(Character.get_ch_list())
