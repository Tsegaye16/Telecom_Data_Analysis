import pandas as pd
import numpy as np

class Pre_Process():
    def __init__(self, df:pd.DataFrame) -> None:
        self.df = df
    def dropDuplicateRows(self) -> pd.DataFrame:
        droped = self.df[self.df.duplicated()].index
        return self.df.drop(index=droped, inplace=True)
    def convertToDatetime(self,df) -> pd.DataFrame:
        df["Start"] = pd.to_datetime(df["Start"])
        df["End"] = pd.to_datetime(df["End"])
        return df
    def convertToNumbers(self) -> pd.DataFrame:
        self.df = self.df.apply(pd.to_numeric, error = "coerce")
        return self.df
    def dropRows(self, columns) -> pd.DataFrame:
        self.df.drop(columns, axis=1, inplace=True)
    def dropColumns(self, df:pd.DataFrame, columns:list) -> pd.DataFrame:
        for col in columns:
            df.drop(col, axis=1, inplace=True)
        return df
    """Fill out numeric value with mean and media"""
    def fillNumericalColumn(self, column) -> pd.DataFrame:
        for col in column:
            skewness = self.df[col].skew()
            if((-1 < skewness) and (skewness < -0.5)):
                self.df[col] = self.df[col].fillna(self.df[col].mean())
            else:
                self.df[col] = self.df[col].fillna(self.df[col].median())
    def fixOutlier(df, column) -> pd.DataFrame:
        df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(), df[column])
        return df[column]
    """fill missing value of categorical data with mode"""
    def fillCategoricalColumns(self, column) -> pd.DataFrame:
        for col in column:
            mod = self.df[col].mod()[0]
            self.df[col] = self.df[col].fillna(mod)
    """missing value that the percentage is greater than 30, clean"""
    def getColumnBasedMissing(self):
        null_col = self.df.isnull().sum()
        total_entry = self.df.shape[0]
        missing_percentage = []
        for col in null_col:
            value = str(round(((col/total_entry) * 100), 2)) + "%"
            missing_percentage.append(value)
        missing_df = pd.DataFrame(null_col, columns=["total_missing_values"])
        missing_df["missing_percentage"] = missing_percentage
        return missing_df
    def convertBytesToMegabytes(self, column):
        megabyte = 1*10e+5
        total_MB = []
        for i in column.values:
            i = i / megabyte
            total_MB.append(i)
        return total_MB
