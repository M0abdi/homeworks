# oop2 task 2


class Matrix2x2:
    def __init__(self, a11=0, a12=0, a21=0, a22=0):
        """
        Initialize a 2x2 matrix:
        [a11  a12]
        [a21  a22]
        """
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22
    
    def __add__(self, other):
        """Add two matrices."""
        result = Matrix2x2()
        result.a11 = self.a11 + other.a11
        result.a12 = self.a12 + other.a12
        result.a21 = self.a21 + other.a21
        result.a22 = self.a22 + other.a22
        return result
    
    def __sub__(self, other):
        """Subtract two matrices."""
        result = Matrix2x2()
        result.a11 = self.a11 - other.a11
        result.a12 = self.a12 - other.a12
        result.a21 = self.a21 - other.a21
        result.a22 = self.a22 - other.a22
        return result
    
    def __mul__(self, other):
        """Multiply matrix by another matrix or a number."""
        # Matrix multiplication
        if isinstance(other, Matrix2x2):
            result = Matrix2x2()
            result.a11 = self.a11 * other.a11 + self.a12 * other.a21
            result.a12 = self.a11 * other.a12 + self.a12 * other.a22
            result.a21 = self.a21 * other.a11 + self.a22 * other.a21
            result.a22 = self.a21 * other.a12 + self.a22 * other.a22
            return result
        # Scalar multiplication
        else:
            result = Matrix2x2()
            result.a11 = self.a11 * other
            result.a12 = self.a12 * other
            result.a21 = self.a21 * other
            result.a22 = self.a22 * other
            return result
    
    def __rmul__(self, other):
        """Handle multiplication when number is on the left side."""
        return self * other
    
    def __truediv__(self, other):
        """Divide matrix by a number."""
        if other == 0:
            raise ValueError("Cannot divide by zero")
        
        result = Matrix2x2()
        result.a11 = self.a11 / other
        result.a12 = self.a12 / other
        result.a21 = self.a21 / other
        result.a22 = self.a22 / other
        return result
    
    def determinant(self):
        """Calculate determinant of the matrix."""
        return self.a11 * self.a22 - self.a12 * self.a21
    
    def transpose(self):
        """Transpose the matrix (swap rows and columns)."""
        result = Matrix2x2()
        result.a11 = self.a11
        result.a12 = self.a21
        result.a21 = self.a12
        result.a22 = self.a22
        return result
    
    def __str__(self):
        return f"[{self.a11}  {self.a12}]\n[{self.a21}  {self.a22}]"
    
    def __repr__(self):
        return f"Matrix2x2({self.a11}, {self.a12}, {self.a21}, {self.a22})"


# Example usage
print("=== Matrix2x2 Examples ===\n")

# Create matrices
m1 = Matrix2x2(1, 2, 3, 4)
m2 = Matrix2x2(5, 6, 7, 8)

print("Matrix m1:")
print(m1)
print()

print("Matrix m2:")
print(m2)
print()

# Addition
print("1. Addition (m1 + m2):")
result = m1 + m2
print(result)
print()

# Subtraction
print("2. Subtraction (m1 - m2):")
result = m1 - m2
print(result)
print()

# Matrix multiplication
print("3. Matrix multiplication (m1 * m2):")
result = m1 * m2
print(result)
print()

# Multiplication by a number
print("4. Multiplication by a number (m1 * 3):")
result = m1 * 3
print(result)
print()

print("5. Multiplication by a number (2 * m1):")
result = 2 * m1
print(result)
print()

# Division by a number
print("6. Division by a number (m1 / 2):")
result = m1 / 2
print(result)
print()

# Determinant
print("7. Determinant of m1:")



det = m1.determinant()
print(f"det(m1) = {det}")
print()

print("Determinant of m2:")
det = m2.determinant()
print(f"det(m2) = {det}")
print()

# Transpose
print("8. Transpose of m1:")
transposed = m1.transpose()
print(transposed)
print()

# More examples
print("=== More Examples ===\n")

# Create identity matrix
identity = Matrix2x2(1, 0, 0, 1)
print("Identity matrix:")
print(identity)
print()

# Multiply by identity
print("m1 * identity:")
result = m1 * identity
print(result)
print("(Should be same as m1)")

# Check if multiplication with identity works
print(f"m1 == m1 * identity? {m1.a11 == result.a11 and m1.a12 == result.a12 and m1.a21 == result.a21 and m1.a22 == result.a22}")
print()

# Zero matrix
zero = Matrix2x2(0, 0, 0, 0)
print("Zero matrix + m1:")
result = zero + m1
print(result)
print("(Should be same as m1)")

# Determinant of special matrix
special = Matrix2x2(2, 3, 4, 5)
print(f"\nSpecial matrix:\n{special}")
print(f"Its determinant: {special.determinant()}")
