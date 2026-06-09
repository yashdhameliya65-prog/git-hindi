from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Employee(BaseModel):
    id : int
    name : str
    salery : float
    position : str

employees : List[Employee] = []

@app.get("/")
def read_root():
    return("welcome to our company")

@app.get("/employees")
def get_employees():
    return employees

@app.post("/employees")
def add_employee(employee: Employee):
    employees.append(employee)
    return employee

@app.put("/employees")
def updated_employee(id: int, employee: Employee):
    for i in range(len(employees)):
        if employees[i].id == id:
            employees[i] = employee
            return "employee updated"
    return "not found"

@app.delete("/employees")
def deleted_employees(id: int): 
    for i in range(len(employees)):
        if employees[i].id == id:
            del employees[i]
            return "employee deleted"
    return "not found"
