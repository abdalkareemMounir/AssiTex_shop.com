from function import manage_csv
import time


def read_data():
    x = input("enter meters: ")
    y = input("enter price: ")
    z = input("enter type: ")
    t = time.strftime("%d-%m-%Y")
    return [x,y,z,t]

"""df1 = pandas.DataFrame([[5,100,"blosh"],[10,100,"blosh"]],columns=["meters","price","type"])
"""
p='assi_shop.csv'
mylist = read_data()
manage_csv.add_toCSV(mylist,"assi_shop.csv")