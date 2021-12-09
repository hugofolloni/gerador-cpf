import random

def print_cpf(cpf):
    first_part = cpf[0:3]
    second_part = cpf[3:6]
    third_part = cpf[6:9]
    fourth_part = cpf[9:11]
    printable_cpf = first_part + '.' + second_part + '.' + third_part + '-' + fourth_part
    print('\n' + printable_cpf)


def check_digits(cpf):
    sum = 0
    for i in range(9):
        sum += int(cpf[i]) * (10-i)
    first_digit = (sum * 10) % 11
    if first_digit == 10:
        first_digit = 0
    cpf += str(first_digit)

    sum = 0
    for i in range(10):
        sum += int(cpf[i]) * (11-i)
    second_digit = (sum * 10) % 11
    if second_digit == 10:
        second_digit = 0
    cpf += str(second_digit)

    print_cpf(cpf)
    validate_cpf(cpf)
        

def generate_cpf():
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))
    check_digits(cpf)


def validate_cpf(input_cpf):
    if len(input_cpf) != 11:
        return print('CPF inválido - tamanho incorreto')
    first_number = input_cpf[0]
    every_number_equals = True
    for i in range(1, 10):
        if first_number != input_cpf[i]:
            every_number_equals = False
    if every_number_equals:
        return print('CPF inválido - todos os números iguais')
    sum = 0
    for i in range(9):
        sum += int(input_cpf[i]) * (10-i)
    first_digit = (sum * 10) % 11
    if first_digit == 10:
        first_digit = 0
    if first_digit != int(input_cpf[9]):
        print('CPF inválido - dígito verificador 1')
    else:
        sum = 0
        for i in range(10):
            sum += int(input_cpf[i]) * (11-i)
        second_digit = (sum * 10) % 11
        if second_digit == 10:
            second_digit = 0
        if second_digit != int(input_cpf[10]):
            print('CPF inválido - dígito verificador 2')
        else:
            print('CPF válido')

def main():
    user = input('\n\nO que deseja fazer?\n1 - Gerar CPF\n2 - Validar CPF\n  ')
    if user == '1':
        generate_cpf()
    elif user == '2':
        input_cpf = input('\nDigite o CPF (apenas números): ')
        validate_cpf(input_cpf)
    else:
        print('Opção inválida!\n\n\n')
        main()

main()