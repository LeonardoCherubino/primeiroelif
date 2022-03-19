#Estudando Elif com Lira
meta = int(input('Entre com o valor da meta: '))
vendas = int(input('Entre com o valor das vendas: '))

if vendas < meta:
    print('Não bateu a meta. Não ganha bônus')
elif vendas > (meta * 2):
    bonus = 0.07 * vendas
    print('Ganhou {} de bônus'.format(bonus))
else:
    bonus = 0.03 * vendas
    print('Ganhou {} de bônus'.format(bonus))

