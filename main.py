# Program to sort words

def sort_list(thy_list):
    for i in range(len(thy_list[1]) - 1, 0, -1):
        for j in range(i):
            if thy_list[1][j] < thy_list[1][j+1]:
                temp = thy_list[1][j]
                thy_list[1][j] = thy_list[1][j+1]
                thy_list[1][j+1] = temp

                temp = thy_list[0][j]
                thy_list[0][j] = thy_list[0][j + 1]
                thy_list[0][j + 1] = temp
    return thy_list



with open("all_words.txt", "r",  encoding='utf-8') as f:

    f_contet = f.read().split()

word_in_list =[]
num_for_word =[]


with open("svenska-ord.txt", "r",encoding='utf-8') as fSAOL:
    words_SAOL = fSAOL.read().split()

for word in f_contet:
    stripped_word = word.strip()
    if stripped_word in word_in_list:
        index = word_in_list.index(stripped_word)
        num_for_word[index] = num_for_word[index] + 1


    else:

        word_in_list.append(stripped_word.lower())
        num_for_word.append(1)
list_with_num = [word_in_list, num_for_word]

list_with_num = sort_list(list_with_num)


with open ("word_list_swe.txt", "w",  encoding='utf-8') as f_done:
   for i in range(len(list_with_num[0])):
       if list_with_num [0][i] in words_SAOL:
        f_done.write("Nr{}  Frec: {} Word: {} \n".format(i+1, list_with_num[1][i], list_with_num[0][i]))