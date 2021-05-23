import csv 
import pandas as pd
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    icecream_sales=[]
    temperature=[]
    df = pd.read_csv(data_path)
    for row in df:
        print(row["Ice-cream Sales( ₹ )"])
        icecream_sales.append(float(row["Ice-cream Sales( ₹ )"]))
        temperature.append(float(row["Temperature"]))

    return {"x":icecream_sales,"y":temperature}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation btw temp and ice cream is:", correlation)

def setup():
    
    output =  getDataSource("IceCream.csv")
    findCorrelation(output)

setup()