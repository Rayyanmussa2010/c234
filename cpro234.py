import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

dataset=pd.read_csv('projectC234_EPL.csv')
goal_column=dataset['Goals']
sorted_club_data_by_ascending_order=goal_column.groupby(dataset['Club'])
sum_of_of_goal_by_each_club=sorted_club_data_by_ascending_order.sum()
epl_top_goals=dataset.sort_values(['Club'])(by=['Goals'], ascending=False)[:10]