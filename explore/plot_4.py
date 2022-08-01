'''plot.py Plot loads data from the clean csv file and produces a plot that is saved.
'''

#standard imports
import pandas as pd
import matplotlib.pyplot as plt


def plot(df):
  '''plot(df) takes as input a clean dataframe and generates a plot. The 
  style of the plot and variables are up to you.
  '''

  plt.scatter(df['LONGITUDE'], df['LATITUDE'], alpha=0.01, s=1)
  plt.xlabel('LONGITUDE')
  plt.ylabel('LATITUDE')    
  return plt



#The main() function  of this program
if __name__ == "__main__":
    cdf = pd.read_csv('clean.csv')
    plot(cdf)
    plt.savefig('plot_4.png')
