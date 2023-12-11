class Vector:
    def __init__(self, *args):
        if not args:
            self.x = self.y = self.z = 0
        elif len(args) == 1:
            if isinstance(args[0], (list, tuple)):
                if len(args[0]) == 3:
                    self.x, self.y, self.z = args[0]
                else:
                    raise ValueError("Vector must have three coordinates.")
            elif isinstance(args[0], int):
                self.x = self.y = self.z = args[0]
            else:
                raise ValueError("Invalid argument type.")
        elif len(args) == 3:
            self.x, self.y, self.z = args
        else:
            raise ValueError("Invalid number of arguments.")

    def __abs__(self):
        return self.length()

    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __xor__(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def triple_product(a, b, c):
        return a ^ (b ^ c)

    def __or__(self, other):
        epsilon = 1e-10  # Small value to handle floating-point imprecision
        return abs(self ^ other) < epsilon

    @staticmethod
    def are_complanar(a, b, c):
        return (a ^ b) | c == 0