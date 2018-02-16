import argparse
import json

from lib.database import Database

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help = 'log filename')

    args = parser.parse_args()

    db = Database()

    with open(args.filename, 'r') as f:
        entry = json.loads(f.read())
        
        benchmark = entry["benchmark"]
        method = entry["method"]
        configuration = entry["configuration"]
        synthesis = entry["synthesis"]
        circuit = entry["circuit"]

        if not db.has_entry(benchmark, method, configuration):
            db.insert_entry(benchmark, method, configuration, synthesis, circuit)
