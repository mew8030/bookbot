def get_num_words(words):
    print(f"----------- Word Count ----------")
    sum = 0
    for word in words.split():
        sum += 1
    return sum

def get_num_chars(book):
    letters = {}
    book = book.lower()
    for letter in book:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters
def sort_on(items):
    return items["num"]

def get_sorted(dic):
    task = []
    for k, value in dic.items():
        task.append({ "key" : k , "num" : value })
    task.sort(reverse=True, key=sort_on)
    return task

def print_analysis_of_book(lst):
    print(f"--------- Character Count -------")
    for item in lst:
        if item["key"].isalpha():
            print(f"{item["key"]}: {item["num"]}")
    print(f"============= END ===============")