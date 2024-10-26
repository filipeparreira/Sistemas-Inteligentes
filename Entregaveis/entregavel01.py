class Estado:
    def __init__(self, nome, pai, filhos):
        self.nome = nome
        self.pai = pai
        self.filhos = filhos
    
    def get_filhos(self):
        return self.filhos
    
    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return self.__str__()

def objetivo(estado_corrente, inicial, lista_estados):
    if estado_corrente.nome == inicial.nome and len(lista_estados) > 2:
        print("Entrou no if dentro de objetivo")
        return True
    else:
        return False
    
def busca_retrocesso(grafo, inicial):
    # Inicialização das listas
    LE = [inicial]  # Lista de estados no caminho atual
    LNE = [inicial]  # Lista de novos estados
    BSS = []  # Lista de becos sem saída
    EC = inicial  # Estado corrente / atual
    executado = False
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
              BSS.insert(0, EC) # Acrescenta EC em BSS;
              LE.pop(0)  # Remove o primeiro elemento de LE
              LNE.pop(0)  # Remove o primeiro elemento de LNE
              EC = LNE[0]
              LE.insert(0, EC) # Acrescenta EC em LE;
        else:
            print('Entrou no ELSE')
            # Verifica se os filhos do EC estão em LE, BSS ou em LNE
            #   se estiver não adiciona a LNE
            for filho in EC.get_filhos():
                if filho not in LE and filho not in LNE and filho not in BSS:
                    LNE.insert(0, filho)
            
            
            if not executado:
                # Transformo todos os estados em classes 
                LNE_aux = list()           
                for estado in LNE:
                    LNE_aux.append(Estado(str(estado), EC, grafo[str(estado)]))
                LNE = LNE_aux 
                    
            print(f"Lista LNE: {LNE}")
            EC = LNE.pop(0)
            print(f"Lista LNE1: {LNE}")
            LE.insert(0, EC)
            
    return "Falha"

A = Estado('A', None, None)
B = Estado('B', None, None)
C = Estado('C', None, None)
D = Estado('D', None, None)
E = Estado('E', None, [D, C, B, A])
A.filhos = [B, C, D, E]
B.filhos = [A, C, D, E]
C.filhos = [B, A, E, D]
D.filhos = [C, B, A, E]


for filho in E.filhos:
    print(f'Filho de E: {filho} || Filhos de {filho}: {filho.filhos}')
    

grafo_lista = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['B', 'A', 'E', 'D'],
    'D': ['C', 'B', 'A', 'E'],
    'E': ['D', 'C', 'B', 'A']
}

# Teste de lógica
inicial = Estado('A', None, grafo_lista['A'])

#busca_retrocesso(grafo_lista, inicial)