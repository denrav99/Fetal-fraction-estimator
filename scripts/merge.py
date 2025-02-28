import pandas as pd
import os

def merge(x_labels, y_labels, results_directory):
	features_df = x_labels  # Assuming this is your features table
	target_df = y_labels      # Assuming this is your target table

	merged_df = pd.merge(features_df, target_df, on="Patient")
	merged_df = merged_df[merged_df["FFY"] != 0]

	features = merged_df.drop(columns=["Patient", "FFY"])
	target = merged_df["FFY"] 

	features.to_csv(os.path.join(results_directory, "features.csv"), index=False)
	target.to_csv(os.path.join(results_directory, "target.csv"), index=False)

	print("features saved as features.csv(fragment insert sizes and their counts), target saved as target.csv(FFY)")

	return features, target 
