import requests # for access the request library you need to install the request library

def get_air_quality(city_name, waqi_token):
    waqi_url = f"https://api.waqi.info/feed/{city_name}/?token={waqi_token}"
    
    response = requests.get(waqi_url)
    air_quality_data = response.json()

    if 'data' in air_quality_data and air_quality_data['data']:
        aqi = air_quality_data['data']['aqi']
        iaqi = air_quality_data['data'].get('iaqi', {})

        print(f"Air Quality in {city_name}: (AQI: {aqi})")
        print("Pollutants:")
        for pollutant, data in iaqi.items():
            print(f"  {pollutant}: {data['v']} µg/m³")
    else:
        print("Air quality data not available.")

waqi_token = "667d0df116fce45789e187f8d3c47ee3848c8885"
city_name = input("Enter the city name: ")
get_air_quality(city_name, waqi_token)
