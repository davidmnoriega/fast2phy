from sys import exit, stderr
from os.path import isfile
from argparse import ArgumentParser, ArgumentTypeError


class DefaultParser(ArgumentParser):
    """Override ArgumentParser's handing of no argument error.
    Only print help message if error is for missing argument,
    otherwise, only print the error."""
    def error(self, message):
        stderr.write('error: %s\n' % message)
        if 'required' in message:
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
    parser.add_argument('-o',
                        '--output',
                        required=False,
                        help="Specify output PHYLIP file")
    parser.add_argument('--inplace',
                        required=False,
                        action='store_true',
                        help="Flatten FASTA file in place")
    return vars(parser.parse_args())
