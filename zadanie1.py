def concat(*args: str, **Reversed) -> str:
    stroka = ''
    if not Reversed:
        for iter in args:
            stroka += iter
    else:
        for iter in reversed(args):
            stroka += iter
    return print(stroka)


concat('Hello', ' ', 'world')
concat('Hello', ' ', 'world', Reversed=True)
