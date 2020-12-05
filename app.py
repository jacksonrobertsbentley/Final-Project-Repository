
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

points = pd.read_excel("Fantasy Points per week.xlsm", header=0, index_col=0)
matchups = pd.read_excel("Fantasy Matchups.xlsm",header=0,index_col=0)
real_wins = pd.read_excel("Fantasy Win Totals.xlsx",header=0,index_col=0)
simulation_times = st.sidebar.slider("How many times would you like to simulate the season?",1,1000,100,1)

points.T.boxplot(column=None, by=None)
plt.title("Distribution of Scores for Each Owner")
plt.xticks(rotation=90)
st.pyplot(plt.gcf(),clear_figure=True)

std = points.std(axis=1)
mean = points.mean(axis=1)
summarypoints = pd.concat([mean.rename('Mean'),std.rename('Standard Deviation')], axis=1)

players_list = list(points.index.values)

player_wins_df = pd.DataFrame()
for player in players_list:
    my_wins = []
    my_losses = []
    for sim in range (simulation_times):
        winners = []
        losers = []
        np.random.seed(sim + 5)
        for i in range(1,13):
            for j in range(0,6):       
                away_team = matchups.iloc[j,2*i-2]
                home_team = matchups.iloc[j,2*i-1]
                mean_away = mean.loc[away_team]
                std_away = std.loc[away_team]
                mean_home = mean.loc[home_team]
                std_home = std.loc[home_team]
                away_points = np.random.normal(mean_away,std_away,size=1)
                home_points = np.random.normal(mean_home,std_home,size=1)
                if home_points > away_points:
                    winners.append(home_team)
                    losers.append(away_team)
                else:
                    winners.append(away_team)
                    losers.append(home_team)
        my_wins.append(winners.count(player))
        my_losses.append(losers.count(player))
    player_wins_df[player]=my_wins
    plt.plot(range(1,simulation_times+1),my_wins,'-o')
    plt.title('Number of Wins per Simulation\nFor ' + player + '\'s Fantasy Football Team')
    plt.xlabel('Simulation Number')
    plt.ylabel('Wins')
    plt.yticks(np.arange(0,13,step = 1))
    st.pyplot(plt.gcf(),clear_figure=True)

player_wins_df.boxplot()
plt.title("Distribution of Predicted Wins for Each Owner")
plt.xticks(rotation=90)
st.pyplot(plt.gcf(), clear_figure=True)

percentiles = {}
z_scores = {}
for player in players_list:
    rw = real_wins.loc[player,"Wins"]
    wins_rw = player_wins_df.loc[:,player]
    rw_percentile = wins_rw[wins_rw<=rw].count()
    z = (rw-wins_rw.mean())/wins_rw.std()
    z_scores[player] = z
    percentiles[player] = rw_percentile/simulation_times

st.write("Percentiles:",percentiles, "\n\nz-scores:", z_scores)
st.write(pd.show_versions())