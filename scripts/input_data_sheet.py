import csv
import pandas as pd
import os

def input_data_sheet(counts_files, results_directory):
	fragment_lengths = set()

	for f in counts_files:
		with open(f, "r") as patient_file:
			reader = csv.reader(patient_file, delimiter="\t")
			next(reader, None)
		
			for row in reader:
				fragment_length = int(row[0])
				fragment_lengths.add(fragment_length)
		

	fragment_lengths = sorted(fragment_lengths)
	patient_data = []

	for f in counts_files:
		patient_counts = {length: 0 for length in fragment_lengths}
		patient_name = os.path.basename(f).replace("_output_counts.txt", "")
	

		with open(f, "r") as patient_file:
			reader=csv.reader(patient_file, delimiter="\t")
			next(reader, None)
		
			for row in reader:
				fragment_length = int(row[0])
				count = int(row[1])
				patient_counts[fragment_length] = count

		row_data = [patient_name] + [patient_counts[length] for length in fragment_lengths]
		patient_data.append(row_data)

	columns = ["Patient"] + fragment_lengths
	x_labels_df = pd.DataFrame(patient_data, columns=columns)

	x_labels_df.to_csv(os.path.join(results_directory, "x_labels.csv"), index=False)

	print(f" features-table saved as: x_labels.csv")

	return x_labels_df
