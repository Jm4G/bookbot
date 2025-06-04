def num_words(text):
     word = text.split()
     return len(word)

def char_num(text_string):
     letter_list = {}
     for letter in text_string:
          letter = letter.lower()
          
          if letter in letter_list:
               letter_list[letter] += 1

          else:
               letter_list[letter] = 1

     return letter_list


def sort_list(letter_count):
     dict_list = []

     for letter in letter_count:
          key = letter
          value = letter_count[key]
          new_dict = {"char": key, "num": value}
          dict_list.append(new_dict)

     dict_list.sort(reverse=True, key=sort_on)
     return dict_list


def sort_on(dict):
     return dict["num"]


def final_output(list):
    for dict in list:
        if dict["char"].isalpha():
             print(f"{dict["char"]}: {dict["num"]}")
    