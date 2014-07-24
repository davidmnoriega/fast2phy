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
        output_file = args.output_file
    else:
        output_file_name = args.fasta_file.split('.')[0]
        output_file = '{0}.phylip'.format(output_file_name)

    sequence_count = len(f.keys())

    with open(output_file, 'w+b') as output:
        first = 1
        for key in f.keys():
            if first == 1:
                sequence_length = len(f[key])
                output.write(' {0} {1}\n'.format(sequence_count, sequence_length))
                first += 1

            subseq = []
            for chunk in grouper(f[key][:LINE_LENGTH], CHUNK_LENGTH):
                subseq.append(''.join(item[0] for item in chunk))
            subseq = ' '.join(subseq)
            if len(key) < CHUNK_LENGTH:
                key = key.ljust(CHUNK_LENGTH)
            else:
                key = key[:CHUNK_LENGTH]

            output.write('{0} {1}\n'.format(key, subseq))
            output.flush()

        sequence_length -= LINE_LENGTH
        start = LINE_LENGTH
        stop = LINE_LENGTH * 2

        output.write('\n')

        while sequence_length > 0:
            for key in f.keys():
                subseq = []
                for chunk in grouper(f[key][start:stop], CHUNK_LENGTH, ' '):
                    subseq.append(''.join(item[0] for item in chunk))
                subseq = ' '.join(subseq)

                output.write('{0} {1}\n'.format(PAD_STRING, subseq))
            sequence_length -= LINE_LENGTH
            start += LINE_LENGTH
            stop += LINE_LENGTH

            output.write('\n')
            output.flush()


if __name__ == '__main__':
    main()
