import numpy as np

def lorenz_63(t_current, state_current):
    sigma = 10.0
    rho = 28.0
    beta = 8.0/3.0

    x_current = state_current[0]
    y_current = state_current[1]
    z_current = state_current[2]

    dx_dt = sigma * (y_current - x_current)
    dy_dt = x_current * (rho - z_current) - y_current
    dz_dt = x_current * y_current - (beta * z_current)

    rates_of_change = np.array([dx_dt, dy_dt, dz_dt], dtype=float)

    return rates_of_change