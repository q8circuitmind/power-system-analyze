import cmath
import math

def analyze_three_phase(V_ll, P, pf, freq=50):
    V_ph = V_ll / math.sqrt(3)
    S = P / pf
    Q = math.sqrt(S**2 - P**2)
    theta = math.acos(pf)
    if pf < 1:
        Q = -Q
    I = S / (math.sqrt(3) * V_ll)
    Z = V_ph / I
    R = Z * pf
    X = Z * math.sin(theta)
    return {
        "V_phase_V": round(V_ph, 1),
        "S_kVA": round(S/1000, 2),
        "Q_kVAR": round(Q/1000, 2),
        "I_A": round(I, 2),
        "Z_ohm": round(abs(Z), 3),
        "R_ohm": round(R, 3),
        "X_ohm": round(X, 3),
        "load_type": "Inductive" if X > 0 else "Capacitive"
    }

if __name__ == "__main__":
    r = analyze_three_phase(V_ll=400, P=50000, pf=0.85)
    for k, v in r.items():
        print(f"{k}: {v}")
