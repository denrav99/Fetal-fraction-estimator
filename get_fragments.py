import os
import glob
import pysam
from collections import Counter

base_dir = "/proj/sens2017106/denise_fluffy_test9" 
bam_files = glob.glob(os.path.join(base_dir, "**/*.bam"), recursive=True) 
out = "/proj/sens2017106/nobackup/denise/thesis/FF_estimator/fragments"
blacklist = "/proj/sens2017106/nobackup/denise/blacklist_proj/output/tables/blacklist_separated_by_sex/finished_blacklist_sex_separated_0.25.bed"
min_insert_size = 120
max_insert_size = 225

overall_fragment_counts = Counter()

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



for bam_file in bam_files:

	fragment_counts = Counter()
        
	bam_name = os.path.basename(bam_file).replace(".bam", "")
	output_file = os.path.join(out, f"{bam_name}_output.txt")

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
		

		overall_fragment_counts.update(fragment_counts)

	print(f"Processed: {bam_file}")

summary_file = os.path.join(out, "fragment_length_summary.txt")
with open(summary_file, "w") as summary:
	summary.write("FragmentLength\tCount\n")
	for length, count in sorted(overall_fragment_counts.items()):
		summary.write(f"{length}\t{count}\n")

print("All bamfiles processed")
