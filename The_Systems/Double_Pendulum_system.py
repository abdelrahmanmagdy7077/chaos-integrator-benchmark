import numpy as np

def double_pendulum_derivative(t_current, state_current):
    mass_1 = 1.0
    mass_2 = 1.0
    length_1 = 1.0
    length_2 = 1.0
    gravity = 9.81

    theta_1 = state_current[0]
    theta_2 = state_current[1]
    omega_1 = state_current[2]
    omega_2 = state_current[3]

    delta_theta = theta_1 - theta_2
    denominator_base = 2 * mass_1 + mass_2 - mass_2 * np.cos(2 * theta_1 - 2 * theta_2)

    num_1a = -gravity * (2 * mass_1 + mass_2) * np.sin(theta_1)
    num_1b = -mass_2 * gravity * np.sin(theta_1 - 2 * theta_2)
    num_1c = -2 * np.sin(delta_theta) * mass_2 * ((omega_2 ** 2) * length_2 + (omega_1 ** 2) * length_1 * np.cos(delta_theta))

    num_2a = 2 * np.sin(delta_theta)
    num_2b = (omega_1 ** 2) * length_1 * (mass_1 + mass_2)
    num_2c = gravity * (mass_1 + mass_2) * np.cos(theta_1)
    num_2d = (omega_2 ** 2) * length_2 * mass_2 * np.cos(delta_theta)

    d_theta1_dt = omega_1
    d_theta2_dt = omega_2
    d_omega1_dt = (num_1a + num_1b + num_1c) / (length_1 * denominator_base)
    d_omega2_dt = (num_2a * (num_2b + num_2c + num_2d)) / (length_2 * denominator_base)

    rates_of_change = np.array([d_theta1_dt, d_theta2_dt, d_omega1_dt, d_omega2_dt], dtype=float)

    return rates_of_change