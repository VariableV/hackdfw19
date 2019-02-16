from flask import Flask, render_template
import json

web = Flask(__name__)

@web.route("/")
def main():
    # data format:
    # image, space, lot capacity
    addy = "909 Araf Ave, Richardson, TX"
    addy2 = "9615 Hillview Drive, Dallas, TX"
    data = [
        ["https://www.bdcnetwork.com/sites/bdc/files/parking.jpg", "Saad's house", addy, "https://google.com/maps/place/"+addy.replace(" ", "+"), 2, 12.99]
        ,["https://www.bdcnetwork.com/sites/bdc/files/parking.jpg", "Owen's house", addy2, "https://google.com/maps/place/"+addy2.replace(" ", "+"), 3, 12.99]
    ]
    return render_template("index.html", data = data)

if __name__ == "__main__":
    web.run()
