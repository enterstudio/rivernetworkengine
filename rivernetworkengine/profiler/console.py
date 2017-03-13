import argparse
import sys
from rivernetworkengine import Logger
import profiler

def console():
    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('shapefile',
                        help='Path to the SHP input file',
                        type=argparse.FileType)
    parser.add_argument('--start_id',
                        help='Path to the CSV output file',
                        type=argparse.FileType)
    parser.add_argument('--end_id',
                        help='(Optional) ID of endppoint. Will use outflow as a default.',
                        type=argparse.FileType)
    parser.add_argument('--id_name',
                        help='Name of the field to use as id. \'OBJECTID\' is used as default.',
                        type=argparse.FileType)
    parser.add_argument('--attrib',
                        help='Comma-separated list of attributes to summarize.',
                        type=argparse.FileType)
    parser.add_argument('csvoutput',
                        help='Path to the CSV output file',
                        type=str)
    parser.add_argument('--program',
                        default="thing",
                        help='Path or url to the Program XML file (optional)')
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
        profiler.main(args.shapefile.name)
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
