import os
import glob
import pandas as pd

base_dir = "filepath to txt files"
txt_files = glob.glob(os.path.join(base_dir, "*output.txt"))

for f in txt_files:
	print(f)
	data = pd.read_csv(f, sep="\t", header = 0)

	fragment_lengths = data["InsertSize"]
	fragment_counts = {}

	for fragment in fragment_lengths:

		if fragment in fragment_counts:
			fragment_counts[fragment] += 1
		else:
			fragment_counts[fragment] = 1


	count_df = pd.DataFrame(list(fragment_counts.items()), columns=["InsertSize", "count"])

	output_filename = f.replace(".txt", "_with_counts.txt")

	count_df.to_csv(output_filename, sep="\t", index=False)
