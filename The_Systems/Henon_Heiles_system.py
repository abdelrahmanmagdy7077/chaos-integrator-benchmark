import numpy as np

def henon_heiles(t_current, state_current):

    lambda_param = 1.0

    x_current = state_current[0]
    y_current = state_current[1]
    vx_current = state_current[2]
    vy_current = state_current[3]

    dx_dt = vx_current
    dy_dt = vy_current
    dvx_dt = -x_current - (2.0 * lambda_param * x_current * y_current)
    dvy_dt = -y_current - (
        lambda_param * (x_current**2 - y_current**2)
    )

    rates_of_change = np.array(
        [dx_dt, dy_dt, dvx_dt, dvy_dt], dtype=float
    )

    return rates_of_change