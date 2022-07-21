import time
print('__---Bem vindo a JetBov---__')
time.sleep(1.5)
print('1 -> [SIM] 2 -> [NÃO]')
add_cabeca = int(input('Inserir animal ao piquete: '))  # input para iniciar software

piquete1 = float(input('Informe GMD do piquete1: '))  # inputs para definir GDM
piquete2 = float(input('Informe GMD do piquete2: '))
piquete3 = float(input('Informe GMD do piquete3: '))

contador = 1  # variavel para definir a quantidade de animais no piquete
while contador < 11:
    if add_cabeca == 1:  # condicional para adicionar animal 1 iniciar coleta de dados do animal
        animal = str(input('Animal a ser rotacionado: ')).upper()
        print(f'Animal com brinco {animal} selecionado')
        peso_inicial = float(input('Informe o peso atual do animal: '))
        print('Piquetes disponíveis')
        print('1 -> [Piquete1] 2 -> [Piquete2] 3 -> [Piquete3]')
        tempo1 = int(input('Defina o tempo de pastagem piquete1: '))
        tempo2 = int(input('Defina o tempo de pastagem piquete2: '))
        tempo3 = int(input('Defina o tempo de pastagem piquete3: '))
        tempo_total = tempo1 + tempo2 + tempo3  # soma do tempo total de pastagem
        if tempo_total > 30:  # condicional para advertência de tempo de permanência excedido
            print('Tempo médio para recuperaçao da pastagem excedido.')  # mensagem apenas informativa
        peso_final = peso_inicial + (piquete1 * tempo1) + (piquete2 * tempo2) + (piquete3 * tempo3)  # peso final animal
        gdm = (peso_final - peso_inicial) / tempo_total  # calculo de ganho medio diario do animal baseado nos dados

        print(f'Animal {animal} iniciará a rotação com {peso_inicial:.2f}Kg, terá um tempo de rotação de {tempo_total} '
              f'dias com GMD de {gdm:.3f}.')  # print com informações de pertinentes ao criador
        print(f'Podendo chegar ao final da rotação de pastagem com um peso de {peso_final:.2f}Kg.')
        print('1 -> [SIM] 2 -> [NÃO]')  # condicional para adicionar mais animais
        add_cabeca = int(input('Inserir animal ao piquete: '))
        contador = contador + 1
    else:
        print('Ecerrando.')
        break
else:
    print('Limite de cabeças de gado por piquete atingido.')  # mensagem de advertência apartir dai o programa para
