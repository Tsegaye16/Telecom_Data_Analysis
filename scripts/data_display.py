import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

class DataFrame:
    @staticmethod
    def getTopTen(df: pd.DataFrame, column: str, drop_index: bool = True) -> pd.DataFrame:
        df.sort_values(column, ascending=False, inplace=True)
        if drop_index:
            df.reset_index(drop=True, inplace=True)
            
    def replaceOutliersWithIQR(df, columns):
        for col in columns:
            Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
            IQR = Q3 - Q1
            cut_off = IQR * 1.5
            lower, upper = Q1 - cut_off, Q3 + cut_off
            df[col] = np.where(df[col] > upper, upper, df[col])
            df[col] = np.where(df[col] < lower, lower, df[col])

        return df.head(10)
    
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def listColoumnNames(self) -> pd.DataFrame:
        return self.df.columns
    
    def getColumnsList(self)-> pd.DataFrame:
        return self.df.columns.to_list()
    
    def formatFloat(value)-> pd.DataFrame:
        return f'{value:,.2f}'

    def showDataInformation(self) -> pd.DataFrame:
        return self.df.info()

    def showDataDescription(self) -> pd.DataFrame:
        return self.df.describe()
    #show the correlations
    def showCorrelation(self) -> pd.DataFrame:
        numeric_df = self.df.select_dtypes(include=["number"])
    
        # Check if there are numeric columns
        if numeric_df.empty:
            return "No numeric columns available to compute correlation."
    
        # Compute and return correlation
        return numeric_df.corr()
    #count null values
    def getNullCounts(self)-> pd.DataFrame:
        print(self.df.isnull().sum())
    #skwiness 
    def skewness(self)-> pd.DataFrame:
        # Select only numeric columns
        numeric_df = self.df.select_dtypes(include=["number"])
        
        # Check if there are numeric columns
        if numeric_df.empty:
            return "No numeric columns available to compute skewness."
        
        # Compute skewness
        return numeric_df.skew()
    """
    Plot a scatter chart and runs correlation test
    """
    def bivariateAnalysis(self, df, cols, colors): 
        
        for i in range(len(cols)):
            plt.style.use('fivethirtyeight')
            plt.figure(figsize=(8, 4)) 
            sns.scatterplot(data = df, x=cols[i][0], y=cols[i][1], s=20, color=colors[i])
            print(self.corrMatrix(df, cols[i]))
            
    def fixOutlier(df, column):
        df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].mode(),df[column])
        
        return df[column]

    

        
  
        