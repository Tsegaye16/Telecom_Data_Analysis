from tkinter import Image
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots



from IPython.display import Image
import plotly.io as pio


def format_float(value):
    return "{:.2f}".format(value)
def plot_hist(df:pd.DataFrame, column:str, color:str) -> None:
    sns.displot(data = df, x = column, color = color, kde = True, height = 7, aspect = 2)
    plt.title(f"Distribution of {column}", size=20, fontweight="bold")
    plt.show()
def plot_count(df:pd.DataFrame, column:str) -> None:
    plt.figure(figsize=(10,6))
    sns.countplot(data = df, x = column)
    plt.title(f"Count of {column}", size=20, fontwight="bold")
    plt.show()
def blot_bar(df:pd.DataFrame,x_col:str,y_col:str, title:str,xlabel:str,ylabel:str) -> None:
    plt.figure(figsize=(10,6))
    sns.barplot(data = df, x = x_col, y = y_col)
    plt.title(title, size=20, fontwight="bold")
    plt.xlabel(xlabel, size=15)
    plt.ylabel(ylabel,fontsize=16)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()
def plot_heatmap(df:pd.DataFrame, title:str, cbar=False)->None:
    plt.figure(figsize=(12, 7))
    sns.heatmap(df, annot=True, cmap='viridis', vmin=0, vmax=1, fmt='.2f', linewidths=.7, cbar=cbar )
    plt.title(title, size=18, fontweight='bold')
    plt.show()

def plot_box(df:pd.DataFrame, x_col:str, title:str) -> None:
    plt.figure(figsize=(12, 7))
    sns.boxplot(data = df, x=x_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.show()
def plotly_plot_scatter(df, x_col, y_col, marker_size, hover=[]):
    fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            opacity=0.8,
            hover_data=hover,
            title=f'{x_col} vs. {y_col}')
    fig.update_traces(marker_size=marker_size)
    fig.show()

def plot_box_multi(df:pd.DataFrame, x_col:str, y_col:str, title:str) -> None:
    plt.figure(figsize=(12, 7))
    sns.boxplot(data = df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks( fontsize=14)
    plt.show()

def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data = df, x=x_col, y=y_col)
    plt.title(f'{x_col} Vs. {y_col}\n', size=20)
    plt.xticks(fontsize=14)
    plt.yticks( fontsize=14)
    plt.show()
def mult_hist(sr, rows, cols, title_text, subplot_titles, interactive=False):
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)
    for i in range(rows):
        for j in range(cols):
            x = ["-> " + str(i) for i in sr[i+j].index]
            fig.add_trace(go.Bar(x=x, y=sr[i+j].values), row=i+1, col=j+1)
    fig.update_layout(showlegend=False, title_text=title_text)
    if(interactive):
        fig.show()
    else:
        return Image(pio.to_image(fig, format='png', width=1200))
        
pd.options.display.float_format = format_float
