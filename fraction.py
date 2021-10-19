def gcd(a, b): return gcd(b, a%b) if b else a
"""Find the gratest common divisor.
    @param a: first number
    @param b: second number
    @return: gcd of a and b"""

class Fraction:
    """My Fraction class to represent fractions."""
    
    def __init__(self,top,bottom):
        """Constructor - create a fraction (irreducible form).
        @param top: numerator of fraction
        @param bottom: denominator of fraction"""
        
        if (type(top) is not int or type(bottom) is not int):
            raise TypeError('Numerator and denominator must be integers.')
        elif bottom == 0:
            raise ZeroDivisionError('The denominator cannot be zero.')
        elif bottom < 0:    #store 'minus' in the numerator of the fraction
                top *= -1
                bottom *= -1
        #make irreducible form
        self.num = top // gcd(top,bottom)
        self.den = bottom // gcd(top,bottom)
        
    def __str__(self):
        """Printing fraction form. e.g. 3/5"""
        return(str(self.num) + "/" + str(self.den))
    
    def __repr__(self):
        """Represent fraction form. e.g. 3/5"""
        return(str(self.num) + "/" + str(self.den))
    
    def __add__(self,other):
        """Add two fractions.
        @return: Fraction object"""
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum,newden)
        
    def __sub__(self,other):
        """Subtract two fractions.
        @return: Fraction object"""
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum,newden)
                
    def __mul__(self,other):
        """Multiply two fractions.
        @return: Fraction object"""
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum,newden)
                        
    def __truediv__(self,other):  
        """Divide two fractions.
        @return: Fraction object"""
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum,newden)
        
    """Here are overloads of the comparison operators."""
    def __lt__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first < second
    
    def __le__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first <= second
    
    def __gt__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first > second
    
    def __ge__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first >= second
    
    def __eq__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first == second
    
    def __ne__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first != second
    
    def get_num(self):
        """Return the numerator."""
        return self.num
    
    def get_den(self):
        """Return the denominator."""
        return self.den

import decimal #to find the number of decimal places
class FractionEx:
    
    mixed = "True"
    
    def __init__(self,top,bottom):
        if ((type(top) is not int and type(top) is not float) or
            (type(bottom) is not int and type(bottom) is not float)):
            raise TypeError('Numerator and denominator must be real numbers.')
        elif bottom == 0:
            raise ZeroDivisionError('The denominator cannot be zero.')
        elif bottom < 0:
                top *= -1
                bottom *= -1
                
        exp_top = decimal.Decimal(str(top)).as_tuple().exponent * -1
        exp_bot = decimal.Decimal(str(bottom)).as_tuple().exponent * -1
        
        if exp_top >= exp_bot:
            multiplier = exp_top
        else:
            multiplier = exp_bot
        
        top = top * 10**multiplier
        bottom = bottom * 10**multiplier
        
        self.num = int(top // gcd(top,bottom))
        self.den = int(bottom // gcd(top,bottom))
        
    def __str__(self):
        if self.mixed == "True":
            total_part = self.num // self.den
            self.num = self.num - total_part * self.den
            return(str(total_part) + "(" + str(self.num) + "/" + str(self.den) + ")")
        else:
            return(str(self.num) + "/" + str(self.den))
        
    
    def __repr__(self):
        if self.mixed == "True":
            total_part = self.num // self.den
            self.num = self.num - total_part * self.den
            return(str(total_part) + "(" + str(self.num) + "/" + str(self.den) + ")")
        else:
            return(str(self.num) + "/" + str(self.den))
    
    def __add__(self,other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum,newden)
        
    def __sub__(self,other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum,newden)
                
    def __mul__(self,other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum,newden)
                        
    def __truediv__(self,other):  
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum,newden)
        
    def __lt__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first < second
    
    def __le__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first <= second
    
    def __gt__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first > second
    
    def __ge__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first >= second
    
    def __eq__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first == second
    
    def __ne__(self,other):
        first = self.num * other.den
        second = other.num * self.den
        return first != second
    
    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.den
        