import requests, json, time, datetime
from firebase import firebase

global FirebaseURL
FirebaseURL = 'https://lendaspacev2.firebaseio.com/'

#Go Through Users
def GetData():
    Firebase = firebase.FirebaseApplication(FirebaseURL, None)
    UsersData = Firebase.get('/Users', None)
    arr = []
    for key,value in UsersData.items():
        UserFullName, UserPhone, LotLocation, LotCount, LotImage, LotName, LotPPH, LotTimeStart, LotTImeEnd = RasterizeData(key, Firebase)
        tmp = [UserFullName, UserPhone, LotLocation, LotCount, LotImage, LotName, LotPPH, LotTimeStart, LotTImeEnd]
        arr.append(tmp)
    return arr

#Get All Data From Specific User
def RasterizeData(UserName, Firebase):
    CurentUser = Firebase.get('/Users', f'{str(UserName)}')
    UserInfo = CurentUser['UserInfo']
    UserParking = CurentUser['UserParking']

    UserFullName = UserInfo['name']
    UserPassword = UserInfo['password']
    UserPhone = UserInfo['phone']

    LotLocation = UserParking['address']
    LotCount = UserParking['count']
    LotImage = UserParking['imageURL']
    LotName = UserParking['lotname']
    LotPPH = UserParking['pricing']
    LotTimeStart = UserParking['time-start']
    LotTImeEnd = UserParking['time-end']

    return UserFullName, UserPhone, LotLocation, LotCount, LotImage, LotName, LotPPH, LotTimeStart, LotTImeEnd

#Add User To Database
def AddUser():
    UserName = input("UserName: ")
    firebase = firebase.FirebaseApplication(FirebaseURL, None)
    UserData = {
        "UserInfo": {
            "name": UserFullName,
            "password": UserPassword,
            "phone": UserPhone
        },
        "UserParking":  {
            "address":LotLocation,
            "count": LotCount,
            "imageURL": ImageURL,
            "lotname": LotName,
            "pricing": LotPPH,
            "time-end": LotTimeEnd,
            "time-start": LotTimeStart
        }
    }
    firebase.post(f'/Users/{str(UserName)}', None, UserData)

#GetData("User1")