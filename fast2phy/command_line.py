from sys import exit, stderr
from os.path import isfile
from argparse import ArgumentParser, ArgumentTypeError


class DefaultParser(ArgumentParser):
    """Override ArgumentParser's handing of no argument error.
    Only print help message if error is for missing argument,
    otherwise, only print the error."""
    def error(self, message):
        stderr.write('error: %s\n' % message)
        # Fix for Python 3.2
        if 'required' or 'too few' in message:
            self.print_help()
        exit(2)


def check_file(filename):
    "argparse type to check if file exists"
    if not isfile(filename):
        raise ArgumentTypeError("Specified file: {0} does not exist".format(filename))
    return filename


def make_parser():
    "Defines command line parser for fast2phy"
    parser = DefaultParser(prog='fast2phy',
                           usage='%(prog)s [options] FILE',
                           description="Convert aligned FASTA format to interleaved PHYLIP format")
    parser.add_argument('fasta_file',
                        metavar='FILE',
                        type=check_file,
                        help="Aligned FASTA file to convert")
    parser.add_argument('--inplace',
                        required=False,
                        action='store_true',
                        help="Flatten FASTA file in place")

    parser_group = parser.add_mutually_exclusive_group()

    parser_group.add_argument('--output',
                              required=False,
                              dest='output_file',
                              help="Specify output PHYLIP file")
    parser_group.add_argument('--stdout',
                              required=False,
                              action='store_true',
                              help="Print to stdout instead of file")

    return parser.parse_args()
