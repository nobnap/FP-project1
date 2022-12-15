""" Projeto 1
Este projeto tem como objetivo corrigir os erros existentes
numa base de dados corrompida.
"""


#Parte 1

def corrigir_palavra(palavra):
    
    """corrigir_palavra: cad. carateres -> cad. carateres
    
    Esta função recebe uma cadeia de carateres que representa uma palavra 
    corrompida e remove, caso existam, duas letras iguais consecutivas, uma
    maiúscula, e outra minúscula (Aa, por exemplo).
    
    Exemplo: "cCdatabasacCADde" -> "database"
    """
    
    palavra_lista = list(palavra)
    i = len(palavra_lista) - 1
    res = ""
    
    #Este ciclo while compara cada letra à letra anterior
    while i >= 0:
        if ord(palavra_lista[i]) == ord(palavra_lista[i - 1]) + 32:
            del palavra_lista[i - 1:i + 1]
            i = len(palavra_lista) - 1
        elif ord(palavra_lista[i]) == ord(palavra_lista[i - 1]) - 32:
            del palavra_lista[i - 1:i + 1]
            i = len(palavra_lista) - 1
        else:
            i -= 1
    
    for el in palavra_lista:
        res += el
    
    return res


def eh_anagrama(p1, p2):
    
    """eh_anagrama: cad. carateres x cad. carateres -> booleano
    
    Esta função recebe duas palavras em forma de cadeias de carateres e 
    compara-as, retornando True se forem anagramas uma da outra.
    
    Exemplo: "sala" x "laas" -> True
    """
    
    if len(p1) != len(p2) or len(p1) == 0:
        return False
    
    lista_p1 = lista_carateres(p1)
    lista_p2 = lista_carateres(p2)
    
    for el in lista_p1:
        if el not in lista_p2:
            return False
    
    return True


def corrigir_doc(doc):
    
    """corrigir_doc: cad. carateres -> cad. carateres
    
    Esta função recebe um documento corrompido em forma de cadeia de carateres
    e retorna o documento corrigido, recorrendo às funções corrigir_palavra e
    eh_anagrama, assim como à função auxiliar encontrar_palavras.
    """
    
    lista_doc = []
    res = ""
    remover = []
    
    if type(doc) != str:
        raise ValueError("corrigir_doc: argumento invalido")
    
    for i in range(len(doc)):
        if ord(doc[i]) not in range(97, 123) and ord(doc[i]) not in range(65, 91) and doc[i] != " ":
            raise ValueError("corrigir_doc: argumento invalido")
        if doc[0] == " ":
            raise ValueError("corrigir_doc: argumento invalido")
        if i != 0 and doc[i] == " " and doc[i] == doc[i-1]:
            raise ValueError("corrigir_doc: argumento invalido")
    
    doc = encontrar_palavras(doc)
    
    for el in doc:
        lista_doc += [corrigir_palavra(el)]
    
    #cria uma lista com palavras que são anagramas e diferentes entre si
    for i in range(len(lista_doc) - 1): 
        for j in range(i + 1, len(lista_doc)): 
            if lista_doc[i] not in remover and lista_doc[j] not in remover and \
               lista_doc[i].lower() != lista_doc[j].lower() and eh_anagrama(lista_doc[i], lista_doc[j]):
                remover += [lista_doc[j]]
    
    for i in range(len(lista_doc)):
        if lista_doc[i] not in remover:
            res += lista_doc[i] + " "
    
    #res é limitado para que o output não inclua um espaço após a última palavra
    return res[:len(res)-1]


#funções auxiliares
def encontrar_palavras(doc):
    
    """encontrar_palavras: cad. carateres -> lista
    
    Esta é uma função auxiliar que transforma um documento(frase) numa lista de 
    palavras. É utilizada na função corrigir_doc.
    """
    
    lista = []
    palavra = ""
    
    for i in range(len(doc)):
        if  doc[i] == " ":
            lista.append(palavra)
            palavra = ""
        elif i == len(doc) - 1:
            palavra += doc[i]
            lista.append(palavra)
        else:
            palavra += doc[i]
    
    return lista


def lista_carateres(arg):
    
    """lista_carateres: cad. carateres -> lista
    
    Esta é uma função auxiliar que recebe uma cadeia de carateres e devolve uma 
    lista com tuplos constituidos por cada letra da cadeia e o número de vezes 
    que a mesma se repete. É utilizada nas funções eh_anagrama e validar_cifra.
    
    Exemplo: "salA" -> [(1, "s"), (2, "a"), (1, "l")]
    """
    
    arg = list(arg)
    tamanho = len(arg) 
    cont = 1
    res = []
    letras_ante = ()
    
    #O .lower() foi utilizado para que a contagem inclua letras maiúsculas no mesmo
    #tuplo que a sua equivalente minúscula
    for i in range(tamanho):
        if arg[i] != "-" and arg[i].lower() not in letras_ante:
            for j in range(i+1, tamanho):
                if arg[i].lower() == arg[j].lower():
                    cont += 1
            res += [(cont, arg[i].lower())]
            letras_ante += (arg[i].lower(),)
            cont = 1
    
    return res


