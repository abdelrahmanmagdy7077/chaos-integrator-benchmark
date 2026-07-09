def verlet(acceleration, t_start, t_end, y_initial, v_initial, step_size):
    time_points = [t_start]
    solution_points = [y_initial]

    num_steps = int(round((t_end - t_start) / step_size))

    t_current = t_start
    y_current = y_initial

    accel_initial = acceleration(t_start, y_initial)

    # I used kinematic equations and solved for y_initial to get this formula
    y_previous = y_initial - (v_initial * step_size) + 0.5 * accel_initial * (step_size ** 2)

    for i in range (1, num_steps + 1):
        accel_current = acceleration(t_current, y_current)

        # Verlet method formula
        y_next = 2 * y_current - y_previous + accel_current * (step_size ** 2)

        y_previous = y_current
        y_current = y_next
        t_current = t_start + (i * step_size)

        solution_points.append(y_current)
        time_points.append(t_current)

    return time_points, solution_points