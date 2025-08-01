my_list = ['a', 'b', 'a', 'c', 'b', 'a']
frequency = {}
for item in my_list:
    frequency[item] = frequency.get(item, 0) + 1
print("Frequency of elements:", frequency)

