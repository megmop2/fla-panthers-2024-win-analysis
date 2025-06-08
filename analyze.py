import pandas as pd

# load in FLA data
FLA_data = pd.read_csv("FLA.csv")

print(FLA_data.head())

# Check for nulls and clean the dataset
cleaned_data = FLA_data.dropna()

# Were any rows dropped? - no rows dropped!
print(len(FLA_data))

print(len(cleaned_data))

# Columns of the dataset
print(cleaned_data.columns)

# What was the home vs. away win % in the 2024 season for the FLA panthers?
# make sure season is filtered to 2024
# make sure all game situations are account for!

print(cleaned_data['situation'].unique()) # you want the "all" column

# Filter by 2024 season - want all situations!
season2024 = cleaned_data[
    (cleaned_data['season'] == 2024) &
    (cleaned_data['situation'] == 'all')
]

print(season2024)

# Home and away subsets
print(season2024['home_or_away'].unique())

home_games = season2024[season2024['home_or_away'] == 'HOME']
away_games = season2024[season2024['home_or_away'] == 'AWAY']

# Home and away game wins (goalsFor > goalsAgainst)
home_wins = home_games[home_games['goalsFor'] > home_games['goalsAgainst']]

away_wins = away_games[away_games['goalsFor'] > away_games['goalsAgainst']]

# Win % for home vs. away
home_win_percent = len(home_wins) / len(home_games) * 100 if len(home_games) > 0 else 0

away_win_percent = len(away_wins) / len(away_games) * 100 if len(away_games) > 0 else 0

print(f"Home Win Percentage for 2024 Season: {home_win_percent:.1f}%")
print(f"Away Win Percentage for 2024 Season: {away_win_percent:.1f}%")

"""
The FLA Panthers had a home win percentage of 56.1% and an away win percentage
of 43.9% during the 2024 season.
"""

# Bar chart to compare
import matplotlib.pyplot as plt

# Labels, values, colors
labels = ['Home', 'Away']
win_percentages = [home_win_percent, away_win_percent]
colors = ['skyblue', 'red']

# Create bar chart
plt.bar(labels,win_percentages, color = colors)

# Add labels
plt.ylabel('Win Percentage (%)')
plt.title('Fla Panthers 2024 Home vs. Away Win %')
plt.ylim(0,100) # y axis from 0 to 100

# Add values to top of bars
plt.annotate(f"{home_win_percent:.1f}%", xy=(0, home_win_percent + 1), ha='center')
plt.annotate(f"{away_win_percent:.1f}%", xy=(1, away_win_percent + 1), ha='center')

# Save image
plt.savefig("fla_win_chart.png", dpi=300, bbox_inches='tight')

plt.show()
