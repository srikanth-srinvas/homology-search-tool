from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import argparse


def homology_search(fasta_file, blast_program, evalue, database, outfmt):
  """
  Performs a homology search using BLAST+ and generates a report.

  Args:
      fasta_file (str): Path to the FASTA file containing query sequences.
      blast_program (str): BLAST program to use (e.g., "blastn" for nucleotide).
      evalue (float): Expectation value threshold.
      database (str): BLAST database to search against (e.g., "nr").
      outfmt (int): BLAST output format (default: 5 for XML).

  Returns:
      str: A comprehensive report summarizing the BLAST search results.
  """

  report = f"Homology Search Report for: {fasta_file}\n"
  report += f"BLAST Program: {blast_program}\n"
  report += f"E-value Threshold: {evalue}\n"
  report += f"Database: {database}\n\n"

  with open(fasta_file, "r") as handle:
      sequences = list(SeqIO.parse(handle, "fasta"))

  for sequence in sequences:
      fasta_string = sequence.seq.format("fasta")
      sequence_id = sequence.id

      report += f"**Query Sequence ID: {sequence_id}**\n"

      try:
          blast_results = NCBIWWW.qblast(program=blast_program, query=fasta_string,
                                         evalue=evalue, database=database, outfmt=outfmt)
          with open("blast_output.xml", "w") as out_handle:
              out_handle.write(blast_results.read())
          blast_results.close()

          with open("blast_output.xml", "r") as handle:
              blast_record = NCBIXML.read(handle)

          if not blast_record.alignments:
              report += f"\tNo significant hits found for this query.\n\n"
          else:
              for alignment in blast_record.alignments:
                  hit_id = alignment.title.split()[1]
                  evalue = alignment.hsps[0].expect

                  report += f"\tHit ID: {hit_id}\n"
                  report += f"\tE-value: {evalue:.2e}\n"
                  report += f"\t**Alignment:**\n{alignment.hsps[0].alignment}\n\n"

      except Exception as e:
          report += f"\tError: {e}\n\n"

  return report


def main():
  """
  Parses user arguments and runs the homology search.
  """

  parser = argparse.ArgumentParser(description="Homology Search Tool")
  parser.add_argument("-f", "--fasta", required=True, help="Path to the FASTA file")
  parser.add_argument("-p", "--program", default="blastn", help="BLAST program (default: blastn)")
  parser.add_argument("-e", "--evalue", type=float, default=0.001, help="E-value threshold (default: 0.001)")
  parser.add_argument("-d", "--database", default="nr", help="BLAST database (default: nr)")
  parser.add_argument("-o", "--output", default="homology_report.txt", help="Output report filename (default: homology_report.txt)")

  args = parser.parse_args()

  report = homology_search(args.fasta, args.program, args.evalue, args.database, 5)

  with open(args.output, "w") as out_handle:
      out_handle.write(report)

  print(f"Homology search results saved to: {args.output}")


if __name__ == "__main__":
  main()