import math
import os

# Classes
class Locadora:
    def __init__(self, veiculos, locacoes):
        self._veiculos = veiculos #list (Veiculo)
        self._locacoes = locacoes #list (Locacao)

    def carrega_dados():
        pass

    def salva_dados():
        pass

    def consulta_veiculo():
        pass

    def realiza_locacao():
        pass

    def realiza_devolucao():
        pass

    def relatorio_resumo():
        pass

class Veiculo:
    def __init__(self, linha):
        self.deserializar(linha)

    def get_codigo(self):
        return self._codigo

    def get_modelo(self):
        return self._modelo
    
    def get_cor(self):
        return self._cor
    
    def get_ano(self):
        return self._ano
    
    def get_cidade(self):
        return self._cidade
    
    def get_valor_diaria(self):
        return self._valor_diaria
    
    def get_valor_km_rodado(self):
        return self._valor_km_rodado

    def serializar(self):
        return f'{self._codigo}\t{self._modelo}\t{self._cor}\t{self._ano}\t{self._odometro}km\t{self._cidade}\t{self._disponivel}\tR${self._valor_diaria}\tR${self._valor_km_rodado}'
    
    def deserializar(self, linha):
        dados = linha.split("\t")
        self._codigo = int(dados[0]) #int
        self._modelo = dados[1] #str
        self._cor = dados[2] #str
        self._ano = int(dados[3]) #int
        self._odometro = int(dados[4]) #int
        self._cidade = dados[5] #str
        self._disponivel = bool(dados[6]) #bool
        self._valor_diaria = float(dados[7]) #float
        self._valor_km_rodado = float(dados[8]) #float

    #def __str__(self):
    #    return f'Modelo: {self._modelo}\nCor: {self._cor}\nAno: {self._ano}\nOdômetro: {self._odometro}km\nCidade: {self._cidade}\nDisponível: {self._disponivel}\nValor diária: R${self._valor_diaria}\nValor por km rodado: R${self._valor_km_rodado}'

class Locacao:
    def __init__(self, linha):
        self.deserializar(linha)
    
    def valor_diarias():
        pass

    def valor_roaming():
        pass

    def valor_km_rodado():
        pass

    def serializar(self):
        return f'{self._veiculo}\t{self._cliente}\t{self._origem}\t{self._destino}\t{self._km_rodado}\t{self._qt_dias_reserva}\t{self._qt_dias_realizado}'
    
    def deserializar(self, linha):
        dados = linha.split("\t")
        self._veiculo = dados[0] #Veiculo
        self._cliente = dados[1] #str
        self._origem = dados[2] #str
        self._destino = dados[3] #str
        self._km_rodado = int(dados[4]) #int
        self._qt_dias_reserva = int(dados[5]) #int
        self._qt_dias_realizado = int(dados[6]) #int

# Função com o propósito de verificar os inputs do usuário.
def verifica_input(tipo):
    match(tipo):
        case 'int':
            while True:
                try:
                    valor = int(input('-> '))

                except ValueError:
                    print('Insira um número inteiro.')

                else:
                    return valor

        case 'float':
            while True:
                try:
                    valor = float(input('-> '))

                except ValueError:
                    print('Insira um número.')

                else:
                    return valor
            
veiculos = []
locacoes = []

# Instanciação dinâmica dos objetos
# Veículos
arq = open('veiculos.txt')
arq.readline()
for linha in arq:
    v = Veiculo(linha)
    veiculos.append(v)
arq.close()

# Locação

locadora = Locadora(veiculos, locacoes)

# Menu
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('LOCAÇÃO:')
    print('1 - Consultar veículos')
    print('2 - Realizar locação')
    print('3 - Realizar devolução')
    print('4 - Consultar locação')
    print('5 - Resumo')
    print('6 - Salvar')
    print('7 - Sair')
    
    escolha = verifica_input('int')
    
    return escolha

escolha = None

