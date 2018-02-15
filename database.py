from tinydb import TinyDB, Query


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

    def insert_entry(self, benchmark, method, configuration, synthesis, circuit):
        self.db.insert({'benchmark': benchmark, 'method': method, 'configuration': configuration,
                        'synthesis': synthesis, 'circuit': circuit})
