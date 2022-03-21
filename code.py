import plotly.figure_factory as ff
import statistics
import random
import plotly_express as px
import math
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()

population_mean = statistics.mean(data)
print("Mean = ", population_mean)
population_standarddeviation = statistics.stdev(data)
print("Standard deviation = ", population_standarddeviation)

dataset = []
for i in range(0, 1000):
     random_index= random.randint(0,len(data))
     value = data[random_index]
     dataset.append(value)
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print("Mean of 1000 values is ",mean)
print("std_deviation of 1000 values is ",std_deviation)