# Author: Nishka Awasthi
# It is ok to post my anonymized solution

# Set Globals
p, q, r, s, t = 0, 0, 0, 0, 0
eq = ""
idx = 0

# Parse through and find the answer to the entire equation
# If you haven't found an operand yet, call the function
# again
def recurs():
    global eq
    global idx
    global p, q, r, s, t
    #eq = 'CEpqr'
    operators = ['K', 'A', 'N', 'C', 'E']

    # Operands
    if eq[idx] in operators:
        # identify operator
        # get operands for operator
        # return evaluation
        if eq[idx] == 'K':
            idx += 1
            op1 = recurs()
            op2 = recurs()

            if op1 == op2 and op1 == 1:
                return(1)
            else: return(0)

        elif eq[idx] == 'A':
            idx += 1
            op1 = recurs()
            op2 = recurs()

            if op1 == op2 and op1 == 0:
                return(0)
            else: return (1)

        elif eq[idx] == 'N':
            idx += 1
            op1 = recurs()

            if op1 == 1:
                return(0)
            else: return (1)

        elif eq[idx] == 'C':
            idx += 1
            op1 = recurs()
            op2 = recurs()

            if op1 == 1 and op2 == 0:
                return(0)
            else: return(1)


        else: # eq[idx] == 'E'
            idx += 1
            op1 = recurs()
            op2 = recurs()

            if op1 == op2:
                return(1)
            else: return(0)
    else:
    # if not operator, then wffs
    # move to next index, return value
        if eq[idx] == 'p':
            idx += 1
            return p
        elif eq[idx] == 'q':
            idx += 1
            return q
        elif eq[idx] == 'r':
            idx += 1
            return r
        elif eq[idx] == 's':
            idx += 1
            return s
        elif eq[idx] == 't':
            idx += 1
            return t

def main():
    global p, q, r, s, t
    global eq, idx
    eq = raw_input()
    not_taut = False

    while eq != '0':
        #Suppose eq = 'CEpqr'
        for i in range(2):
            p = i
            for j in range(2):
                q = j
                for k in range(2):
                    r = k
                    for l in range(2):
                        s = l
                        for m in range(2):
                            t = m
                            idx = 0
                            not_taut = False
                            if recurs() == 0:
                                # Break the second it is not False
                                not_taut = True
                                break
                        if not_taut:
                            break
                    if not_taut:
                        break
                if not_taut:
                    break
            if not_taut:
                break
        if not_taut:
            print('not')
        else: print('tautology')
        eq = raw_input()
        #----end of while loop

main()