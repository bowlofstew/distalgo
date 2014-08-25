import sys
import logging
import argparse

__version__ = "1.0.0a4"

from .api import entrypoint

if hasattr(sys, '_real_argv'):
    sys.argv[0] = sys._real_argv

log = logging.getLogger(__name__)
formatter = logging.Formatter(
    '[%(asctime)s]%(name)s:%(levelname)s: %(message)s')
log._formatter = formatter

def parseArgs():
    LogLevelNames = [n.lower() for n in logging._nameToLevel]

    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument("-s", "--perffile")
    parser.add_argument("-u", "--dumpfile")
    parser.add_argument('--iterations', type=int, default=1)
    parser.add_argument("--nolog", action="store_true", default=False)
    parser.add_argument("-f", "--logfile", action="store_true", default=False)
    parser.add_argument("--logfilename")
    parser.add_argument("--logdir")
    parser.add_argument("-L", "--logconsolelevel",
                        choices=LogLevelNames, default="info")
    parser.add_argument("-F", "--logfilelevel",
                        choices=LogLevelNames, default="debug")
    parser.add_argument("-i", "--loadincmodule",
                        action="store_true", default=False)
    parser.add_argument("-m", "--incmodulename")
    parser.add_argument("-r", "--recompile", dest="recompile",
                        help="Force recompile DistAlgo source file. ",
                        action="store_true", default=False)
    parser.add_argument("-c", "--compiler-flags", default="")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("file",
                        help="DistAlgo file to execute.")
    parser.add_argument("args", nargs=argparse.REMAINDER,
                        help="arguments passed to program in sys.argv[1:].")

    return parser.parse_args()

def libmain():
    """
    Main program entry point. Parses command line options, sets up global
    variables, and calls the 'main' function of the DistAlgo program.
    """

    entrypoint(parseArgs())

def die(mesg = None):
    if mesg != None:
        sys.stderr.write(mesg + "\n")
    sys.exit(1)

if __name__ == '__main__':
    libmain()
