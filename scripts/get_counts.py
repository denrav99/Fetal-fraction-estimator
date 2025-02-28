import pandas as pd
import os

def get_counts(fragment_txt_files, counts_directory):

	output_files = []

	for f in fragment_txt_files:
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

		output_filename = os.path.join(counts_directory, os.path.basename(f).replace(".txt", "_counts.txt"))

		output_files.append(output_filename)

		count_df.to_csv(output_filename, sep="\t", index=False)

	return output_files
