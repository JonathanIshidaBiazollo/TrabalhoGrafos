#Ex01 - Lista de Adjacência
#Obs: Os vértices não podem repetir,
#porém as arestas sim, considerando que o usuário possa querer criar arestas múltiplas em um multigrafo
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Cria um grafo vazio para ser alimentado pelas outras funções
def criarGrafo():
  grafo = {}
  return grafo

#Função para imprimir o grafo de forma mais estética, pulando linha e criando uma linha de separação antes e depois
def imprimirGrafo(grafo):
  print("-"*40)
  for vertice in grafo:
    print(vertice, ": ", grafo[vertice])
  print("-"*40)

#Inserir Vértice(Igual para ambos):
def inserirVertice(grafo, vertice):
  if vertice not in grafo:
    grafo[vertice] =  []

#Inserir Aresta
#Funciona para ambos
def inserirAresta(grafo, origem, destino, direcionado):
  if origem not in grafo:
    inserirVertice(grafo, origem)

  if destino not in grafo:
    inserirVertice(grafo, destino)

  if direcionado:
    grafo[origem].append(destino)
  else:
    grafo[origem].append(destino)

    if origem != destino:#isso evita que em grafo NÂO direcionado se eu colocar um laço, origem: A, destino: A, apareça na lista 2 vezes o mesmo vértice
      grafo[destino].append(origem)

#Remover Vértice(Igual para ambos)
def removerVertice(grafo, vertice):
  if vertice in grafo:
    for v in grafo:
      while vertice in grafo[v]:#percorre todo o grafo verificando se existe esse vértice no grafo
        grafo[v].remove(vertice)#remove o vértice da lista de adjacência, todas as suas referÊncias
    del grafo[vertice]#remove o vértice do grafo
  else:
    print(f"{vertice} NÂO existe nesse grafo, tente novamente")

#Remover Arestas, funciona para ambos
def removerAresta(grafo, origem, destino, direcionado):
  if origem not in grafo or destino not in grafo:
    print("Verifique os vértices, pois 1 ou ambos não existem neste grafo")
    return
  if origem in grafo and destino in grafo and direcionado:#verifico se os 2 vértices existem
    while destino in grafo[origem]:#agora verifico se a aresta entre esses 2 vértices existe e retiro ela mesmo que apareça 2,3 ou mais vezes, já que arestas múltiplas podem existir, se não pudessem existir, trocaria simplesmente o while por if
      grafo[origem].remove(destino)
  else:
    while destino in grafo[origem] and origem in grafo[destino]:# a ideia é a mesma do direcionado, porém como no NÂO direcionado eu preciso tirar em ambos os vértices é necessário fazer essa verificação tanto na orighem quanto no destino
      grafo[origem].remove(destino)
      grafo[destino].remove(origem)

#Calcular grau de cada vértice, Grafo NÂO DIRECIONADO
def calcularGrauVerticeNaoDirecionado(grafo):
  print("="*40)
  print("Lista de graus de cada vértice do grafo NÂO DIRECIONADO:")
  print("="*40)
  for v in grafo:
    grau = len(grafo[v]) + grafo[v].count(v)
          #tamanho do vértice + 1 se tiver laços
    print(f"{v}: {grau}")

#Calcular grau de cada vértice, Grafo DIRECIONADO
def calcularGrauVerticeDirecionado(grafo):
  print("="*40)
  print("Lista de graus de cada vértice do grafo DIRECIONADO:")
  print("="*40)
  for v in grafo:
    entrada = 0
    saida = len(grafo[v])#o grau de saída é sempre o tamanho de cada vértice

    for vertice in grafo:
      if v in grafo[vertice]:
        entrada += grafo[vertice].count(v)#conta todas as vezes que a aresta aparece, mesmo que repetida
    print(f"{v}")
    print(f"Entrada: {entrada}")
    print(f"Saída: {saida}")
    print(f"Total: {entrada + saida}")
    print("-"*20)

#Verificar se existe uma aresta que vai de um vértice para outro
#Serve tanto para grafos direcionados e não direcionados
def verificaArestaExistente(grafo, origem, destino):
  if origem in grafo and destino in grafo:#verifico se existem os vértices
    if destino in grafo[origem]: #e se existe uma aresta que os conecta
      return True
  return False

