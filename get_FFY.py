import os
import pandas as pd
import csv

base_directory = "filepath to all tiddit.amycne.tab files"
FFY_values = {}

for f in os.listdir(base_directory):
	filepath = os.path.join(base_directory, f)
	#print(filepath)
	
	patient_name = f.replace(".tiddit.AMYCNE.tab", "")
	
	with open(filepath, "r") as patient_file:
		reader = csv.reader(patient_file, delimiter="\t")

		rows = list(reader)
		row = rows[1]
		FFY_row = row[0].split()
		FFY = float(FFY_row[3].strip())

#		print(rows)
		
#		print(FFY)		

		FFY_values[patient_name] = FFY		


FFY_df = pd.DataFrame(list(FFY_values.items()), columns = ["Patient", "FFY"])
output_file = "y_lables.csv"
FFY_df.to_csv(output_file, index = False)
#print(FFY_values)

#for patient, FFY in FFY_values.items():
#	print(f"Patient: {patient}, FFY: {FFY}")		

