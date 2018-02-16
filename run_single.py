import argparse
import json

from lib.database import Database
from lib.runners import run_and_log, insert_and_log
from lib.synthesis import get_default_algorithms

algorithms = get_default_algorithms()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--configuration', default="{}", type=json.loads, help='JSON string for algorithm parameters')
    parser.add_argument('-m', '--method', default='lhrs', help='Synthesis method (lhrs)')
    parser.add_argument('-l', '--logname', help='log to file instead of adding to database')
    parser.add_argument('benchmark', help='benchmark')

    args = parser.parse_args()

    if args.logname:
        run_and_log(args.benchmark, args.method, algorithms[args.method], args.configuration, args.logname)
    else:
        db = Database()
        insert_and_log(args.benchmark, args.method, algorithms[args.method], args.configuration, db)

# parallel "python3 run_single.py -c '{\"cut_size\": {2}, \"mapping_strategy\": \"{3}\", \"class_method\": 1, \"esopscript\": \"{4}\"}' --logname logs/{1}-{2}-{3}-{4}.json {1}" ::: adder bar div hyp log2 max multiplier sin sqrt square ::: 6 10 16 ::: direct min_db ::: def def_wo4