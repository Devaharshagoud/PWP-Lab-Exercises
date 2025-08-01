my_list = [1, 2, 2, 3, 4, 4, 5]
removed_list = list(dict.fromkeys(my_list))  # Or: list(set(my_list)) (unordered)
print("List without duplicates:", removed_list)

