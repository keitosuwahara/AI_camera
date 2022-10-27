import pandas as pd
import numpy as np

print("Series")
print("")

sr=pd.Series({"suwa":"kei","yama":"yuu","isi":"doro"})
print(sr.head())

print("-----------------------------")
print("Series + index")
print("")

sr2=pd.Series(["kei","yuu","doro"],index=["suwa","yama","isi"])
print(sr2.head())

print("-----------------------------------------")
print("DataFrame")
print("")

data=[
    ["suwa","yama","doro"],
    ["kyoto","zama","inaka"],
    ["080","090","0120"]
]
print(pd.DataFrame(data=data, index=["2002","1980","2000"], columns=["name","address","phonenum"]))

print("____________________________")
print("DataFrame + columns abstraction")
print("")

df=pd.DataFrame(data=data, index=["2002","1980","2000"], columns=["name","address","phonenum"])
print(df[["name","address"]])

print("________________________________")
print("DataFrame + index abstraction")
print("")

df=pd.DataFrame(data=data, index=["2002","1980","2000"], columns=["name","address","phonenum"])
print(df["2002":"2002"])
print("")
print(df["2002":"1980"])




if __name__ == "__main__":
    pass