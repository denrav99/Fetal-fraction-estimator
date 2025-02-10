import pandas as pd

features_df = pd.read_csv("x_labels.csv")  # Assuming this is your features table
target_df = pd.read_csv("y_labels.csv")      # Assuming this is your target table

merged_df = pd.merge(features_df, target_df, on="Patient")
merged_df = merged_df[merged_df["FFY"] != 0]

X = merged_df.drop(columns=["Patient", "FFY"])  # All columns except Patient_ID and FFY_value
y = merged_df["FFY"]  # Target column

X.to_csv("features.csv", index=False)
y.to_csv("target.csv", index=False)
