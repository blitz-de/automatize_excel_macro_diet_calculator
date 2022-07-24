breakfast = {'Oats': [3, 4, 5], 'Whole Eggs': [3, 4, 5], 'Protein Toast': [3, 4, 5],
             'White Toast': [3, 4, 5], 'Pancakes': [3, 4, 5], 'Tomato': [3, 4, 5],
             'Salad': [3, 4, 5]}

# print(breakfast.items())
for k in breakfast:
    print(breakfast[k][1])
    # print(list(breakfast).index(k))
