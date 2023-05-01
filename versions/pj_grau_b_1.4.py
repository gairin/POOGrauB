import math
import os

# Classes
class Locadora:
    def __init__(self):
        self.carrega_dados()

    def carrega_dados(self):
        veiculos = []
        locacoes = []

        arq = open('veiculos.txt')
        arq.readline()
        for linha in arq:
            veiculos.append(Veiculo(linha))
        arq.close()

        arq = open('locacoes.txt')
        arq.readline()

        x = 0
        for linha in arq:
            locacoes.append(Locacao(linha, veiculos[x]))
            x += 1

        arq.close()

        self._veiculos = veiculos #list (Veiculo)
        self._locacoes = locacoes #list (Locacao)
    
        return veiculos, locacoes

    def salva_dados(self, codigo, atr, valor, lista):
        # De forma simples, essa linha aqui funciona de forma idêntica ao setter, em apenas uma linha.
        # Aqui, aqui o atributo (atr) do veículo/locação (lista) específico do cliente ([codigo - 1])
        # que eu passar de parâmetro vai ser setado com um valor (valor) qualquer
        # que eu posso passar de parâmetro nesse método. Na linha 155 tem um exemplo de como funciona e como chamar.
        setattr(lista[codigo - 1], atr, valor)

    def consulta_veiculo(self):
        print('CONSULTAR VEÍCULOS:')
        print('Atributos disponíveis: modelo, cor, ano, cidade\n')

        atributo = str(input("Atributo de pesquisa: ")).lower()

        while atributo not in ['modelo', 'cor', 'ano', 'cidade']:
            print('Este atributo não pode ser pesquisado.')
            print('Atributos disponíveis: modelo, cor, ano, cidade\n')

            atributo = str(input("Atributo de pesquisa: ")).lower()

        caracteristica = str(input("Característica: ")).title()

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Pesquisa por: {atributo} e {caracteristica}')
        print('Veículos disponíveis:')

        achado = False

        match(atributo):
            case 'modelo':
                for veiculo in self._veiculos:
                    if caracteristica == veiculo.get_modelo():
                        print(veiculo.serializar())
                        achado = True

            case 'cor':
                for veiculo in self._veiculos:
                    if caracteristica == veiculo.get_cor():
                        print(veiculo.serializar())
                        achado = True

            case 'ano':
                for veiculo in self._veiculos:
                    if caracteristica == veiculo.get_ano():
                        print(veiculo.serializar())
                        achado = True

            case 'cidade':
                for veiculo in self._veiculos:
                    if caracteristica == veiculo.get_cidade():
                        print(veiculo.serializar())
                        achado = True
        
        if achado == False:
            print('Nenhum veículo com estas características foi encontrado.')

        input('Pressione ENTER para continuar')

    def realiza_locacao(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        cidades_disponiveis = []

        for veiculo in self._veiculos:
            cidades_disponiveis.append(veiculo.get_cidade())
            
        cidade_origem = str(input('Insira sua cidade de origem: ')).title()

        while cidade_origem not in cidades_disponiveis:
            cidade_origem = str(input('Não há veículos nessa cidade, tente outra cidade: ')).title()

        print('Veículos disponíveis em', cidade_origem)

        veiculos_disponiveis = []

        for veiculo in self._veiculos:
            if veiculo.get_cidade() == cidade_origem:
                print(veiculo.serializar())
                veiculos_disponiveis.append(veiculo.get_codigo())
        
        print('Selecione um veículo para alugar:')

        disponibilidade = []

        for x in veiculos_disponiveis:
            disponibilidade.append(self._veiculos[x].get_disponivel())
        
        if True in disponibilidade:
            veiculo_alugado = verifica_input('int')
            
            while veiculo_alugado not in veiculos_disponiveis:
                print('Código inválido.')
                veiculo_alugado = verifica_input('int')
            
            while self._veiculos[veiculo_alugado - 1].get_disponivel() == False:
                print('Este veículo não está disponível, selecione outro.')
                veiculo_alugado = verifica_input('int')

            nome_cliente = str(input('Insira seu nome: ')).title()
            
            while nome_cliente != self._locacoes[veiculo_alugado - 1].get_cliente():
                print('O nome não bate com a locação. Tente novamente')
                nome_cliente = str(input('Insira seu nome: '))
                
            if nome_cliente not in lista_de_clientes:
                print('Insira o número de diárias:')
                input_diarias = verifica_input('int')

                while input_diarias != self._locacoes[veiculo_alugado - 1].get_qt_dias_reserva():
                    print('Isso não coincide com a locação. Tente de novo.')
                    input_diarias = verifica_input('int')
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print('INFORMAÇÕES DE LOCAÇÃO:')
                print('Veículo:', self._veiculos[veiculo_alugado - 1].get_modelo(), self._veiculos[veiculo_alugado - 1].get_cor(), self._veiculos[veiculo_alugado - 1].get_ano())
                print('Cidade de origem:', cidade_origem)
                print('Número de diárias:', input_diarias)
                print(f'Custo por diária: R${self._veiculos[veiculo_alugado - 1].get_valor_diaria()}')
                print(f'Custo total: R${(self._veiculos[veiculo_alugado - 1].get_valor_diaria() * input_diarias):.2f}')
                confirmacao = str(input('Confirmar locação?: ')[0].lower())

                if confirmacao == 's':
                    print('Veículo locado.')
                    self.salva_dados(veiculo_alugado, 'set_disponivel', False, veiculos)
                    lista_de_clientes.append(nome_cliente)
                    input('Pressione ENTER para continuar')
                
                else:
                    print('Veículo não locado.')
                    input('Pressione ENTER para continuar')
            
            else:
                print('Você não pode alugar mais de um veículo ao mesmo tempo.')
                input('Pressione ENTER para continuar')
        
        else:
            print('Não há nenhum veículo disponível. Retornando automaticamente.')
            input('Pressione ENTER para continuar')

    def realiza_devolucao(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        nome_cliente = str(input('Insira seu nome: ')).title()
        if nome_cliente in lista_de_clientes:
            destino = str(input('Insira a cidade onde o carro foi entregue: ')).title()

            print('Informe os km rodados:')
            km_rodado = verifica_input('int')

            for locacao in self._locacoes:
                if locacao.get_cliente() == nome_cliente:
                    if locacao.get_veiculo().get_disponivel() == False:
                        locacao_cliente = locacao
                        veiculo_cliente = locacao.get_veiculo()
                        break
            
            cidade_origem = locacao_cliente.get_origem()
            valor_diaria = veiculo_cliente.get_valor_diaria()
            valor_km = veiculo_cliente.get_valor_km_rodado()
            diarias_cliente = locacao_cliente.get_qt_dias_reserva()

            print("Os dias reservados foram:", diarias_cliente, "dias")
            
            qt_dias_realizado = int(input("Informe por quantos dias ficou com o carro alugado: "))  
            
            #aqui n esta dando print, n consegui arrumar
            
            # Desconto por devolver cedo
            if cidade_origem == destino:
                if diarias_cliente > qt_dias_realizado: #se devolver na mesma cidade n tem custo adicional
                    valor_desconto = (diarias_cliente - qt_dias_realizado) * (20/100) #Caso tenha devolvido o carro antes, o sistema dá um desconto de 20% sobre as diárias não utilizadas
                    valor_total = (valor_diaria * diarias_cliente + km_rodado * valor_km) - valor_desconto
                    valor_total -= valor_desconto
                    print("Valor total a pagar é R$", valor_total)
                    input("Pressione ENTER para continuar")
                    #na devolução, o sistema atualiza a cidade e o odômetro do carro, e o libera para nova locação.  (n lembro como faz)  
                
                elif diarias_cliente < qt_dias_realizado:
                    valor_multa = (qt_dias_realizado - diarias_cliente) * (30/100) #Caso tenha devolvido o carro antes, o sistema dá um desconto de 20% sobre as diárias não utilizadas
                    valor_total = (valor_diaria * diarias_cliente + km_rodado * valor_km)
                    valor_total += valor_multa
                    print("Valor total a pagar é R$", valor_total)
                    input("Pressione ENTER para continuar")
                
                else:
                    valor_total = (valor_diaria * diarias_cliente + km_rodado * valor_km)
                    print("Valor total a pagar é R$", valor_total)
                    input("Pressione ENTER para continuar")

            else:
                if diarias_cliente > qt_dias_realizado:
                    valor_desconto = (diarias_cliente - qt_dias_realizado) * (20/100) #Caso tenha devolvido o carro antes, o sistema dá um desconto de 20% sobre as diárias não utilizadas
                    valor_total = (valor_diaria * diarias_cliente + km_rodado * valor_km)
                    valor_multa_cidade = valor_total * (15/100)
                    valor_total += valor_multa_cidade
                    valor_total -= valor_desconto
                    print("Valor total a pagar é R$", valor_total)
                    input("Pressione ENTER para continuar")
                    #na devolução, o sistema atualiza a cidade e o odômetro do carro, e o libera para nova locação.  (n lembro como faz)  
                
                elif diarias_cliente < qt_dias_realizado:
                    valor_multa = (qt_dias_realizado - diarias_cliente) * (30/100) #Caso tenha devolvido o carro antes, o sistema dá um desconto de 20% sobre as diárias não utilizadas
                    valor_total = (valor_diaria * diarias_cliente + km_rodado * valor_km)
                    valor_multa_cidade = valor_total * (15/100)
                    valor_total += valor_multa_cidade
                    valor_total += valor_multa
                    print("Valor total a pagar é R$", valor_total)
                    input("Pressione ENTER para continuar")
                
                else:
                    valor_total = (valor_diaria * diarias_cliente + km_rodado * valor_km)
                    print("Valor total a pagar é R$", valor_total)
                    input("Pressione ENTER para continuar")

        else:
            print('Você não tem um veículo alugado agora.')

    def relatorio_resumo():
        pass
    
    def get_locacoes(self):
        return self._locacoes
    
    def get_veiculos(self):
        return self._veiculos

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
    
    def set_odometro(self, valor):
        self._odometro += valor
    
    def set_cidade(self, cidade):
        self._cidade = cidade

    def get_cidade(self):
        return self._cidade
    
    def set_disponivel(self, valor):
        self._disponivel = valor

    def get_disponivel(self):
        return self._disponivel
    
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
        if dados[6] == 'S':
            self._disponivel = True #bool
        else:
            self._disponivel = False #bool
        self._valor_diaria = float(dados[7]) #float
        self._valor_km_rodado = float(dados[8]) #float

    #def __str__(self):
    #    return f'Modelo: {self._modelo}\nCor: {self._cor}\nAno: {self._ano}\nOdômetro: {self._odometro}km\nCidade: {self._cidade}\nDisponível: {self._disponivel}\nValor diária: R${self._valor_diaria}\nValor por km rodado: R${self._valor_km_rodado}'

class Locacao:
    def __init__(self, linha, veiculo):
        self.deserializar(linha, veiculo)
    
    def get_veiculo(self):
        return self._veiculo
    
    def get_cliente(self):
        return self._cliente
    
    def get_origem(self):
        return self._origem
    
    def get_qt_dias_reserva(self):
        return self._qt_dias_reserva
    
    def valor_diarias():
        pass

    def valor_roaming():
        pass

    def valor_km_rodado():
        pass

    def serializar(self):
        return f'{self._veiculo}\t{self._cliente}\t{self._origem}\t{self._destino}\t{self._km_rodado}\t{self._qt_dias_reserva}\t{self._qt_dias_realizado}'
    
    def deserializar(self, linha, veiculo):
        dados = linha.split("\t")
        self._veiculo = veiculo #Veiculo
        self._cliente = dados[1] #str
        self._origem = dados[2] #str
        self._destino = dados[3] #str
        if dados[4] == '':
            self._km_rodado = None
        else:
            self._km_rodado = int(dados[4]) #int
        self._qt_dias_reserva = int(dados[5]) #int
        if dados[6].replace('\n', '') == '':
            self._qt_dias_realizado = None
        else:
            self._qt_dias_realizado = int(dados[6].replace('\n', '')) #int

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

locadora = Locadora()

veiculos = locadora.get_veiculos()
locacoes = locadora.get_locacoes()

lista_de_clientes = []
for x in range(0, len(veiculos)):
    if veiculos[x].get_disponivel() == False:
        lista_de_clientes.append(locacoes[x].get_cliente())

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

while escolha != 7:
    escolha = menu()

    match(escolha):
        case 1:
            # Consultar veículos
            os.system('cls' if os.name == 'nt' else 'clear')
            locadora.consulta_veiculo()

        case 2:
            # Realizar locação
            locadora.realiza_locacao()
             
        case 3:
            # Realizar devolução
            locadora.realiza_devolucao()

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
# #2 - CHECK
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