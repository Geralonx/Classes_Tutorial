# --- Definition einer Funktion, die mit optionalen Parametern überlden ist. --- #
def adder(x, y, debug=False):
    # debug-Argument ist optional, da es einen default Wert hat, welcher immer 
    # dann verwendet wird, wenn beim Aufurf dafür kein Wert übergeben wird.
    if debug:
        print(f"Evaluating {x} + {y}:")
        result = x + y
        print(f"Result: {result}")
        return result
    return x + y

# --- Aufruf der Funktion ohne den optionalen Parameter. --- #
# -> Zusatzfunktionalität wird nicht ausgeführt 
adder(10, 20)

# --- Aufruf der Funktion mit dem optionalen Parameter. --- #
# -> Zusatzfunktionalität wird ausgeführt. (Sofern der Wert != False / != None ist)
adder(100, 200, debug=True)
# Evaluating 100 + 200:
# Result: 300

# --- Python dynamik --- #
# (Dazu muss man jetzt wissen, was die if Abfrage macht. 
# Und wie die Datentypen darauf reagieren. Hint: bool() / __bool__)
adder(50, 600, debug='Ja')
# Evaluating 50 + 600:
# Result: 650
adder(1, 2, debug=1)
# Evaluating 1 + 2:
# Result: 3

