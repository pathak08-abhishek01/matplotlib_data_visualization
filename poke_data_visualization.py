import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('file.csv')

# reset index to 'Name'
df.set_index('Name', inplace=True)

# drop column '#'
df.drop('#', inplace=True, axis=1)

# Comparison of Mean Attack Points for variants of Type 1 and Type 2
# Type 1 mean attack points dataframe for every category
type_1 = pd.DataFrame(df.groupby(['Type 1'])['Attack'].mean())

# Type 2 mean attack points dataframe for every category
type_2 = pd.DataFrame(df.groupby(['Type 2'])['Attack'].mean())

# Reset index for both dataframes
type_1.reset_index(inplace=True)
type_2.reset_index(inplace=True)


# Merge both dataframes
merged = pd.merge(type_1, type_2, left_on='Type 1', right_on='Type 2')

# Drop 'Type 1' column permanently
merged.drop('Type 1', inplace=True, axis=1)
# Rename column
merged.rename(columns={'Type 2': 'Type'}, inplace=True)


# Set size of the figure
plt.figure(figsize=(14, 8))

# Line plot for 'Type 1' Pokemon mean attack points
plt.plot(merged['Type'], merged['Attack_x'], color='red')

# Line plot for 'Type 2' Pokemon mean attack points
plt.plot(merged['Type'], merged['Attack_y'], color='blue')

# Setting X-axis label
plt.xlabel('Type')
# Setting Y-axis label
plt.ylabel('Mean Attack Points')

# Title of the plot
plt.title('Comparison of Mean Attack Points for variants of Type 1 and Type 2')

# Setting Y-axis limit
plt.ylim((45, 120))
# Legend
plt.legend(labels=['Type1', 'Type2'])


# Display plot
plt.show()

# Which generation has the highest chances of being legendary?
# Group Pokemons
res = df.groupby(['Type 1', 'Legendary']).size().unstack()
# Plot stacked bar chart
res.plot(kind='bar', stacked=True, figsize=(15, 10))
plt.title('Generation wise Legendary and Non-Legendary Pokemons')
plt.xlabel('Generation')
plt.ylabel('Frequency')
# Display plot
plt.show()

# Visualize the distribution of `Attack` points for `Dragon` type (`Type 1`) Pokemons
# Mean 'Attack' for all Pokemons
mean_attack = df['Attack'].mean()
# Mean 'Attack' for Dragon type Pokemons
dragon = df[(df['Type 1']) == 'Dragon']
mean_dragon = dragon['Attack'].mean()
# Histogram for Dragon type Pokemons
dragon.hist(column='Attack', bins=8)
plt.ylabel('Frequnency')
plt.xlabel('Attack Points')
plt.title('Attack Frequency of Type1 Dragon Pokemons')
plt.axvline(x=mean_attack, color='green')
plt.axvline(x=mean_dragon, color='black')
# Display plot
plt.show()

# Do electric pokemons have a correlation between their health and attack?
# Conditional filtering for 'Electric' pokemons
electric = df[df['Type 1'] == 'Electric']

# Scatter plot for 'Attack' vs 'HP'
electric.plot.scatter(x='HP', y='Attack')
plt.title('Electric Pokemon HP vs Attack')
plt.ylabel('Attack Points')
plt.xlabel('Health Points')

# Display plot
plt.show()

# Legendary higher chances - a different view
# Initializing subplot and axes
fig, (ax_1, ax_2) = plt.subplots(1, 2, figsize=(20, 10))
# Stacked bar-chart representing counts
res.plot(kind='bar', stacked=True, ax=ax_1)
ax_1.set_title('Stacked Bar chart with counts')

# Stacked bar-chart representing percentages
new_res = res.fillna(0)
new_res['Total'] = new_res[True] + new_res[False]
new_res[True] = (new_res[True] / new_res['Total']) * 100
new_res[False] = (new_res[False] / new_res['Total']) * 100
new_res.drop('Total', inplace=True, axis=1)
new_res.plot(kind='bar', stacked=True, ax=ax_2)
ax_2.set_title('Stacked Bar Chart with Percentage')

plt.show()
# Code ends here