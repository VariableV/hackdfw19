import requests, json, time, datetime, random
from firebase import firebase

global FirebaseURL
global PasswordString
FirebaseURL = 'https://lendaspacev2.firebaseio.com/'
PasswordString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

#Go Through Users
def GetData():
    Firebase = firebase.FirebaseApplication(FirebaseURL, None)
    UsersData = Firebase.get('/Users', None)
    arr = []
    for key,value in UsersData.items():
        UserFullName, UserPhone, arr = RasterizeData(key, Firebase)
        tmp = [UserFullName, UserPhone, arr]
        arr.append(tmp)

    return arr

#Get All Data From Specific User
def RasterizeData(UserName, Firebase):
    CurentUser = Firebase.get('/Users', f'{str(UserName)}')
    UserInfo = CurentUser['UserInfo']
    UserParking = CurentUser['UserParking']

    UserFullName = UserInfo['name']
    #UserPassword = UserInfo['password']
    UserPhone = UserInfo['phone']

    arr = []
    for CurrentLot,v in UserParking.items():
        LotLocation = v['address']
        LotCount = v['count']
        LotImage = v['imageURL']
        LotName = v['lotname']
        LotPPH = v['pricing']
        LotTimeStart = v['time-start']
        LotTimeEnd = v['time-end']
        tmp = [CurrentLot, LotLocation, LotCount, LotImage, LotName, LotPPH, LotTimeStart, LotTimeEnd]
        arr.append(tmp)
    
    return UserFullName, UserPhone, arr

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

#GetData()