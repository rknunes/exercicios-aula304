def rertonar_itens_estoque(setor, *args):
    print(f'Lista salva no estoque do setor: {setor}:')
    for item in args:
        print(item)

rertonar_itens_estoque('administrativo', 'docs A e Z', 'pastas', 'notes')   

def lista_de_compras(pessoa, **kwargs):
    fruta = kwargs.get('fruta')
    if fruta is not None:
        print(f'Na lista de compras da {pessoa} ha uma fruta: {fruta}')

lista_de_compras('jureg', fruta='abacate', massas='miojo', verdura='couve')
lista_de_compras('irmao do jorel', bebida='suco', sorvete='creme')    

