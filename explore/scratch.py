'''scratch.py

You will write down any "scratch" code that you use to explore the dataset in
this file. This code does not produce any outputs (it does not modify any files)
but allows you to explore the data. We're separating this code from the rest because 
it allows us to understand your thought process during data exploration.

*Remember to replace the return statements with your code*
'''

#standard imports
import pandas as pd
import matplotlib.pyplot as plt


#TODO 1.
def load(filename):
  '''load(filename) takes as input a filename and loads a dataframe.
  '''
  return pd.read_csv(filename) #demo

def clean(df):
  '''clean(df) takes as input a dataframe and fixes any data errors  
     *that might affect your results*. it returns a copy of the dataframe 
     without errors.
  '''
  df['INJURIES_TOTAL'] = df['INJURIES_TOTAL'].fillna(0)
  df['INJURIES_FATAL'] = df['INJURIES_FATAL'].fillna(0)
  df['INJURIES_INCAPACITATING'] = df['INJURIES_INCAPACITATING'].fillna(0)  
  df['INJURIES_NON_INCAPACITATING'] = df['INJURIES_NON_INCAPACITATING'].fillna(0)
  df['INJURIES_REPORTED_NOT_EVIDENT'] = df['INJURIES_REPORTED_NOT_EVIDENT'].fillna(0)
  df['INJURIES_NO_INDICATION'] = df['INJURIES_NO_INDICATION'].fillna(0)  
  df.loc[df.NUM_UNITS > df.INJURIES_TOTAL + df.INJURIES_NO_INDICATION, 'INJURIES_NO_INDICATION'] = df['NUM_UNITS'] - df['INJURIES_TOTAL']
  
  df = df[df['LATITUDE'].notna()]
  df = df[df['LONGITUDE'].notna()]
  df = df[df['LONGITUDE'] < -10]
  df = df[(df['WEATHER_CONDITION'] != 'UNKNOWN') & (df['LIGHTING_CONDITION'] != 'UNKNOWN') & (df['ROADWAY_SURFACE_COND'] != 'UNKNOWN')]

  return df #demo


#TODO 2.
def plot(df):
  '''plot(df) takes as input a clean dataframe and generates a plot. The 
  style of the plot and variables are up to you.
  '''
  
  plt.scatter(df['A'],df['B'])
  return None



#The main() function  of this program

if __name__ == "__main__":
    df = load('data_2.csv')
    cdf = clean(df)
    #plot(cdf)
    #plt.show()
    pd.set_option('display.max_columns', None)
    # print(cdf.head())

    # The downtown environment (especially the roadway surface condition) might be a 
    # major factor in the high frequency of crashes in the region.

    rc = cdf[(cdf['LATITUDE'] < 41.9034) & (cdf['LATITUDE'] > 41.8556) & (cdf['LONGITUDE'] < -87.6167) & (cdf['LONGITUDE'] > -87.6326)]
    rc = rc['ROADWAY_SURFACE_COND'].value_counts().rename_axis('road_cond').reset_index(name='counts')

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.pie(rc['counts'])
    ax1.set_title('Crash frequency (roadway surface condition) in the downtown region', fontsize=5.5)
    legend_1 = ax1.legend(bbox_to_anchor= (0.5, -0.04), prop={'size': 6}, loc='upper center', labels=['%s, %1.1f %%' % (l, s) for l, s in zip(rc['road_cond'], rc['counts'] * 100 / sum(rc['counts']))])
    
    rc1 = cdf[(cdf['LATITUDE'] >= 41.9034) | (cdf['LATITUDE'] <= 41.8556) | (cdf['LONGITUDE'] >= -87.6167) | (cdf['LONGITUDE'] <= -87.6326)]
    rc1 = rc1['ROADWAY_SURFACE_COND'].value_counts().rename_axis('road_cond').reset_index(name='counts')
    ax2.pie(rc1['counts'])
    ax2.set_title('Crash frequency (roadway surface condition) in other regions', fontsize=5.5)
    legend_2 = ax2.legend(bbox_to_anchor= (0.5, -0.04), prop={'size': 6}, loc='upper center', labels=['%s, %1.1f %%' % (l, s) for l, s in zip(rc1['road_cond'], rc1['counts'] * 100 / sum(rc1['counts']))])
    
    plt.show()

