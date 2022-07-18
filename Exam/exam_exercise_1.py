def library(book_list, book_title):
    result = []
    for i in range(len(book_list)):
        if book_list[i].lower().count(book_title.lower()) > 0:
            result.append(book_list[i])

    return result

print(library(book_list = ["Harry Potter and the Philosopher's stone", "Harry Potter and the chamber of secrets","The adventures of Sherlock Holmes", "The Chamber"], 
book_title = "The chamber"))
