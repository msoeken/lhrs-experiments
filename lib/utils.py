import numpy as np

def thousand_sep(number):
    if number == None:
        return ""
    elif isinstance(number, int) or isinstance(number, np.int64):
        return '{:,}'.format(number)
    elif isinstance(number, float):
        return '{:,.2f}'.format(number)
    else:
        return number

def make_pareto(entries):
    # sort entries
    entries = sorted(entries, key = lambda e: (e["circuit"]["tcount"], e["circuit"]["qubits"]))
    
    if len(entries) == 0:
        return entries
    
    min_qubits = entries[0]["circuit"]["qubits"]
    entries[0]["pareto"] = True

    for e in entries[1:]:
        qubits = e["circuit"]["qubits"]
        if qubits < min_qubits:
            min_qubits = qubits
            e["pareto"] = True
        else:
            e["pareto"] = False
            
    return entries
