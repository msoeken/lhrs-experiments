from timeit import default_timer as timer

import revkit

def lhrs(filename, configuration):
    revkit.read_aiger(filename = filename)
    synthesis = revkit.lhrs(**configuration).dict()
    circuit = revkit.ps(circuit = True, silent = True).dict()

    revkit.store(clear = True, aig = True, circuit = True)

    return synthesis, circuit

def dxs(filename, configuration):
    revkit.read_aiger(filename = filename)
    revkit.xmglut(lut_size = 4)
    synthesis = revkit.dxs(**configuration).dict()
    circuit = revkit.ps(circuit = True, silent = True).dict()

    revkit.store(clear = True, aig = True, circuit = True, xmg = True)

    return synthesis, circuit

def cbs(filename, configuration):
    revkit.read_aiger(filename = filename)
    synthesis = revkit.cbs(**configuration).dict()
    circuit = revkit.ps(circuit = True, silent = True).dict()

    revkit.store(clear = True, aig = True, circuit = True)

    return synthesis, circuit

def hdbs(filename, configuration):
    revkit.read_aiger(filename = filename)
    num_outputs = revkit.ps(aig = True, silent = True)["outputs"]

    # also incorporate conversion to BDD to the runtime
    start = timer()
    revkit.convert(aig_to_bdd = True)
    synthesis = revkit.hdbs(**configuration).dict()
    end = timer()
    synthesis["runtime"] = end - start

    circuit = revkit.ps(circuit = True, silent = True).dict()
    circuit["qubits"] += num_outputs
    circuit["tcount"] *= 2

    return synthesis, circuit

def get_default_algorithms():
    return {'lhrs': lhrs, 'dxs': dxs, 'cbs': cbs, 'hdbs': hdbs}
