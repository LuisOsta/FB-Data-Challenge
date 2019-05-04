import numpy as np
import pandas as pd

df = pd.read_csv("sf_business_cleaned.csv")

zipcodes = df["zipcode"].unique()


def zipcode_counter(zipcode):
    return df[df["zipcode"] == zipcode]["naics_code"].value_counts().iloc[:10]


for val in zipcodes:
    businesses = zipcode_counter(val)
    if(len(businesses) < 5):
        continue
    else:
        print("\n\nZipcode : ", val)
        print(zipcode_counter(val))
