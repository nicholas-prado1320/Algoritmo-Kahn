# Aqui criei um grafo direcionado, representado por um dicionário
grafo = {
    "fundacao": ["paredes"], 
    "paredes": ["laje", "eletrica", "hidraulica"], # Aqui por exemplo, estou dizendo que para fazer a laje, eletrica e hidraulica, precisa fazer as paredes primeiro (paredes = chave e laje, eletrica e hidraulica = lista)
    "laje": ["telhado"], 
    "eletrica": ["reboco"], 
    "hidraulica": ["reboco"], 
    "reboco": ["pintura"], 
    "pintura": ["esquadrias"], 
    "esquadrias": ["acabamento"], 
    "telhado": [], 
    "acabamento": []
}

grau_entrada = {} # Aqui eu criei o grau de entrada vazio

for chaves in grafo: # Nesse primeiro for, eu fiz ele percorrer todas as chaves do grafo
    grau_entrada[chaves] = 0 # Inicializa cada grau de entrada com zero

for chaves in grafo: # Nesse segundo for, eu fiz ele percorrer todas as chaves novamente
    for lista in grafo[chaves]: # No terceiro, após ele percorrer todas as chaves, fiz ele percorrer as listas dentro de cada chave
        grau_entrada[lista] += 1 # Se tiver valor na lista ele soma 1 ao grau de entrada
print(grau_entrada) # Exibe os valores do grau de entrada

fila = []

for lista in grau_entrada: # Percorre todas as listas de atividades armazenadas no grau de entrada
    if grau_entrada[lista] == 0: # Verifica se a atividade atual possui grau de entrada igual a zero 
       fila.append(lista) # Se a condição for verdadeira, adiciona a atividade à fila
print(fila)

atividades = 0

# while atividades