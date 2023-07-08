def main():
    nutrition_list = {
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60",
        "grapes": "90",
        "honeydew": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberries": "50",
        "cherries": "100",
        "tangerine": "50",
        "watermelon": "80",
    }
    
    food = input("Fruit (case sensitive): ")
    nutritional_value = nutrition_list.get(food)

    if nutritional_value:
        print("Calories: ", nutritional_value)
    else:
        print("Not a Valid Food in List.")

main()