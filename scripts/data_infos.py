import pandas as pd
import numpy as np

class dataframeInfo:
    ###############################################################################
    # data information
    ################################################################################

    def __init__(self, df: pd.DataFrame):
        """
            Returns a dataframe Info Object with the passed DataFrame Data
            Parameters
        """
        self.df = df

    def data_shape(self):
        print(f" There are {self.df.shape[0]} rows and {self.df.shape[1]} columns")

        """how many missing values exist or better still what is the % of missing values in the dataset?"""

    def data_types(self):
        t = self.df.dtypes.value_counts()
        return t

    def percent_missing(self):

        # Calculate total number of cells in dataframe
        totalCells = np.product(self.df.shape)

        # Count number of missing values per column
        missingCount = self.df.isnull().sum()

        # Calculate total number of missing values
        totalMissing = missingCount.sum()

        # Calculate percentage of missing values
        print("The dataset contains", round(
            ((totalMissing/totalCells) * 100), 2), "%", "missing values.")
    