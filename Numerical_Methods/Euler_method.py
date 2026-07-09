def euler_method(derivative, t_start, t_end, y_initial, step_size):

    time_points = [t_start]
    solution_points = [y_initial]

    t_current = t_start
    y_current = y_initial

    num_steps = int(round((t_end - t_start) / step_size))

    for i in range(1, num_steps + 1):
        y_current = y_current + step_size * derivative(t_current,y_current)

        t_current = t_start + (i * step_size)

        time_points.append(t_current)
        solution_points.append(y_current)

    return time_points,solution_points

