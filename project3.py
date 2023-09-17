# project3.py
#
# ICS 33 Winter 2023
# Project 3: Why Not Smile?
#
# The main module that executes your Grin interpreter.
#
# WHAT YOU NEED TO DO: You'll need to implement the outermost shell of your
# program here, but consider how you can keep this part as simple as possible,
# offloading as much of the complexity as you can into additional modules in
# the 'grin' package, isolated in a way that allows you to unit test them.

import grin


def main() -> None:
    """Main Input Loop"""

    #User Input Loop:
    grin_lines = user_grin_input()
    user_input_lines = [
        'LET A 3',
        'PRINT A']

    grin_lines_generator = grin.parse(grin_lines) # grin lines generator, made of tokens.


    # Create new Grin_Interpreter object:
    grin_program = grin.grin_program
    grin_interpreter = grin_program.Grin_Interpreter()

    # Interpret GrinLines:
    grin_interpreter.Interpret_GrinLines(grin_lines_generator)



def user_grin_input():
    grin_lines = []
    while True:
        grin_line = input()
        grin_lines.append(grin_line)

        if 'INNUM' in grin_line.split() or 'INSTR' in grin_line.split():
            pass

        if grin_line == '.':
            break

    return grin_lines

if __name__ == '__main__':
    main()
