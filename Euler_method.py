
def euler_method(derivative, t_start, t_end, y_initial, step_size):

    time_points = [t_start]
    solution_points = [y_initial]

    t_current = t_start
    y_current = y_initial

    while t_current < t_end:
        y_current = y_current + step_size * derivative(t_current,y_current)

        t_current = t_current + step_size

        time_points.append(t_current)
        solution_points.append(y_current)

    return time_points,solution_points


# how do I deal with floating points inaccuracies???
# I need to make sure they don't happen because the method should be as accurate as possible