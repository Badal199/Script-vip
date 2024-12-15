import time
from datetime import datetime, timedelta
import random

# Pattern to predict upcoming results
result_pattern = ["SMALL", "SMALL", "BIG", "BIG", "SMALL", "SMALL", "BIG"]

# Initialize period number and last period time
current_period = None
last_updated_time = None

def generate_period_number():
    """Generate a period number based on UTC time."""
    now = datetime.utcnow()
    # Example logic to generate the period number, similar to Java code
    minutes_since_midnight = now.hour * 60 + now.minute
    period_number = f"{now.strftime('%Y%m%d')}1000{10001 + minutes_since_midnight}"
    return period_number

def get_next_result(period_num):
    """Get the result for the current period based on the pattern."""
    # Convert the period number to an index in the pattern
    index = (int(period_num[-5:]) - 10001) % len(result_pattern)
    return result_pattern[index]

# Main loop to simulate a 1-minute timer
try:
    while True:
        # Calculate the current period number
        new_period = generate_period_number()

        # Check if the period number has changed
        if new_period != current_period:
            current_period = new_period
            # Get the result for the current period
            result = get_next_result(current_period)
            # Generate random details for the result
            random_number = random.randint(1, 100)
            emoji = random.choice(["❤️", "💚", "💙"])
            formatted_result = f"{result} {emoji} {random_number}"
            print(f"Period: {current_period} | Result: {formatted_result}")

            # Update last updated time
            last_updated_time = datetime.utcnow()

        # Display remaining time in format "  x x  :  x x"
        now = datetime.utcnow()
        remaining_seconds = 60 - now.second
        formatted_timer = f"   {remaining_seconds // 10} {remaining_seconds % 10}  :  0 0"
        print(f"Timer: {formatted_timer}", end="\r")

        # Wait 1 second before the next check
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram stopped.")