import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
matches = pd.read_csv("IPL_Matches_2022.csv")
# Select numerical columns
correlation = matches[
    ["Margin"]
].corr()

# Print correlation matrix
print("Correlation Analysis:\n")

print(correlation)