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
import Fixed_Bias_Solver as fbs


#### Current Calculations ####
def find_Ib_onBeta(Ic, beta):
    return Ic / beta


def find_Ie(Ve, Re):
    return Ve / Re


def find_Ie_onBeta(Ic, beta):
    return Ic / beta * (beta + 1)


#### Voltage Calculations ####
def find_Ve(Ie, Re):
    return Ie * Re


def find_Vb(Vbb, Ib, Rb):
    return Vbb - Ib * Rb


#### Resistance Calculations ####
def find_Rb(Vbb, Ib, Vbe, Ve):
    return (Vbb - Vbe - Ve) / Ib


def find_Re(Ve, Ie):
    return Ve / Ie


#### Solver ####

# Type 1 Solver
# Expected Inputs: Vcc, Rb, Rc, Re, beta
# Outputs: Vb, Vc, Ve, Vce, Vbe, Ib, Ic, Ie
def type1_solver(Vcc, Rb, Rc, Re, beta):
    Ib = fbs.find_Ib(Vcc, Rb, Re)
    Ic = fbs.find_Ic(Ib, beta)
    Ie = Ib + Ic
    Vc = fbs.find_Vc(Vcc, Ic, Rc)
    Ve = find_Ve(Ie, Re)
    Vb = find_Vb(Vcc, Ib, Rb)
    Vce = fbs.find_Vce(Vc, Ve)
    Vbe = 0.7
    return Vb, Vc, Ve, Vce, Vbe, Ib, Ic, Ie


# Type 2 Solver
# Expected Inputs: Vcc, Vc, Ve, Ic, beta
# Outputs: Vb, Vbe, Vce, Rb, Rc, Re, Ib, Ie
def type2_solver(Vcc, Vc, Ve, Ic, beta):
    Ib = find_Ib_onBeta(Ic, beta)
    Ie = find_Ie_onBeta(Ic, beta)
    Rb = find_Rb(Vcc, Ib, 0.7, Ve)
    Rc = fbs.find_Rc(Vcc, Ic, Vc)
    Re = find_Re(Vcc, Ie)
    Vb = Ve + 0.7
    Vbe = 0.7
    Vce = fbs.find_Vce(Vc, Ve)
    return Vb, Vbe, Vce, Rb, Rc, Re, Ib, Ie


# Type 3 Solver
# Expected Inputs: Ve, Vce, Ib, Rc, Re
# Outputs: Vb, Vc, Ve, Vcc, Vbe, Rb, Ic, Ie, beta
def type3_solver(Ve, Vce, Ib, Rc, Re):
    Ie = find_Ie(Ve, Re)
    Ic = Ie - Ib
    beta = Ic / Ib
    Vcc = fbs.find_Vcc(Vce, Ic, Rc)
    Vb = Ve + 0.7
    Vc = Vce + Ve
    Vbe = 0.7
    Rb = find_Rb(Vcc, Ib, Vbe, Ve)
    return Vb, Vc, Ve, Vcc, Vbe, Rb, Ic, Ie, beta
