# CHECKLIST:
# #1 - CHECK
# #2 - CHECK
# #3 - CHECK
# #4 - CHECK
# #5 - CHECK
# #6 - CHECK
# #7 - CHECK
# TESTES - CHECK

# vou reservar os comentários apenas para partes do código que não ficaram
# auto-explicativas o bastante ou apenas para indicações gerais do que cada
# bloco faz.

import os

# Classes
class Locadora:
    def __init__(self):
        # logo de cara, a classe chama a desserialização dos dados
        self.carrega_dados()

    def carrega_dados(self):
        # a classe locadora irá conter a lista de locações e objetos.
        veiculos = []
        locacoes = []

        # instancicação dinâmica de todos os dados dos arquivos e depois atribuição.
        arq = open('veiculos.txt')
        arq.readline()
        for linha in arq:
            veiculos.append(Veiculo(linha))
        arq.close()

        arq = open('locacoes.txt')
        arq.readline()

        # x serve para que iterar por cada veículo da lista "veiculos", isso é pra
        # passar o veículo correspondente junto da instanciação da locação.
        # como a lista segue uma ordem linear (locação 1 aluga veículo 1 e assim em diante)
        # isso funcionará neste caso.
        x = 0
        for linha in arq:
            locacoes.append(Locacao(linha, veiculos[x]))
            x += 1

        arq.close()

        self._veiculos = veiculos #list (Veiculo)
        self._locacoes = locacoes #list (Locacao)
    
        return veiculos, locacoes

    def seta_dados(self, codigo, atr, valor, lista):
        # este método quando chamada recebe um atributo para que seja atualizado, que é
        # é comparado até que o atributo correspondente seja selecionado.
        # de certa forma, ajuda a unificar as chamadas dos setters
        # eu no começo achava que era isso que tinha que fazer em salva_dados,
        # mas não era o caso. não vou apagar isso, já que está funcionando normalmente

        match(atr):
            case 'disp':
                lista[codigo - 1].set_disponivel(valor)
            case 'odomtr':
                lista[codigo - 1].set_odometro(valor)
            case 'cid':
                lista[codigo - 1].set_cidade(valor)
            case 'kmr':
                lista[codigo - 1].set_km_rodado(valor)
            case 'dest':
                lista[codigo - 1].set_destino(valor)
            case 'diasr':
                lista[codigo - 1].set_qt_dias_realizado(valor)

    def consulta_veiculo(self):
        print('CONSULTAR VEÍCULOS:')
        print('Atributos disponíveis: modelo, cor, ano, cidade\n')

        # essa estrutura repetir-se-á várias vezes no decorrer do programa
        # input do usuário
        print('Atributo de pesquisa:')
        # verificação do input (essa parte será explicada depois quando chegar)
        atributo = verifica_input('str').lower()

        # verificação do conteúdo em si
        while atributo not in ['modelo', 'cor', 'ano', 'cidade']:
            print('Este atributo não pode ser pesquisado.')
            print('Atributos disponíveis: modelo, cor, ano, cidade\n')

            atributo = verifica_input('str').lower()

        print('Característica:')
        caracteristica = verifica_input('str').title()

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Pesquisa por: {atributo} e {caracteristica}')
        print('Veículos disponíveis:')

        achado = False

        # essa estrutura também irá se repetir bastante
        # verificação por atributos, se o modelo (ou qualquer outra coisa) bate
        # com algum valor de qualquer um dos itens possíveis
        match(atributo):
            case 'modelo':
                for veiculo in self._veiculos:
                    if caracteristica == veiculo.get_modelo():
                        print(veiculo)
                        print()

                        # variável lógica básica
                        achado = True

            case 'cor':
                for veiculo in self._veiculos:
                    if caracteristica == veiculo.get_cor():
                        print(veiculo)
                        print()
                        achado = True

            case 'ano':
                for veiculo in self._veiculos:
                    if caracteristica == veiculo.get_ano():
                        print(veiculo)
                        print()
                        achado = True

            case 'cidade':
                for veiculo in self._veiculos:
                    if caracteristica == veiculo.get_cidade():
                        print(veiculo)
                        print()
                        achado = True
        
        # se nada for encontrado, achado nunca será True. então, exibimos uma mensagem
        if achado == False:
            print('Nenhum veículo com estas características foi encontrado.')

        # pausa para que o usuário possa ler a informação sem que o programa volte ao menu
        input('Pressione ENTER para continuar')

    def realiza_locacao(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        cidades_disponiveis = []

        for veiculo in self._veiculos:
            cidades_disponiveis.append(veiculo.get_cidade())
        
        print('Insira sua cidade de origem:')
        cidade_origem = verifica_input('str').title()

        while cidade_origem not in cidades_disponiveis:
            print('Não há veículos nessa cidade, tente outra.')
            cidade_origem = verifica_input('str').title()

        print('Veículos disponíveis em', cidade_origem)

        veiculos_disponiveis = []

        # verificação se na cidade informada há um veículo
        for veiculo in self._veiculos:
            if veiculo.get_cidade() == cidade_origem:
                print(veiculo)
                print()
                veiculos_disponiveis.append(veiculo.get_codigo())
        
        print('Selecione um veículo para alugar:')

        disponibilidade = []

        for x in veiculos_disponiveis:
            disponibilidade.append(self._veiculos[x - 1].get_disponivel())
        
        # pegando os dados de disponibilidade de cada veículo, caso não tenha nenhum disponível
        # para o usuário escolher, ele volta ao menu automaticamente
        if True in disponibilidade:
            veiculo_alugado = verifica_input('int')
            
            while veiculo_alugado not in veiculos_disponiveis:
                print('Código inválido.')
                veiculo_alugado = verifica_input('int')
            
            while self._veiculos[veiculo_alugado - 1].get_disponivel() == False:
                print('Este veículo não está disponível, selecione outro.')
                veiculo_alugado = verifica_input('int')

            print('Insira seu nome:')
            nome_cliente = verifica_input('str').title()
            
            # verificação se o cliente já tem uma reserva
            if nome_cliente not in lista_de_clientes:
                print('Insira o número de diárias:')
                input_diarias = verifica_input('int')
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print('INFORMAÇÕES DE LOCAÇÃO:')
                print('Veículo:', self._veiculos[veiculo_alugado - 1].get_modelo(), self._veiculos[veiculo_alugado - 1].get_cor(), self._veiculos[veiculo_alugado - 1].get_ano())
                print('Cidade de origem:', cidade_origem)
                print('Número de diárias:', input_diarias)
                print(f'Custo por diária: R${self._veiculos[veiculo_alugado - 1].get_valor_diaria()}')
                print(f'Custo total: R${(self._veiculos[veiculo_alugado - 1].get_valor_diaria() * input_diarias):.2f}')
                
                print('Confirmar locação?')
                confirmacao = verifica_input('str')[0].lower()

                if confirmacao == 's':
                    # nova locação instanciada
                    l = Locacao(f'{len(locacoes)+1}\t{nome_cliente}\t{cidade_origem}\t\t\t{input_diarias}\t', veiculos[veiculo_alugado - 1])
                    locacoes.append(l)

                    # dados atualizados no veículo
                    self.seta_dados(veiculo_alugado, 'disp', False, veiculos)
                    
                    # adiciono o nome desse cliente à lista de clientes com locações ativas
                    lista_de_clientes.append(nome_cliente)
                    print('Veículo locado com sucesso.')
                    input('Pressione ENTER para continuar')
                
                else:
                    print('Veículo não locado.')
                    input('Pressione ENTER para continuar')
            
            else:
                print('Você não pode alugar mais de um veículo ao mesmo tempo.')
                input('Pressione ENTER para continuar')
        
        else:
            print('Não há nenhum veículo disponível nesta cidade. Retornando automaticamente.')
            input('Pressione ENTER para continuar')

    def realiza_devolucao(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print('Insira seu nome:')
        nome_cliente = verifica_input('str').title()

        if nome_cliente in lista_de_clientes:
            print('Insira a cidade onde o carro foi entregue:')
            destino = verifica_input('str').title()

            print('Informe os km rodados:')
            km_rodado = verifica_input('int')

            for locacao in self._locacoes:
                if locacao.get_cliente() == nome_cliente:
                    if locacao.get_veiculo().get_disponivel() == False:
                        # seleciona a locação e o veículo do cliente
                        locacao_cliente = locacao
                        veiculo_cliente = locacao.get_veiculo()
                        break
            
            diarias_cliente = locacao_cliente.get_qt_dias_reserva()
            print("Os dias reservados foram:", diarias_cliente, "dias")
            print("Informe por quantos dias ficou com o carro:")
            qt_dias_realizado = verifica_input('int')
            
            # dados são salvos e informações da locação são exibidas
            self.seta_dados(veiculo_cliente.get_codigo(), 'disp', True, veiculos)
            self.seta_dados(veiculo_cliente.get_codigo(), 'odomtr', km_rodado, veiculos)
            self.seta_dados(veiculo_cliente.get_codigo(), 'cid', destino, veiculos)
            self.seta_dados(locacao_cliente.get_codigo(), 'kmr', km_rodado, locacoes)
            self.seta_dados(locacao_cliente.get_codigo(), 'dest', destino, locacoes)
            self.seta_dados(locacao_cliente.get_codigo(), 'diasr', qt_dias_realizado, locacoes)
            locacao_cliente.calc_valor_total()
            valor_total = locacao_cliente.get_valor_total()

            print(locacao_cliente)
            print(f'Custo dos km rodados: R${locacao_cliente.get_km_rodado() * locacao_cliente.get_veiculo().get_valor_km_rodado():.2f}')
            print(f'O total a pagar é de R${valor_total:.2f}')
            input('Pressione ENTER para continuar.')
            
            # remove o nome desse cliente da lista de clientes com locações ativas
            lista_de_clientes.remove(nome_cliente)

        else:
            print('Você não tem um veículo alugado agora.')
            input("Pressione ENTER para continuar")
  
    def consultar_locacoes(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        # cliente escolhe qual tipo de pesquisa fazer
        print('Escolha:')
        print('1 - Pesquisa por nome')
        print('2 - Pesquisa por veículo')
        print('3 - Ambos')

        # verifica se o valor input inserido é int mesmo
        # isso deve evitar exceções de ValueError
        escolha = verifica_input('int')

        # se o usuário não colocar uma opção válida, vamos até que ele faça isso
        while escolha not in range(1, 4):
            print('Escolha inválida. Tente de novo')
            escolha = verifica_input('int')

        if escolha == 1:
            print('Insira o nome:')
            nome_pesquisa = verifica_input('str').title()

            achado = False
            print('Pesquisa por:', nome_pesquisa)
            for locacao in locacoes:
                if locacao.get_cliente() == nome_pesquisa:
                    print('Locação:')
                    print(locacao)
                    print()

                    achado = True
            
            if achado == False:
                print('Este nome não foi encontrado.')

        elif escolha == 2:
            print('Insira o modelo:')
            modelo_pesquisa = verifica_input('str').title()

            achado = False
            print('Pesquisa por:', modelo_pesquisa)
            for veiculo in veiculos:
                if veiculo.get_modelo() == modelo_pesquisa:
                    print('Veículo:')
                    print(veiculo)
                    print()

                    achado = True
            
            if achado == False:
                print('Este veículo não foi encontrado.')

        else:
            print('Insira o nome do cliente e depois o modelo do veículo separados por vírgula:')
            dados_pesquisa = verifica_input('str').title()

            # aqui, eu pedira ao usuário separar as informações por vírgula, aqui eu reenforço isso,
            # verificando se o usuário realmente fez isso
            while ',' not in dados_pesquisa:
                print('Separe as informações por vírgula.')
                dados_pesquisa = verifica_input('str').title()

            # separo as informações em dois elementos de uma lista
            dados_pesquisa = dados_pesquisa.split(', ')

            achado = False
            print(f'Pesquisa por: {dados_pesquisa[0]}, {dados_pesquisa[1]}')
            for locacao in locacoes:
                if locacao.get_cliente() == dados_pesquisa[0]:
                    if locacao.get_veiculo().get_modelo() == dados_pesquisa[1]:
                        print(locacao)
                        achado = True
                        print()

            if achado == False:
                print('Locação não encontrada.')

        input('Pressione ENTER para continuar.')
  
    def relatorio_resumo(self):
        # variáveis para o somatório
        s_km_rodado = 0
        s_dias_contratados = 0
        s_dias_realizados = 0
        s_valor_diarias = 0
        s_valor_diarias_extras = 0
        s_roaming = 0
        s_locacoes = 0

        # usando os métodos getter das locações, faço os somatórios.
        for locacao in locacoes:
            if locacao.get_valor_total() > 0:
                s_km_rodado += locacao.get_km_rodado()
                s_dias_contratados += locacao.get_qt_dias_reserva()
                s_dias_realizados += locacao.get_qt_dias_realizado()
                s_valor_diarias += locacao.get_veiculo().get_valor_diaria() * locacao.get_qt_dias_realizado()

                # isso aqui para locações que estouraram o número de reservas
                if locacao.get_qt_dias_realizado() > locacao.get_qt_dias_reserva():
                    s_valor_diarias_extras += (locacao.get_qt_dias_realizado() - locacao.get_qt_dias_reserva()) * locacao.get_veiculo().get_valor_diaria()

                # se a locação tiver o atributo roaming, isso significa que houve uma taxa de roaming
                # aplicada nessa locação, então ela é somada à soma das taxas de roaming
                if hasattr(locacao, '_roaming'):
                    s_roaming += locacao.get_valor_roaming()

                s_locacoes += locacao.get_valor_total()

        print('RESUMO:')
        print(f'Soma de kms rodados: {s_km_rodado}km')
        print('Soma de diárias contratadas:', s_dias_contratados)
        print('Soma de dias realizados:', s_dias_realizados)
        print(f'Soma dos valores das diárias: R${s_valor_diarias:.2f}')
        print(f'Soma das diárias extras: R${s_valor_diarias_extras:.2f}')
        print(f'Soma das taxas de roaming: R${s_roaming:.2f}')
        print(f'Soma dos valores totais das locações: R${s_locacoes:.2f}')
        input('Pressione ENTER para continuar')
    
    def salva_dados(self):
        # os dados disponíveis são adicionados a um documento de texto
        file = open("veiculos_2.txt", 'w')
        
        file.write("codigo\tmodelo\tcor\tano\todometro\tcidade\tdisponivel\tvalor_diaria\tvalor_km_rodado"+"\n")

        for veiculo in self._veiculos:
            file.write(veiculo.serializar()+"\n")
        
        file.close() # mesma coisa para locações
        print('Veículos salvos.')

        file = open("locacoes_2.txt", 'w')

        file.write("veiculo\tcliente\torigem\tdestino\tkm_rodado\tqt_dias_reserva\tqt_dias_realizado"+"\n")

        for locacao in self._locacoes:
            file.write(locacao.serializar()+"\n")
        
        file.close()
        print('Locações salvas.')
        input('Pressione ENTER para continuar')

    def get_locacoes(self):
        return self._locacoes
    
    def get_veiculos(self):
        return self._veiculos

class Veiculo:
    def __init__(self, linha):
        # logo de cara, os dados são desserializados
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
        return f'{self._codigo}\t{self._modelo}\t{self._cor}\t{self._ano}\t{self._odometro}\t{self._cidade}\t{self._disponivel}\t{self._valor_diaria}\t{self._valor_km_rodado}'
    
    # apenas para exibição em tela para o usuário
    def __str__(self):
        return f'{self._codigo} - {self._modelo} {self._cor} {self._ano}\nOdômetro: {self._odometro}km\nCidade: {self._cidade}\nDisponível: {self._disponivel}\nDiária: R${self._valor_diaria}, R${self._valor_km_rodado}/km'

    def deserializar(self, linha):
        dados = linha.split("\t")
        self._codigo = int(dados[0]) #int
        self._modelo = dados[1] #str
        self._cor = dados[2] #str
        self._ano = int(dados[3]) #int
        self._odometro = int(dados[4]) #int
        self._cidade = dados[5] #str
        
        # substituo S/N por True/False
        if dados[6] == 'S':
            self._disponivel = True #bool
        else:
            self._disponivel = False #bool
        self._valor_diaria = float(dados[7]) #float
        self._valor_km_rodado = float(dados[8]) #float

class Locacao:
    def __init__(self, linha, veiculo):
        # logo de cara, desserializamos os dados
        self.deserializar(linha, veiculo)

        # e calculamos os valores de cada locação/multas/descontos/roaming
        self.calc_valor_total()

    def calc_valor_total(self):
        # se houver destino, quer dizer que a locação já foi fechada
        if self._destino != '':
            # cálculos
            self._valor_total = round(self._qt_dias_reserva * self._veiculo.get_valor_diaria() + self._km_rodado * self._veiculo.get_valor_km_rodado(), 2)

            if self._origem != self._destino:
                self._valor_total += self.valor_roaming(self._valor_total)
            
            if self._qt_dias_reserva > self._qt_dias_realizado:
                self._valor_total -= self.valor_desconto()

            elif self._qt_dias_reserva < self._qt_dias_realizado:
                self._valor_total += self.valor_multa()
        
        else:
            # caso contrário, o valor total será 0
            self._valor_total = 0

    def get_codigo(self):
        return self._codigo

    def get_veiculo(self):
        return self._veiculo
    
    def get_cliente(self):
        return self._cliente
    
    def get_origem(self):
        return self._origem
    
    def set_destino(self, destino):
        self._destino = destino
    
    def get_km_rodado(self):
        return self._km_rodado
    
    def set_km_rodado(self, valor):
        self._km_rodado += valor
    
    def get_qt_dias_reserva(self):
        return self._qt_dias_reserva
    
    def get_qt_dias_realizado(self):
        return self._qt_dias_realizado
        
    def set_qt_dias_realizado(self, valor):
        self._qt_dias_realizado = valor
    
    def valor_diarias(self, diarias):
        return self._veiculo.get_valor_diaria() * diarias

    # esse método só é chamado em quem recebe taxa de roaming
    def valor_roaming(self, valor_total):
        taxa = round(valor_total * (15/100), 2)
        self._roaming = taxa
        return taxa
    
    # o mesmo para esse e o de baixo
    def valor_desconto(self):
        if self._destino != '':
            diaria = self._veiculo.get_valor_diaria()
            return round((diaria + (diaria * (20/100))) * (self._qt_dias_reserva - self._qt_dias_realizado), 2)
        else:
            return 0
    
    def valor_multa(self):
        if self._destino != '':
            diaria = self._veiculo.get_valor_diaria()
            return round((diaria + (diaria * (30/100))) * (self._qt_dias_realizado - self._qt_dias_reserva), 2)
        else:
            return 0

    def get_valor_roaming(self):
        return self._roaming

    def valor_km_rodado(self, km_rodado):
        return self._veiculo.get_valor_km_rodado() * km_rodado
    
    def get_valor_total(self):
        return self._valor_total
    
    def serializar(self):
        return f'{self._veiculo.get_codigo()}\t{self._cliente}\t{self._origem}\t{self._destino}\t{self._km_rodado}\t{self._qt_dias_reserva}\t{self._qt_dias_realizado}'
    
    def __str__(self):
        return f'{self._veiculo.get_modelo()} {self._veiculo.get_cor()} {self._veiculo.get_ano()}\nCliente: {self._cliente} - {self._origem} -> {self._destino}, {self._km_rodado}km rodados\nDias de reserva: {self._qt_dias_reserva}, {self._qt_dias_realizado} utilizados\nTaxa de roaming: R${self._roaming}\nCusto total: R${self._valor_total:.2f}'
    
    def deserializar(self, linha, veiculo):
        dados = linha.split("\t")
        self._veiculo = veiculo #Veiculo
        self._codigo = int(dados[0]) #int
        self._cliente = dados[1] #str
        self._origem = dados[2] #str
        self._destino = dados[3] #str
        
        # se isso for vazio, quer dizer que a locação não foi completa
        if dados[4] == '':
            # eu defino esse valor para 0, caso contrário, isso causaria erros mais pra frente no programa
            self._km_rodado = 0
        else:
            self._km_rodado = int(dados[4]) #int
        self._qt_dias_reserva = int(dados[5]) #int
        if dados[6].replace('\n', '') == '':
            self._qt_dias_realizado = None
        else:
            self._qt_dias_realizado = int(dados[6].replace('\n', '')) #int
        self._roaming = 0

# Função com o propósito de verificar os inputs do usuário.
def verifica_input(tipo):
    # recebe-se de argumento o tipo do dado que queremos
    match(tipo):
        # isso evita que o usuário coloque uma letra onde deveria ser int. isso evita um ValueError
        case 'int':
            while True:
                try:
                    valor = int(input('-> '))

                except ValueError:
                    print('Insira um número inteiro.')

                else:
                    return valor

        # o mesmo para float
        case 'float':
            while True:
                try:
                    valor = float(input('-> '))

                except ValueError:
                    print('Insira um número.')

                else:
                    return valor
        
        # isso acabou não servindo pra nada
        case 'str':
            try:
                valor = str(input('-> '))

            except ValueError:
                print('Coloque texto.')
            
            else:
                return valor

locadora = Locadora()

# para uso externo da lista de veículos e locações
veiculos = locadora.get_veiculos()
locacoes = locadora.get_locacoes()

lista_de_clientes = []
for x in range(0, len(veiculos)):
    # se o veículo não estiver disponível, significa uma locação ativa
    if veiculos[x].get_disponivel() == False:
        # o cliente dono dessa locação é adicionado à lista de clientes com locações ativas
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
            # Consultar locações
            locadora.consultar_locacoes()

        case 5:
            # Resumo
            locadora.relatorio_resumo()

        case 6:
            # Salvar
            locadora.salva_dados()

        case 7:
            # Sair
            print('OK')

        case default:
            print('Inválido')
            input('Pressione ENTER para continuar')