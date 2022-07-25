import xlwings as xw
from collections import ChainMap

headers = ['breakfast', 'launch', 'snacks', 'dinner']
# Protein, Carbs, Fats, Sugar
breakfast = {'Oats': [3, 4, 5, 6], 'Whole Eggs': [30, 40, 50, 6], 'Protein Toast': [99, 67, 51, 62],
             'White Toast': [10, 12, 16, 14], 'Pancakes': [3, 4, 5, 6], 'Tomato': [3, 4, 5, 6],
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

temp_global = 2

def iterate_meal(sheet, meal_type, droplist_row, enter_to_row='', calory_type=0):
    for meal in meal_type:
        # if i >= len(meal_type): break
        sheet[droplist_row + str(list(meal_type).index(meal) + temp_global)].value = meal  # [i]
        # if meal == 'Oats':

        # sheet["A30"].value = enter_to[i]
        # F2, G2, H2
        # [protein g, carb g, fat g]
        iterate_calory_types = len((meal_type[meal]))
        temp = 0
        check_meal_type_and_set_protein_value(sheet, meal, droplist_row, enter_to_row, meal_type[meal][calory_type])



        # if meal == sheet[row_side].value:
        #     for i in range(len(enter_to)):
        #         sheet[enter_to[i]].value = meal_type[meal][0]
        #         sheet[enter_to[i]].value = meal_type[meal][1]
        #         sheet[enter_to[i]].value = meal_type[meal][2]


# check out if the meal chosen from the drop-list and set protein value in the protein row
def check_meal_type_and_set_protein_value(sheet, meal_type, droplist_row, enter_to_row, calory_value):
    if sheet[droplist_row].value == meal_type:
        sheet[enter_to_row].value = calory_value # insert grams of choice from droplist to protein row -- F2, F3

def main():

    wb = xw.Book.caller()
    sheet = wb.sheets('Food List')

    sheet["A1:D1"].value = headers
    sheet_name = wb.sheets('Food List')

    def add_food_to_list(food_list, row_side1, row_side2, row_side3, row_side4, row_side5):
        for food_type in food_list:
            sheet[row_side1 + str(list(food_list).index(food_type)+temp_global)].value = food_type
            sheet[row_side2 + str(list(food_list).index(food_type) + temp_global)].value = food_list[food_type][0]
            sheet[row_side3 + str(list(food_list).index(food_type) + temp_global)].value = food_list[food_type][1]
            sheet[row_side4 + str(list(food_list).index(food_type) + temp_global)].value = food_list[food_type][2]
            sheet[row_side5 + str(list(food_list).index(food_type) + temp_global)].value = food_list[food_type][3]

    iterate_meal(sheet_name, breakfast, "A"); iterate_meal(sheet_name, launch, "B"); iterate_meal(sheet_name, snacks, "C"); iterate_meal(sheet_name, dinner, "D");
    food_list = ChainMap(breakfast, launch, snacks, dinner)
    add_food_to_list(food_list, 'F', 'G', 'H', 'I', 'J')



def daily_meals_sheet():

    wb = xw.Book.caller()
    sheet_daily = wb.sheets('Day Meal3')
    sheet_daily["A46"].value = 33

    def add_calory_values(row_number): #row_number, calory_value
        values_of_diet = [0, 1, 2]

        for i in range(len(row_number)):
            if i >= len(row_number): break
            for j in range(len(values_of_diet)):
                if ((row_number[i] == 2 or 3 or 4) and j ==0):
                    iterate_meal(sheet_daily, breakfast, "D"+str(row_number[i]), "F"+str(row_number[i]), j); # add protein #(sheet, meal_type, row_side, enter_to=''):
                if ((row_number[i] == 2 or 3 or 4) and j ==1):
                    iterate_meal(sheet_daily, breakfast, "D"+str(row_number[i]), "G"+str(row_number[i]), j); # add protein #(sheet, meal_type, row_side, enter_to=''):
                if ((row_number[i] == 2 or 3 or 4) and j ==2):
                    iterate_meal(sheet_daily, breakfast, "D"+str(row_number[i]), "H"+str(row_number[i]), j); # add protein #(sheet, meal_type, row_side, enter_to=''):

    add_calory_values([2,3,4])
    # add_calory_values("F", 2, 0);
    # add_calory_values("G", 2, 1);
    # add_calory_values("H", 2, 2);
    # add_calory_values("F", 3, 0);
    # add_calory_values("G", 3, 1); add_calory_values("H", 3, 2);
    # add_calory_values("F", 4, 0);add_calory_values("G", 4, 1);add_calory_values("H", 4, 2);

    # iterate_meal(sheet_daily, breakfast, "D3", "F3", 0); # add protein #(sheet, meal_type, row_side, enter_to=''):
    # iterate_meal(sheet_daily, breakfast, "D4", "F4", 0); # add protein #(sheet, meal_type, row_side, enter_to=''):

    # iterate_meal(sheet_daily, breakfast, "D2", "G2", 1); # add carbs
    # iterate_meal(sheet_daily, breakfast, "D3", "G3", 1); # add carbs
    # iterate_meal(sheet_daily, breakfast, "D4", "G4", 1);  # add carbs
    #
    # iterate_meal(sheet_daily, breakfast, "D2", "H2", 2); # add fats
    # iterate_meal(sheet_daily, breakfast, "D2", "H3", 2);  # add fats
    # iterate_meal(sheet_daily, breakfast, "D2", "H4", 2);  # add fats

    #=IF(D2="Brown toast";1;IF(D2="Protein toast";5;IF(D2="Whole Eggs";4*E2;0)))
