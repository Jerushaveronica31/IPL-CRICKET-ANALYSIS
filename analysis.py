import pandas as pd

matches_df = pd.read_csv("matches.csv")

# டாஸ் வென்றவர்கள் எடுத்த முடிவுகள் (Batting or Fielding)
print("Toss Decisions Breakdown:")
print(matches_df['toss_decision'].value_counts())