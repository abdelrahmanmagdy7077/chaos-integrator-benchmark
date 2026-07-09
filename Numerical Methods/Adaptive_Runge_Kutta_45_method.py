def runge_kutta_45_adaptive(derivative, t_start, t_end, y_initial, initial_step_size, tolerance):
    time_points = [t_start]
    solution_points = [y_initial]

    t_current = t_start
    y_current = y_initial
    step_size = initial_step_size

    # unlike RK4 & RK5 code i used a while loop here becasue step_size constantly changes so
    # i wont be able to calculate the exact num_steps before the loop here
    while t_current < t_end:

        if t_current + step_size > t_end:
            step_size = t_end - t_current

        k1 = derivative(t_current, y_current)
        k2 = derivative(t_current + (1 / 4) * step_size, y_current + step_size * ((1 / 4) * k1))
        k3 = derivative(t_current + (3 / 8) * step_size, y_current + step_size * ((3 / 32) * k1 + (9 / 32) * k2))
        k4 = derivative(t_current + (12 / 13) * step_size, y_current + step_size * ((1932 / 2197) * k1 - (7200 / 2197) * k2 + (7296 / 2197) * k3))
        k5 = derivative(t_current + step_size, y_current + step_size * ((439 / 216) * k1 - 8 * k2 + (3680 / 513) * k3 - (845 / 4104) * k4))
        k6 = derivative(t_current + (1 / 2) * step_size, y_current + step_size * ( -(8 / 27) * k1 + 2 * k2 - (3544 / 2565) * k3 + (1859 / 4104) * k4 - (11 / 40) * k5))

        average_of_derivatives_5th = step_size * ((16 / 135) * k1 + 0 * k2 + (6656 / 12825) * k3 + (28561 / 56430) * k4 - (9 / 50) * k5 + (2 / 55) * k6)
        average_of_derivatives_4th = step_size * ((25 / 216) * k1 + 0 * k2 + (1408 / 2565) * k3 + (2197 / 4104) * k4 - (1 / 5) * k5 + 0 * k6)

        y_next_5th = y_current + average_of_derivatives_5th
        y_next_4th = y_current + average_of_derivatives_4th

        error = abs(y_next_5th - y_next_4th)

        # this is where the adaptive method shines (it checks if the step is good enough or not)
        if error <= tolerance:
            t_current = t_current + step_size
            y_current = y_next_5th  # cause they are more accuarate than the 4th order ones

            solution_points.append(y_current)
            time_points.append(t_current)

        # this calculate the new step size for the next loop (or the retry if the check step was rejected)
        # added this tiny number (1e-15) because apprently division by zero is possible
        # for the multiplication by 0.9, this shrinks the next step just a bit to avoid going into
        # uncessary errors, wasting time and computation
        step_size = step_size * 0.9 * (tolerance / (error + 1e-15)) ** 0.2

    return time_points, solution_points