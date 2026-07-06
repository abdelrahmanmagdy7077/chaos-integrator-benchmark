def RK4(derv_func, t_i, t_f, s_i, h):

    time_list = [t_i]
    step_position_list = [s_i]


    while t_i < t_f:
        k1 = derv_func(t_i, s_i)
        k2 = derv_func(t_i + h / 2, s_i + (h / 2 * k1))
        k3 = derv_func(t_i + h / 2, s_i + (h / 2 * k2))
        k4 = derv_func(t_i + h, s_i + (h * k3))

        avg = h * 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        s_f = s_i + avg

        t_i = t_i + h
        s_i = s_f

        time_list.append(t_i)
        step_position_list.append(s_f)


    return time_list, step_position_list

