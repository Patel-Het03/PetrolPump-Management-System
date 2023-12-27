
import streamlit as st
import mysql.connector
import pandas as pd

from create import *
from database import *
from delete import *
from read import *
from update import *

def main():
   st.title("Petrol Pump Management System")
   menu = ["PetrolPump", "Owners", "Employee", "Customer","Invoice", "Tanker","Custom"]
   choice = st.sidebar.selectbox("Tables", menu)

   create_table()
   
   if choice == "PetrolPump":
      menu = ["Add", "View", "Update", "remove"]
      choice2 = st.sidebar.selectbox("CRUD Operations", menu)
      if choice2 == "Add":
         st.subheader("Enter Petrolpump Details:")
         create_for_Petrolpump()
      elif choice2 == "View":
         st.subheader("View the Petrolpump details:")
         read_for_Petrolpump()
      elif choice2 == "Update":
         st.subheader("Updated petrolpump  tasks")
         update_for_Petrolpump()
      elif choice2 == "remove":
         st.subheader("Deleted petrolpump  tasks")
         delete_for_Petrolpump()

   elif choice == "Owners":
      menu = ["Add", "View", "Update", "Remove"]
      choice2 = st.sidebar.selectbox("CRUD Operations", menu)
      if choice2 == "Add":
            st.subheader("Enter Owners Details:")
            create_for_Owners()
      elif choice2 == "View":
            st.subheader("View Owners details:")
            read_for_Owners()
      elif choice2 == "Update":
            st.subheader("Update created tasks")
            update_for_Owners()
      elif choice2 == "Remove":
            st.subheader("Delete created tasks")
            delete_for_Owners()

   elif choice == "Employee":
      menu = ["Add", "View", "Update", "Remove"]
      choice2 = st.sidebar.selectbox("CRUD Operations", menu)
      if choice2 == "Add":
         st.subheader("Enter Employee Details:")
         create_for_Employee()
      elif choice2 == "View":
         st.subheader("View the Employee details:")
         read_for_Employee()
      elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Employee()
      elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Employee()

   elif choice == "Customer":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("CRUD Operations", menu)
     if choice2 == "Add":
         st.subheader("Enter trainer Details:")
         create_for_Customer()
     elif choice2 == "View":
         st.subheader("View the trainer details:")
         read_for_Customer()
     elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Customer()
     elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Customer()

   elif choice == "Invoice":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("CRUD Operations", menu)
     if choice2 == "Add":
         st.subheader("Enter Invoice Details:")
         create_for_Invoice()
     elif choice2 == "View":
         st.subheader("View the Invoice details:")
         read_for_Invoice()
     elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Invoice()
     elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Invoice()

   elif choice == "Tanker":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("CRUD Operations", menu)
     if choice2 == "Add":
         st.subheader("Enter Tanker Details:")
         create_for_Tanker()
     elif choice2 == "View":
         st.subheader("View the Tanker details:")
         read_for_Tanker()
     elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Tanker()
     elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Tanker()


   elif choice == "Custom":
      menu = ["Custom Query","Tanker_bill","NearestPetrolPump","Most_Rush_Interval"]
      choice2 = st.sidebar.selectbox("Custom", menu)
      if choice2 == "Custom Query":
         query = st.text_input("Enter Your Query:")
         if st.button("Run Query"):
            c.execute(query)
            data = c.fetchall()
            st.dataframe(data)
      elif choice2 == "Tanker_bill":
         net_value()
      elif choice2=="NearestPetrolPump":
             x=st.number_input("Enter Latitude Coordinate:")
             y=st.number_input("Enter Longitude Coordinate:")


             if st.button("Find"):
                 query = "SET @p0='{}';".format(x)
                 c.execute(query)
                 query = "SET @p1='{}';".format(y)
                 c.execute(query)
                 query="call NearestPetrolPumps(@p0,@p1);"
                 c.execute(query)
                 data=c.fetchall()
                 df3=pd.DataFrame(data, columns=["PetrolPump_Name", "Latitude","Longitude","Distance"])

                 st.dataframe(df3)
      elif choice2=="Most_Rush_Interval":
          id=st.text_input("Enter PetrolPump Registration_No:")
          if st.button("Find"):
                 query = "SET @p2='{}';".format(id)
                 c.execute(query)
                 query="call FindMostRushIntervalForPetrolPump(@p2);"
                 c.execute(query)
                 data=c.fetchall()
                 df4=pd.DataFrame(data,columns=["Most_Rush_Interval"])
                 st.dataframe(df4)
   
              
           


   else:
      st.subheader("About tasks")
def net_value():
   tanker_id = st.text_input("Enter Tanker ID:")
   result = TOTAL_Amount(tanker_id)
   if st.button("RUN Function"):
      df2=pd.DataFrame(result, columns = ["Total Amount"])
      st.dataframe(df2)

if __name__ == '__main__':
   main()

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
