# PetrolPump-Management-System [DBMS]  

##Project Overview
This project, titled PetrolPump Management System, was developed as part of a Database Management System (DBMS) course . The system is designed to efficiently manage and monitor operations within a petrol pump, providing a user-friendly interface for various tasks.

## Impletation Environment

### FrontEnd

- In this Project, frontend part is done by using famous Python library streamlit.

-  Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc.

- We can Perform operations such as Create, Read, Delete, Update aslso known as [CRUD] Operations.

- There is one user defined function which calculate Total Price in Tanker table and a Trigger which is present in Employee table which get activated when someone Try to update Salary field if salary is less that 300000. 

### Backend

- In Backend creation of table and table population is done in MySQL 
- It also uses libraries such as Pandas, sql connector, Streamlit 
- It is mostly done Using Python Language. 

## Project File Structure 

### In Projets folder the following files are present 
* create_database.py --> This file is used to Create database Ptrolpump_Management  
* app.py --> This is the main file you need to run after creation of the databases. It has codes for GUI part.
*  databases.py --> This file has all the important function calls
* create.py --> It creates new table rows when you want to add new data.
* delete.py --> It has delete function implementation used for deleting any specific row in table.
* read.py --> It read data from table and send it to view function to display.
* update.py -->  It updates the data in the table.

###Team Member

- Patel Het(2021CSB1119)
- Kushagra Sharma(2021CSB1107)
- Sushil Kumar(2021CSB1136)


## How TO RUN 
```
- First create databases using Create_database.py
- Install all the librarys
- run app.py file using command: "Python3 -m streamlit run app.py"
```


