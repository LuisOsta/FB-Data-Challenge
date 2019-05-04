import numpy as np
import pandas as pd

columnString = "GEOTYPE|ST|COUNTY|PLACE|CONSCITY|CSA|MSA|MD|CENREG|PLANREG|GEO_COMP|GEO_ID|GEO_TTL|FOOTID_GEO|NAICS2012|NAICS2012_TTL|FOOTID_NAICS|OPTAX|OPTAX_TTL|YEAR|ESTAB|ESTAB_F|RCPTOT|RCPTOT_F|PAYANN|PAYANN_F|PAYQTR1|PAYQTR1_F|EMP|EMP_F|NESTAB|NESTAB_F|NRCPTOT|NRCPTOT_F|RCPTOT_S|RCPTOT_S_F|PAYANN_S|PAYANN_S_F|PAYQTR1_S|PAYQTR1_S_F|EMP_S|EMP_S_F"

columns = columnString.split("|")
finDf = pd.read_csv("EC1200A1.dat", sep="|", skiprows=0,
                    usecols=[*range(0, 31)], names=columns)
print(finDf["ST"].count())
