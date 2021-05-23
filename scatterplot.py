import pandas as pd
import plotly.express as px

##df = pd.read_csv("IceCream.csv")
##fig = px.scatter(df, x="Temperature", y="Ice-cream Sales( ₹ )" )
df = pd.read_csv("TeaCoffe.csv")
fig = px.scatter(df, x="Coffee in ml", y="sleep in hours" )
fig.show()