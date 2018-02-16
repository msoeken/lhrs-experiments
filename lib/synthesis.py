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

def get_default_algorithms():
    return {'lhrs': lhrs, 'dxs': dxs, 'cbs': cbs}
