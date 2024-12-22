""""
# voltages
Vcc, Vbb, Vb, Vc, Ve, Vce, Vbe = 0.0, 0.0, 0.0, 0.0, 0.0, 0.7

# currents
Ib, Ic, Ie = 0.0, 0.0, 0.0

# resistors
Rb, Rc, = 0.0, 0.0

# beta
beta = 0.0
"""


#### Current Calculations ####
def find_Ib(Vbb, Rb, Vbe=0.7):
    return (Vbb - Vbe) / Rb


def find_Ic(Ib, beta):
    return Ib * beta


#### Voltage Calculations ####
def find_Vce(Vc, Ve=0.0):
    return Vc - Ve


def find_Vc(Vcc, Ic, Rc):
    return Vcc - Ic * Rc


def find_Vcc(Vc, Ic, Rc):
    return Vc + Ic * Rc


#### Resistance Calculations ####
def find_Rb(Vbb, Ib, Vbe=0.7):
    return (Vbb - Vbe) / Ib


def find_Rc(Vcc, Ic, Vc):
    return (Vcc - Vc) / Ic


#### Solver ####

# Type 1 Solver
# Expected Inputs: Vcc, Rb, Rc, beta
# Outputs: Vb, Vc, Ve, Vce, Vbe, Ib, Ic, Ie
def type1_solver(Vcc, Rb, Rc, beta):
    Ib = find_Ib(Vcc, Rb)
    Ic = find_Ic(Ib, beta)
    Vc = find_Vc(Vcc, Ic, Rc)
    Vce = find_Vce(Vc, 0)
    Ie = Ib + Ic
    Vbe = 0.7
    Vb = 0.7
    Ve = 0.0
    return Vb, Vc, Ve, Vce, Vbe, Ib, Ic, Ie


# Type 2 Solver
# Expected Inputs: Vcc, Vc, Ib, beta
# Outputs: Vb, Ve, Vbe, Vce, Rb, Rc, Ic, Ie
def type2_solver(Vcc, Vc, Ib, beta):
    Ic = find_Ic(Ib, beta)
    Rb = find_Rb(Vcc, Ib)
    Rc = find_Rc(Vcc, Ic, Vc)
    Vce = Vc
    Ie = Ib + Ic
    Vb = 0.7
    Ve = 0.0
    Vbe = 0.7
    return Vb, Ve, Vbe, Vce, Rb, Rc, Ic, Ie


# Type 3 Solver
# Expected Inputs: Vce, Ib, Ie, Rc
# Outputs: Vb, Vc, Ve, Vcc, Vbe, Rb, Ic, beta
def type3_solver(Vce, Ib, Ie, Rc):
    Ic = Ie - Ib
    Vcc = find_Vcc(Vce, Ic, Rc)  # Vce = Vc
    beta = Ic / Ib
    Rb = find_Rb(Vcc, Ib)
    Vc = Vce
    Vb = 0.7
    Ve = 0.0
    Vbe = 0.7
    return Vb, Vc, Ve, Vcc, Vbe, Rb, Ic, beta
