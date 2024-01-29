import time

def test_system_response(pid, read_temperature):
    """
    Увеличиваем Kp до начала колебаний системы.
    Возвращаем Kp и период колебаний.
    """
    pid.Kp = 0.1
    last_temp = read_temperature()
    increasing = True
    start_time = time.time()
    osc_start_time = None
    osc_end_time = None

    while True:
        temp = read_temperature()
        pid.update(temp)
        output = pid.output
        # Код для управления нагревателем

        if increasing and temp < last_temp:
            increasing = False
            osc_start_time = time.time()

        if not increasing and temp > last_temp:
            increasing = True
            osc_end_time = time.time()
            break

        last_temp = temp
        pid.Kp += 0.1  # Плавно увеличиваем Kp
        time.sleep(1)

    Kc = pid.Kp
    Pc = osc_end_time - osc_start_time
    return Kc, Pc

def ziegler_nichols_tuning(Kc, Pc):
    """
    Расчет параметров PID по Зиглеру-Николсу.
    """
    Kp = 0.6 * Kc
    Ki = 2 * Kp / Pc
    Kd = Kp * Pc / 8
    return Kp, Ki, Kd

# Пример использования
pid = PID(0.0, 0.0, 0.0)  # Инициализируем PID с нулевыми параметрами
Kc, Pc = test_system_response(pid, read_temperature)
Kp, Ki, Kd = ziegler_nichols_tuning(Kc, Pc)

pid.Kp = Kp
pid.Ki = Ki
pid.Kd = Kd

# Теперь можно использовать pid с настроенными параметрами
