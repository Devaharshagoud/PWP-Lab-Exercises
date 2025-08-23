import pandas as pd
s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([2, 4, 6, 8, 10])

print("Series 1:")
print(s1)

print("\nSeries 2:")
print(s2)

print("\nAddition of two Series:")
print(s1 + s2)

print("\nSubtraction of two Series:")
print(s1 - s2)

print("\nMultiplication of two Series:")
print(s1 * s2)

print("\nDivision of two Series:")
print(s1 / s2)

#post Lab 2
data = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
print("Dictionary:")
print(data)
series = pd.Series(data)
print("\nConverted Pandas Series:")
print(series)


#Post Lab 3:
import numpy as np
list_data = [10, 20, 30, 40]
series_from_list = pd.Series(list_data)
print("Series from list:")
print(series_from_list)

array_data = np.array([100, 200, 300, 400])
series_from_array = pd.Series(array_data)
print("\nSeries from NumPy array:")
print(series_from_array)

dict_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
series_from_dict = pd.Series(dict_data)
print("\nSeries from dictionary:")
print(series_from_dict)


#Post Lab 4:
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])
vertical = pd.concat([s1, s2])
print("Vertical Stacking:\n", vertical)
horizontal = pd.concat([s1, s2], axis=1)
print("\nHorizontal Stacking:\n", horizontal)



















