def runge_kutta_4(derivative, t_start, t_end, y_initial, step_size):

    time_points = [t_start]
    solution_points = [y_initial]

    num_steps = int(round((t_end - t_start) / step_size))

    t_current = t_start
    y_current = y_initial

    for i in range(1, num_steps + 1):
        k1 = derivative(t_current, y_current)
        k2 = derivative(t_current + step_size / 2, y_current + ((step_size / 2) * k1))
        k3 = derivative(t_current + step_size / 2, y_current + ((step_size / 2) * k2))
        k4 = derivative(t_current + step_size, y_current + (step_size * k3))

        average_of_derivatives = step_size * (1 / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

        y_current = y_current + average_of_derivatives
        t_current = t_start + (i * step_size)

        solution_points.append(y_current)
        time_points.append(t_current)



    return time_points, solution_points




