"""
Tool definitions for the Ask-the-Web Agent
"""


def get_current_weather(city: str, unit: str = "celsius") -> str:
    """Get the current weather for a given city.
    
    Args:
        city: The name of the city
        unit: Temperature unit, either 'celsius' or 'fahrenheit' (default: 'celsius')
    
    Returns:
        A string describing the current weather conditions
    """
    # Simple dummy implementation - returns realistic weather data
    weather_data = {
        "San Francisco": ("18°C", "foggy"),
        "San Diego": ("23°C", "sunny"),
        "Seattle": ("12°C", "rainy"),
        "New York": ("15°C", "cloudy"),
        "London": ("10°C", "rainy"),
        "Paris": ("16°C", "partly cloudy"),
        "Tokyo": ("20°C", "clear"),
    }
    
    temp, condition = weather_data.get(city, ("20°C", "pleasant"))
    
    if unit.lower() == "fahrenheit":
        # Convert to Fahrenheit for display
        celsius = int(temp.replace("°C", ""))
        fahrenheit = int(celsius * 9/5 + 32)
        temp = f"{fahrenheit}°F"
    
    return f"It is {temp} and {condition} in {city}."