#Parte 2

def obter_posicao(letra, num):
    
    """obter_posicao: cad. carateres x inteiro -> inteiro
    
    Esta função começa numa posição(num) no pinpad e muda
    essa posição de acordo com a letra submetida.
    (E: esquerda, D: direita, C: cima, B: baixo)
    
    Exemplo: "D" x 1 -> 2
    """
    
    posicoes = (1,2,3,4,5,6,7,8,9)
    atual_tuplo = num-1
    atual = posicoes[atual_tuplo] 
    
    if letra == "D" and atual not in (3, 6, 9):
        atual = posicoes[atual_tuplo+1]
    
    if letra == "E" and atual not in (1, 4, 7):
        atual = posicoes[atual_tuplo-1]
    
    if letra == "B" and atual not in (7, 8, 9):
        atual = posicoes[atual_tuplo+3]  
    
    if letra == "C" and atual not in (1, 2, 3):
        atual = posicoes[atual_tuplo-3]   
    
    return atual


def obter_digito(cadeia, num):
    
    """obter_digito: cad. carateres x inteiro -> inteiro
    
    Esta função começa numa posição(num) no pinpad e muda
    essa posição de acordo com a sequência de letras 
    submetida, recorrendo à função obter_posicao.
    
    Exemplo: "CEE" x 5 -> 1
    """
    
    for i in range(len(cadeia)):
        num = obter_posicao(cadeia[i], num)
    
    return num


def obter_pin(tuplo):
    
    """obter_pin: tuplo -> tuplo
    
    Esta função recebe um tuplo contendo cadeias de carateres e devolve o código
    correspondente ao movimento da posição no pinpad de acordo com as regras
    utilizadas nas funções obter_posicao e obter_digito.
    """
    
    if type(tuplo) != tuple or len(tuplo) < 4 or len(tuplo) > 10:
        raise ValueError("obter_pin: argumento invalido")
    
    for el in tuplo:
        if len(el) < 1:
            raise ValueError("obter_pin: argumento invalido")
        for letra in el:
            if letra not in ("C","B","E","D"):
                raise ValueError("obter_pin: argumento invalido")
    
    result_tuplo = (obter_digito(tuplo[0], 5),)
    
    for i in range(1, len(tuplo)):
        posicao = result_tuplo[i-1]
        result_tuplo += (obter_digito(tuplo[i], posicao),)
    
    return result_tuplo


#Parte 3

def eh_entrada(arg):
    
    """eh_entrada: universal -> booleano
    
    Esta função recebe um argumento e devolve True ou False dependendo se esse
    argumento é uma entrada válida.
    """
    
    if type(arg) != tuple or len(arg) != 3:
        return False
    
    if type(arg[0]) != str:
        return False
    
    for i in arg[0]:
        if ord(i) not in range(97, 123) and ord(i) != 45:
            return False
        
    if arg[0][0] == "-":
        return False
    
    if type(arg[1]) != str or len(arg[1]) != 7:
        return False
    
    if arg[1][0] != "[" or arg[1][6] != "]":
        return False
    
    for i in range(1, len(arg[1])-1):
        if ord(arg[1][i]) not in range(97, 123):
            return False 
        
    if type(arg[2]) != tuple or len(arg[2]) < 2:
        return False
    
    for i in arg[2]:
        if type(i) != int or i <= 0:
            return False
    
    return True


def validar_cifra(cifra, checksum):
    
    """validar_cifra: cad. carateres x cad. carateres -> booleano
    
    Esta função recebe uma cifra e uma sequência de segurança com os
    5 carateres mais comuns da cifra e devolve True se a sequência for coerente
    com a cifra.
    """
    
    tamanho = len(cifra)
    cont = 1
    letras_ante = ()
    compara = lista_carateres(cifra)
    check_real = ""
    
    #Este ciclo for ordena os carateres obtidos em lista_carateres por ordem 
    #decrescente de ocorrência e, para aqueles que têm número igual de ocorrências, 
    #ordem alfabética
    for i in range(len(compara)):
        for j in range(i+1, len(compara)):
            if compara[i][0]<compara[j][0]:
                compara[i],compara[j]=compara[j],compara[i]
            if compara[i][0]==compara[j][0]:
                if compara[i][1]>compara[j][1]:
                    compara[i],compara[j]=compara[j],compara[i]
    
    for k in range(0,5):
        check_real += compara[k][1]
    
    return check_real == checksum[1:6]


