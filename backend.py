from flask import Flask, render_template
import maindb
import json

web = Flask(__name__)

"""
Things to do
-> Purchase button
-> Register (FUNCTION-owen + HTML-maheen)
-> Login (FUNCTION-owen + HTML-maheen)
-> Add a Lot (FUNCTION-owen + HTML-maheen)
"""


"""
[
    ['Jake Schmelling', '2134443922', [
        ['BfAJQAkYFDtwJpzVRcEmumLK', '123 Main St, Richardson, TX 75081', 65, 'https://cdn.discordapp.com/attachments/529866501667422208/546432963714351104/blog65-1.jpg', 'Living Parking Homes', 234.99, 'gg','gg'], 
        ['PGjWfhtKxsJhOMCXZuVZDEiz', '9393 Whistle Stop Pl, Dallas, TX 75231', 21, 'https://cdn.discordapp.com/attachments/529866518180265993/546456578241593374/DART-Lake-Highlands-Station-04.jpg', 'Train Stop - Royal', 124, 'gg', 'gg']
    ]], 
    ['John Doe', 2147845597, [
        ['CMOkbddIsEWKxFbWZJSQCqQO', '2620 N Houston St, Dallas, TX 75201', 5000, 'https://cdn.discordapp.com/attachments/541399521352220682/546467783626719242/LTG-AmericanAirlinesCenter-Parking-DallasTX_110916-003w625h400.jpg', 'The Lexus Garage At The American Airlines Center', 50000, 'gg', 'gg']
    ]], 
    ['Saad Zafar', 5147773228, [
        ['wfoFJHNoDOOsYjdHsVWmdJcF', '9393 Whistle Stop Pl, Dallas, TX 75231', 85, 'https://cdn.discordapp.com/attachments/541399521352220682/546468409630523403/DART-Lake-Highlands-Station-04.jpg', 'Whistle Stop Parking Lot', 1200, 'gg', 'gg']
    ]]
    ]
"""

@web.route("/rent")
def penis():
    x = maindb.GetData()
    data = []
    for i in x:
        important = i[2]
        for j in range(0, len(important)):
            # image, lotname, lotloc, googlemaps, lotcount, lotpph, name, phone, end time, start time
            tmp = [important[j][3], important[j][4], important[j][1], "https://google.com/maps/place/"+important[j][1].replace(" ", "+"), important[j][2], important[j][5], i[0], i[1], important[j][6], important[j][7]]
            data.append(tmp)
    return render_template("rent-out.html", data = data)

@web.route("/")
def main():
    # data format:
    # image, space, lot capacity
    #addy = "909 Araf Ave, Richardson, TX"
    #addy2 = "9615 Hillview Drive, Dallas, TX"
    #UserFullName, UserPhone, LotLocation, LotCount, LotImage, LotName, LotPPH, LotTimeStart, LotTImeEnd = maindb.GetData("User1")
    #data = [
    #    [LotImage, LotName, LotLocation, "https://google.com/maps/place/"+LotLocation.replace(" ", "+"), LotCount, LotPPH]
    #    ["https://www.bdcnetwork.com/sites/bdc/files/parking.jpg", "Saad's house", addy, "https://google.com/maps/place/"+addy.replace(" ", "+"), 2, 12.99]
    #    ,["https://www.bdcnetwork.com/sites/bdc/files/parking.jpg", "Owen's house", addy2, "https://google.com/maps/place/"+addy2.replace(" ", "+"), 3, 12.99]
    #]
    return render_template("index.html")


if __name__ == "__main__":
    web.run()