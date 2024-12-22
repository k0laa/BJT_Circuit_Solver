"""
# voltages
Vcc, Ve, Vb, Vc, Vce, Vbe, VR1, VR2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.7, 0.0, 0.0

# currents
Ie, Ib, Ic, IR1, IR2 = 0.0, 0.0, 0.0, 0.0, 0.0

# resistors
Re, Rb, Rb1, Rb2, Rc = 0.0, 0.0, 0.0, 0.0

# beta
beta = 0.0
"""

import Fixed_Bias_Solver as fbs


#### Current Calculations ####
def find_Ib(Vth, Rth, Re, beta, Vbe=0.7):
    return (Vth - Vbe) / (Rth + (beta + 1) * Re)


#### Voltage Calculations ####
def find_Vth(Vcc, R1, R2):
    return Vcc * R2 / (R1 + R2)


#### Resistance Calculations ####
def find_Rth(R1, R2):
    return R1 * R2 / (R1 + R2)


#### Solver ####

# Type 1 Solver
# Expected Inputs: Vcc, Rb, Rc, Re, beta
# Outputs: Vb, Vc, Ve, Vce, Vbe, Ib, Ic, Ie
def type1_solver(Vcc, Rb1, Rb2, Rc, Re, beta):
    Rth = find_Rth(Rb1, Rb2)
    Vth = find_Vth(Vcc, Rb1, Rb2)
    Ib = find_Ib(Vth, Rth, Re, beta)
    Ic = fbs.find_Ic(Ib, beta)
    Ie = Ib + Ic
    # devam edicel!!
