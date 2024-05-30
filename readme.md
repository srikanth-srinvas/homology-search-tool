# Homology Search Tool


![alt text](image.png)


This Python script performs homology searches using BLAST+ and Biopython. It analyzes your FASTA file containing query sequences, generates a report summarizing the results, and saves it to a text file.

## Features

- **BLAST+ Integration:** Leverages BLAST+ to search against various biological sequence databases.
- **Biopython Compatibility:** Utilizes Biopython's SeqIO module for efficient sequence handling.
- **User-Friendly Input:** Accepts command-line arguments for file paths, BLAST program, e-value threshold, database selection, and output filename.
- **Detailed Report Generation:** Creates a report including search parameters and significant hits for each query sequence.

## Installation

### Prerequisites

Ensure you have Python (version 3.x recommended) and Biopython installed. You can install Biopython using the following command:

```bash
pip install biopython
```

### BLAST+ Installation

Install BLAST+ on your system following the appropriate method for your operating system. Refer to the [NCBI BLAST+ documentation](https://www.ncbi.nlm.nih.gov/blast/) for detailed instructions.

### Clone or Download

Clone this repository using Git or download the script file (`main.py`).

## Usage

1. **Save the Script:** Save the script file (`main.py`) in a directory on your system.
2. **Open Terminal/Command Prompt:** Navigate to the directory where you saved the script.
3. **Run the Script:** Execute the script using the following command, replacing placeholders with your actual values:

```bash
python main.py -f <fasta_file_path> -o <output_report_filename> [optional arguments]
```

## Arguments

- `-f <fasta_file_path>` (Required): Path to your FASTA file containing query sequences.
- `-o <output_report_filename>` (Required): Desired filename for the output report (default: `homology_report.txt`).
- `-p <blast_program>` (Optional): BLAST program to use (default: `blastn` for nucleotides, `blastp` for proteins).
- `-e <evalue>` (Optional): E-value threshold (default: `0.001`).
- `-d <database>` (Optional): BLAST database to search against (default: `nr` for non-redundant protein sequences).

## Example

```bash
python main.py -f my_sequences.fasta -o blast_results.txt -p blastp -e 0.01 -d swissprot
```

This command will run a BLASTP search against the SwissProt protein database with an e-value threshold of `0.01` and save the results to a file named `blast_results.txt`.

## Additional Notes

- **Database Installation:** Download and install the specific BLAST+ databases you want to use from the [NCBI FTP server](https://www.ncbi.nlm.nih.gov/blast/).
- **Environment Variable (Optional):** Consider adding the BLAST+ executables directory to your system's PATH environment variable for easier command-line access.


---

This project utilizes [Biopython](https://biopython.org/) and its SeqIO module, as well as the BLAST+ software from [NCBI](https://www.ncbi.nlm.nih.gov/blast/).
