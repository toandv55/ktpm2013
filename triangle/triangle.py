from decimal import Decimal
def detect_triangle(a, b, c):
    # check in put type
    input_error = "Invalid input type"
    _type = "Normal triangle"
    if (isinstance(a, str)):
        if a.isdigit():
            a = float(a)
        else:
            return input_error
    if (isinstance(b, str)):
        if b.isdigit():
            b = float(b)
        else:
            return input_error
    if (isinstance(c, str)):
        if c.isdigit():
            c = float(c)
        else:
            return input_error
    # check input value rangedetect_triangle(2, 3, 13**0.5)
    if (a <= 0 or b  <= 0 or c <=  0):
        return "Invalid value range"
    # check if this is a triangle
    if (Decimal(a + b) <= Decimal (c) or Decimal(a + c) <= Decimal(b) or 
        Decimal(b + c) <= Decimal(a)):
        return "Not a triangle"
    # check triangle type
    if (Decimal(a) == Decimal(b) or Decimal(b) == Decimal(c) or 
        Decimal(a) == Decimal(c)):
        _type = "Isosceles triangle"
        if (round(Decimal(a**2 + b**2), 10) == round(Decimal(c**2), 10) or 
            round(Decimal(b**2 + c**2), 10) == round(Decimal(a**2), 10) or
            round(Decimal(a**2 + c**2), 10) == round(Decimal(b**2), 10)):
            return "Isosceles and Right triangle"
    if (round(Decimal(a**2 + b**2), 10) == round(Decimal(c**2), 10) or 
        round(Decimal(b**2 + c**2), 10) == round(Decimal(a**2), 10) or
        round(Decimal(a**2 + c**2), 10) == round(Decimal(b**2), 10)):
            _type = "Right triangle"
    if (Decimal(a) == Decimal(b) == Decimal(c)):
            _type = "Equilateral triangle"
    return _type
    
        
    