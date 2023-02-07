import json
import os
from fastapi import FastAPI

"""
As done with all other assignments, after completion of all exercises please push this directory using Git.
Execution of 'git add .\Modules\M05_API\ ', then committing these changes and eventually pushing them will start the pre-written test code.
This code will test whether the APIs that you created conform to the asked functionality.
For a more detailed description about how to execute and review these tests, we ask you to return to either the (M03) SQL or (M04) ML course.
At the bottom of these notebooks all steps are discussed in great detail.
"""

app = FastAPI()
# dataPath = os.path.join(os.getcwd().split('datacademy_demo')[0], "datacademy_demo", "data", "M5_API", "customers.json") 
dataPath = os.path.join("data", "M05_API", "customers.json")

with open(dataPath, 'rb') as jsonFile:
    customers = json.load(jsonFile)
    customers = {i: customers[str(i)] for i in range(len(customers.keys()))}

# API GET Request(s) ####
@app.get("/get-customer/{customerId}")
def get_customer(customerId: int):
    if customerId not in customers:
        return {"Error", "Customer does not exists yet."}
    return customers[customerId]

#TODO: Create get request with end point: "/get-customer-by-name/{lastName}"
...



#TODO: Create get request with end point: "/get-customers/"
...



# API POST Request(s) ####
@app.post("/create-customer/{customerId}")
def create_customer(customerId: int, firstName: str, lastName: str, address: str):
    if customerId in customers:
        return {"Error", f"customerId already used, next id available is: {max(customers.keys())+1}."}
        
    if (customerId - max(customers.keys())) > 1:
        return {"Error", f"customerId do not fit neatly together, next id available is: {max(customers.keys())+1}."}

    customers[customerId] = {
        "firstName": firstName,
        "lastName": lastName,
        "address": address
    }
    return customers[customerId]

#TODO: Create post request with end point: "/create-customer-auto-increment/"
...




# API PUT Request(s) ####
@app.put("/update-customer-address/{customerId}")
def update_customer_address(customerId: int, address: str):
    if customerId not in customers:
        return {"Error", "Customer does not exists."}

    customers[customerId]['address'] = address
    return customers[customerId]

#TODO: Create put request with end point: "/update-customer-address-by-name/"
...




# API DELETE Request(s) ####
@app.delete("/delete-customer/{customerId}")
def delete_customer(customerId: int):
    if customerId not in customers:
        return {"Error", "Customer does not exists."}

    del customers[customerId]
    return {"Message": f"Customer {customerId} deleted successfully."}

#TODO: Create delete request with end point: "/delete-customer-by-name/"
...


