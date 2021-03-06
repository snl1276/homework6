def inspect(function_to_decorate):
    def accepting_arguments(*args, **Reversed):
        print('Args:', args)
        print('Kwargs:',  Reversed)
        print(function_to_decorate(*args, **Reversed))
    return accepting_arguments


@inspect
def concat(*args: str, **Reversed) -> str:
    stroka = ''
    if not Reversed:
        for iter in args:
            stroka += iter
    else:
        for iter in reversed(args):
            stroka += iter
    print('Retvalue: ', stroka)
    return stroka


concat('Hello', ' ', 'world', Reversed=True)
