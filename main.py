import random

weather_labels = ["Rainy", "Sunny", "Cloudy", "Snowy", "Windy", "Humid"]
temperature_labels = ["Warm", "Cold", "Hot", "Cool"]
gender_labels = ["Male", "Female"]

synonyms = {
    "Rainy": ["Rainy", "Rain", "Rainy Day", "Rainy Weather", "Rainy Day Weather"],
    "Sunny": ["Sunny", "Sun", "Sunny Day", "Sunny Weather", "Sunny Day Weather"],
    "Cloudy": ["Cloudy", "Cloud", "Cloudy Day", "Cloudy Weather", "Cloudy Day Weather"],
    "Snowy": ["Snowy", "Snow", "Snowy Day", "Snowy Weather", "Snowy Day Weather"],
    "Windy": ["Windy", "Wind", "Windy Day", "Windy Weather", "Windy Day Weather"],
    "Humid": ["Humid", "Humidity", "Humid Day", "Humid Weather", "Humid Day Weather"],
    "Warm": ["Warm", "Warm Day", "Warm Weather", "Warm Day Weather"],
    "Cold": ["Cold", "Cold Day", "Cold Weather", "Cold Day Weather"],
    "Hot": ["Hot", "Hot Day", "Hot Weather", "Hot Day Weather"],
    "Cool": ["Cool", "Cool Day", "Cool Weather", "Cool Day Weather"],
    "Male": ["Male", "Man", "Male Day", "Male Weather", "Male Day Weather"],
    "Female": ["Female", "Woman", "Female Day", "Female Weather", "Female Day Weather"],
}   

class Clothing:
    def __init__(self, name, price, color, type, weather_labels=None, temperature_labels=None, gender_labels=None):
        self.name = name
        self.price = price
        self.color = color
        self.type = type
        self.weather_labels = set(weather_labels or [])
        self.temperature_labels = set(temperature_labels or [])
        self.gender_labels = set(gender_labels or [])
    def __str__(self):
        return f"{self.type}: {self.name} ({self.color}) - ${self.price}"

# Tops
Tshirt = Clothing("Tshirt", 25, "Red", "Top", weather_labels=["Sunny"], temperature_labels=["Warm", "Hot"], gender_labels=["Male", "Female"])
Long_sleeve = Clothing("Long Sleeve", 30, "Blue", "Top", weather_labels=["Cloudy"], temperature_labels=["Cool", "Cold"], gender_labels=["Male", "Female"])
Tank_top = Clothing("Tank Top", 20, "Green", "Top", weather_labels=["Sunny"], temperature_labels=["Hot", "Warm"], gender_labels=["Male", "Female"])
Hoodie = Clothing("Hoodie", 45, "Black", "Top", weather_labels=["Windy"], temperature_labels=["Cool", "Cold"], gender_labels=["Male", "Female"])
Sweater = Clothing("Sweater", 40, "White", "Top", weather_labels=["Cloudy"], temperature_labels=["Cool", "Cold"], gender_labels=["Male", "Female"])
Rain_jacket = Clothing("Rain Jacket", 60, "Yellow", "Top", weather_labels=["Rainy"], temperature_labels=["Cool"], gender_labels=["Male", "Female"]) 
Puffer_jacket = Clothing("Puffer Jacket", 120, "Brown", "Top", weather_labels=["Snowy"], temperature_labels=["Cold"], gender_labels=["Male", "Female"])
Rain_coat = Clothing("Rain Coat", 80, "Black", "Top", weather_labels=["Rainy"], temperature_labels=["Cool"], gender_labels=["Male", "Female"])

