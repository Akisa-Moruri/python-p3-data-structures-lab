spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
#get_names()
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

#get_spiciest_foods()
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"]>5]

#print_spicy_foods()
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

print_spicy_foods(spicy_foods)

#get_spicy_food_by_cuisine()
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None

cuisine = "Thai"
spicy_food = get_spicy_food_by_cuisine(spicy_foods, cuisine)
if spicy_food:
    print(f"Spicy food from {cuisine}: {spicy_food['name']}")
else:
    print(f"No spicy food found from {cuisine}") 

#print_spiciest_foods()
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            heat_emojis = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")


#get_average_heat_level()
def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods == 0:
        return 0  
    average_heat_level = total_heat_level / num_foods
    return round(average_heat_level)

average_heat = get_average_heat_level(spicy_foods)
print(f"Average heat level of spicy foods: {average_heat}")

#create_spicy_food()
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

new_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
print(updated_spicy_foods)
