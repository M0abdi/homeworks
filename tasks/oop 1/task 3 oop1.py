import math

class Vector2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y


    
    def add(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def add2(self, other: 'Vector2D') -> None:
        self.x += other.x
        self.y += other.y
    
    def sub(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def sub2(self, other: 'Vector2D') -> None:
        self.x -= other.x
        self.y -= other.y
    
    def mult(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def mult2(self, scalar: float) -> None:
        self.x *= scalar
        self.y *= scalar
    
    def __str__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"
    
    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)
    
    def scalar_product(self, other: 'Vector2D') -> float:
        return self.x * other.x + self.y * other.y
    
    def cos(self, other: 'Vector2D') -> float:
        dot_product = self.scalar_product(other)
        magnitudes = self.length() * other.length()
        if magnitudes == 0:
            return 0.0
        return dot_product / magnitudes
    
    def equals(self, other: 'Vector2D') -> bool:
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)
    





    
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return self.add(other)
    
    def __iadd__(self, other: 'Vector2D') -> 'Vector2D':
        self.add2(other)
        return self
    
    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return self.sub(other)
    
    def __isub__(self, other: 'Vector2D') -> 'Vector2D':
        self.sub2(other)
        return self
    
    def __mul__(self, scalar: float) -> 'Vector2D':
        return self.mult(scalar)
    
    def __imul__(self, scalar: float) -> 'Vector2D':
        self.mult2(scalar)
        return self
    
    def __eq__(self, other: 'Vector2D') -> bool:
        return self.equals(other)
    
    def __repr__(self) -> str:
        return self.__str__()






#--------------------------------------------------------------------------------------------------------------






if __name__ == "__main__":




    
    # Test original methods
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    
    print("=== ORIGINAL METHODS ===")
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"v1 + v2 (new): {v1.add(v2)}")
    print(f"v1 - v2 (new): {v1.sub(v2)}")
    print(f"v1 * 2 (new): {v1.mult(2)}")
    print(f"Length of v1: {v1.length()}")
    print(f"Scalar product: {v1.scalar_product(v2)}")
    print(f"Cosine of angle: {v1.cos(v2)}")
    print(f"Vectors equal: {v1.equals(v2)}")





    
    
    # Test in-place operations
    v3 = Vector2D(5, 6)
    v3.add2(v2)
    print(f"v3 after add2: {v3}")






    
    # Test magic methods
    print("\n=== MAGIC METHODS ===")
    v4 = Vector2D(2, 3)
    v5 = Vector2D(1, 1)
    
    print(f"v4 + v5: {v4 + v5}")
    print(f"v4 - v5: {v4 - v5}")
    print(f"v4 * 3: {v4 * 3}")
    
    v4 += v5
    print(f"v4 after += v5: {v4}")
    
    v4 *= 2
    print(f"v4 after *= 2: {v4}")
    
    print(f"v4 == v5: {v4 == v5}")
