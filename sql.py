import sqlite3
import random
from faker import Faker

# Initialize Faker for generating random data
fake = Faker()

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert records, create table
cursor = connection.cursor()

# Create the table if it doesn't already exist
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    STUDENT_ID INTEGER PRIMARY KEY,
    NAME VARCHAR(50),
    DATE_OF_BIRTH DATE,
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MATH_MARKS INT,
    ENGLISH_MARKS INT,
    SCIENCE_MARKS INT,
    ATTENDANCE_PERCENTAGE FLOAT
);
"""
cursor.execute(table_info)    # here it table get creted 

# Generate and insert records in table 

for student_id in range(1, 51):  # STUDENT_ID from 1 to 50
    name = fake.name()
    dob = fake.date_of_birth(minimum_age=12, maximum_age=18)
    cls = random.choice(['6th Grade', '7th Grade', '8th Grade', '9th Grade', '10th Grade'])
    section = random.choice(['A', 'B', 'C'])
    math_marks = random.randint(0, 100)
    english_marks = random.randint(0, 100)
    science_marks = random.randint(0, 100)
    attendance_percentage = round(random.uniform(50.0, 100.0), 2)

    cursor.execute(
        "INSERT INTO STUDENT (STUDENT_ID, NAME, DATE_OF_BIRTH, CLASS, SECTION, MATH_MARKS, ENGLISH_MARKS, SCIENCE_MARKS, ATTENDANCE_PERCENTAGE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (student_id, name, dob, cls, section, math_marks, english_marks, science_marks, attendance_percentage)
    )

# Display all the records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()











# import sqlite3

# ## Connectt to SQlite
# connection=sqlite3.connect("student.db")

# # Create a cursor object to insert record,create table

# cursor=connection.cursor()

# ## create the table
# table_info="""
# Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
# SECTION VARCHAR(25),MARKS INT);

# """
# cursor.execute(table_info)

# ## Insert Some more records

# cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
# cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
# cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
# cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
# cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

# ## Disspaly ALl the records

# print("The isnerted records are")
# data=cursor.execute('''Select * from STUDENT''')
# for row in data:
#     print(row)

# ## Commit your changes int he databse
# connection.commit()
# connection.close()