# useful_bioinformatics_scripts
A small collection of scripts I have found useful when performing bioinformatic tasks. When code was not written by me, attribution is provided. Most of these are for manipulating tables and/or file IDs with Bash.

# scripts
```bash
bash batch_rename_folders.sh
```
Batch renames folders contained in a given directory. Relies on a tab-delimited file, indicated in the bash script, containing old_id in the first column and new_id in the second column. 
< br / >

```bash
bash col_mean.sh {input.tsv}
```
Calculates the mean of a given column. Currently specifies the first column ($1), but this can be changed to indicate a different column if desired.


```python
python join_tables.py -t1 {table1.tsv} -t2 {table2.tsv} --left_column {left_col} --right_column {right_col} --filter_columns {col1, col2...} --output_table {output.tsv}
```
Uses pd.merge to perform a left merge. Can also specify the columns that should be returned using --filter_columns. Requires pandas. Can use join_tables.py -h for more information.


```bash
awk -f linearize_fasta.awk {input.fasta}
```
Awk script to linearize a fasta file, i.e. header in Col1 and sequence in Col2. 


```bash
bash regex_rename_files.sh {input_file} {regular_expression} {replacement}
```
Uses sed to dynamically rename files. Regular expression and replacement do not need to be in quotes.


```python
python rename_fasta_headers.py --tab {new_names.txt} {file.fasta} > {newfile.fasta}
```
Renames fasta headers based on a tab-delimited file containing [oldname] [newname]. Originally writte by Jason Kwong (https://github.com/kwongj/fa-rename). Can use rename_fasta_headers.py -h for more information.