# Bottoms
Jeans = Clothing("Jeans", 40, "Blue", "Bottom", weather_labels=["Cloudy"], temperature_labels=["Cool", "Warm"], gender_labels=["Male", "Female"])
Shorts = Clothing("Shorts", 25, "Khaki", "Bottom", weather_labels=["Sunny"], temperature_labels=["Warm", "Hot"], gender_labels=["Male", "Female"])
Pants = Clothing("Chinos", 35, "Black", "Bottom", weather_labels=["Cloudy"], temperature_labels=["Cool", "Warm"], gender_labels=["Male", "Female"])
Skirt = Clothing("Skirt", 30, "Green", "Bottom", weather_labels=["Sunny"], temperature_labels=["Warm", "Hot"], gender_labels=["Female"])
Leggings = Clothing("Leggings", 28, "Charcoal", "Bottom", weather_labels=["Cloudy"], temperature_labels=["Cool", "Cold"], gender_labels=["Female"])
Capris = Clothing("Capris", 32, "Purple", "Bottom", weather_labels=["Sunny"], temperature_labels=["Warm", "Hot"], gender_labels=["Female"])
Sweatpants = Clothing("Sweatpants", 35, "Brown", "Bottom", weather_labels=["Cloudy"], temperature_labels=["Cool", "Cold"], gender_labels=["Male", "Female"])
Rain_pants = Clothing("Rain Pants", 50, "Dark Grey", "Bottom", weather_labels=["Rainy"], temperature_labels=["Cool"], gender_labels=["Male", "Female"])

# Shoes
Running_shoes = Clothing("Running Shoes", 60, "Black", "Shoes", weather_labels=["Sunny"], temperature_labels=["Warm", "Hot"], gender_labels=["Male", "Female"])
Casual_sneakers = Clothing("Casual Sneakers", 55, "White", "Shoes", weather_labels=["Sunny"], temperature_labels=["Warm", "Hot"], gender_labels=["Male", "Female"])
Sandals = Clothing("Sandals", 30, "Tan", "Shoes", weather_labels=["Sunny"], temperature_labels=["Hot", "Warm"], gender_labels=["Male", "Female"])
Rain_boots = Clothing("Rain Boots", 70, "Navy", "Shoes", weather_labels=["Rainy"], temperature_labels=["Cool"], gender_labels=["Male", "Female"]) 
Snow_boots = Clothing("Snow Boots", 90, "Black", "Shoes", weather_labels=["Snowy"], temperature_labels=["Cold"], gender_labels=["Male", "Female"]) 
Loafers = Clothing("Loafers", 65, "Brown", "Shoes", weather_labels=["Sunny"], temperature_labels=["Warm"], gender_labels=["Male", "Female"])
High_heels = Clothing("Heels", 100, "Black", "Shoes", weather_labels=["Sunny"], temperature_labels=["Warm", "Hot"], gender_labels=["Female"])

# Accessories
Beanie = Clothing("Beanie", 15, "Grey", "Accessory", weather_labels=["Snowy"], temperature_labels=["Cold"], gender_labels=["Male", "Female"])
Scarf_wool = Clothing("Wool Scarf", 20, "Burgundy", "Accessory", weather_labels=["Snowy"], temperature_labels=["Cold"], gender_labels=["Male", "Female"])
Scarf_light = Clothing("Light Scarf", 18, "Cream", "Accessory", weather_labels=["Cloudy"], temperature_labels=["Cool"], gender_labels=["Male", "Female"])
Gloves = Clothing("Gloves", 18, "Black", "Accessory", weather_labels=["Snowy"], temperature_labels=["Cold"], gender_labels=["Male", "Female"]) 
Umbrella = Clothing("Umbrella", 25, "Black", "Accessory", weather_labels=["Rainy"], temperature_labels=["Cool"], gender_labels=["Male", "Female"]) 
Sun_hat = Clothing("Sun Hat", 22, "Beige", "Accessory", weather_labels=["Sunny"], temperature_labels=["Hot", "Warm"], gender_labels=["Male", "Female"]) 
Sunglasses = Clothing("Sunglasses", 35, "Black", "Accessory", weather_labels=["Sunny"], temperature_labels=["Warm", "Hot"], gender_labels=["Male", "Female"]) 

