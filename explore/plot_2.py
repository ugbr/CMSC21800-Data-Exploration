'''plot.py Plot loads data from the clean csv file and produces a plot that is saved.
'''

#standard imports
import pandas as pd
import matplotlib.pyplot as plt


def plot(df):
  '''plot(df) takes as input a clean dataframe and generates a plot. The 
  style of the plot and variables are up to you.
  '''
  
  wc = cdf['WEATHER_CONDITION'].value_counts().rename_axis('weather_cond').reset_index(name='counts')
  lc = cdf['LIGHTING_CONDITION'].value_counts().rename_axis('lighting_cond').reset_index(name='counts')
  rc = cdf['ROADWAY_SURFACE_COND'].value_counts().rename_axis('road_cond').reset_index(name='counts')

  fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
  ax1.pie(wc['counts'])
  ax1.set_title('Crash frequency (weather condition)', fontsize=6)
  ax2.pie(lc['counts'])
  ax2.set_title('Crash frequency (lighting condition)', fontsize=6)
  ax3.pie(rc['counts'])
  ax3.set_title('Crash frequency (roadway surface condition)', fontsize=6)

  legend_1 = ax1.legend(bbox_to_anchor= (0.5, -0.04), prop={'size': 6}, loc='upper center', labels=['%s, %1.1f %%' % (l, s) for l, s in zip(wc['weather_cond'], wc['counts'] * 100 / sum(wc['counts']))])
  legend_2 = ax2.legend(bbox_to_anchor= (0.5, -0.04), prop={'size': 6}, loc='upper center', labels=['%s, %1.1f %%' % (l, s) for l, s in zip(lc['lighting_cond'], lc['counts'] * 100 / sum(lc['counts']))])
  legend_3 = ax3.legend(bbox_to_anchor= (0.5, -0.04), prop={'size': 6}, loc='upper center', labels=['%s, %1.1f %%' % (l, s) for l, s in zip(rc['road_cond'], rc['counts'] * 100 / sum(rc['counts']))])

  return plt



#The main() function  of this program
if __name__ == "__main__":
    cdf = pd.read_csv('clean.csv')
    plot(cdf)
    plt.savefig('plot_2.png')
