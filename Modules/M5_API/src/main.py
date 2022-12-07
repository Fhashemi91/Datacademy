from fastapi import FastAPI
from pydantic import BaseModel
import os
import json

app = FastAPI()
dataPath = os.path.join(os.getcwd().split('datacademy')[0], "datacademy", "data", "M5_API", "customers.json")

with open(dataPath, 'rb') as jsonFile:
    customers = json.load(jsonFile)
    customers = {i: customers[str(i)] for i in range(len(customers.keys()))}

# API GET Request(s) ####
@app.get("/get-customer/{customerId}")
def get_customer(customerId: int):
    if customerId not in customers:
        return {"Error", "Customer does not exists yet."}
    return customers[customerId]


@app.get("/get-customer-by-name/")
def get_customer_by_name(lastName: str):
    for customerId in customers:
        if customers[customerId]['lastName'] == lastName:
            return customers[customerId]

    return {"Error", f"Customer with last name: '{lastName}' does not exists"}


@app.get("/get-customers/")
def get_customers(skip: int = 0, limit: int = 3):
    return {i: customers[i] for i in range(skip, min(skip+limit, len(customers)))}


# API POST Request(s) ####
@app.post("/create-customer/{customerId}")
def create_customer(customerId: int, firstName: str, lastName: str, address: str):
    if customerId in customers:
        return {"Error", f"customerId already used, next id available is: {max(customers.keys())+1}."}

    customers[customerId] = {
        "firstName": firstName,
        "lastName": lastName,
        "address": address
    }
    return customers[customerId]


@app.post("/create-customer-auto-increment/")
def create_customer_autoincrement(firstName: str, lastName: str, address: str):
    customerId = max(customers.keys()) + 1

    customers[customerId] = {
        "firstName": firstName,
        "lastName": lastName,
        "address": address
    }
    return customers[customerId]


# API PUT Request(s) ####
@app.put("/update-customer-address/{customerId}")
def update_customer_address(customerId: int, address: str):
    if customerId not in customers:
        return {"Error", "Customer does not exists."}

    customers[customerId]['address'] = address
    return customers[customerId]


@app.put("/update-customer-address-by-name/")
def update_customer_address_by_name(firstName: str, lastName: str, address: str):
    for customerId in customers:
        if customers[customerId]['firstName'] == firstName and customers[customerId]['lastName'] == lastName:
            customers[customerId]['address'] = address

            return customers[customerId]


# API DELETE Request(s) ####
@app.delete("/delete-customer/{customerId}")
def delete_customer(customerId: int):
    if customerId not in customers:
        return {"Error", "Customer does not exists."}

    del customers[customerId]
    return {"Message": f"Customer {customerId} deleted successfully."}


@app.delete("/delete-customer-by-name/")
def delete_customer_by_name(firstName: str, lastName: str):
    foundCustomer = False
    for customer in customers:
        if customers[customer]['firstName'] == firstName and customers[customer]['lastName'] == lastName:
            foundCustomer = True
            del customers[customer]
            break

    if not foundCustomer:
        return {"Error": "The customer you are trying to delete does not exist."}
    else:
        return {"Message": f"Customer {firstName} {lastName} deleted successfully."}
