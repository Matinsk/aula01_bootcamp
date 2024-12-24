programa_ativo = True
while programa_ativo:

        nome = input("Digite seu nome: ")
        salario = input("Digite seu salário: ")
        bonus = input("Digite o bônus adquirido: ")



        try:
            salario = float(salario)
            bonus = float(bonus)
            if bonus < 1:
                print("O valor do bônus deve ser acima de 1")
                break
            salario_ajustado = salario * bonus
            print(f'Olá {nome} o seu bônus é de: R${salario_ajustado}')
            programa_ativo = False
        except:
            print("Variáveis com tipagem de dados incorreta!")
            break