#Question1

myname= "Tara"
print(myname)
len(myname)
print(len(myname))

count = 0
for letter in myname:
    if letter == "r":
        count += 1
print (count)

#Question2

my_list = [1, 5, "4", "six", 3.14]

# try and exception 

for value in my_list:
    try:
        number = int(value)
        print(number)
    except ValueError:
        print("Skipping invalid value:", value)

# attemp to creat a new list 

new_list = []

def clean_list(my_list):
    for value in my_list:
        try:
            accepted_value = int(value)
            new_list.append(accepted_value)
        except (ValueError, TypeError):
            
            pass  # Skip rejected values
    return (new_list)

print(new_list)

# Sum of neighboring numbers in new list 

new_list= [1, 5, 4, 3]
total1=[]
for i in range(len(new_list) - 1):
    total1 = new_list[i] + new_list[i + 1]
    new_list.append(total1)
    
print(total1)

# Question 3
import csv
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotnine import (
    ggplot, aes, geom_point, labs, theme_minimal, ggsave
)


df = pd.read_csv("cnv_data.csv")
print(df.head())


# Create a folder for the plots
os.makedirs("plots", exist_ok=True)

# Scatterplot using Matplotlib
plt.figure(figsize=(12, 6))

# Create a folder for the plots
os.makedirs("plots", exist_ok=True)

# Scatterplot using Matplotlib
plt.figure(figsize=(12, 6))

#Plot the FPKM values 
plt.scatter(
    df["position_mb"],
    df["log2_ratio"]
)

plt.xlabel("position")
plt.ylabel("ratio")
plt.title("position vs ratio")


plt.tight_layout()
plt.savefig("plots/scatter_matplotlib.png", dpi=300)
plt.show 


# Question 6
# Import random
import random 

# Create an If statement to stimulate 20 games

for game in range(1, 20):
    print("Game", game)

    Alice = random.randint(1, 6)
    Bob = random.randint(1, 6)

    print("Player 1:", Alice)
    print("Player 2:", Bob)

    if Alice > Bob :
        print("Alice wins!")
    elif Bob > Alice:
        print("Bob wins!")
    else:
        print("It's a draw!")

    print()

