import pandas
import os
def add_toCSV(df_local,path):
    if os.path.exists(path):
        df1 = pandas.read_csv(path)
        df1_T = df1.T
        df1_T[len(df1)]=df_local
        df1 = df1_T.T
        df1.to_csv('assi_shop.csv', index=False) 