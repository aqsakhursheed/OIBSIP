import requests

def get_weather(city_name):
    # Free WeatherAPI key (Instant Working & Free Tier)
    api_key = "429ee59c2d1942c7999101630263108"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"

    try:
        response = requests.get(url)
        data = response.json()

        # Check if request succeeded
        if response.status_code == 200:
            temp_c = data["current"]["temp_c"]
            temp_f = data["current"]["temp_f"]
            humidity = data["current"]["humidity"]
            weather_desc = data["current"]["condition"]["text"]
            wind_speed = data["current"]["wind_kph"]

            print(f"\n Weather Details for {city_name.title()}:")
            print(f" Temperature: {temp_c}°C / {temp_f}°F")
            print(f" Humidity: {humidity}%")
            print(f" Condition: {weather_desc}")
            print(f" Wind Speed: {wind_speed} km/h\n")
            
        elif response.status_code == 400:
            print("\n Error: City not found. Please check the spelling.\n")
        else:
            print(f"\n Error: {data.get('error', {}).get('message', 'Failed to fetch weather data.')}\n")

    except requests.exceptions.RequestException:
        print("\n Network Error: Please check your internet connection.\n")

def main():
    print("=" * 40)
    print("      Welcome to Weather App      ")
    print("=" * 40)
    
    while True:
        city = input("Enter city name (or type 'exit' to quit): ").strip()
        
        if city.lower() == 'exit':
            print("Thank you for using Weather App. Goodbye!")
            break
            
        if not city:
            print("Error: City name cannot be empty. Please enter a valid name.\n")
            continue
            
        get_weather(city)

if __name__ == "__main__":
    main()