import numpy as np


def three_body_problem(t_current, state_current):
    G = 1.0
    m1 = 1.0
    m2 = 1.0
    m3 = 1.0

    # to avoid division by zero shenanigans
    epsilon = 1e-5

    r1 = state_current[0:3]  # [x1, y1, z1]
    r2 = state_current[3:6]  # [x2, y2, z2]
    r3 = state_current[6:9]  # [x3, y3, z3]

    v1 = state_current[9:12]  # [vx1, vy1, vz1]
    v2 = state_current[12:15]  # [vx2, vy2, vz2]
    v3 = state_current[15:18]  # [vx3, vy3, vz3]

    r12 = r2 - r1
    r13 = r3 - r1
    r23 = r3 - r2

    d12 = np.linalg.norm(r12) + epsilon
    d13 = np.linalg.norm(r13) + epsilon
    d23 = np.linalg.norm(r23) + epsilon

    a1 = (G * m2 * r12 / (d12**3)) + (G * m3 * r13 / (d13**3))
    a2 = (-G * m1 * r12 / (d12**3)) + (G * m3 * r23 / (d23**3))
    a3 = (-G * m1 * r13 / (d13**3)) - (G * m2 * r23 / (d23**3))


    dr_dt = np.concatenate([v1, v2, v3])
    dv_dt = np.concatenate([a1, a2, a3])
    rates_of_change = np.concatenate([dr_dt, dv_dt])

    return rates_of_change