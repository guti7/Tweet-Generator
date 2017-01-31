# Fibonacci numbers module
def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,  # , print in same line with space, no comma print in new line
        a, b = b, a + b

def fib2(n):  # return Fibonacci series up to n
    result = []
    a = 0
    b = 1
    while b < n:
        result.append(b)
        # a, b = b, a + b
        temp = a
        a = b
        b = temp + b
    return result


# File as a script
# The parsing from the command line only runs if the module is executed as
# the "main" file
if __name__ == "__main__":
    import sys  # needed to read from command line

    if len(sys.argv) > 1:
        fib(int(sys.argv[1]))  # read one argument
