def decorator_imprimir(func):
    def inner(capital, taxa, tempo):
        print(f'CAPITAL: R$ {capital}   TAXA: {taxa} %   TEMPO: {tempo} meses')
        rendimento = func(capital, taxa, tempo)
        print('RENDIMENTO MENSAL = R$ %.2f' % rendimento)
    return inner

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

juros_simples(1000, 5, 6)