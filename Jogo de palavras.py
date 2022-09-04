# Leitura de arquivos .txt com a função integrada: open();
# atribuída à uma variável e devolve um 'objeto de arquivo'.
def separa_ae():
    print('-' * 150)


fin = open('words.txt')


def only_words_over_20chars(file_object):
    for line in file_object:  # <-- Loop for sendo usado para iterar o objeto de arquivo(fin) linha por linha.
        word = line.strip()  # <-- Método strip() sendo usado para conter os espaços redundantes.
        if len(word) > 20:  # <-- Imprimindo apenas as palavras com mais de 20 caracteres.
            print(word)


'''
Lembrando que a função len() lê os caracteres de uma string começando de 1, entao se você pegar alguma palavra da lista
e contar 20 caracteres(começando de 0), e usar um len(), ele irá contar 21 caracteres.
'''
print(len('counterdemonstrations'))  # <-- Dito e feito :3

separa_ae()  # <-- função que criei pra printar 150 hífens no console, pra ajudar na separação dos tópicos


def has_no_e(word):  # <-- função deve retornar True se não tiver a letra 'e' na string.
    if 'e' in word:
        return False
    return True


def has_no_e_in_list(file_object):
    count_characters = 0
    count_qtde_de_e = 0
    for line in file_object:  # <-- esse loop faz a contagem de caracteres de cada linha do meu arquivo de texto.
        size = len(line)-1  # <-- aqui uso o len() para contar a quantidade de caracteres de cada palavra.
        count_characters = count_characters + size  # <-- temos um contador que vai contar o total de caracteres.
        if 'e' in line:
            count_qtde_de_e += 1

    print(f'O total de caracteres da lista é {count_characters}!')
    print(f"O total de vezes que a letra 'e' aparece é: {count_qtde_de_e}!")
    media = round((count_qtde_de_e/count_characters)*100, 2)
    print(f"A letra 'e' está presente em {media}% de todo o objeto")


has_no_e_in_list(fin)
separa_ae()


def avoids(word, forbidden):  # < -- Função que recebe uma palavra e uma série de letras proibidas, caso a palavra tenha
    for letter in word:      # uma delas a função retorna False imediatamente.
        if letter in forbidden:
            return False
        return True


def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
        return True


def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
        return True


def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])


def puzzle(word):
    index = 0
    count = 0
    while index < len(word):
        print(word[index])
        if word[index] != word[index+1]:
            return False
        else:
            count = count + 1
            index = index + 2
    print(f'Totalizam-se {count} pares de letras iguais')
    return True

print(puzzle('aabbcc'))