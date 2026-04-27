def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


def sort(args):
    i = 0
    while i < len(args):
        if args[i] == "*" or args[i] == "/":
            left = float(args[i - 1])
            right = float(args[i + 1])

            if args[i] == "*":
                result = mul(left, right)
            else:
                result = div(left, right)

            del args[i - 1:i + 2]
            args.insert(i - 1, result)

            i = 0
        else:
            i += 1

    i = 0
    while i < len(args):
        if args[i] == "+" or args[i] == "-":
            left = float(args[i - 1])
            right = float(args[i + 1])

            if args[i] == "+":
                result = sum(left, right)
            else:
                result = sub(left, right)

            del args[i - 1:i + 2]
            args.insert(i - 1, result)

            i = 0
        else:
            i += 1

    return args


def calculate(args):
    return sort(args)