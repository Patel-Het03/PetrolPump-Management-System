import pandas as pd
import streamlit as st
from database import *

def delete_for_Petrolpump():
    result = view_all_Petrolpump_data()
    df = pd.DataFrame(result, columns=['Registration_No','Petrolpump_Name','Latitude','Longitude','Company_Name','Opening_Year','State','City'])
    with st.expander("View all Petrolpump"):
        st.dataframe(df)

    list_of_Petrolpump = [i[0] for i in view_only_Registration_No()]
    selected_Petrolpump = st.selectbox("Petrolpump to delete", list_of_Petrolpump)
    st.warning("Do you want to delete ::{}".format(selected_Petrolpump))
    if st.button("Delete Petrolpump"):
        delete_data_Petrolpump(selected_Petrolpump)
        st.success("Petrolpump has been deleted successfully")
    result2 = view_all_Petrolpump_data()
    df2 = pd.DataFrame(result2, columns=['Registration_No','Petrolpump_Name','Latitude','Longitude','Company_Name','Opening_Year','State','City'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def delete_for_Owners():
    result = view_all_Owners_data()
    df = pd.DataFrame(result, columns=['Owner_Name', 'Contact_NO', 'DOB', 'Gender', 'Address', 'Partnership'])
    with st.expander("View all Owners"):
        st.dataframe(df)

    list_of_Owners = [i[0] for i in view_only_Owner_Name()]
    selected_Owners = st.selectbox("Owners to delete", list_of_Owners)
    st.warning("Do you want to delete ::{}".format(selected_Owners))
    if st.button("Delete Owners"):
        delete_data_Owners(selected_Owners)
        st.success("Owners has been deleted successfully")

    result2 = view_all_Owners_data()
    df2 = pd.DataFrame(result2, columns=['Owner_Name', 'Contact_NO', 'DOB', 'Gender', 'Address', 'Partnership'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def delete_for_Employee():
    result = view_all_Employee_data()
    df = pd.DataFrame(result, columns=['Employee_ID', 'Emp_Name', 'Emp_Gender', 'Designation','DOB', 'Salary', 'Emp_Address', 'Email_ID' , 'Petrolpump_No', 'Manager_ID'])
    with st.expander("View all Employee"):
        st.dataframe(df)

    list_of_Employee = [i[0] for i in view_only_Employee_ID()]
    selected_Employee = st.selectbox("Employee to delete", list_of_Employee)
    st.warning("Do you want to delete ::{}".format(selected_Employee))
    if st.button("Delete Employee"):
        delete_data_Employee(selected_Employee)
        st.success("Employee has been deleted successfully")
    result2 = view_all_Employee_data()
    df2 = pd.DataFrame(result2, columns=['Employee_ID', 'Emp_Name', 'Emp_Gender', 'Designation','DOB', 'Salary', 'Emp_Address', 'Email_ID' , 'Petrolpump_No', 'Manager_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def delete_for_Customer():
    result = view_all_Customer_data()
    df = pd.DataFrame(result, columns=['Customer_Code', 'C_Name' , 'Phone_No', 'Email_ID' , 'Gender', 'City' , 'Age'])
    with st.expander("View all Customer"):
        st.dataframe(df)

    list_of_Customer = [i[0] for i in view_only_Customer_Code()]
    selected_Customer = st.selectbox("Customer to delete", list_of_Customer)
    st.warning("Do you want to delete ::{}".format(selected_Customer))
    if st.button("Delete customer"):
        delete_data_Customer(selected_Customer)
        st.success("customer has been deleted successfully")
    result2 = view_all_Customer_data()
    df2= pd.DataFrame(result2, columns=['Customer_Code', 'C_Name' , 'Phone_No', 'Email_ID' , 'Gender', 'City' , 'Age'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def delete_for_Invoice():
    result = view_all_Invoice_data()
    df = pd.DataFrame(result, columns=['Invoice_No' , 'Date' , 'Invoice_Type' , 'Fuel_Amount' , 'Fuel_Type' , 'Discount' , 'Total_Price' , 'Customer_Code'])
    with st.expander("View all Invoices"):
        st.dataframe(df)

    list_of_Invoices = [i[0] for i in view_only_Invoice_No()]
    selected_Invoice = st.selectbox("Invoices to delete", list_of_Invoices)
    st.warning("Do you want to delete ::{}".format(selected_Invoice))
    if st.button("Delete Invoice"):
        delete_data_Invoice(selected_Invoice)
        st.success("transaction has been deleted successfully")
    result2 = view_all_Invoice_data()
    df2 = pd.DataFrame(result2, columns=['Invoice_No' , 'Date' , 'Invoice_Type' , 'Fuel_Amount' , 'Fuel_Type' , 'Discount' , 'Total_Price' , 'Customer_Code'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def delete_for_Tanker():
    result = view_all_Tanker_data()
    df = pd.DataFrame(result, columns=['Tanker_ID', 'Capacity', 'pressure', 'Fuel_ID' , 'Fuel_Amount', 'Fuel_Name' , 'Fuel_Price' , 'Petrolpump_No'])
    with st.expander("View all Tankers"):
        st.dataframe(df)

    list_of_Tanker = [i[0] for i in view_only_Tanker_ID()]
    
    selected_Tanker = st.selectbox("Tanker to delete", list_of_Tanker)
    st.warning("Do you want to delete ::{}".format(selected_Tanker))
    if st.button("Delete Tanker"):
        delete_data_Tanker(selected_Tanker)
        st.success("Tanker has been deleted successfully")
    result2 = view_all_Tanker_data()
    df2 = pd.DataFrame(result2, columns=['Tanker_ID', 'Capacity', 'pressure', 'Fuel_ID' , 'Fuel_Amount', 'Fuel_Name' , 'Fuel_Price' , 'Petrolpump_No'])
    with st.expander("Updated data"):
        st.dataframe(df2)


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
