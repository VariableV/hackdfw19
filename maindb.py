import requests, json, time, datetime, random
from firebase import firebase

global FirebaseURL
global PasswordString
FirebaseURL = 'https://lendaspacev2.firebaseio.com/'
LotIDString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

#Go Through Users
def GetData():
    Firebase = firebase.FirebaseApplication(FirebaseURL, None)
    UsersData = Firebase.get('/Users', None)
    arr = []
    for key,value in UsersData.items():
        UserFullName, UserPhone, xd = IterateData(key, Firebase)
        tmp = [UserFullName, UserPhone, xd]
        arr.append(tmp)

    return arr

#Get All Data From Specific User
def IterateData(UserName, Firebase):
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
def RegisterUser():
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

#Add A Lot
def AddLot():
    LotID = ""
    for x in range(24):
        Letter = random.choice(LotIDString)
        LotID = LotID + Letter
