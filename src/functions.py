def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def sort(args):
    mul_indexes = []
    div_indexes = []
    sum_indexes = []
    sub_indexes = []

    for y in range(len(args)):
        if args[y] == "*":
            mul_indexes.append(y)
        elif args[y] == "/":
            div_indexes.append(y)
        elif args[y] == "+":
            sum_indexes.append(y)
        elif args[y] == "-":
            sub_indexes.append(y)
    
    for i in range(len(mul_indexes)):
        result = mul(int(args[mul_indexes[i]-1]), int(args[mul_indexes[i]+1]))
        del args[mul_indexes[i]-1:mul_indexes[i]+2]
        args.insert(mul_indexes[i]-1, result)
        if len(mul_indexes) > i+1:
            result = mul(int(args[mul_indexes[i]-1]), int(args[mul_indexes[i]+1]))
            mul_indexes[i+1]-=2



    for i in range(len(div_indexes)):
        result = div(int(args[div_indexes[i]-1]), int(args[div_indexes[i]+1]))
        del args[div_indexes[i]-1:div_indexes[i]+2]
        args.insert(div_indexes[i]-1, result)
        if len(div_indexes) > i+1:
            div_indexes[i+1]-=2



    for i in range(len(sum_indexes)):
        result = sum(int(args[sum_indexes[i]-1]), int(args[sum_indexes[i]+1]))
        del args[sum_indexes[i]-1:sum_indexes[i]+2]
        args.insert(sum_indexes[i]-1, result)
        if len(sum_indexes) > i+1:
           sum_indexes[i+1]-=2



    for i in range(len(sub_indexes)):
        result = sub(int(args[sub_indexes[i]-1]), int(args[sub_indexes[i]+1]))
        del args[sub_indexes[i]-1:sub_indexes[i]+2]
        args.insert(sub_indexes[i]-1, result)
        if len(sub_indexes) > i+1:
            sub_indexes[i+1]-=2

    print(args)





# [5,*,5,-,5,*,5]
# list vur_indexes = [1, 5]
# int bol_indexes = []
# int toplama_indexes = []
# int cixma_indexes = [3]

def calculate(args):
    sort(args)