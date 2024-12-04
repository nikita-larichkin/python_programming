import decalc


def create_list(*args, **kwargs) -> list[str]:
    lst = []
    for value in args:
        lst += [f'Point_{args.index(value)} = {decalc.deg_to_gms(value)}']
    for name, value in kwargs.items():
        lst += [f'{name} = {decalc.deg_to_gms(value)}']

    return lst


print(create_list(172.25899161, 321.4234971, 12.697987681352, pole=21.89617856, put_1=148.85786440))
