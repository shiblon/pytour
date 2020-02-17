# vim:tw=50

"""Numbers

There are several numeric types built into Python,
including integers (types |int| and |long|),
floating point numbers (type |float|), and complex
numbers (type |complex|).

  10        # This is an 'int'
  10.5      # This is a 'float'
  6 + 3.2j  # This is a 'complex'

The interactive Python interpreter makes a nice
calculator, and unlike this tutorial, you don't
even have to type |print| there - the |repr| of
every operation is output automatically. Basic
math is easy - you can do addition, subtraction,
multiplication, division, and exponentiation,
among other things.  Parentheses do what you would
expect.

Exercises

- Print the number of atoms in the
  sun, as a large integer: |119 * 10 ** 55|.

Bonus Work

- Try opening an interactive Python prompt (in a
  terminal, not here) and using it as a
  calculator.

"""

# Basic numeric types.
print("I'm an int:", 10)
print("I'm a float:", 2.79)
print("I'm complex:", 3.14 + 1j)

# Math is easy.

a = 1000.0

# Some basic math operators:
print()
print("Basic Math Operators:")
print("Div:", a / 10.0)  # Divide by 10
print("Mul:", a * 10)    # Multiply by 10
print("Add:", a + 12)    # Add 12
print("Sub:", a - 15)    # Subtract 15
print("Exp:", a ** 5)    # Take a to the 5th power.

# Grouping:
print()
print("Parentheses:")
print("Multiplication before addition:", 3 + 2 * 5)
print("Force addition to come first:", (3 + 2) * 5)
