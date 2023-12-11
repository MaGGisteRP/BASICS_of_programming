class Vector:
    def __init__(self, *args):
        if not args:
            self.x = self.y = self.z = 0
        elif len(args) == 1:
            if isinstance(args[0], (list, tuple)):
                if len(args[0]) == 3:
                    self.x, self.y, self.z = args[0]
                else:
                    raise ValueError("Вектор должен иметь три координаты.")
            elif isinstance(args[0], int):
                self.x = self.y = self.z = args[0]
            else:
                raise ValueError("Недопустимый тип аргумента.")
        elif len(args) == 3:
            self.x, self.y, self.z = args
        else:
            raise ValueError("Недопустимое количество аргументов.")

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

    @staticmethod #Статический метод, который связан с классом, а не с его экземплярами.
    def triple_product(a, b, c):
        return a ^ (b ^ c)

    def __or__(self, other):
        epsilon = 1e-10  # Небольшое значение для обработки неточностей с плавающей запятой
        return abs(self ^ other) < epsilon

    @staticmethod
    def are_complanar(a, b, c):
        return (a ^ b) | c == 0

x = int(input("Enter x-coordinate of the vector: "))
y = int(input("Enter y-coordinate of the vector: "))
z = int(input("Enter z-coordinate of the vector: "))

user_vector = Vector(x, y, z)
print(f"User Input Vector: ({user_vector.x}, {user_vector.y}, {user_vector.z})")
print(f"Length of User Input Vector: {user_vector.length()}")