while escolha != 8:
    escolha = menu()

    match(escolha):
        case 1:
            #Consultar veículos
            os.system('cls' if os.name == 'nt' else 'clear')

            print('CONSULTAR VEÍCULOS:')
            print('Atributos disponíveis', end=': ')
            for a in ['modelo', 'cor', 'ano', 'cidade']:
                print(a, end=', ')

            print()
            atributo = str(input("Atributo de pesquisa: ")).lower()

            while atributo not in ['modelo', 'cor', 'ano', 'cidade']:
                print('Este atributo não pode ser pesquisado.')
                print('Atributos disponíveis', end='')

                for a in ['modelo', 'cor', 'ano', 'cidade']:
                    print(a, end=', ')

                atributo = str(input("Atributo de pesquisa: ")).lower()

            caracteristica = str(input("Característica: ")).title()

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Pesquisa por: {atributo} e {caracteristica}')
            print('Veículos disponíveis:')

            achado = False

            match(atributo):
                case 'modelo':
                    for veiculo in veiculos:
                        if caracteristica == veiculo.get_modelo():
                            print(veiculo.serializar())
                            achado = True

                case 'cor':
                    for veiculo in veiculos:
                        if caracteristica == veiculo.get_cor():
                            print(veiculo.serializar())
                            achado = True

                case 'ano':
                    for veiculo in veiculos:
                        if caracteristica == veiculo.get_ano():
                            print(veiculo.serializar())
                            achado = True

                case 'cidade':
                    for veiculo in veiculos:
                        if caracteristica == veiculo.get_cidade():
                            print(veiculo.serializar())
                            achado = True
            
            if achado == False:
                print('Nenhum veículo com estas características foi encontrado.')

            input('Pressione ENTER para continuar')

        case 2:
            # Realizar locação
            '''
            2. Realizar locação:  Cliente informa a cidade de origem e o sistema mostra todos os
            veículos disponíveis para a cidade e seus respectivos atributos. Em seguida, o cliente
            indica qual o código do veículo que deseja alugar, informa seu nome e a quantidade de
            diárias. O sistema mostra o valor total das diárias e realiza a locação caso o cliente
            aceite. O sistema não deve permitir que o cliente tenha mais de um carro alugado
            simultaneamente.
            '''

            cidade_origem = str(input('Insira sua cidade de origem: '))

            veiculos_achados = 0

            print('Procurando por veículos em', cidade_origem)

            for veiculo in veiculos:
                if cidade_origem == veiculo.get_cidade():
                    print(veiculo.serializar())
                    veiculos_achados.append(veiculo.get_codigo())
            
            if achado == 0:
                print('Não foram encontrados veículos em', cidade_origem)
            
            else:
                escolha = verifica_input('int')

                while escolha not in veiculos_achados:
                    print('Código inválido.')
                    escolha = verifica_input('int')

                nome_cliente = str(input('Insira seu nome: '))

                qt_diarias = verifica_input('int')

                valor_diaria = veiculos[escolha - 1].get_valor_diaria()
                valor_km_rodado = veiculos[escolha - 1].get_valor_km_rodado()

                print(f'Valor das diárias deste veículo: R${valor_diaria}')
                print(f'Valor por km rodado: R${valor_km_rodado}p/km')
                print(f'Total das diárias: R${valor_diaria * qt_diarias}')
                escolha_locacao = str(input('Deseja locar o veículo?'))[0].upper()

                #if escolha_locacao == 'S':
                    #locacoes.append(Locacao())
                #else:
                    #print('F')

            # a lista de locações é pra instanciar, provável
            # tem que usar os nomes da lista locacoes.txt aqui pra fazer as locações? cada um deles?
            # aí eu passo como as informações pedidas os atributos do locacoes.txt?
            # list append + locações + nomes dos clientes

            
        case 3:
            pass

        case 4:
            pass

        case 5:
            pass

        case 6:
            pass

        case 7:
            print('OK')

        case default:
            print('Inválido')

# CHECKLIST:
# #1 - CHECK
# #2 -
# #3 -
# #4 -
# #5 -
# #6 -
# #7 - CHECK

