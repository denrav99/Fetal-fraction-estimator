import os
import pandas as pd
import csv

def get_FFY(ffy_directory):
	FFY_values = {}

	for f in os.listdir(ffy_directory):
		filepath = os.path.join(ffy_directory, f)
		#print(filepath)
	
		patient_name = f.replace(".tiddit.AMYCNE.tab", "")
	
		with open(filepath, "r") as patient_file:
			reader = csv.reader(patient_file, delimiter="\t")

			rows = list(reader)
			row = rows[1]
			FFY_row = row[0].split()
			FFY = float(FFY_row[3].strip())
		
			FFY_values[patient_name] = FFY		


	FFY_df = pd.DataFrame(list(FFY_values.items()), columns = ["Patient", "FFY"])

	print("Patient-ID and corresponding FFY:")
	for patient, FFY in FFY_values.items():
		print(f"Patient: {patient}, FFY: {FFY}")		

	return FFY_df
