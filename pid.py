import time

class AdaptivePID:
    def __init__(self, P, I, D):
        self.Kp_base = P
        self.Ki_base = I
        self.Kd_base = D
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.sample_time = 0.01
        self.current_time = time.time()
        self.last_time = self.current_time
        self.clear()

    def clear(self):
        self.SetPoint = 0.0
        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.last_error = 0.0
        self.int_error = 0.0
        self.windup_guard = 20.0
        self.output = 0.0

    def update(self, feedback_value):
        error = self.SetPoint - feedback_value
        self.current_time = time.time()
        delta_time = self.current_time - self.last_time
        delta_error = error - self.last_error

        if (delta_time >= self.sample_time):
            self.PTerm = self.Kp * error
            self.ITerm += error * delta_time
            self.ITerm = min(max(self.ITerm, -self.windup_guard), self.windup_guard)

            self.DTerm = 0.0
            if delta_time > 0:
                self.DTerm = delta_error / delta_time

            self.last_time = self.current_time
            self.last_error = error

            self.output = self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)

            self.adapt_pid()

    def adapt_pid(self):
        # Простой алгоритм адаптации
        if abs(self.last_error) > some_threshold:
            self.Kp = self.Kp_base * some_factor
            self.Ki = self.Ki_base * some_factor
            self.Kd = self.Kd_base * some_factor
        else:
            self.Kp = self.Kp_base
            self.Ki = self.Ki_base
            self.Kd = self.Kd_base

# Пример использования
pid = AdaptivePID(1.0, 0.1, 0.01)
pid.SetPoint = 100.0

while True:
    temp = read_temperature()  # Замените на функцию чтения температуры
    pid.update(temp)
    output = pid.output
    # Код для управления нагревателем
    time.sleep(1)
  