'''
1. Consultar veículos:  Usuário informa o nome de um atributo (modelo, cor, ano ou
cidade) seguido do valor do atributo, e o sistema mostra uma tabela com todos os
dados dos veículos que se enquadram na condição.
2. Realizar locação:  Cliente informa a cidade de origem e o sistema mostra todos os
veículos disponíveis para a cidade e seus respectivos atributos. Em seguida, o cliente
indica qual o código do veículo que deseja alugar, informa seu nome e a quantidade de
diárias. O sistema mostra o valor total das diárias e realiza a locação caso o cliente
aceite. O sistema não deve permitir que o cliente tenha mais de um carro alugado
simultaneamente.
3. Realizar   devolução:  Cliente   informa   seu   nome,   a   cidade   de   devolução   e   a
quilometragem percorrida. Nesse instante, o sistema informa a quantidade de dias
contratados e o cliente confirma ou informa a quantidade real de dias que utilizou o
carro. Caso tenha devolvido o carro antes, o sistema dá um desconto de 20% sobre as
diárias não utilizadas, mas se devolveu depois, tem uma multa de 30% sobre as diárias
extras. Depois, o sistema calcula e informa o valor referente aos quilômetros rodados e
a possível taxa de roaming. Se devolver na mesma cidade de origem não tem custo
adicional, mas se devolver em uma cidade diferente, a taxa é de 15% sobre o valor total
(diárias + km rodado). Ainda na devolução, o sistema atualiza a cidade e o odômetro do
carro, e o libera para nova locação.
4. Consultar locações:  Usuário informa nome do cliente e/ou modelo do veículo e o
sistema mostra todos os dados dos veículos e das locações correspondentes, ativas e
finalizadas.
5. Resumo: Mostrar na tela um resumo de todas as locações já finalizadas, contendo os
somatórios de km rodados, quantidade de dias  contratados e realizados,  valor das
diárias contratadas, valor das diárias extras, valor da taxa de roaming, valor dos km
rodados e valor total das locações.
6. Salvar: Salva os dados dos veículos no arquivo “veiculos.txt”. As locações tanto ativas
quanto finalizadas devem ser salvas no arquivo “locacoes.txt”. Atributos sem dados
devem ser salvos como string vazia. Utilizar o caractere <TAB> como separador dos
dados.
7. Sair: Encerra o sistema, liberando os objetos instanciados dinamicamente. Caso algum
dado não tenha sido salvo em arquivo, salvar automaticamente.
'''

'''
Cenário: Um cliente acessa o sistema da locadora e solicita a locação de um carro, informando
a cidade de origem. Ele consulta a lista de veículos disponíveis na cidade e escolhe um deles.
Depois informa a quantidade de dias que  pretende  ficar com o veículo. Nesse momento, o
sistema calcula e mostra para o cliente o valor total  estimado  das diárias e pergunta se o
usuário quer reservar o carro. Caso afirmativo, o sistema registra a locação. Quando o cliente
devolver o veículo, o sistema solicita a cidade de devolução e a quilometragem percorrida. O
sistema também mostra a quantidade de diárias contratadas, e pede para o cliente confirmar
ou informar uma quantidade diferente da reservada.  Nesse instante, o sistema  calcula e
informa o valor referente aos quilômetros rodados, a possível diferença nas diárias e a taxa de
roaming. Ainda na devolução, o sistema atualiza a cidade e o odômetro do carro, e o libera
para nova locação.
'''

'''
Observações:
•Carregar   automaticamente   os   arquivos   “veiculos.txt”   e   “locacoes.txt”   ao   iniciar   o
programa,   instanciando   dinamicamente   os   objetos.   Os   formatos   dos   arquivos   de
exemplo devem ser obedecidos à risca;
•Todas as ações devem ser realizadas sobre os objetos em memória;
•Todas as funcionalidades descritas nesta definição devem ser implementadas;
•Os nomes de classes, atributos e métodos especificados acima na estrutura das classes
devem ser mantidos na implementação do código (ou seja, não os renomeie). Novos
métodos e atributos devem ser nomeados de acordo com a sua respectiva função;
•Se necessário, implemente métodos getters e setters para os atributos das classes.
Métodos setters devem verificar o valor sendo setado ao atributo quando necessário;
•Para padronizar  a persistência  de dados,  implementar os métodos “serializar()”  e
“deserializar()”;
'''