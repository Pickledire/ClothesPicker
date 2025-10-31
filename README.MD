# Outfit Recommender

Simple CLI tool that suggests a sensible outfit based on weather, temperature, and gender.

## What it does
- Asks for:
  - Weather: Rainy, Sunny, Cloudy, Snowy, Windy, Humid
  - Temperature: Warm, Cold, Hot, Cool
  - Gender: Male, Female
- Matches against predefined rules and prints a coherent outfit:
  - One Top, one Bottom, Shoes, and an Accessory
  - Shows total price of the selected items

## Run
```bash
python3 main.py
```

## Example
```
What is the weather today? (Rainy/Sunny/Cloudy/Snowy/Windy/Humid): Sunny
What is the temperature today? (Warm/Cold/Hot/Cool): Hot
What is your gender? (Male/Female): Male

Suggested outfit:
Price: $137
- Top: Tank Top (Green) - $20
- Bottom: Shorts (Khaki) - $25
- Shoes: Sandals (Tan) - $30
- Accessory: Sun Hat (Beige) - $22
```

Notes:
- Item choices are curated to fit the conditions (e.g., rain → rain boots + umbrella).
- If an exact match is not found, the closest matching rule is chosen.

