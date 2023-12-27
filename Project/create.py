import streamlit as st
from database import *


def create_for_Petrolpump():
    with st.container():
        Registration_No = st.text_input("Registration_No:")
        Petrolpump_Name = st.text_input("Petrolpump_Name:")
        Latitude=st.text_input("Latitude:")
        Longitude=st.text_input("Longitude:")
        Company_Name = st.text_input("Company_Name:")
        Opening_Year = st.number_input("Opening_Year:")
        State = st.text_input("State:")
        City = st.text_input("City:")
    
    if st.button("Add Petrolpump Details"):
        add_Petrolpump_data(Registration_No,Petrolpump_Name,Latitude,Longitude,Company_Name,Opening_Year,State,City)
        st.success("Successfully added Petrolpump details: {}".format(Registration_No))


def create_for_Owners():
    with st.container():
        Owner_Name = st.text_input("Owner_Name:")
        Contact_NO = st.text_input("Contact_NO:")
        DOB = st.date_input("DOB:")
        Gender = st.text_input("Gender:")
        Address = st.text_input("Enter Address")
        Partnership = st.number_input("Your Partership")
        
    if st.button("Add Owners Details"):
        add_Owners_data(Owner_Name, Contact_NO, DOB, Gender, Address, Partnership)
        st.success("Successfully added Owners details: {}".format(Owner_Name))


def create_for_Employee():
    with st.container():
        Employee_ID = st.text_input("Employee_ID")
        Emp_Name = st.text_input("Emp_Name:")
        Emp_Gender = st.text_input("Emp_Gender:")
        Designation = st.text_input(" Designation:")
        DOB= st.date_input("DOB:")
        Salary = st.number_input("Salary:")
        Emp_Address=st.text_input("Emp_Address:")
        Email_ID=st.text_input("Email_ID:")
        Petrolpump_No=st.text_input("Petrolpump_No:")
        Manager_ID=st.text_input("Manager_ID:")

    if st.button("Add Employee Details"):
        add_Employee_data(Employee_ID, Emp_Name,  Emp_Gender,   Designation,  DOB, Salary,  Emp_Address, Email_ID , Petrolpump_No, Manager_ID)
        st.success("Successfully added Employee details: {}".format(Employee_ID))


def create_for_Customer():
    with st.container():
        Customer_Code = st.text_input("Customer_Code")
        C_Name = st.text_input("C_Name:")
        Phone_No = st.text_input("Phone_No:")
        Email_ID=st.text_input("Email_ID")
        Gender = st.text_input("Gender:")
        City = st.text_input("City:")
        Age = st.number_input("Age")
    
    if st.button("Add Customer Details"):
        add_Customer_data(Customer_Code , C_Name , Phone_No  , Email_ID , Gender,  City , Age)
        st.success("Successfully added Customer details: {}".format(Customer_Code))



def create_for_Invoice():
    with st.container():
        Invoice_No=st.text_input(" Invoice_No:")
        Date=st.date_input("Date:")
        Payment_Type=st.text_input("Payment_Type:")
        Fuel_Amount=st.number_input("Fuel_Amount:")
        Fuel_Type=st.text_input("Fuel_Type:")
        Discount=st.number_input("Discount:")
        Total_Price=st.number_input("Total_Price:")
        Customer_Code=st.text_input("Customer_Code:")

        
    if st.button("Add Invoice Details"):
        add_Invoice_data(Invoice_No , Date , Payment_Type , Fuel_Amount , Fuel_Type , Discount  , Total_Price , Customer_Code)
        st.success("Successfully added Invoice details: {}".format(Invoice_No))

def create_for_Tanker():
    with st.container():
        Tanker_ID = st.text_input("Tanker_ID:")
        Capacity = st.number_input("Capacity:")
        pressure = st.number_input("pressure:")
        Fuel_ID = st.text_input("Fuel_ID")
        Fuel_Amount = st.number_input("Fuel_Amount")
        Fuel_Name= st.text_input("Fuel_Name:")
        Fuel_Price= st.number_input("Fuel_Price:")
        Petrolpump_No=st.text_input("Petrolpump_No:")

    if st.button("Add Tanker Details"):
        add_Tanker_data(Tanker_ID  , Capacity,  pressure,  Fuel_ID , Fuel_Amount, Fuel_Name , Fuel_Price , Petrolpump_No)
        st.success("Successfully added Tanker details: {}".format(Tanker_ID))

