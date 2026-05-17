import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# LOAD DATASET
# =====================================

matches = pd.read_csv("IPL_Matches_2022.csv")

# =====================================
# BASIC INFORMATION
# =====================================

print("\nTotal IPL Matches Played:")
print(len(matches))

# =====================================
# TEAM WINS ANALYSIS
# =====================================

team_wins = matches["WinningTeam"].value_counts()

print("\nMost Successful IPL Teams:\n")
print(team_wins)

# Create bar chart
plt.figure(figsize=(10, 5))

team_wins.plot(kind="bar")

plt.title("IPL 2022 Team Wins")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")

plt.xticks(rotation=45)

# Save chart
plt.savefig("charts/team_wins.png")

plt.show()

# =====================================
# TOSS DECISION ANALYSIS
# =====================================

toss_decision = matches["TossDecision"].value_counts()

print("\nToss Decisions:\n")
print(toss_decision)

# Pie chart
plt.figure(figsize=(6, 6))

toss_decision.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Toss Decision Analysis")

plt.ylabel("")

plt.savefig("charts/toss_decision_pie.png")

plt.show()

# =====================================
# VENUE ANALYSIS
# =====================================

venue_matches = matches["Venue"].value_counts().head(10)

print("\nTop Venues:\n")
print(venue_matches)

plt.figure(figsize=(10, 5))

venue_matches.plot(kind="bar")

plt.title("Top IPL Venues")
plt.xlabel("Venue")
plt.ylabel("Matches Hosted")

plt.xticks(rotation=75)

plt.savefig("charts/venue_analysis.png")

plt.show()

# =====================================
# WINNING MARGIN ANALYSIS
# =====================================

margin = matches["Margin"]

plt.figure(figsize=(8, 5))

plt.hist(margin, bins=10)

plt.title("Winning Margin Distribution")
plt.xlabel("Winning Margin")
plt.ylabel("Frequency")

plt.savefig("charts/winning_margin_histogram.png")

plt.show()

# =====================================
# PROJECT COMPLETED
# =====================================

print("\nIPL Data Analysis Completed Successfully!")