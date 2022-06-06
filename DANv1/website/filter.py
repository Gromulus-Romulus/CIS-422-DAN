# Prototype for filtering dog profiles.
#
# Author: Nathan Malamud
# Date: June 4th, 2022
#

import pandas as pd
import numpy as np

from dogdb import get_dog_by_ID, get_dogs

# TODO: divide user_attributes into categorical and numerical values

# TODO: map user_attributes to dog attrs

# Categorical attributes
USER_BREEDS = ['bloodhound', 'labrador retriever', 'basset hound', 'frenchie']

# Quantitative attributes
USER_ATTRS = {
    'yard_requirement': 1,
    'shedding': 1,
    'attention_requirement': 2
}

# import dog profiles from csv table
SQL_DATA = get_dogs()
PROFILES = pd.DataFrame(SQL_DATA, columns = ["sql_id", "name", "photo", "sex", "age", "breed",
"grouping", "weight", "notes", "fixed", "walks", "barking", "trained",
"training_time", "yard_requirement", "friendly", "energy", "attention_requirement", "good_with_pets", "good_with_kids",
"shedding", "size"])

# Filter by breeds
PROFILES_by_breed = PROFILES[PROFILES["breed"].isin(USER_BREEDS)]

# Filter by quantitative attributes
quantitative_attrs = list(USER_ATTRS.keys())

# Convert to pandas dataframe
USER_DF = pd.DataFrame(data = USER_ATTRS, index=[0])

# Filter PROFILES_BY_BREED to isolate quantitative attributes
PROFILES_by_attrs = PROFILES_by_breed[quantitative_attrs]

# Use euclidean distance algorithm to determine which dogs are good fits
# The distance threshold is kind of an arbitray value, but it determines the degree to which
# a dog should be "close" to ideal
distance_threshold = 2.000

# Source: https://stackoverflow.com/questions/56115205/euclidean-distance-between-two-pandas-dataframes
def Euclidean_Dist(df1, df2, cols=['x_coord','y_coord']):
    return np.linalg.norm(df1[cols].values - df2[cols].values,
                axis=1)

distances = Euclidean_Dist(USER_DF, PROFILES_by_attrs, cols=quantitative_attrs)

# Filter by distance, and now print to console
IDEAL_DOGS = PROFILES_by_breed[distances <= 2.000]

ids = list(IDEAL_DOGS['sql_id'])
photos = list(IDEAL_DOGS['photo'])
names = list(IDEAL_DOGS['name'])
breeds = list(IDEAL_DOGS['breed'])
ages = list(IDEAL_DOGS['age'])

print(ids)
print(photos)
print(names)