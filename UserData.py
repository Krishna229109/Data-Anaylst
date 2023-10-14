import pandas as pd
import numpy as np

#define List
name =[]
age = []

# Create loop for Name
for i in range(5):
	Name = input(f"Enter {i+1} name : ")
	name.append(Name)
	
#Create Lopp for Number
for i in range(5):
	Age = int(input(f" \n Enter {i+1} number : "))
	age.append(Age)
	
#create dictonary
dict = {
"names":name ,
"ages":age
}

print("\n Print The DataFrame of UserInput \n ")


df = pd.DataFrame(dict)

#print DataFrame
#print(df)

CSV = df.to_csv("Userdata.csv")

#new = pd.read_csv("Userdata.csv")
#print(new)

# print to excel 
Excel = pd.ExcelWriter("Userdata.xlsx")