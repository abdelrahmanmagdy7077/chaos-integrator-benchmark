#I used Fehlberg coefficients in this method to set up for the adaptive RK45 method
def runge_kutta_5_fehlberg(derivative, t_start, t_end, y_initial, step_size):
    time_points = [t_start]
    solution_points = [y_initial]

    num_steps = int(round((t_end - t_start) / step_size))

    t_current = t_start
    y_current = y_initial

    for i in range(1, num_steps + 1):
        k1 = derivative(t_current, y_current)
        k2 = derivative(t_current + (1 / 4) * step_size, y_current + step_size * ((1 / 4) * k1))
        k3 = derivative(t_current + (3 / 8) * step_size, y_current + step_size * ((3 / 32) * k1 + (9 / 32) * k2))
        k4 = derivative(t_current + (12 / 13) * step_size, y_current + step_size * ((1932 / 2197) * k1 - (7200 / 2197) * k2 + (7296 / 2197) * k3))
        k5 = derivative(t_current + step_size, y_current + step_size * ((439 / 216) * k1 - 8 * k2 + (3680 / 513) * k3 - (845 / 4104) * k4))
        k6 = derivative(t_current + (1 / 2) * step_size, y_current + step_size * ( -(8 / 27) * k1 + 2 * k2 - (3544 / 2565) * k3 + (1859 / 4104) * k4 - (11 / 40) * k5))

        average_of_derivatives = step_size * ((16 / 135) * k1 + 0 * k2 + (6656 / 12825) * k3 + (28561 / 56430) * k4 - (9 / 50) * k5 + (2 / 55) * k6)

        y_current = y_current + average_of_derivatives
        t_current = t_start + (i * step_size)

        solution_points.append(y_current)
        time_points.append(t_current)

    return time_points, solution_points