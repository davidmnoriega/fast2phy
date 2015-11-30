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
  --inplace             Flatten FASTA file in place
  --output OUTPUT_FILE  Specify output PHYLIP file
  --stdout              Print to stdout instead of file
```

By default, fast2phy will take the specified aligned fasta file and output an
interleaved phylip file.  fast2phy uses
[pyfasta](https://github.com/brentp/pyfasta/), from Brent Pedersen, to read in
fasta files.  pyfasta by default will create a flattened version of the fasta,
effectively copying the fasta file.  The flattening process removes all the
headers and new lines from the sequences. This may not be desired if the
original fasta file is very large. Using the `--inplace` option will keep the
headers in place, keeping a valid fasta file, but will remove all the new line
characters.

Read pyfasta's [README](https://github.com/brentp/pyfasta/blob/master/README.rst#flattening) for more details.

The `--stdout` option will instead print the generated PHYLIP file to the
screen. This is useful if you want to pipe  the results to another program, like
gzip.
