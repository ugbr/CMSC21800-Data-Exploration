'''plot.py Plot loads data from the clean csv file and produces a plot that is saved.
'''

#standard imports
import pandas as pd
import matplotlib.pyplot as plt


def plot(df):
  '''plot(df) takes as input a clean dataframe and generates a plot. The 
  style of the plot and variables are up to you.
  '''
  fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

  ax1.set_title('Crash severity (weather condition)', fontsize=6)
  wc = cdf[['CRASH_TYPE', 'WEATHER_CONDITION']]
  tab1 = pd.crosstab(index=wc['WEATHER_CONDITION'], columns=wc['CRASH_TYPE'])
  tab1.plot(kind='bar', ax=ax1, fontsize=4).legend(prop={'size': 4})

  ax2.set_title('Crash severity (lighting condition)', fontsize=6)
  lc = cdf[['CRASH_TYPE', 'LIGHTING_CONDITION']]
  tab2 = pd.crosstab(index=lc['LIGHTING_CONDITION'], columns=lc['CRASH_TYPE'])
  tab2.plot(kind='bar', ax=ax2, fontsize=4).legend(prop={'size': 4})

  ax3.set_title('Crash severity (roadway surface condition)', fontsize=6)
  rc = cdf[['CRASH_TYPE', 'ROADWAY_SURFACE_COND']]
  tab3 = pd.crosstab(index=rc['ROADWAY_SURFACE_COND'], columns=rc['CRASH_TYPE'])
  tab3.plot(kind='bar', ax=ax3, fontsize=4).legend(prop={'size': 4})

  return plt



#The main() function  of this program
if __name__ == "__main__":
    cdf = pd.read_csv('clean.csv')
    plot(cdf)
    plt.savefig('plot_3.png')
