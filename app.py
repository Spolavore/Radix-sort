def radix_sort_msd(strings):
    max_length = len(max(strings, key=len))
    return msd_sort(strings, 0, max_length)


def msd_sort(strings, start, length):
    if start >= length:
        return strings

    buckets = [[] for _ in range(27)]  # Usamos 27 para incluir caracteres não alfabéticos

    for string in strings:
        if start < len(string):
            char_index = ord(string[start]) - 65
        else:
            char_index = 0

        buckets[char_index].append(string)

    sorted_strings = []
    for bucket in buckets:
        if bucket:
            sorted_strings.extend(msd_sort(bucket, start + 1, length))

    return sorted_strings

# funcao para contar a frequencia de cada palavra
def countWords(arr):
    hash = {}
    for i in range(0, len(arr)):
        if arr[i] in hash:
            hash[arr[i]] += 1
        else:
            hash[arr[i]] = 1

    return hash
    

if __name__ == '__main__':
    fileToRead = int(input('Insira o arquivo que deseja ordenar:\n(1) Frankestein (2) War and Peace:'))
    output = 0

    if(fileToRead == 1):  
      with open('frankestein.txt', 'r') as file:
          res = file.read()
          res = res.split(' ')
          output = radix_sort_msd(res) 
          rankedWords = countWords(output)
          rankedWordsOrr = sorted(rankedWords.items(), key=lambda x:x[1], reverse=True)

      # Cria e escreve as palavras ordenadas
      with open('frankenstein_sorted.txt', 'w') as file:
          for i in range(0, len(output)):
              file.write(f'{output[i]}\n')

      # Cria e escreve o outPut das frequencia das palavras ordenadas
      with open('frankenstein_counted.txt', 'w') as file:
            chaves = list(rankedWords.keys())
            for i in range(0, len(chaves)):
                file.write(f'{chaves[i]} {rankedWords[chaves[i]]}\n')

      # Cria e escreve o frankestein_ranked
      with open('frankenstein_ranked.txt', 'w') as file:
  
            for i in range(0, 1000):
                file.write(f'{rankedWordsOrr[i][0]} {rankedWordsOrr[i][1]}\n')

    elif(fileToRead == 2):
      with open('war_and_peace.txt', 'r') as file:
        res = file.read()
        res = res.split(' ')
        output = radix_sort_msd(res)
        rankedWords = countWords(output)
        rankedWordsOrr = sorted(rankedWords.items(), key=lambda x:x[1], reverse=True)

      # Cria e escreve as palavras ordenadas
      with open('war_and_peace_sorted.txt', 'w') as file:
          for i in range(0, len(output)):
              file.write(f'{output[i]}\n')    

      # Cria e escreve o outPut das frequencia das palavras ordenadas
      with open('war_and_peace_counted.txt', 'w') as file:
            chaves = list(rankedWords.keys())
            for i in range(0, len(chaves)):
                file.write(f'{chaves[i]} {rankedWords[chaves[i]]}\n')
      # Cria e escreve o war_and_peace_ranked.txt
      with open('war_and_peace_ranked.txt', 'w') as file:
            for i in range(0, 1000):
                file.write(f'{rankedWordsOrr[i][0]} {rankedWordsOrr[i][1]}\n')

    else:
        print('Comando indiposnível')

    