from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self.cardapio = []
        self.avaliacao = []
        self.estado=False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)}')
        for i in cls.restaurantes:
            print(f'{i.nome.ljust(25)} | {i.categoria.ljust(25)} | {i.media_avaliacao}')

    def receber_avaliacao(self, cliente, nota, ):
        avaliacao = Avaliacao(cliente, nota)
        self.avaliacao.append(avaliacao)
        if 0 > nota > 5:
            print('Nota inválida, Só da se for de 0-5.')
            return
        
        

    @property
    def media_avaliacao(self):
        if not self.avaliacao:
            return 0
        soma_das_notas = 0
        for i in self.avaliacao:
            soma_das_notas = soma_das_notas + i.nota
        quantidade_de_notas = len(self.avaliacao)
        media = soma_das_notas / quantidade_de_notas
        media = round(media,1)
        return media
    
    
    def adicionar_carpadio(self, item):
        if isinstance(item,ItemCardapio):
            self.cardapio.append(item)
            
    def exibir_cardapio(self):
        print('Olá! Aqui está nosso cardápio')
        print(f'{"Nome do item:" .ljust(20)} I {"Preço:" .ljust(20)} I  {"descrição:" .ljust(15)}' )
        for b in self.cardapio:
            print(f'{b.nome.ljust(20)} I RS{str(b.preco).ljust(20)} I {b.descricao.ljust(20)}')
        
""" FIM DA CLASSE """





