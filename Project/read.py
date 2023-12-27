import pandas as pd
import streamlit as st
from database import *


def read_for_Petrolpump():
    result = view_all_Petrolpump_data()
    df = pd.DataFrame(result, columns=['Registration_No','Petrolpump_Name','Company_Name','Opening_Year','State','City'])
    with st.expander("View all Petrolpumps"):
        st.dataframe(df)

def read_for_Owners():
    result = view_all_Owners_data()
    df = pd.DataFrame(result, columns=['Owner_Name', 'Contact_NO', 'DOB', 'Gender', 'Address', 'Partnership'])
    with st.expander("View all Owners"):
        st.dataframe(df)

def read_for_Employee():
    result = view_all_Employee_data()
    df = pd.DataFrame(result, columns=['Employee_ID', 'Emp_Name', 'Emp_Gender', 'Designation', 'DOB', 'Salary',  'Emp_Address', 'Email_ID' , 'Petrolpump_No', 'Manager_ID'])
    with st.expander("View all Employees"):
        st.dataframe(df)

def read_for_Customer():
    result = view_all_Customer_data()
    df = pd.DataFrame(result, columns=['Customer_Code', 'C_Name' , 'Phone_No' , 'Email_ID' , 'Gender', 'City' , 'Age'])
    with st.expander("View all Customers"):
        st.dataframe(df)

def read_for_Invoice():
    result = view_all_Invoice_data()
    df = pd.DataFrame(result, columns=['Invoice_No' , 'Date','Payment_Type', 'Fuel_Amount' , 'Fuel_Type' , 'Discount' , 'Total_Price' , 'Customer_Code'])
    with st.expander("View all Invoices"):
        st.dataframe(df)

def read_for_Tanker():
    result = view_all_Tanker_data()
    df = pd.DataFrame(result, columns=['Tanker_ID', 'Capacity', 'pressure', 'Fuel_ID' , 'Fuel_Amount', 'Fuel_Name' , 'Fuel_Price' , 'Petrolpump_No'])
    with st.expander("View all Tankers"):
        st.dataframe(df)

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
