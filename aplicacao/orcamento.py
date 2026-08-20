from dominio.contrato import Contrato
from dominio.imovel import *
import csv
import textwrap

def gerar_orcamento():
    print('Bem vindo a Imobiliária RM!')
    menu_imovel = textwrap.dedent('''
    Selecione o tipo de Imóvel você gostaria de alugar:
    [1] Apartamento
    [2] Casa
    [3] Estúdio
    ''')
    opcoes_validas_imovel = {
        '1': Apartamento(),
        '2': Casa(),
        '3': Estudio()
    }
    opcao_imovel = selecionar_opcao(menu_imovel, opcoes_validas_imovel.keys())
    imovel = opcoes_validas_imovel.get(opcao_imovel)

    if type(imovel) == Apartamento:
        imovel = configurar_apartamento()
    elif type(imovel) == Casa:
        imovel = configurar_casa()
    else:
        imovel = configurar_estudio()

    opcoes_validas_parcelas = {'1', '2', '3', '4', '5'}
    texto_quantidade_parcelas = 'Digite a quantidade de vezes que deseja parcelar o valor do contrato (R$2000), sendo possível parcelar até 5 vezes.'
    quantidade_parcelas = int(selecionar_opcao(texto_quantidade_parcelas, opcoes_validas_parcelas))

    contrato = Contrato(imovel, parcelas=quantidade_parcelas)

    gerar_csv_orcamento(contrato)

      

def selecionar_opcao(texto_opcoes: str, opcoes: set) -> str:
    print(texto_opcoes)
    opcao = ''
    while True:
        opcao = input('Digite uma opção: ')
        if opcao in opcoes:
            break
        print('Opção inválida!\n')
    return opcao



def configurar_apartamento() -> Apartamento:
    quantidade_quartos = calcular_quantidade_quartos()
    quantidade_garagem = calcular_quantidade_vagas_garagem()
    usuario_possui_criancas = possui_criancas()
    return Apartamento(quantidade_quartos, quantidade_garagem, usuario_possui_criancas)
        


def configurar_casa() -> Casa:
    quantidade_quartos = calcular_quantidade_quartos()
    quantidade_garagem = calcular_quantidade_vagas_garagem()
    return Casa(quantidade_quartos, quantidade_garagem)


def configurar_estudio() -> Estudio:
    quantidade_vagas = calcular_quantidade_vagas_estacionamento()
    return Estudio(quantidade_vagas)


def calcular_quantidade_quartos() -> int:
    while True:
        quantidade_quartos = input('Digite a quantidade de quartos que deseja no ímovel, sendo possívels ter entre 1 a 2 quartos, no momento: ')
        if quantidade_quartos.isdigit():
            quantidade_quartos = int(quantidade_quartos)
            if 1 <= quantidade_quartos <= 2:
                return quantidade_quartos
        print('Opção inválida!\n')



def calcular_quantidade_vagas_garagem() -> int:
    while True:
        quantidade_garagem = input('Digite a quantidade de vagas de garagem que deseja no ímovel, sendo possívels ter entre 0 a 1 garagem, no momento: ')
        if quantidade_garagem.isdigit():
            quantidade_garagem = int(quantidade_garagem)
            if 0 <= quantidade_garagem <= 1:
                return quantidade_garagem
        print('Opção inválida!\n')



def possui_criancas() -> bool:
    while True:
        possui_criancas_in = input('Possui criança, digite 1 para "Sim" ou 2 para "Não": ')
        if possui_criancas_in.isdigit():
            possui_criancas_in = int(possui_criancas_in)
            if 1 <= possui_criancas_in <= 2:
                return True if possui_criancas_in == 1 else False
        print('Opção inválida!\n')



def calcular_quantidade_vagas_estacionamento() -> int:
    while True:
        quantidade_estacionamento = input('Digite a quantidade de vagas de estacionamento que deseja no ímovel: ')
        if quantidade_estacionamento.isdigit():
            quantidade_estacionamento = int(quantidade_estacionamento)
            if quantidade_estacionamento > 0:
                return quantidade_estacionamento
        print('Opção inválida!\n')



def gerar_csv_orcamento(contrato: Contrato):
    with open(file='data/arquivo.csv', mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(['mes', 'valor_aluguel', 'parcela_contrato', 'total'])
        valores_alugueis_total = contrato.listar_valores_alugueis()
        valor_aluguel = contrato.imovel.calcular_valor_mensal()
        parcelas_contrato = contrato.listar_parcelas_contrato()
        for mes in range(1, 13):
            writer.writerow([mes, valor_aluguel, parcelas_contrato[mes-1], valores_alugueis_total[mes-1]])