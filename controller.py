from flask import Flask, jsonify, request
import uuid
import os
import json
from datetime import date, datetime


def create_hold(request_body):
    hold_id = str(uuid.uuid4())
    # logic for write data to text file
    hold_data_init = {
        "holds":[{
        "user_id": request_body["user_id"],
        "book_id": request_body["book_id"],
        "hold_id": hold_id,
        "created_at": createDate()
        }
        ]
    }
    hold_data = {
        "user_id": request_body["user_id"],
        "book_id": request_body["book_id"],
        "hold_id": hold_id,
        "created_at": createDate()
    }


    if os.path.getsize('holds.json') != 0:
        with open('holds.json', 'r') as json_file:
            addingHold = json.load(json_file)
            
            addingHold["holds"].append(hold_data)

        with open("holds.json", "w") as json_file:
            json.dump(addingHold, json_file, indent = 4, ensure_ascii=False)
            
    else:
        with open("holds.json", "w") as json_file:
            json.dump(hold_data_init, json_file, indent = 4, ensure_ascii=False)            
    
    return hold_data

def createDate():
    created_at = datetime.now()
    year = created_at.year
    day = created_at.day
    month = created_at.month
    if(month < 10 and day < 10):
        todaysDate = str(year) + "-0" + str(month) + "-0" + str(day)
    elif (month < 10):
        todaysDate = str(year) + "-0" + str(month) + "-" + str(day)
    elif(day < 10):
        todaysDate = str(year) + "-" + str(month) + "-0" + str(day)
    else:
        todaysDate = str(year) + "-" + str(month) + "-" + str(day)

    return todaysDate

def check_holds(book_id):
    if os.path.getsize('holds.json') == 0:
        return "Success"
    else:
        with open('holds.json', 'r') as json_file:
            data = json.load(json_file)
        
        holds = data["holds"]
        for hold in holds:
            if hold['book_id'] == book_id:
                return "Unavailable"           
        return "Success"
    
def retrieveHold(book_id):

    if os.path.getsize('holds.json') != 0:
            
        with open('holds.json', 'r') as json_file:
            data = json.load(json_file)
        
        holds = data["holds"]

        for hold in holds:
        
            if hold['book_id'] == book_id:
                return hold
    else:
        return {"message": "No holds"}        

def removeHold(book_id, user_id):
    foundBook = False
    with open('holds.json', 'r') as json_file:
        data = json.load(json_file)
    
    holds = data["holds"]
    for hold in holds:
        if hold['book_id'] == book_id and hold['user_id'] == user_id:
            delete_confirm = {
        "user_id": hold["user_id"],
        "book_id": hold["book_id"],
        "hold_id": hold["hold_id"],
        "created_at": hold["created_at"]
    }       
            data["holds"].remove(hold)
            foundBook = True

    if foundBook == False:
        delete_confirm = {
    "user_id": "N/A",
    "book_id": book_id,
    "hold_id": "N/A",
    "created_at": "N/A"
        }

    
    with open('holds.json', "w") as json_file:
        json.dump(data, json_file, indent = 4, ensure_ascii=False)

    return delete_confirm
