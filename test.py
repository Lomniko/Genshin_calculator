asc_gem_table = [["sliver", 1], ["fragment", 3], ["fragment", 6], ["chunk", 3],  ["chunk", 6],  ["gemstone", 6]]
empty_list = {}
rotation = 0
for rank, amount in asc_gem_table:
    total = empty_list.get(rank, 0) + amount
    empty_list[rank] = total
print(empty_list)