clothes = [
    # Tops
    Tshirt, Long_sleeve, Tank_top, Hoodie, Sweater, Rain_jacket, Puffer_jacket, Rain_coat,
    # Bottoms
    Jeans, Shorts, Pants, Skirt, Leggings, Capris, Sweatpants, Rain_pants,
    # Shoes
    Running_shoes, Casual_sneakers, Sandals, Rain_boots, Snow_boots, Loafers,
    # Accessories
    Beanie, Scarf_wool, Scarf_light, Gloves, Umbrella, Sun_hat, Sunglasses,
]

RULES = [
    # Rainy
    {"weather_labels" : "Rainy", "temperature_labels": "Warm", "gender_labels": "Male", "outfit": [Rain_coat, Jeans, Rain_boots, Umbrella]},
    {"weather_labels" : "Rainy", "temperature_labels": "Warm", "gender_labels": "Female", "outfit": [Rain_coat, Jeans, Rain_boots, Umbrella]},
    {"weather_labels" : "Rainy", "temperature_labels": "Cold", "gender_labels": "Male", "outfit": [Rain_jacket, Sweatpants, Rain_boots, Umbrella]},
    {"weather_labels" : "Rainy", "temperature_labels": "Cold", "gender_labels": "Female", "outfit": [Rain_jacket, Leggings, Rain_boots, Umbrella]},
    {"weather_labels" : "Rainy", "temperature_labels": "Hot", "gender_labels": "Male", "outfit": [Tshirt, Rain_pants, Rain_boots, Umbrella]},
    {"weather_labels" : "Rainy", "temperature_labels": "Hot", "gender_labels": "Female", "outfit": [Tshirt, Rain_pants, Rain_boots, Umbrella]},
    {"weather_labels" : "Rainy", "temperature_labels": "Cool", "gender_labels": "Male", "outfit": [Rain_jacket, Jeans, Rain_boots, Umbrella]},
    {"weather_labels" : "Rainy", "temperature_labels": "Cool", "gender_labels": "Female", "outfit": [Rain_jacket, Jeans, Rain_boots, Umbrella]},
    # Sunny
    {"weather_labels" : "Sunny", "temperature_labels": "Warm", "gender_labels": "Male", "outfit": [Tshirt, Shorts, Casual_sneakers, Sunglasses]},
    {"weather_labels" : "Sunny", "temperature_labels": "Warm", "gender_labels": "Female", "outfit": [Tshirt, Skirt, Casual_sneakers, Sunglasses]},
    {"weather_labels" : "Sunny", "temperature_labels": "Cold", "gender_labels": "Male", "outfit": [Long_sleeve, Jeans, Loafers, Sunglasses]},
    {"weather_labels" : "Sunny", "temperature_labels": "Cold", "gender_labels": "Female", "outfit": [Long_sleeve, Jeans, Loafers, Sunglasses]},
    {"weather_labels" : "Sunny", "temperature_labels": "Hot", "gender_labels": "Male", "outfit": [Tank_top, Shorts, Sandals, Sun_hat]},
    {"weather_labels" : "Sunny", "temperature_labels": "Hot", "gender_labels": "Female", "outfit": [Tank_top, Skirt, Sandals, Sun_hat]},
    {"weather_labels" : "Sunny", "temperature_labels": "Cool", "gender_labels": "Male", "outfit": [Long_sleeve, Jeans, Casual_sneakers, Scarf_light]},
    {"weather_labels" : "Sunny", "temperature_labels": "Cool", "gender_labels": "Female", "outfit": [Long_sleeve, Jeans, Casual_sneakers, Scarf_light]},
    # Windy
    {"weather_labels" : "Windy", "temperature_labels": "Warm", "gender_labels": "Male", "outfit": [Hoodie, Jeans, Running_shoes, Scarf_light]},
    {"weather_labels" : "Windy", "temperature_labels": "Warm", "gender_labels": "Female", "outfit": [Hoodie, Jeans, Running_shoes, Scarf_light]},
    {"weather_labels" : "Windy", "temperature_labels": "Cold", "gender_labels": "Male", "outfit": [Hoodie, Sweatpants, Running_shoes, Beanie]},
    {"weather_labels" : "Windy", "temperature_labels": "Cold", "gender_labels": "Female", "outfit": [Hoodie, Leggings, Running_shoes, Beanie]},
    {"weather_labels" : "Windy", "temperature_labels": "Hot", "gender_labels": "Male", "outfit": [Tshirt, Shorts, Casual_sneakers, Scarf_light]},
    {"weather_labels" : "Windy", "temperature_labels": "Hot", "gender_labels": "Female", "outfit": [Tshirt, Shorts, Casual_sneakers, Scarf_light]},
    {"weather_labels" : "Windy", "temperature_labels": "Cool", "gender_labels": "Male", "outfit": [Sweater, Jeans, Running_shoes, Scarf_light]}, 
    {"weather_labels" : "Windy", "temperature_labels": "Cool", "gender_labels": "Female", "outfit": [Sweater, Jeans, Running_shoes, Scarf_light]},
    # Humid
    {"weather_labels" : "Humid", "temperature_labels": "Warm", "gender_labels": "Male", "outfit": [Tshirt, Shorts, Casual_sneakers, Sun_hat]},
    {"weather_labels" : "Humid", "temperature_labels": "Warm", "gender_labels": "Female", "outfit": [Tshirt, Shorts, Casual_sneakers, Sun_hat]},
    {"weather_labels" : "Humid", "temperature_labels": "Cold", "gender_labels": "Male", "outfit": [Long_sleeve, Jeans, Casual_sneakers, Scarf_light]},
    {"weather_labels" : "Humid", "temperature_labels": "Cold", "gender_labels": "Female", "outfit": [Long_sleeve, Jeans, Casual_sneakers, Scarf_light]},
    {"weather_labels" : "Humid", "temperature_labels": "Hot", "gender_labels": "Male", "outfit": [Tank_top, Shorts, Sandals, Sun_hat]},
    {"weather_labels" : "Humid", "temperature_labels": "Hot", "gender_labels": "Female", "outfit": [Tank_top, Shorts, Sandals, Sun_hat]},
    {"weather_labels" : "Humid", "temperature_labels": "Cool", "gender_labels": "Male", "outfit": [Long_sleeve, Jeans, Casual_sneakers, Scarf_light]},
    {"weather_labels" : "Humid", "temperature_labels": "Cool", "gender_labels": "Female", "outfit": [Long_sleeve, Jeans, Casual_sneakers, Scarf_light]},
]




user_weather = input("What is the weather today? (Rainy/Sunny/Cloudy/Snowy/Windy/Humid): ").strip().title()
user_temperature = input("What is the temperature today? (Warm/Cold/Hot/Cool): ").strip().title()
user_gender = input("What is your gender? (Male/Female): ").strip().title()


def Match_rules(rules, user_weather, user_temperature, user_gender ):
    best_score = 0
    best_outfit = []
    for rule in rules:
        if rule["weather_labels"] == user_weather and rule["temperature_labels"] == user_temperature and rule["gender_labels"] == user_gender:
            return rule["outfit"]
        else:
            score = 0
            if rule["weather_labels"] == user_weather:
                score += 1
            if rule["temperature_labels"] == user_temperature:
                score += 1
            if rule["gender_labels"] == user_gender:
                score += 1
            if score > best_score:
                best_score = score
                best_outfit = rule["outfit"]
    return best_outfit

outfit = Match_rules(RULES, user_weather, user_temperature, user_gender)
if not outfit:
    print("No matching outfit found.")
else:
    print("Suggested outfit:")
    print(f"Price: ${sum(item.price for item in outfit)}")
    for item in outfit:
        print(f"- {item}")