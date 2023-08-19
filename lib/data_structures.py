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


def get_names(spicy_foods):
    name = []
    for food in spicy_foods:
        name.append(food["name"])
    return name
    pass


def get_spiciest_foods(spicy_foods):
    real_spicy = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            real_spicy.append(food)
    return real_spicy
    pass


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
    pass


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None
    pass


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
    pass


def get_average_heat_level(spicy_foods):
    all_heat = 0
    for food in spicy_foods:
        all_heat += food["heat_level"]
    average_heat = all_heat / len(spicy_foods)
    return int(average_heat)

    pass


def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_food = spicy_foods.copy()
    new_spicy_food.append(spicy_food)
    return new_spicy_food
    pass


print(get_names(spicy_foods))
print(get_spiciest_foods(spicy_foods))
print_spicy_foods(spicy_foods)
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))
print_spiciest_foods(spicy_foods)
print(get_average_heat_level(spicy_foods))