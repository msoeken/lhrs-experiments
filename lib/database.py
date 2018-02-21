import functools
from tinydb import TinyDB, Query
import numpy as np

class Database:
    def __init__(self, filename="lhrs.json"):
        self.db = TinyDB(filename)

    def has_entry(self, benchmark, method, configuration):
        q = Query()
        entries = self.db.search((q.benchmark == benchmark) & (
            q.method == method) & (q.configuration == configuration))
        return len(entries) > 0

    def get_entry(self, benchmark, method, configuration):
        q = Query()
        entries = self.db.search((q.benchmark == benchmark) & (
            q.method == method) & (q.configuration == configuration))
        assert(len(entries) == 1)
        return entries[0]

    def get_entries(self, *benchmarks):
        q = Query()
        query = functools.reduce(lambda a, b: a | b, [q.benchmark == name for name in benchmarks])
        return self.db.search(query)

    def insert_entry(self, benchmark, method, configuration, synthesis, circuit):
        self.db.insert({'benchmark': benchmark, 'method': method, 'configuration': configuration,
                        'synthesis': synthesis, 'circuit': circuit})

    def get_main_statistics(self, benchmark, method, configuration):
        if isinstance(benchmark, str):
            if not self.has_entry(benchmark, method, configuration):
                return None, None, None
            
            entry = self.get_entry(benchmark, method, configuration)
            return int(entry["circuit"]["qubits"]), int(entry["circuit"]["tcount"]), entry["synthesis"]["runtime"]
        else:
            return [self.get_main_statistics(b, method, configuration) for b in benchmark]

    def get_class_counters(self, configuration):
        def counter_as_array(counter):
            return [np.array(l) for l in counter]

        q = Query()
        entries = self.db.search(q.configuration == configuration)
        return [sum(l) for l in zip(*[counter_as_array(e["synthesis"]["class_counter"]) for e in entries])]

        # sums = None

        # q = Query()
        # entries = self.db.search(q.configuration == configuration)
        # for e in entries:
        #     counters = [np.array(l) for l in e["synthesis"]["class_counter"]]

        #     if sums is None:
        #         sums = counters
        #     else:
        #         sums = [sum(l) for l in zip(sums, counters)]

        # return sums


