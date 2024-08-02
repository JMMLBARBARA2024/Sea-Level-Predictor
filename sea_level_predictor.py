import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
# from scipy._lib._ccallback_c import plus1_t


##***********************************************************************##
def draw_plot():
    ## Read data from file ##
    df = pd.read_csv("epa-sea-level.csv")

    ## Create scatter plot ##
    fig, ax = plt.subplots()
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    plt.scatter(x, y)

    ## Create first line of best fit ##
    regre_1 = linregress(x, y)
    x_predict_1 = pd.Series([i for  i in range(1880, 2051)])
    y_predict_1 = regre_1.slope * x_predict_1 + regre_1.intercept
    plt.plot(x_predict_1, y_predict_1, "red")

    ## Create second line of best fit ##
    current_df = df.loc[df["Year"] >= 2000]
    current_x = current_df["Year"]
    current_y = current_df["CSIRO Adjusted Sea Level"]
    regre_2 = linregress(current_x, current_y)
    x_predict_2 = pd.Series([i for  i in range(2000, 2051)])
    y_predict_2 = regre_2.slope * x_predict_2 + regre_2.intercept
    plt.plot(x_predict_2, y_predict_2, "black")

    ## Add labels and title ##
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    ## Save plot and return data for testing (DO NOT MODIFY) ##
    plt.savefig('sea_level_plot.png')

    return plt.gca()
##***********************************************************************##
