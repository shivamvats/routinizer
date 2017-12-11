import argparse
import pickle as pk
from executor import setReadIndex

parser = argparse.ArgumentParser(description="Routinizer settings.")
parser.add_argument("index", help="New index of read essays.")
args = parser.parse_args()
setReadIndex(args.index)


