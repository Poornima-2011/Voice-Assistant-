# wish.py
from datetime import datetime

def wish_user():
    """Function to greet the user based on the time of day."""
    # Get the current hour
    hour = datetime.now().hour
    
    if hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"
