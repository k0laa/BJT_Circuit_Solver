# voltages
Vcc, Ve, Vb, Vc, Vce, Vbe = 0.0, 0.0, 0.0, 0.0, 0.0, 0.7

# currents
Ie, Ib, Ic = 0.0, 0.0, 0.0

# resistors
Re, Rb1, Rb2, Rc = 0.0, 0.0, 0.0, 0.0

# betas
beta = 0.0


def find_Ib(Vb, Vbe, Rb1, Rb2, Re, beta):
    Vth = find_Vth(Vb, Rb1, Rb2)
    Rth = find_Rth(Rb1, Rb2)
    return (Vth - Vbe) / (Rth + (beta + 1) * Re)


def find_Vth(Vb, Rb1, Rb2):
    return Vb / (Rb1 + Rb2) * Rb2


def find_Rth(Rb1, Rb2):
    return Rb1 * Rb2 / (Rb1 + Rb2)


def find_Ic(Ib, beta):
    return Ib * beta


def find_Ie(Ib, Ic):
    return Ib + Ic


def find_Ie_onBeta(Ib, beta):
    return Ib * (beta + 1)


def find_Vce(Vc, Ve):
    return Vc - Ve


def find_Vc(Vcc, Ic, Rc):
    return Vcc - (Ic * Rc)


def find_Ve(Ie, Re):
    return Ie * Re


def find_Vb(Vth, Ib, Rth):
    return Vth - (Ib * Rth)


def find_Vb_onDiode(Ve):
    return Ve + 0.7
