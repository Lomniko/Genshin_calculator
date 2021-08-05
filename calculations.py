import math
from character import Character

asc_num = [1,2,3,4,5,6]
asc_levels = [20, 40, 50, 60, 70, 80]
asc_gem_table = {1: ["sliver", 1], 2: ["fragment", 3], 3: ["fragment", 6], 4: ["chunk", 3], 5: ["chunk", 6], 6: ["gemstone", 6]}


def get_leveling_data():
    with open("genshin_exp_table.txt") as file:
        filtered_data = [int(s) for s in file.read().split() if s.isdigit()]
    iter_data = iter(filtered_data)
    dict_exp_table = dict(zip(iter_data, iter_data))
    return dict_exp_table


def lvl_calc(name, intended_lvl, intended_asc, lvl=1, exp=0, asc=0):
    exp_books = {"purple": 20000, "blue": 5000, "green": 1000}
    asc_cost = {0: 0, 1: 20000, 2: 40000, 3: 60000, 4: 80000, 5: 100000, 6: 120000}

    lvl_data = get_leveling_data()
    exp_difference = 0 - exp
    for num in range(lvl, intended_lvl):
        exp_difference += lvl_data[num]

    #  Высчитываем книжки.
    #  print(f"Итоговый опыт: {exp_difference}")
    prlp_books = exp_difference // exp_books["purple"]
    prpl_exp = prlp_books * exp_books["purple"]
    blue_books = (exp_difference - prpl_exp) // exp_books["blue"]
    blue_exp = blue_books * exp_books["blue"]
    green_books = math.ceil(((exp_difference - prpl_exp) - blue_exp) / exp_books["green"])
    green_exp = green_books * exp_books["green"]
    wasted_exp = abs(exp_difference - prpl_exp - blue_exp - green_exp)

    # Высчитываем пр. материалы на повышение
    mora_cost = prlp_books * 4000 + blue_books * 1000 + green_books * 200
    name, asc_gem, boss_material, common_material, specialty_material = Character.ch_list[name].get_parameters()
    for num in range(asc+1, intended_asc+1):
        mora_cost += asc_cost[num]

    gem_cost = []
    for num in range(asc+1, intended_asc+1):
        gem_cost.append(asc_gem_table[num])

    upd_gem_cost = {}
    for rank, amount in gem_cost:
        total = upd_gem_cost.get(rank, 0) + amount
        upd_gem_cost[rank] = total

    # Cтоит добавить материалы, по крайней мере гемы
    return prlp_books, blue_books, green_books, wasted_exp, mora_cost, asc_gem, upd_gem_cost


def talent_calculator(trg_tal1_lvl, trg_tal2lvl, trg_tal3_lvl, tal1_lvl=1, tal2_lvl=1, tal3_lvl=1):
    talent_cost = {1: 0, 2: 12500, 3: 17500, 4: 25000, 5: 30000, 6: 37500, 7: 120000, 8: 260000, 9: 450000, 10: 700000}
    cost1, cost2, cost3 = 0
    for num in range(tal1_lvl, trg_tal1_lvl + 1):
        cost1 += talent_cost[num]
    for num in range(tal2_lvl, trg_tal2lvl + 1):
        cost2 += talent_cost[num]
    for num in range(tal3_lvl, trg_tal3_lvl + 1):
        cost3 += talent_cost[num]
    return cost1, cost2, cost3


def calculate_ch(name, intended_lvl, intended_asc, lvl=1, exp=0, asc=0):
    prlp_books, blue_books, green_books, wasted_exp, mora_cost, asc_gem, gem_cost =\
        lvl_calc(name, intended_lvl, intended_asc, lvl, exp, asc)
    print(f"Персонаж: {name}, затраты на повышение составляют:\nHero's Wit: {prlp_books}, Adventurer's Experience: "
          f"{blue_books}, Wanderer's Advice: {green_books}.\n Требуемая Мора: {mora_cost}. В процессе теряется {wasted_exp} exp.")

    for el in gem_cost:
        print(f"{gem_cost[el]}x {asc_gem} {el}. ", end="")


def calculate_talent(trg_tal1_lvl, trg_tal2_lvl, trg_tal3_lvl, tal1_lvl=1, tal2_lvl=1, tal3_lvl=1):
    cost1, cost2, cost3 = talent_calculator(trg_tal1_lvl, trg_tal2_lvl, trg_tal3_lvl, tal1_lvl, tal2_lvl, tal3_lvl)
    print(f"Стоимость повышения талантов:\nНормальные атаки: {cost1}, Навык: {cost2}, Ульт: {cost3}, суммарно выходит: {cost1+cost2+cost3}")


if __name__ == "__main__":
    calculate_ch("Albedo", 4, 0)