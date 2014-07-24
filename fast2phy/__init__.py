from itertools import zip_longest
from pyfasta import Fasta
from fast2phy.command_line import make_parser

LINE_LENGTH = 60
CHUNK_LENGTH = 10
PAD_STRING = ''.ljust(CHUNK_LENGTH)


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def main():
    args = make_parser()
    if args.inplace:
        f = Fasta(args.fasta_file, flatten_inplace=True)
    else:
        f = Fasta(args.fasta_file)

    if args.output_file is not None:
        output = open(args.output_file, 'w')
    else:
        output_file_name = args.fasta_file.split('.')[0]
        output_file = '{0}.phylip'.format(output_file_name)
        output = open(output_file, 'w')

    sequence_count = len(f.keys())
    sequence_length = len(f[next(iter(f.keys()))])
    # print('', sequence_count, sequence_length, sep=' ')
    output.write(' {0} {1}\n'.format(sequence_count, sequence_length))

    for key in f.keys():
        subseq = []
        for chunk in grouper(f[key][:LINE_LENGTH], CHUNK_LENGTH):
            subseq.append(''.join(item[0] for item in chunk))
        subseq = ' '.join(subseq)
        if len(key) < CHUNK_LENGTH:
            key = key.ljust(CHUNK_LENGTH)
        else:
            key = key[:CHUNK_LENGTH]
        # print(key, ' ', subseq)
        output.write('{0} {1}\n'.format(key, subseq))

    sequence_length -= LINE_LENGTH
    start = LINE_LENGTH
    stop = LINE_LENGTH * 2
    # print()
    output.write('\n')

    while sequence_length > 0:
        for key in f.keys():
            subseq = []
            for chunk in grouper(f[key][start:stop], CHUNK_LENGTH, ' '):
                subseq.append(''.join(item[0] for item in chunk))
            subseq = ' '.join(subseq)
            # print(PAD_STRING, ' ', subseq)
            output.write('{0} {1}\n'.format(PAD_STRING, subseq))
        sequence_length -= LINE_LENGTH
        start += LINE_LENGTH
        stop += LINE_LENGTH
        # print()
        output.write('\n')

    output.close()


if __name__ == '__main__':
    main()
