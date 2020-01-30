from book import Book
import time
import csv
​
def insertion_sort(books):
    # TO-DO: implement insertion sort
​
    return books
​
​
# Version A: Conventional, recursive Quick Sort
def quick_sort_A( books, low, high ):
    # TO-DO: implement Quick Sort
​
    return books
​
​
# Version B:
# NOT done in place because for large inputs, we
# exceed Python's maximum recursion depth with 
# in-place Quick Sort
def quick_sort_B( books ):
    # STRETCH: implement Quick Sort for larger datasets
​
    return books
​
​
def book_sort(books):
    # STRETCH: combine Insertion & Quick Sort for
    # an improved sorting algorithm
    
    return books
​
# Read in book data from CSV file
# provided by https://github.com/uchidalab/book-dataset
with open('book_data.csv', encoding='utf8') as csvfile:
    my_books_long = []
    data = csv.DictReader(csvfile)
    for book in data:
        #print(book['title'], book['author'], book['genre'])
        my_books_long.append(Book(book['title'], book['author'], book['genre']))
    my_books_medium = my_books_long[0:997]
    my_books_short = my_books_long[0:10]
​
print("***********~Test with 10 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_short)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")
​
# start = time.time()
# sorted_books = quick_sort_A(my_books_short, 0, len(my_books_short))
# end = time.time()
# print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")
​
​
print("\n***********~Test with ~1,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_medium)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")
​
# start = time.time()
# sorted_books = quick_sort_A(my_books_medium, 0, len(my_books_medium))
# end = time.time()
# print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")
​
​
print("\n**********~Test with +2,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_long)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")
​
# start = time.time()
# sorted_books = quick_sort_B(my_books_long)
# end = time.time()
# print("Quick Sort (B) took:  " + str((end - start)*1000) + " milliseconds")
​
# start = time.time()
# sorted_books = book_sort(my_books_long)
# end = time.time()
# print("Book Sort took:       " + str((end - start)*1000) + " milliseconds\n")