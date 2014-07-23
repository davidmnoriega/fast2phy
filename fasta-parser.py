#!/usr/bin/env python
from itertools import zip_longest
from pyfasta import Fasta
from sys import argv

LINE_LENGTH = 60
CHUNK_LENGTH = 10
PAD_STRING = ''.ljust(CHUNK_LENGTH)

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def main():
    f = Fasta(argv[1])
    sequence_count = len(f.keys())
    sequence_length = len(f[next(iter(f.keys()))])
    print('', sequence_count, sequence_length, sep=' ')
    #count = 1
    for key in f.keys():
        subseq = []
        for chunk in grouper(f[key][:LINE_LENGTH], CHUNK_LENGTH):
            subseq.append(''.join(item[0] for item in chunk))
        subseq = ' '.join(subseq)
        if len(key) < CHUNK_LENGTH:
            key = key.ljust(CHUNK_LENGTH)
        else:
            key = key[:CHUNK_LENGTH]
        print(key, ' ', subseq)
    
    sequence_length -= LINE_LENGTH
    start = LINE_LENGTH
    stop = LINE_LENGTH * 2
    print()

    while sequence_length > 0:
        #count += 1
        #print(count)

        for key in f.keys():
            subseq = []
            for chunk in grouper(f[key][start:stop], CHUNK_LENGTH, ' '):
                #print(subseq)
                subseq.append(''.join(item[0] for item in chunk))
            #print(subseq)
            subseq = ' '.join(subseq)
            print(PAD_STRING, ' ', subseq)
        sequence_length -= LINE_LENGTH
        start += LINE_LENGTH
        stop += LINE_LENGTH
        print()


if __name__ == '__main__' :
    main()
