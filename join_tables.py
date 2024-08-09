#!/mnt/c/Software/WSL/miniconda3/bin/python3
# Noah Winters
# Uses pd.merge to join two tables.
import pandas as pd
import argparse

# Add argparse arguments
parser=argparse.ArgumentParser(description="Uses pd.merge to join two tables.")
parser.add_argument('-t1', '--input_table1', action='store', help='Input table 1.', required = True)
parser.add_argument('-t2', '--input_table2', action='store', help='Input table 2.', required = True)
parser.add_argument('-lc', '--left_column', action='store', help='Left hand column to join on', required = True)
parser.add_argument('-rc', '--right_column', action='store', help='Right hand column to join on', required = True)
parser.add_argument('-f', '--filter_columns', nargs = '+', default = [], type = str, help='Comma-separated list of columns to extract')
parser.add_argument('-o', '--output_table', action='store', help='Output table.')
args=parser.parse_args()


t1 = pd.read_csv(args.input_table1, sep = '\t')
t2 = pd.read_csv(args.input_table2, sep = '\t')
t3 = pd.merge(t1, t2, how = "left", right_on = args.left_column, left_on = args.right_column)

if len(args.filter_columns) > 0:
    t3 = t3[args.filter_columns]
    t3.to_csv(args.output_table, sep = '\t', index = False)
else:
    t3.to_csv(args.output_table, sep = '\t', index = False)