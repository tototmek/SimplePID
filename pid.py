class PID:
    def __init__(self, p, i, d, max_u, min_u):
        self.p = p
        self.i = i
        self.d = d
        self.max_u = max_u
        self.min_u = min_u
        self.prevE = 0
        self.integral = 0
    
    def out(self, Yzad, Ypom, dt):
        e = Yzad - Ypom
        proportional = self.p * e
        self.integral += self.i * e * dt
        derivative = self.d * (e - self.prevE) / dt

        int_max = (self.max_u - proportional if self.max_u > proportional else 0)
        int_min = (self.min_u - proportional if self.min_u < proportional else 0)
        self.integral = min(int_max, max(int_min, self.integral))
        self.prevE = e

        u = min(self.max_u, max(self.min_u,
            proportional + self.integral + derivative))
        return u
