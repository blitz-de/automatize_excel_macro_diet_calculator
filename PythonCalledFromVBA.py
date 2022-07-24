import xlwings as xw
from collections import ChainMap

headers = ['breakfast', 'launch', 'snacks', 'dinner']
# Protein, Carbs, Fats, Sugar
breakfast = {'Oats': [3, 4, 5, 6], 'Whole Eggs': [3, 4, 5, 6], 'Protein Toast': [3, 4, 5, 6],
             'White Toast': [3, 4, 5, 6], 'Pancakes': [3, 4, 5, 6], 'Tomato': [3, 4, 5, 6],
             'Salad': [3, 4, 5, 6]}

launch = {'Rice': [3, 4, 5, 6], 'Spaghetti': [3, 4, 5, 6], 'Quinoa': [3, 4, 5, 6],
          'Salmon': [3, 4, 5, 6], 'Shrimps': [3, 4, 5, 6], 'Octopus': [3, 4, 5, 6],
          'Noodles': [3, 4, 5, 6], 'Onions': [3, 4, 5, 6], 'Tomatoes': [3, 4, 5, 6],
          'White Potatoes': [3, 4, 5, 6]}
snacks = {'Strawberry Shake': [3, 4, 5, 6], 'Avocado Shake': [3, 4, 5, 6], 'Plums': [3, 4, 5, 6],
          'Blueberries': [3, 4, 5, 6], 'Blackberries': [3, 4, 5, 6], 'Red Berries': [3, 4, 5, 6],
          'Strawberries': [3, 4, 5, 6], 'Banana': [3, 4, 5, 6]}
dinner = {'Tuna Salad': [3, 4, 5, 6], 'Beans': [3, 4, 5, 6], 'Toast': [3, 4, 5, 6],
          'Eggs': [3, 4, 5, 6], 'Shrimps': [3, 4, 5, 6], 'Oats': [3, 4, 5, 6]}

temp = 2

def iterate_meal(sheet, meal_type, row_side, enter_to=''):
    for meal in meal_type:
        # if i >= len(meal_type): break
        sheet[row_side + str(list(meal_type).index(meal) + temp)].value = meal  # [i]
        if meal == 'Oats':
            sheet[enter_to].value = meal_type[meal][0]

def test():
    pass
# check out if the meal chosen from the drop-list and set protein value in the protein row
def check_meal_type_and_set_protein_value(meal, meal_type, sheet, protein_row):
    if meal == meal_type:
        sheet[""].value = protein_row

def main():



    protein_per_egg = 2
    wb = xw.Book.caller()
    sheet = wb.sheets('Food List')

    sheet["A1:D1"].value = headers
    sheet["A2:A2"].value = len(breakfast)


    sheet_name = wb.sheets('Food List')

    def add_food_to_list(food_list, row_side1, row_side2, row_side3, row_side4, row_side5):
        for food_type in food_list:
            sheet[row_side1+str(list(food_list).index(food_type)+temp)].value = food_type
            sheet[row_side2 + str(list(food_list).index(food_type) + temp)].value = food_list[food_type][0]
            sheet[row_side3 + str(list(food_list).index(food_type) + temp)].value = food_list[food_type][1]
            sheet[row_side4 + str(list(food_list).index(food_type) + temp)].value = food_list[food_type][2]
            sheet[row_side5 + str(list(food_list).index(food_type) + temp)].value = food_list[food_type][3]

    iterate_meal(sheet_name, breakfast, "A"); iterate_meal(sheet_name, launch, "B"); iterate_meal(sheet_name, snacks, "C"); iterate_meal(sheet_name, dinner, "D");
    food_list = ChainMap(breakfast, launch, snacks, dinner)
    add_food_to_list(food_list, 'F', 'G', 'H', 'I', 'J')

def add_calory_values():
    wb = xw.Book.caller()
    sheet_daily = wb.sheets('Day Meal3')

    iterate_meal(sheet_daily, breakfast, "C2", "F2");

    #=IF(D2="Brown toast";1;IF(D2="Protein toast";5;IF(D2="Whole Eggs";4*E2;0)))
