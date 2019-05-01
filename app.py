from flask import Flask, render_template, request, jsonify
import requests
from config import weather_key, defaultWeather, myClasses

app = Flask(__name__)

values = {
    "lastWeather": defaultWeather
}


@app.route("/getclasses")
def getclasses():
    return jsonify(myClasses)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather/<lat>/<lon>")
def weather(lat,lon):
    url = "http://api.openweathermap.org/data/"
    url += "2.5/weather?lat={}&lon={}&appid={}&units={}"
    url = url.format(lat,lon,weather_key,"imperial")

    r = requests.get(url.format(lat,lon,weather_key,"imperial"))
    data = r.json()

    if int(data["cod"]) < 200 or int(data["cod"]) > 299:
        print("Error, couldn't get data")
        return jsonify(values["lastWeather"])
    else:
        values["lastWeather"] = data

    return jsonify(data)


if __name__ == "__main__":
    app.debug = True
    app.run()