def listarVizinhosVertice(grafo, vertice):
  if vertice in grafo:
    print("-"*40)
    print(f"Lista de adjacência de {vertice}: ")
    if not grafo[vertice]:
      print(f"{vertice} NÃO possuí vizinhos")
    else:
      for v in grafo[vertice]:
        print(v)
  else:
    print("Vértice não encontrado")

# Verificar se um percurso é válido
# Funciona para grafos direcionados e não direcionados
def verificarPercurso(grafo, percurso):
  if not percurso:
    print("Nenhum vértice informado, tente de novo")
    return False

  for vertice in percurso:
    if vertice not in grafo:
      print("Existem vértices informados que não existem no grafo, tente noavamente")
      return False

  for i in range(len(percurso) - 1):
      origem = percurso[i]
      destino = percurso[i + 1]

      if not verificaArestaExistente(grafo, origem, destino):
          return False

  return True

#Menu do programa
def menu():
  grafo = criarGrafo()

  while True:
    print("="*40)
    print("Qual o tipo de Grafo que você deseja?")
    print("0 - Sair")
    print("1 - Direcionado")
    print("2 - Não Direcionado")
    print("="*40)
    op = input()
    match op:
      case "0":
        print("Sistema Finalizado")
        return
      case "1":
        direcionado = True
        break
      case "2":
        direcionado = False
        break
      case _:
        limpar_tela()
        print("Opção inválida, tente novamente")

  while True:
    print("="*40)
    print(" "*15, "Menu")
    print("="*40)
    print("0 - Sair")
    print("1 - Mostrar o Grafo")
    print("2 - Inserir Vértice")
    print("3 - Inserir Aresta")
    print("4 - Remover Vértice")
    print("5 - Remover Aresta")
    print("6 - Exibir grau de cada vértice")
    print("7 - Verificar aresta existente")
    print("8 - Listar todos os vizinhos de um vértice")
    print("9 - Verificar percurso")

    opcao = input("Digite uma opção: ")

    match opcao:
      case "0":
        limpar_tela()
        print("Sistema de grafos finalizado...")
        break
      case "1":
        limpar_tela()
        imprimirGrafo(grafo)#Como foi criada uma função pra deixar mais bonitinho a apresentação do grafo é melhor usar essa função do que só chamar o grafo
      case "2":
        limpar_tela()
        vertice = input("Vértice a ser inserido: ").upper()
        inserirVertice(grafo, vertice)
        imprimirGrafo(grafo)
      case "3":
        limpar_tela()
        origem = input("Vértice Origem da aresta: ").upper()
        destino = input("Vértice Destino da aresta: ").upper()
        inserirAresta(grafo, origem, destino, direcionado)
        imprimirGrafo(grafo)
      case "4":
        limpar_tela()
        vertice = input("Vértice a ser removido: ").upper()
        removerVertice(grafo, vertice)
        imprimirGrafo(grafo)
      case "5":
        limpar_tela()
        origem = input("Vértice Origem da aresta: ").upper()
        destino = input("Vértice Destino da aresta: ").upper()
        removerAresta(grafo, origem, destino, direcionado)
        imprimirGrafo(grafo)
      case "6":
        limpar_tela()
        imprimirGrafo(grafo)
        if direcionado:
          calcularGrauVerticeDirecionado(grafo)
        else:
          calcularGrauVerticeNaoDirecionado(grafo)
      case "7":
        limpar_tela()
        origem = input("Vértice Origem da aresta: ").upper()
        destino = input("Vértice Destino da aresta: ").upper()
        existente = verificaArestaExistente(grafo, origem, destino)
        if existente:
          print(f"{origem} -> {destino} existe")
        else:
          print(f"{origem} -> {destino} NÂO existe")
      case "8":
        limpar_tela()
        vertice = input("Vértice a ser consultado: ").upper()
        listarVizinhosVertice(grafo, vertice)
      case "9":
        limpar_tela()
        print("Exemplo de percurso: a b c")
        print("Exemplo de percurso: A b C")
        percurso = input("Digite o percurso desejado separando cada vértice por espaço: ").upper().split()
        print(" -> ".join(percurso))
        existePercurso = verificarPercurso(grafo, percurso)
        if existePercurso:
          print("Percurso VÁLIDO")
        else:
          print("Percurso INVÁLIDO")
      case _:
        limpar_tela()
        print("Opção inválida, tente novamente")

menu()