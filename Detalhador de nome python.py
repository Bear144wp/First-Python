nome = input('Digite seu nome')
idade = int(input('Digite sua idade'))

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome nao contem espaços')

    print(f'seu nome contém {len(nome)} letras')
    print(f'a ultima letra do seu none é {nome [-1]}')
    print(f'a primeira letra do seu none é {nome [0]}')

else:
    print('Voce nao digitou porra nenhunma')

print(f'A váriavel do seu nome é: {type(idade)}')