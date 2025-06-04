from stats import num_words
from stats import char_num
from stats import sort_list
from stats import final_output
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    else:
        book_text = get_book_text(sys.argv[1])
        
            

    #word_count = num_words(book_text)
    letter_num = char_num(book_text)
    sorted_list = sort_list(letter_num)
    


    print("========= BOOKBOT ==========")
    print("Analyzing book fount at books/...")
    #print("---------- Word Count ----------")
    #print(f"Found {word_count} total words")
    print("------- Character Count -------")
    final_output(sorted_list)
    print("========= END ==========")



def get_book_text (path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents    

main()