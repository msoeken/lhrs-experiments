import json

from benchmarks import get_filename


def run_and_log(benchmark, method, algorithm, configuration, logname):
    filename = get_filename(benchmark)

    synthesis, circuit = algorithm(filename, configuration)

    entry = {'benchmark': benchmark, 'method': method,
             'configuration': configuration, 'synthesis': synthesis, 'circuit': circuit}

    with open(logname, 'w') as f:
        f.write(json.dumps(entry))
