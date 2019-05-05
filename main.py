import numpy as np
import pandas as pd

df = pd.read_csv("sf_business_cleaned.csv")

naics_codes = df["naics_code"].unique()


def naics_code_counter(naics_code):
    return df[df["naics_code"] == naics_code]["zipcode"].value_counts().iloc[:10]


def outputBusinessByZipcode():
    for val in naics_codes:
        businessZipcodes = naics_code_counter(val)

        if(len(businessZipcodes) < 5):
            continue
        else:
            businessZipcodes.to_csv(
                'businessBynaics_codes.csv', mode='a', header=[val])
            print("\n\nnaics_code : ", val)
            print(businessZipcodes)


outputBusinessByZipcode()
