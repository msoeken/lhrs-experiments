import argparse
import json

from runners import run_and_log
from synthesis import get_default_algorithms

algorithms = get_default_algorithms()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--configuration', dest='configuration', default="{}", type=json.loads, help='JSON string for algorithm parameters')
    parser.add_argument('--method', dest='method', default='lhrs', help='Synthesis method (lhrs)')
    parser.add_argument('benchmark', help='benchmark')
    parser.add_argument('logname', help='log filename')

    args = parser.parse_args()

    run_and_log(args.benchmark, args.method, algorithms[args.method], args.configuration, args.logname)
