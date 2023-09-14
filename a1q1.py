"""
	Name: Pratham Shah
	NSID: mvr659
	Student Number: 11353450
	Assignment: a1
"""


class Var_expr:

    def __init__(self, bexpr):
        self._val = bexpr

    def __str__(self):
        return self._val


class Bin_expr:

    def __init__(self, op, expr1, expr2):
        self._e1 = Expr(expr1)
        self._e2 = Expr(expr2)
        self._op = op

    def __str__(self):
        return '<' + str(self._e1) + " " + self._op + " " + str(self._e2) + '>'


class Not_expr:

    def __init__(self, bexpr):
        self._val = Expr(bexpr)

    def __str__(self):
        return '<' + "not " + str(self._val) + '>'


#
#   We stick to fully parenthesized expressions i.e., each function call
#       We can have too many parens, but the following are not ok
#               a and b, not a and b, must be (a and b), ((not a) and b)*
#

class Expr:
    def __init__(self, bexpr):

        #
        # the key part of my solution appears here
        #

        if len(bexpr) == 1:  # if the expression is only a variable then the length will also be 1
            self._val = Var_expr(bexpr[0])
        else:
            if bexpr[1] == 'not':
                self._val = Not_expr(bexpr[2:-1])  # if the second expression is not then the list from next expression till second-last one will be passed
            else:
                if bexpr[1] == "(":
                    idx = self.match_location(1, bexpr)  # getting index of the end parenthesis for the second parenthesis for limiting the expression's inner expression
                else:
                    idx = 1
                self._val = Bin_expr(bexpr[idx + 1], bexpr[1: idx + 1], bexpr[idx + 2: -1])  # calling Bin_expr to set the value with the arguments from expression as per the index calculated above

    #
    #	The following helper function will find the location for a close parenthesis
    #   matching the open parenthesis in location st

    def match_location(self, st, expr):
        n = 1
        i = st
        while n:
            i += 1
            if expr[i] == "(":
                n += 1
            if expr[i] == ")":
                n -= 1
        return i

    def __str__(self):
        return str(self._val)


#
#	This is how Python makes it easy to test. If you import this into a testing file
#	the code doesn't get started up

if __name__ == '__main__':

    exprs = open('exprs.txt', 'r')
    for expr in exprs:
        ans = Expr(expr.split())
        print("String representation of input:", ans)
