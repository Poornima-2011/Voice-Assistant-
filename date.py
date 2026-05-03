# date.py
from datetime import datetime

def get_current_date():
    """Function to return the current date in a readable format."""
    today = datetime.today()
    current_date = today.strftime("%d-%m-%Y")  # Format as: day-month-year (e.g., 10-03-2025)
    
    # Return the formatted date
    return current_date
