class Estado:
    def __init__(self, nome, pai, filhos):
        self.nome = nome
        self.pai = pai
        self.filhos = filhos
    
    def get_filhos(self):
        return self.filhos
    
    def __str__(self):
        return self.nome

def objetivo(estado_corrente, inicial, lista_estados):
    if estado_corrente == inicial and len(lista_estados) > 2:
        return True
    else:
        return False
    
def busca_retrocesso(grafo, inicial):
    # Inicialização das listas
    LE = [inicial]  # Lista de estados no caminho atual
    LNE = [inicial]  # Lista de novos estados
    BSS = []  # Lista de becos sem saída
    EC = inicial  # Estado corrente / atual
    
    # Verifica se é um verticie final do "grafo"
    while LNE != []:
        print(f"\nEstado Corrente (EC): {EC}")
        print(f"Lista de Estados no Caminho (LE): {LE}")
        print(f"Lista de Novos Estados (LNE): {LNE}")
        print(f"Lista de Becos Sem Saída (BSS): {BSS}")

        # Se encontramos o objetivo, retornar o caminho
        if objetivo(EC, inicial, LE):
          return LE
        
        # O estado corrente não tem filhos quando LE == EC.filhos
        if set(LE) == set(EC.get_filhos()):
            while LE != [] and EC == LE[0]:  # Enquanto LE não estiver vazio e EC for o primeiro em LE
            # Marcar como beco sem saída
              BSS.append(EC) # Acrescenta EC em BSS;
              LE.pop(0)  # Remove o primeiro elemento de LE
              LNE.pop(0)  # Remove o primeiro elemento de LNE
              EC = LNE[0]
              LE.append(EC) # Acrescenta EC em LE;
        else:
            # Verifica se os filhos do EC estão em LE, BSS ou em LNE
            #   se estiver não adiciona a LNE
            for filho in EC.get_filhos():
                if filho not in LE and filho not in LNE and filho not in BSS:
                    LNE.append(filho)
            EC = LNE.pop(0)
            LE.append(EC)
    return "Falha"

grafo_lista = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['B', 'A', 'E', 'D'],
    'D': ['C', 'B', 'A', 'E'],
    'E': ['D', 'C', 'B', 'A']
}

# Teste de lógica
inicial = Estado('A', None, grafo_lista['A'])
busca_retrocesso(grafo_lista, inicial)