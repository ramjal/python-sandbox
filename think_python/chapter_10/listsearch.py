
# Search for a word in a sorted list
def search_in_list(thelist, word):
    if len(thelist) == 0:
        return False
    if len(thelist) == 1:
        if word == thelist[0]:
            return True
        else:
            return False

    mid = len(thelist) // 2
    if word >= thelist[mid]:
        thelist = thelist[mid:]
    else:
        thelist = thelist[:mid]

    return search_in_list(thelist, word)
