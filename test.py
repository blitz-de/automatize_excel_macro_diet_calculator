import xlwings as xw

breakfast = {'Oats': [3, 4, 5], 'Whole Eggs': [13, 14, 15], 'Protein Toast': [33, 44, 55],
             'White Toast': [3, 4, 5], 'Pancakes': [3, 4, 5], 'Tomato': [3, 4, 5],
             'Salad': [3, 4, 5]}

array = ["f", "g", "h"]


def add_calory_values(row_number):
    values_of_diet = [0, 1, 2]

    '''
    2 - 0
    3 - 0
    4 - 0
    
    2 - 1
    3 - 1
    4 - 1
    
    2 - 2
    3 - 2
    4 -2
    '''
    for i in range(len(row_number)):
        if i >= len(row_number): break
        for j in range(len(values_of_diet)):
            # print(row_number[i].__class__)
            # 2,0 -> 2,1 -> 2,2 -- 3,0 -> 3,1 -> 3,2
            # print(row_number[i])
            if ((row_number[i] == 2 or 3 or 4) and j ==0):
               print("I am in the first if: ", row_number[i], "jj: ", j)
            if ((row_number[i] == 2 or 3 or 4) and j == 1):
                print("I am in the second if: ", row_number[i], "jj: ", j)
            if ((row_number[i] == 2 or 3 or 4) and j == 2):
                print("I am in the third if: ", row_number[i], "jj: ", j)

            #
            # if row_number[i] == 3 :
            #     print("I am in the second if: ", row_number[i], "jj: ", j)
            #
            # if row_number[i] == 4 and j == 2:
            #     print("I am in the third if: ", row_number[i], "jj: ", j)
add_calory_values([2,3,4])

# iterate_breakfast_values = len(breakfast)
# temp = 0
# row_array = [1,2,3]
# def pass_array(row_num):
#     print(str(row_num[0]))
#
# pass_array(row_array)
# print(range(len(array)-1))
# while iterate_breakfast_values >0:
#
#     # print(len(breakfast))
#     temp = iterate_breakfast_values
#     print(temp)
#     iterate_breakfast_values = iterate_breakfast_values -1


# print(array[0])
#
# print(len(array))
#
# for k in breakfast:
#     # print(len((breakfast[k])))
#
#     print(breakfast["Oats"][1])
#     # print(list(breakfast).index(k))

