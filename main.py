import random

labels = ["Rainy", "Sunny", "Cloudy", "Snowy", "Windy", "Humid"]
gender = ["Male", "Female"]
temperature = ["Warm", "Cold", "Hot", "Cool"]


class Clothing:
    def __init__(self, name, price, color, type, labels=None, gender=None):
        self.name = name
        self.price = price
        self.color = color
        self.type = type
        self.labels = set(labels or [])
        self.gender = set(gender or [])
    def __str__(self):
        return f"{self.type}: {self.name} ({self.color}) - ${self.price}"

# Tops
Tshirt = Clothing("Tshirt", 25, "Red", "Top", gender=["Male", "Female"], labels=["Warm", "Hot", "Sunny", "Humid"])
Long_sleeve = Clothing("Long Sleeve", 30, "Blue", "Top", gender=["Male", "Female"], labels=["Cool", "Cold", "Cloudy", "Windy"])
Tank_top = Clothing("Tank Top", 20, "Green", "Top", gender=["Male", "Female"], labels=["Hot", "Warm", "Sunny", "Humid"])
Hoodie = Clothing("Hoodie", 45, "Black", "Top", gender=["Male", "Female"], labels=["Cool", "Cold", "Windy", "Cloudy"])
Sweater = Clothing("Sweater", 40, "White", "Top", gender=["Male", "Female"], labels=["Cool", "Cold", "Cloudy", "Windy"])
Rain_jacket = Clothing("Rain Jacket", 60, "Yellow", "Top", gender=["Male", "Female"], labels=["Rainy", "Windy", "Cool"]) 
Puffer_jacket = Clothing("Puffer Jacket", 120, "Brown", "Top", gender=["Male", "Female"], labels=["Cold", "Snowy", "Windy"])
Rain_coat = Clothing("Rain Coat", 80, "Black", "Top", gender=["Male", "Female"], labels=["Rainy", "Windy"])

# Bottoms
Jeans = Clothing("Jeans", 40, "Blue", "Bottom", gender=["Male", "Female"], labels=["Cool", "Warm", "Cloudy", "Windy"])
Shorts = Clothing("Shorts", 25, "Khaki", "Bottom", gender=["Male", "Female"], labels=["Warm", "Hot", "Sunny", "Humid"])
Pants = Clothing("Chinos", 35, "Black", "Bottom", gender=["Male", "Female"], labels=["Cool", "Warm", "Cloudy", "Windy"])
Skirt = Clothing("Skirt", 30, "Green", "Bottom", gender=["Female"], labels=["Warm", "Hot", "Sunny", "Humid"])
Leggings = Clothing("Leggings", 28, "Charcoal", "Bottom", gender=["Female"], labels=["Cool", "Cold", "Cloudy"])
Capris = Clothing("Capris", 32, "Purple", "Bottom", gender=["Female"], labels=["Warm", "Sunny", "Humid"])
Sweatpants = Clothing("Sweatpants", 35, "Brown", "Bottom", gender=["Male", "Female"], labels=["Cool", "Cold", "Cloudy", "Windy"])
Rain_pants = Clothing("Rain Pants", 50, "Dark Grey", "Bottom", gender=["Male", "Female"], labels=["Rainy", "Windy", "Cool"])

# Shoes
Running_shoes = Clothing("Running Shoes", 60, "Black", "Shoes", gender=["Male", "Female"], labels=["Sunny", "Cloudy", "Warm", "Cool"])
Casual_sneakers = Clothing("Casual Sneakers", 55, "White", "Shoes", gender=["Male", "Female"], labels=["Sunny", "Cloudy", "Warm", "Cool", "Humid"])
Sandals = Clothing("Sandals", 30, "Tan", "Shoes", gender=["Male", "Female"], labels=["Hot", "Warm", "Sunny", "Humid"])
Rain_boots = Clothing("Rain Boots", 70, "Navy", "Shoes", gender=["Male", "Female"], labels=["Rainy", "Windy"]) 
Snow_boots = Clothing("Snow Boots", 90, "Black", "Shoes", gender=["Male", "Female"], labels=["Snowy", "Windy"])
Loafers = Clothing("Loafers", 65, "Brown", "Shoes", gender=["Male", "Female"], labels=["Sunny", "Cloudy", "Warm"])
High_heels = Clothing("Heels", 100, "Black", "Shoes", gender=["Female"], labels=["Warm", "Hot", "Sunny", "Humid"])

# Accessories
Beanie = Clothing("Beanie", 15, "Grey", "Accessory", gender=["Male", "Female"], labels=["Cold", "Snowy", "Windy"])
Scarf_wool = Clothing("Wool Scarf", 20, "Burgundy", "Accessory", gender=["Male", "Female"], labels=["Cold", "Snowy", "Windy", "Cloudy"])
Scarf_light = Clothing("Light Scarf", 18, "Cream", "Accessory", gender=["Male", "Female"], labels=["Cool", "Windy", "Cloudy"])
Gloves = Clothing("Gloves", 18, "Black", "Accessory", gender=["Male", "Female"], labels=["Cold", "Snowy", "Windy"]) 
Umbrella = Clothing("Umbrella", 25, "Black", "Accessory", gender=["Male", "Female"], labels=["Rainy", "Windy"]) 
Sun_hat = Clothing("Sun Hat", 22, "Beige", "Accessory", gender=["Male", "Female"], labels=["Sunny", "Hot", "Humid"]) 
Sunglasses = Clothing("Sunglasses", 35, "Black", "Accessory", gender=["Male", "Female"], labels=["Sunny", "Hot", "Warm"]) 

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

def recommend_for_weather(weather_label, temperature, gender):
    options = [c for c in clothes if weather_label in c.labels and temperature in c.labels and gender in c.gender]
    if not options:
        return None
    # Ensure we try to cover outfit variety
    by_type = {t: [c for c in options if c.type == t] for t in ["Top", "Bottom", "Shoes", "Accessory"]}
    selection = []
    if by_type["Top"]:
        selection.append(random.choice(by_type["Top"]))
    if by_type["Bottom"]:
        selection.append(random.choice(by_type["Bottom"]))
    if by_type["Shoes"]:
        selection.append(random.choice(by_type["Shoes"]))
    if by_type["Accessory"]:
        selection.append(random.choice(by_type["Accessory"]))
    return selection or [random.choice(options)]

user_input = input("What is the weather today? (Rainy/Sunny/Cloudy/Snowy/Windy/Humid): ").strip().title()
user_temperature = input("What is the temperature today? (Warm/Cold/Hot/Cool): ").strip().title()
user_gender = input("What is your gender? (Male/Female): ").strip().title()
if user_input not in labels:
    print(f"Unknown weather '{user_input}'. Try one of: {', '.join(labels)}")
    exit()
if user_temperature not in temperature:
    print(f"Unknown temperature '{user_temperature}'. Try one of: {', '.join(temperature)}")
    exit()
if user_gender not in gender:
    print(f"Unknown gender '{user_gender}'. Try one of: {', '.join(gender)}")
    exit()
print("Suggested outfit:")
outfit = recommend_for_weather(user_input, user_temperature, user_gender)
total_cost = sum(item.price for item in outfit)
if not outfit:
    print("No items found for that weather.")
    exit()
for item in outfit:
    print(f"- {item}")
print(f"Total cost: ${total_cost}")
print(f"Average cost: ${total_cost / len(outfit)}")