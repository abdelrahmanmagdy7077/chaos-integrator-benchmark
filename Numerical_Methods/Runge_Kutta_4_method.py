import numpy as np

def runge_kutta_4(derivative, t_start, t_end, y_initial, step_size):

    y_current = np.array(y_initial, dtype=float)

    num_steps = int(round((t_end - t_start) / step_size))

    time_points = np.zeros(num_steps + 1)
    solution_points = np.zeros((num_steps + 1, len(y_current)))

    time_points[0] = t_start
    solution_points[0] = y_current

    t_current = t_start

    for i in range(1, num_steps + 1):
        k1 = derivative(t_current, y_current)
        k2 = derivative(t_current + step_size / 2, y_current + ((step_size / 2) * k1))
        k3 = derivative(t_current + step_size / 2, y_current + ((step_size / 2) * k2))
        k4 = derivative(t_current + step_size, y_current + (step_size * k3))

        average_of_derivatives = step_size * (1 / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

        y_current = y_current + average_of_derivatives
        t_current = t_start + (i * step_size)

        time_points[i] = t_current
        solution_points[i] = y_current



    return time_points, solution_points




