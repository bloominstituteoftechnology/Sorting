def katiesort(books):
    empty = []
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for a in alpha:
        for b in books:
            if b[0].lower() == a:
                empty.append(b)
                books.remove(b)
    return empty


print(katiesort(['beer', 'galaxy', 'red', 'clear', 'science', 'math']))
