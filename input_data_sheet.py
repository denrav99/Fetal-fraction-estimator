import pandas as pd
import csv
import os

counts_directory = "/proj/sens2017106/nobackup/denise/thesis/FF_estimator/fragments/counts"

fragment_lengths = set()

for f in os.listdir(counts_directory):
	filepath = os.path.join(counts_directory, f)
	
	with open(filepath, "r") as patient_file:
		reader = csv.reader(patient_file, delimiter="\t")
		next(reader, None)
		
		for row in reader:
			fragment_length = int(row[0])
			fragment_lengths.add(fragment_length)
		

fragment_lengths = sorted(fragment_lengths)
patient_data = []

for f in os.listdir(counts_directory):
	filepath = os.path.join(counts_directory, f)

	patient_counts = {length: 0 for length in fragment_lengths}
	patient_name = f.replace("_output_with_counts.txt", "")
	

	with open(filepath, "r") as patient_file:
		reader=csv.reader(patient_file, delimiter="\t")
		next(reader, None)
		
		for row in reader:
			fragment_length = int(row[0])
			count = int(row[1])
			patient_counts[fragment_length] = count

	row_data = [patient_name] + [patient_counts[length] for length in fragment_lengths]
	patient_data.append(row_data)

columns = ["Patient"] + fragment_lengths
consolidated_df = pd.DataFrame(patient_data, columns=columns)

output_file = "x_labels.csv"
consolidated_df.to_csv(output_file, index=False)


print(f"table saved as: {output_file}")
