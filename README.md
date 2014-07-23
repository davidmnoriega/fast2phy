fast2phy
========

Convert aligned FASTA format to interleaved PHYLIP format

Pronounced `fɑst tu faɪ` like the Greek letter Φ. 
Alternatively, if you are like me and you pronounce phylip as philip.

Usage
-----

```
fast2phy [options] FILE

Convert aligned FASTA format to interleaved PHYLIP format

positional arguments:
  FILE                  Aligned FASTA file to convert

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Specify output PHYLIP file
  --inplace             Flatten FASTA file in place
```

By default, fast2phy will take the specified aligned fasta file and output an interleaved phylip file. 
fast2phy uses [pyfasta](https://github.com/brentp/pyfasta/), from Brent Pedersen, to read in fasta files. 
pyfasta by default will create a flattened version of the fasta, effectively copying the fasta file. 
The flattening process removes all the headers and new lines from the sequences. This may not
be desired if the original fasta file is very large. Using the `--inline` option will keep the headers in place,
keeping a valid fasta file, but will remove all the new line characters.

Read pyfasta's [README](https://github.com/brentp/pyfasta/blob/master/README.rst#flattening) for more details.