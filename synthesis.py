import revkit

def lhrs(filename, configuration):
    revkit.read_aiger(filename = filename)
    synthesis = revkit.lhrs(**configuration).dict()
    circuit = revkit.ps(circuit = True).dict()

    revkit.store(clear = True, aig = True, circuit = True)

    return synthesis, circuit

def get_default_algorithms():
    return {'lhrs': lhrs}