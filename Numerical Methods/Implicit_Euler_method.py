# so in the implicit formulas we have y_(n+1) on both sides of equation
# so the standard way this is done is that we build a predictor of the answer then optimize from there

def implicit_euler(derivative, t_start, t_end, y_initial, step_size):

    time_points = [t_start]
    solution_points = [y_initial]

    t_current = t_start
    y_current = y_initial

    num_steps = int(round((t_end - t_start) / step_size))

    for i in range(1, num_steps + 1):
        t_next = t_current + step_size

        #predictor (initial guess)
        k1 = derivative(t_current, y_current)
        y_guess = y_current + step_size * k1

        #now to be able to solve the equation i will make the loop that check if the prediction is good or bad
        tolerance = 1e-6
        max_iterations = 50 #if the guess is so bad we have to have a limit to how many times we try to use it

        for j in range(1, max_iterations + 1):
            k_implicit = derivative(t_next, y_guess)
            y_new = y_current + step_size * k_implicit
            if abs(y_new - y_guess) < tolerance:
                break
            y_guess = y_new

        y_current = y_new
        t_current = t_next

        time_points.append(t_current)
        solution_points.append(y_current)

    return time_points,solution_points

