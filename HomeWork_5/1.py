from random import choices
def list_rand_words(count: int, alp: str = 'абв'):
    words_list = []
    if count<1:
      return "Error"
    for i in range(count):
        letters = choices(alp, k=3)
        words_list.append("".join(letters))
    return words_list
  
text=list_rand_words(int(input()))
def del_some_words(my_text):
    if 'Error' in my_text:
      return ''
    
    my_text = list(filter(lambda x: 'абв' not in x, my_text))
    return " ".join(my_text)

my_text = del_some_words(text)
print(text)


print(my_text)

