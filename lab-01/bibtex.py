def extractauthor(a):
    if "," in a:
        arr = a.split(",", 2)
        return (arr[0].strip(), arr[1].strip())
    else:
        arr = a.split(" ")
        return (arr[-1].strip(), "".join(arr[:-1]).strip())


def extractauthors(a):
    authors_list = []
    for author in a.split("and"):
        authors_list.append(extractauthor(author))
    return authors_list
