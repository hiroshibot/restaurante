from modelos.restaurante import Restaurante

from modelos.cardapio.bebida import Bebida

from modelos.cardapio.item_cardapio import ItemCardapio

from modelos.avaliacao import Avaliacao

Restaurante("Japa Food", "Japonesa")
Restaurante("Burger King", "Fast Food")
Restaurante("Pizza House", "Italiana")

print("Eu Canibal como 18 paçocas na janta")
print("e homens")a

Restaurante.listar_restaurantes()
def menu():
    while True:
        print('''Bem-Vindo ao Restaurnate!
        (1- Adicionar Restaurante
        (2- Adicionar um novo item ao cardápio
        (3- Adicionar avaliação
        (4-Listar restaurantes
        (5- Mostrar cardápio
        (6-Mudar estado
        (7- Sair
    ''')
        escolha=input('Escolha um a opção:')
        if escolha=='1':
            nome_restaurante=input('Digite o nome do seu Restaurante:')
            qual_categoria=input('Digite a categoria do Restaurante:')
            Restaurante(nome_restaurante, qual_categoria)
        
        
        if escolha=='2':
            restaurante_nome=input('Qual o nome do restaurante:')
            for p in Restaurante.restaurantes:
               if p.nome==restaurante_nome:
                   item=input('Nome do item:')
                   descricao=input('Descricao item:')
                   preco=float(input('preco item'))
                   item=ItemCardapio(item,descricao,preco)
                   p.adicionar_carpadio(item)
                   print('item add com suceso')
                   break
            else:
                print('restaurante n foi achado')
                   
               
           
            
        elif escolha=='3':
            avaliar_restaurante=input('Fale o nome do Restaurante que deseja adicionar a avaliação:')
            
            for i in Restaurante.restaurantes:
                if i.nome ==  avaliar_restaurante:
                    cliente = input('Nome do cliente : ')
                    nota = int(input('Nota (0-5):'))
                    i.receber_avaliacao(cliente,nota) 
                    
                    
        elif escolha=='4':
            print('Aqui está a lista de nossos Restaurantes:')
            Restaurante.listar_restaurantes()
            
            
        elif escolha=='5':
            nome_do_restaurante=input('Qual restaurante você deseja ver cardapio:')
            for w in Restaurante.restaurantes:
                if w.nome==nome_do_restaurante:
                    w.exibir_cardapio()
                    break
            else:
                print('Restaurante nao encontrado')
                          
        elif escolha=='6':
            mudar_estado=input('Digite o nome do Restaurante que você deseja mudar o esotado:')
            for restaurante in Restaurante.restaurantes:
                if restaurante.nome==mudar_estado.title():
                    restaurante.trocar_estado()
                    print('Estado alterado kaceta')
                    break
                
        elif escolha=='7':
            print('Fechando...')
            break
            
            
            
            
        
menu()
