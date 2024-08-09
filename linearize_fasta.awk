#!/usr/bin/env bash
# Noah Winters
# Awk script to linearize a fasta file, i.e. header in Col1 and sequence in Col2
# Run using awk -f linearize_fasta.awk <file.fasta>
/^>/ {printf("%s%s\t",(N>0?"\n":""),$0);N++;next;}
     {printf("%s",$0);}
END  {printf("\n");}
