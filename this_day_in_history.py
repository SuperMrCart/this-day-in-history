import requests
from datetime import datetime

def get_history_events():
    # Get the current date
    today = datetime.now()
    month = today.month
    day = today.day

    # Make a request to the API
    url = f"https://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        print("Failed to retrieve data")
        return None

def display_events(events):
    print("This Day in History:\n")

    # Display Events
    print("Events:")
    for event in events['Events']:
        print(f"{event['year']}: {event['text']}")

    # Display Births
    print("\nBirths:")
    for birth in events['Births']:
        print(f"{birth['year']}: {birth['text']}")

    # Display Deaths
    print("\nDeaths:")
    for death in events['Deaths']:
        print(f"{death['year']}: {death['text']}")
        
def display_limited_events(events, limit=10):
    print("This Day in History:\n")

    # Display limited Events
    print("Events:")
    for event in events['Events'][:limit]:
        print(f"{event['year']}: {event['text']}")

def display_limited_births(events, limit=5):
    # Display limited Births
    print("\nBirths:")
    for birth in events['Births'][:limit]:
        print(f"{birth['year']}: {birth['text']}")

def display_limited_deaths(events, limit=5):
    # Display limited Deaths
    print("\nDeaths:")
    for death in events['Deaths'][:limit]:
        print(f"{death['year']}: {death['text']}")

if __name__ == "__main__":
    events = get_history_events()
    if events:
        display_limited_events(events)
        display_limited_births(events)
        display_limited_deaths(events)