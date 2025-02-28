import glob
import os
import pysam
from collections import Counter


def get_fragments(bam_directory, blacklist, results_directory):

	bam_files = glob.glob(os.path.join(bam_directory, "**/*.bam"), recursive=True) 
	min_insert_size = 120
	max_insert_size = 225


	blacklist_dict = {}
	with open(blacklist, "r") as f:
		for line in f:
			chrom, start, end = line.strip().split()
			start, end = int(start), int(end)
			if chrom not in blacklist_dict:
				blacklist_dict[chrom] = []
			blacklist_dict[chrom].append((start, end))


	def is_in_blacklist(chrom, start, end):
		if chrom in blacklist_dict:
			for blk_start, blk_end in blacklist_dict[chrom]:
				if start >= blk_start and end <= blk_end:
					return True
		return False

	output_files = []


	for bam_file in bam_files:

		fragment_counts = Counter()
        
		bam_name = os.path.basename(bam_file).replace(".bam", "")
		output_file = os.path.join(results_directory, f"{bam_name}_output.txt")

		with pysam.AlignmentFile(bam_file, "rb") as bam, open(output_file, "w") as output:
			output.write("Chromosome\tStart\tEnd\tInsertSize\n")
			for read in bam.fetch():
				if read.is_unmapped:
            				continue
				if not read.is_proper_pair:
					continue

        
				if read.template_length < min_insert_size:
					continue

				if read.template_length > max_insert_size:
					continue

				start = read.reference_start + 1  
				end = read.reference_end 
				chromosome = read.reference_name        

				insert_size = read.template_length

				if is_in_blacklist(chromosome, start, end):
					continue
			
				fragment_counts[insert_size] += 1


				output.write(f"{chromosome}\t{start}\t{end}\t{insert_size}\n")
		
		output_files.append(output_file)
		print(f"Processed: {bam_file}")

	print("All bamfiles processed, extraction and filtering of fragments complete")

	return output_files
