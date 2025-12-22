# oop2 task 1


class RationalFraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
    
    def reduce(self):
        """Reduce the fraction to simplest form."""
        if self.numerator == 0:
            self.denominator = 1
            return
            
        # in here (Find greatest common divisor)
        a = abs(self.numerator)
        b = abs(self.denominator)
        while b:
            a, b = b, a % b
        gcd = a
        
        self.numerator //= gcd
        self.denominator //= gcd
        
        # Ensure denominator is positive
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
    
    def __add__(self, other):
        """Add two fractions and return new reduced fraction."""
        if not isinstance(other, RationalFraction):
            other = RationalFraction(other)
        
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        
        result = RationalFraction(new_numerator, new_denominator)
        result.reduce()
        return result
    
    def __iadd__(self, other):
        """Add another fraction to current fraction in-place."""
        if not isinstance(other, RationalFraction):
            other = RationalFraction(other)
        
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.reduce()
        return self
    
    def __sub__(self, other):
        """Subtract two fractions and return new reduced fraction."""
        if not isinstance(other, RationalFraction):
            other = RationalFraction(other)
        
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        
        result = RationalFraction(new_numerator, new_denominator)
        result.reduce()
        return result
    
    def __isub__(self, other):
        """Subtract another fraction from current fraction in-place."""
        if not isinstance(other, RationalFraction):
            other = RationalFraction(other)
        
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.reduce()
        return self
    
    def __mul__(self, other):
        """Multiply two fractions and return new reduced fraction."""
        if not isinstance(other, RationalFraction):
            other = RationalFraction(other)
        
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        
        result = RationalFraction(new_numerator, new_denominator)
        result.reduce()
        return result
    
    def __imul__(self, other):
        """Multiply current fraction by another fraction in-place."""
        if not isinstance(other, RationalFraction):
            other = RationalFraction(other)
        
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        self.reduce()
        return self
    
    def __truediv__(self, other):
        """Divide two fractions and return new reduced fraction."""
        if not isinstance(other, RationalFraction):
            other = RationalFraction(other)
        
        # Dividing by a/b is same as multiplying by b/a
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        
        result = RationalFraction(new_numerator, new_denominator)
        result.reduce()
        return result
    
    def __idiv__(self, other):
        """Divide current fraction by another fraction in-place."""
        if not isinstance(other, RationalFraction):
            other = RationalFraction(other)
        
        self.numerator *= other.denominator
        self.denominator *= other.numerator
        self.reduce()
        return self
    
    def to_float(self):
        """Return float representation of fraction."""
        return self.numerator / self.denominator
    
    def __eq__(self, other):
        """Check if two fractions are equal."""
        if not isinstance(other, RationalFraction):
            other = RationalFraction(other)
        
        # Reduce both fractions first
        self_copy = RationalFraction(self.numerator, self.denominator)
        self_copy.reduce()
        
        other_copy = RationalFraction(other.numerator, other.denominator)
        other_copy.reduce()
        
        return (self_copy.numerator == other_copy.numerator and 
                self_copy.denominator == other_copy.denominator)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return f"RationalFraction({self.numerator}, {self.denominator})"


# testing our code and outputs
print("=== Examples ===")


f1 = RationalFraction(2, 4)  
f2 = RationalFraction(1, 2)  
f3 = RationalFraction(3, 4)  

print(f"f1 = {f1}")
print(f"f2 = {f2}")
print(f"f3 = {f3}")

# reduce() method
print(f"\n1. reduce() method:")
f4 = RationalFraction(4, 8)
print(f"Before reduce: {f4}")
f4.reduce()
print(f"After reduce: {f4}")

# __add__ method
print(f"\n2. __add__ method:")
result = f1 + f2
print(f"{f1} + {f2} = {result}")

# __iadd__ method
print(f"\n3. __iadd__ method:")
f1_copy = RationalFraction(2, 4)
print(f"Before iadd: {f1_copy}")
f1_copy += f2
print(f"After iadd: {f1_copy}")

# __sub__ method
print(f"\n4. __sub__ method:")
result = f3 - f2
print(f"{f3} - {f2} = {result}")

# __isub__ method
print(f"\n5. __isub__ method:")
f3_copy = RationalFraction(3, 4)
print(f"Before isub: {f3_copy}")
f3_copy -= f2
print(f"After isub: {f3_copy}")

# __mul__ method
print(f"\n6. __mul__ method:")
result = f2 * f3
print(f"{f2} * {f3} = {result}")

# __imul__ method
print(f"\n7. __imul__ method:")
f2_copy = RationalFraction(1, 2)
print(f"Before imul: {f2_copy}")
f2_copy *= f3
print(f"After imul: {f2_copy}")

# __truediv__ method
print(f"\n8. __truediv__ method:")
result = f3 / f2
print(f"{f3} / {f2} = {result}")

# __idiv__ method (Note: Python uses /= for __itruediv__)
print(f"\n9. __idiv__ method:")
f3_copy = RationalFraction(3, 4)
print(f"Before idiv: {f3_copy}")
f3_copy /= f2
print(f"After idiv: {f3_copy}")

# to_float() method
print(f"\n10. to_float() method:")
print(f"{f3} as float = {f3.to_float()}")

# __eq__ method
print(f"\n11. __eq__ method:")
print(f"{f1} == {f2} ? {f1 == f2}")
print(f"{RationalFraction(2, 4)} == {RationalFraction(1, 2)} ? {RationalFraction(2, 4) == RationalFraction(1, 2)}")

# with integers
print(f"\n12. Working with integers:")
f5 = RationalFraction(1, 2)
result = f5 + 1  
print(f"1/2 + 1 = {result}")
