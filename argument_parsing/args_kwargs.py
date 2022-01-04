# args_kwargs.py

# python3 args_kwargs.py result.txt
# python3 args_kwargs.py -o result.txt -l DEBUG -c ...

def my_function(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])

    print(kwargs['key01'])
    print(kwargs['key02'])


my_function("hey", True, 19, 'don', key01="haha", key02="hihi")

