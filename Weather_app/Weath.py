
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

WEATHER_CODES = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Heavy Drizzle",
    61: "Light Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    71: "Light Snow",
    73: "Moderate Snow",
    75: "Heavy Snow",
    80: "Rain Showers",
    81: "Moderate Rain Showers",
    82: "Heavy Rain Showers",
    95: "Thunderstorm",
    96: "Thunderstorm with Hail",
    99: "Thunderstorm with Hail"
}


def get_weather(city):
    # Find the city coordinates
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(
        geo_url,
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        },
        timeout=10
    )
    response.raise_for_status()
    results = response.json().get("results", [])

    if not results:
        return None, "City not found. Please enter a valid city."

    place = results[0]

    # Fetch current weather
    weather_url = "https://api.open-meteo.com/v1/forecast"

    response = requests.get(
        weather_url,
        params={
            "latitude": place["latitude"],
            "longitude": place["longitude"],
            "current": (
                "temperature_2m,relative_humidity_2m,"
                "apparent_temperature,precipitation,"
                "weather_code,wind_speed_10m"
            ),
            "timezone": "auto"
        },
        timeout=10
    )
    response.raise_for_status()

    data = response.json()
    current = data["current"]

    location = [place["name"]]
    if place.get("admin1"):
        location.append(place["admin1"])
    if place.get("country"):
        location.append(place["country"])

    weather = {
        "city": ", ".join(location),
        "time": current["time"],
        "temperature": current["temperature_2m"],
        "feels_like": current["apparent_temperature"],
        "humidity": current["relative_humidity_2m"],
        "wind": current["wind_speed_10m"],
        "precipitation": current["precipitation"],
        "condition": WEATHER_CODES.get(
            current["weather_code"], "Other Conditions"
        )
    }

    return weather, None


@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if not city:
            error = "Please enter a city name."
        else:
            try:
                weather, error = get_weather(city)
            except requests.exceptions.RequestException:
                error = (
                    "Unable to connect to the weather service. "
                    "Check your internet connection and try again."
                )
            except (KeyError, ValueError, TypeError):
                error = "Unable to read weather data. Please try again."

    return render_template(
        "index.html",
        weather=weather,
        error=error,
        city=city
    )


if __name__ == "__main__":
    app.run(debug=True)
