# Fetal-fraction-estimator
Predicting fetal fraction from chromosome Y using insert size using Linear Regression.

#1. FFY extraction

Use get_FFY.py to extract FFY values from TIDDIT.amycne.tab files

#2. Features extraction

* Use get_fragments.py to extract fragments inside given length interval excluding fragments from blacklisted regions.

* Use get.counts.py to extract all fragment lengths and their counts

* Use input_data_sheet.py to get features table

* Use merge.py to merge target och features on patient.

#4. Linear regression

Use machine_lenrning.py to perform scaling, PCA and linear regression.


