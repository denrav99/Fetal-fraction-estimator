import pandas as pd
import os
import glob
import argparse
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse
import csv
import pysam
from collections import Counter

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from get_FFY import get_FFY
from get_fragments import get_fragments
from get_counts import get_counts
from input_data_sheet import input_data_sheet
from merge import merge
from run_model import run_model

parser = argparse.ArgumentParser(description="Fetal fraction estimation from chrY using linear regression")

parser.add_argument("--bam_directory", type=str, required=True)
parser.add_argument("--blacklist", type=str, required=True)
parser.add_argument("--results_directory", type=str, required=True)
parser.add_argument("--counts_directory", type=str, required=True)
parser.add_argument("--FFY_directory", type=str, required=True)

args = parser.parse_args()


y_labels = get_FFY(args.FFY_directory)

print("started extracting and filtering fragments from bamfiles")
fragment_files = get_fragments(args.bam_directory, args.blacklist, args.results_directory)

print("Started counting unique fragment lengths")
counts_files = get_counts(fragment_files, args.counts_directory)

x_labels = input_data_sheet(counts_files, args.results_directory)

print("Creating features and target")
features, target = merge(x_labels, y_labels, args.results_directory)

print("Running regression model")
regression_results = run_model(features, target)
