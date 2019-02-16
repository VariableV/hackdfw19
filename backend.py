from flask import Flask, render_template
#import maindb
import json

web = Flask(__name__)

"""
Things to do
-> Popup modal
    -> Owner name
    -> Phone Number
    -> Purchase button
-> Register
-> Login
-> Add a lot button
"""

@web.route("/")
def main():
    # data format:
    # image, space, lot capacity
    addy = "909 Araf Ave, Richardson, TX"
    addy2 = "9615 Hillview Drive, Dallas, TX"
    #UserFullName, UserPhone, LotLocation, LotCount, LotImage, LotName, LotPPH, LotTimeStart, LotTImeEnd = maindb.GetData("User1")
    data = [
    #    [LotImage, LotName, LotLocation, "https://google.com/maps/place/"+LotLocation.replace(" ", "+"), LotCount, LotPPH]
        ["https://www.bdcnetwork.com/sites/bdc/files/parking.jpg", "Saad's house", addy, "https://google.com/maps/place/"+addy.replace(" ", "+"), 2, 12.99]
        ,["https://www.bdcnetwork.com/sites/bdc/files/parking.jpg", "Owen's house", addy2, "https://google.com/maps/place/"+addy2.replace(" ", "+"), 3, 12.99]
    ]
    """x = maindb.GetData()
    data = []
    for i in x:
        tmp = [i[4], i[5], i[2], i[2].replace(" ", "+"), i[3], i[6]]
        data.append(tmp)"""
    return render_template("index.html", data = data)

if __name__ == "__main__":
    web.run()