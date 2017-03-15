import argparse
import sys
from os import path
from rivernetworkengine import Logger
from profiler import Profile

def console():
    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('shapefile',
                        help='Path to the SHP input file',
                        type=str)
    parser.add_argument('csvoutput',
                        help='Path to the CSV output file',
                        type=str)
    parser.add_argument('--start_id',
                        help='Path to the CSV output file',
                        type=int)
    parser.add_argument('--end_id',
                        help='(Optional) ID of endppoint. Will use outflow as a default.',
                        type=int)
    parser.add_argument('--cols',
                        help='(Optional) Comma-separated list of attributes/columns to summarize. If not provided then all will be included',
                        type=str)
    parser.add_argument('--logfile',
                        help='Write the results of the operation to a specified logfile (optional)')
    parser.add_argument('--verbose',
                        help = 'Get more information in your logs (optional)',
                        action='store_true',
                        default=False)

    args = parser.parse_args()

    log = Logger("Program")
    log.setup(args)

    try:
        if not path.isfile(args.shapefile):
            raise Exception('Shapefile not found: {'.format(args.shapefile))
        if not args.start_id:
            raise Exception('Must include a valid --start_id parameter')
        theProfile = Profile(args.shapefile, args.start_id, args.end_id)

        includedcols = ""
        if args.cols:
            includedcols = args.cols

        theProfile.writeCSV(args.csvoutput, includedcols)
    except AssertionError as e:
        log.error("Assertion Error", e)
        sys.exit(0)
    except Exception as e:
        log.error('Unexpected error: {0}'.format(sys.exc_info()[0]), e)
        raise
        sys.exit(0)


"""
This handles the argument parsing and calls our main function
If we're not calling this from the command line then
"""
if __name__ == '__main__':
    console()
