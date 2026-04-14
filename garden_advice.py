"""
Garden Advice App
=================
Provides gardening tips and advice based on user input (season and plant type)
as well as the current month and season detected automatically.

Features:
- User interaction via input() for season and plant type
- Advice stored in dictionaries for easy extension
- Modular functions with docstrings
- Input validation for all user inputs
- Automatic season detection based on current month
"""

import datetime


# --- Data ---

MONTH_TO_SEASON = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Autumn", 10: "Autumn", 11: "Autumn"
}

# Advice stored in dictionaries for multiple seasons and plant types
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
    "spring": "Start sowing seeds and prepare your soil with compost.",
    "autumn": "Plant spring bulbs and rake up fallen leaves for compost."
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Ensure herbs get plenty of sunlight and good drainage.",
    "tree": "Mulch around the base to retain moisture and suppress weeds."
}

SEASONAL_ADVICE = {
    "Spring": [
        "Start sowing seeds indoors for tomatoes, peppers and aubergines.",
        "Begin preparing your soil by adding compost.",
        "Watch out for late frosts and protect tender plants.",
        "Prune roses and other shrubs as new growth appears.",
        "Plant onion sets and early potatoes."
    ],
    "Summer": [
        "Water plants early in the morning or late evening to reduce evaporation.",
        "Deadhead flowers regularly to encourage more blooms.",
        "Keep on top of weeding before weeds set seed.",
        "Harvest vegetables regularly to encourage continued cropping.",
        "Apply mulch around plants to retain moisture."
    ],
    "Autumn": [
        "Plant spring bulbs such as tulips, daffodils and crocuses.",
        "Rake up fallen leaves and add them to your compost heap.",
        "Lift and store tender bulbs before the first frost.",
        "Divide and transplant perennials.",
        "Plant garlic cloves for a harvest next summer."
    ],
    "Winter": [
        "Plan next year's garden layout and order seeds from catalogues.",
        "Clean and oil your garden tools to keep them in good condition.",
        "Protect tender plants with fleece or move them indoors.",
        "Check stored bulbs and tubers for rot.",
        "Feed the birds — they will repay you by eating pests in spring."
    ]
}


# --- Functions ---

def get_user_input(prompt, valid_options):
    """
    Prompt the user for input and validate against a list of valid options.

    Parameters:
        prompt (str): The message displayed to the user.
        valid_options (list): A list of accepted string values (lowercase).

    Returns:
        str: A validated, lowercase string matching one of the valid options.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"  Invalid input. Please choose from: {', '.join(valid_options)}\n")


def get_season_advice(season):
    """
    Return gardening advice based on the given season.

    Parameters:
        season (str): The season entered by the user (e.g. 'summer').

    Returns:
        str: Advice string for the season, or a default message if not found.
    """
    return SEASON_ADVICE.get(season, "No advice available for this season.")


def get_plant_advice(plant_type):
    """
    Return gardening advice based on the given plant type.

    Parameters:
        plant_type (str): The type of plant entered by the user (e.g. 'flower').

    Returns:
        str: Advice string for the plant type, or a default message if not found.
    """
    return PLANT_ADVICE.get(plant_type, "No advice available for this plant type.")


def get_season_from_month(month):
    """
    Determine the season based on the given month number.

    Parameters:
        month (int): A month number between 1 and 12.

    Returns:
        str: The corresponding season name, or 'Unknown' if the month is invalid.
    """
    if not isinstance(month, int) or month < 1 or month > 12:
        return "Unknown"
    return MONTH_TO_SEASON.get(month, "Unknown")


def get_monthly_advice(season):
    """
    Return a list of seasonal gardening tips for the current time of year.

    Parameters:
        season (str): The season name (e.g. 'Summer').

    Returns:
        list: A list of tip strings for the season.
    """
    return SEASONAL_ADVICE.get(season, ["No advice available for this season."])


def display_tips(tips):
    """
    Print a numbered list of gardening tips.

    Parameters:
        tips (list): A list of tip strings to display.
    """
    for i, tip in enumerate(tips, 1):
        print(f"  {i}. {tip}")


def main():
    """
    Main entry point for the Garden Advice App.
    Collects user input, displays personalised advice, and shows
    seasonal tips based on the current month.
    """
    print("=" * 45)
    print("        Welcome to the Garden Advice App")
    print("=" * 45)

    # Get user input with validation
    valid_seasons = list(SEASON_ADVICE.keys())
    valid_plants = list(PLANT_ADVICE.keys())

    season = get_user_input(
        f"\nEnter your season ({', '.join(valid_seasons)}): ",
        valid_seasons
    )
    plant_type = get_user_input(
        f"Enter your plant type ({', '.join(valid_plants)}): ",
        valid_plants
    )

    # Build and display personalised advice
    advice = get_season_advice(season)
    advice += "\n  " + get_plant_advice(plant_type)

    print(f"\n--- Personalised Advice for {season.capitalize()} / {plant_type.capitalize()} ---")
    print(f"  {advice}")

    # Auto-detect current season and display monthly tips
    current_month = datetime.datetime.now().month
    current_season = get_season_from_month(current_month)
    tips = get_monthly_advice(current_season)

    print(f"\n--- Seasonal Tips for {current_season} (Month {current_month}) ---")
    display_tips(tips)

    print("\nHappy gardening!")


if __name__ == "__main__":
    main()
