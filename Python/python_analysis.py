import pandas as pd
df = pd.read_csv(r"E:\portfolio\E-Commerce Sales & Profitability Analysis\ecommerce_analysis.csv")
print(df.shape)
df["Profit"] = df["Sales_Amount"] - df["Cost_Amount"]
print(df.groupby("Product")["Sales_Amount"].sum().sort_values(ascending=False))
print(df.groupby("Product")["Profit"].sum().sort_values(ascending=False))
print(df.groupby("Product").agg(Sales=("Sales_Amount","sum"), Profit=("Profit","sum")))
print(df.groupby("Product").agg(Sales=("Sales_Amount","sum"), Profit=("Profit","sum")).assign(Margin=lambda x: x["Profit"] / x["Sales"] * 100).sort_values("Margin"))
print(df.groupby("Product").agg(Sales=("Sales_Amount","sum"), Profit=("Profit","sum")).assign(Margin=lambda x: x["Profit"] / x["Sales"] * 100).sort_values(["Sales","Margin"], ascending=[False, True]))

