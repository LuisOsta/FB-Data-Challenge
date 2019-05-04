import numpy as np
import pandas as pd

df = pd.read_csv("sf_business_cleaned.csv")

zipcodes = df["naics_code"].unique()


def naics_code_counter(naics_code):
    return df[df["naics_code"] == naics_code]["zipcode"].value_counts().iloc[:10]


def outputBusinessByZipcode():
    for val in zipcodes:
        businesses = naics_code_counter(val)

        if(len(businesses) < 10):
            continue
        else:
            businesses.to_csv('businessByZipcodes.csv', mode='a', header=[val])
            print("\n\nnaics_code : ", val)
            print(businesses)


outputBusinessByZipcode()
