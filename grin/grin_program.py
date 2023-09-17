import grin

# NEED TO INCLUDE INHERITANCE
class Grin_Interpreter:

    def __init__(self):
        self.seen_lines = {}    # line number : grin_line.
        self.variables = {}     # name : value


    def Interpret_GrinLines(self, grin_lines_generator):
        """Main function which calls generator grin_lines, interprets line one at a time, handles tokens for each line and ouputs expected behavior."""

        while True:
            grin_line = next(grin_lines_generator)

            print(grin_line)

            #LET
            
            #PRINT

            #INNUM

            #INSTR

            #MATH:
                #ADD
                #SUB
                #MULT
                #DIV

            #GOTO
                #Conditional

            #GOSUB
                #Conditional

            #RETURN

            #END

            #'.'
            # NOTE: parse removes the '.' from input. "Behaves as an END statement when encountered..", so ill make a check but idk..








