# Prototype for filtering dog profiles.
#
# Author: Nathan Malamud
# Date: June 4th, 2022
#

import pandas as pd
import numpy as np

from website.dogdb import get_dogs

def magic_filter_function(user_attributes):

    # Order of user_attributes:
    attr_order = [
        "walks",
        "barking",
        "trained",
        "yard_requirement",
        "friendly",
        "energy",
        "attention_requirement",
        "good_with_pets",
        "good_with_kids",
        "shedding",
        "size"
    ]

    # import dog profiles from csv table
    SQL_DATA = get_dogs()
    PROFILES = pd.DataFrame(SQL_DATA, columns = ["sql_id", "name", "photo", "sex", "age", "breed",
    "grouping", "weight", "notes", "fixed", "walks", "barking", "trained",
    "training_time", "yard_requirement", "friendly", "energy", "attention_requirement", "good_with_pets", "good_with_kids",
    "shedding", "size"])

    # Convert to pandas dataframe
    user_df_data = {}
    for i in range(len(attr_order)):
        attr = attr_order[i]
        user_df_data[attr] = user_attributes[i]

    USER = pd.DataFrame(data = user_df_data, index=[0])

    # Filter dataframe by attribute
    PROFILES_by_attr = PROFILES[attr_order]

    # Use euclidean distance algorithm to determine which dogs are good fits
    # The distance threshold is kind of an arbitray value, but it determines the degree to which
    # a dog should be "close" to ideal
    distance_threshold = 3.000

    # Source: https://stackoverflow.com/questions/56115205/euclidean-distance-between-two-pandas-dataframes
    def Euclidean_Dist(df1, df2, cols=['x_coord','y_coord']):
        return np.linalg.norm(df1[cols].values - df2[cols].values,
                    axis=1)

    distances = Euclidean_Dist(USER, PROFILES_by_attr, cols=attr_order)

    # Filter by distance, and now print to console
    IDEAL_DOGS = PROFILES[distances <= distance_threshold]

    ids = list(IDEAL_DOGS['sql_id'])

    return ids
