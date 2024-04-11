import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

uk = pd.read_csv('uk_population.csv')

uk['male'] = uk['male'] / -1000
uk['female'] = uk['female'] / 1000


large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
#plt.style.use('seaborn-whitegrid')
sns.set_style("white")


ages = ['85_', '80_84', '75_79', '70_74', '65_69', '60_64', '55_59', '50_54',
            '45_49', '40_44', '35_39', '30_34', '25_29', '20_24', '15_19', 
            '10_14', '5_9', '0_4']


plt.rcParams["figure.figsize"] = (15, 8)

ax1 = sns.barplot(x='male', y='age', data=uk, order=ages, palette="Blues")
ax2 = sns.barplot(x='female', y='age', data=uk, order=ages, palette="Greens")
plt.title("Population pyramid for the UK, 2020 estimates")
plt.xticks(ticks=[-2000, -1000, 0, 1000, 2000],
           labels=['2,000k', '1,000k', '0', '1,000k', '2,000k'])

plt.grid()
plt.xlabel("Male/Female")
plt.savefig('population_pyramid.png')
