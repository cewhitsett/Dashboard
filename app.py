from flask import Flask, render_template, request, jsonify
import requests
from config import weather_key, defaultWeather

app = Flask(__name__)
weatherUrl = "http://api.openweathermap.org/data/"
values = {
    "lastWeather": defaultWeather
}

@app.route("/")
def index():
    print("buy")
    return render_template("index.html")


@app.route("/weather/<lat>/<lon>")
def weather(lat,lon):
    url = weatherUrl + "/2.5/weather?lat={}&lon={}&appid={}"
    r = requests.get(url.format(lat,lon,weather_key))
    data = r.json()
    if data["cod"] < 200 or data["cod"] > 299:
        print("Error, couldn't get data")
        return jsonify(values["lastWeather"])
    else:
        values["lastWeather"] = data
    print("Hey")
    return jsonify(data)
if __name__ == "__main__":
    app.debug = True
    app.run()