def filtrar_bdb(lista):
    
    """filtrar_bdb: lista -> lista
    
    Esta função recebe uma lista com entradas e devolve uma lista das entradas
    que não são válidas de acordo com a função validar_cifra.
    """
    
    res = []
    
    if type(lista) != list or len(lista) < 1:
        raise ValueError("filtrar_bdb: argumento invalido")
    
    for i in range(len(lista)):
        if not eh_entrada(lista[i]):
            raise ValueError("filtrar_bdb: argumento invalido")
        if not validar_cifra(lista[i][0],lista[i][1]):
            res += [lista[i]]
    
    return res


#Parte 4

def obter_num_seguranca(tuplo):
    
    """obter_num_seguranca: tuplo -> inteiro
    
    Esta função recebe um tuplo contendo vários números e devolve a menor 
    diferença entre 2 números possível utilizando aqueles presentes no tuplo.
    """
    
    tamanho = len(tuplo)
    dif = ()
    
    for i in range(tamanho):
        for j in range(i+1,tamanho):
            dif += (abs(tuplo[i]-tuplo[j]),)
    
    return min(dif)


def decifrar_texto(cifra, num):
    
    """decifrar_texto: cad. carateres x inteiro -> cad. carateres
    
    Esta função recebe uma cifra e o número obtido na função obter_num_segurança
    e descodifica a cifra utilizando o mesmo.
    """
    
    letra = [chr(i) for i in range(97, 123)]
    num = num%26
    res = ""
    
    for i in range(len(cifra)):
        if cifra[i] == "-":
            res += " "
        else:
            i_letras = ord(cifra[i])-97
            inc = num + (-1)**i
            dif = 26 - i_letras 
            if inc >= dif:
                res += letra[inc-dif]
            else:
                res += letra[i_letras+inc]
    
    return res


def decifrar_bdb(lista):
    
    """decifrar_bdb: lista -> lista
    
    Esta função recebe uma lista de entradas e devolve essas entradas decifradas.
    """
    
    res = []
    
    if type(lista) != list or len(lista) < 1:
        raise ValueError("decifrar_bdb: argumento invalido")
    
    for i in lista:
        if not eh_entrada(i):
            raise ValueError("decifrar_bdb: argumento invalido")
        res += [decifrar_texto(i[0], obter_num_seguranca(i[2]))]
    
    return res


#Parte 5

def eh_utilizador(x):
    
    """eh_utilizador: universal -> booleano
    
    Esta função recebe um argumento e devolve True se este for válido.
    """
    
    return type(x) == dict and len(x) == 3 and type(x["name"]) == str and\
           len(x["name"]) >= 1 and type(x["pass"]) == str and len(x["pass"]) >= 1 and\
           type(x["rule"]) == dict and len(x["rule"]) == 2 and\
           type(x["rule"]["vals"]) == tuple and len(x["rule"]["vals"]) == 2 and\
           type(x["rule"]["char"]) == str and len(x["rule"]["char"]) == 1 and\
           x["rule"]["vals"][0] <= x["rule"]["vals"][1] and\
           x["rule"]["vals"][0] > 0 and x["rule"]["vals"][1] > 0


def eh_senha_valida(ppass, rule):
    
    """eh_senha_valida: cad. carateres x dicionário -> booleano
    
    Esta função recebe uma senha e um dicionário com as suas regras de criação e
    devolve True se a senha seguir as regras gerais e as regras de criação.
    
    Regras Gerais: 
     - A senha deve conter pelo menos 3 vogais
     - A senha deve conter um carater que se repita duas vezes seguidas
    Regras de Criação:
     - A senha deve conter a letra que aparece no dicionário após "char".
     - Essa letra deve aparecer um número de vezes  x pertencente ao intervalo 
    [a, b] que se encontra após "vals" sob a forma de tuplo(a, b).
    """
    
    cont_char = 0
    cont_vog = 0
    duas_seguidas = False
    vogais = ("a","e","i","o","u")
    
    for i in range(len(ppass)):
        if ppass[i] in vogais:
            cont_vog += 1
        if ppass[i] == rule["char"]:
            cont_char += 1
        if i != 0 and ppass[i]==ppass[i-1]:
            duas_seguidas = True
    
    return cont_char >= rule["vals"][0] and cont_char <= rule["vals"][1] \
           and cont_vog >= 3 and duas_seguidas


def filtrar_senhas(lista):
    
    """filtrar_senhas: lista -> lista
    
    Esta função recebe uma lista de dicionários com utilizadores e devolve uma 
    lista com o nome dos utilizadores com senhas inválidas.
    """
    
    res = []
    
    if type(lista) != list or len(lista) < 1:
        raise ValueError("filtrar_senhas: argumento invalido")
    
    for i in range(len(lista)):
        if not eh_utilizador(lista[i]):
            raise ValueError("filtrar_senhas: argumento invalido")
        if not eh_senha_valida(lista[i]["pass"],lista[i]["rule"]):
            res += [lista[i]["name"]]
    
    return sorted(res)