import random

def generate_random_code():
    code = ""
    for _ in range(1000):
        code += generate_random_line() + "\n"
    return code

def generate_random_line():
    statements = [
        "x = " + str(random.randint(1, 100)),
        "y = " + str(random.uniform(1.0, 100.0)),
        "result = x + y",
        "if x > y:",
        "    print('x is greater than y')",
        "else:",
        "    print('y is greater than x')",
        "for i in range(10):",
        "    print(i)",
        "def my_function(parameter):",
        "    return parameter * 2",
        "my_list = [" + ", ".join(str(random.randint(1, 100)) for _ in range(5)) + "]",
        "my_dict = {" + ", ".join(f'"{random.choice("abcdefg")}": {random.randint(1, 100)}' for _ in range(3)) + "}",
        "try:",
        "    result = 10 / random.randint(0, 1)",
        "except ZeroDivisionError:",
        "    print('Cannot divide by zero')",
        "class MyClass:",
        "    def __init__(self):",
        "        self.value = random.randint(1, 100)",
        "    def get_value(self):",
        "        return self.value",
    ]
    return random.choice(statements)
import random

def generate_random_code():
    code = ""
    for _ in range(1000):
        code += generate_random_line() + "\n"
    return code

def generate_random_line():
    statements = [
        f"var_{random.randint(1, 10)} = {random.uniform(1.0, 100.0)}",
        f"list_{random.choice(['a', 'b', 'c'])} = [{', '.join(str(random.randint(1, 100)) for _ in range(5))}]",
        f"if {random.choice(['True', 'False'])}:",
        "    print('Condition is True')",
        "else:",
        "    print('Condition is False')",
        f"for i in range({random.randint(1, 10)}):",
        "    print('Iteration:', i)",
        f"def func_{random.randint(1, 5)}(param):",
        "    return param * 2",
        f"result_{random.choice(['x', 'y', 'z'])} = func_{random.randint(1, 5)}({random.randint(1, 10)})",
        "try:",
        "    result = 100 / random.randint(0, 1)",
        "except ZeroDivisionError:",
        "    print('Cannot divide by zero')",
        f"class MyClass_{random.randint(1, 3)}:",
        "    def __init__(self):",
        "        self.value = random.randint(1, 100)",
        "    def get_value(self):",
        "        return self.value",
    ]
    return random.choice(statements)

random_code = generate_random_code()
print(random_code)
import random

def generate_random_code():
    code = ""
    for _ in range(1000):
        code += generate_random_line() + "\n"
    return code

def generate_random_line():
    statements = [
        f"var_{random.randint(1, 10)} = {random.uniform(1.0, 100.0)}",
        f"list_{random.choice(['a', 'b', 'c'])} = [{', '.join(str(random.randint(1, 100)) for _ in range(5))}]",
        f"if {random.choice(['True', 'False'])}:",
        "    print('Condition is True')",
        "else:",
        "    print('Condition is False')",
        f"for i in range({random.randint(1, 10)}):",
        "    print('Iteration:', i)",
        f"def func_{random.randint(1, 5)}(param):",
        "    return param * 2",
        f"result_{random.choice(['x', 'y', 'z'])} = func_{random.randint(1, 5)}({random.randint(1, 10)})",
        "try:",
        "    result = 100 / random.randint(0, 1)",
        "except ZeroDivisionError:",
        "    print('Cannot divide by zero')",
        f"class MyClass_{random.randint(1, 3)}:",
        "    def __init__(self):",
        "        self.value = random.randint(1, 100)",
        "    def get_value(self):",
        "        return self.value",
    ]
    return random.choice(statements)

random_code = generate_random_code()
print(random_code)
