import pandas as pd
import numpy as np
import Testing as ts
def organizing
data= ts.import_clean_data("Tea Room/2017-2018/item_sales.csv")

#print(data.groupby(["Gross Sales"]).sum().sort_values("Item", ascending=False))

sort_by_gross_sales = data.sort_values('Gross Sales', ascending=False)

print(sort_by_gross_sales)