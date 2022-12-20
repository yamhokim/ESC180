# Problem 1
# open("text.txt", encoding="latin-1").read().split()
# a)
def word_counts(w):
    word_dict = {}
    filename = r"C:\Users\YamHo Jobs\PyZo Projects\Labs\Lab09\sampletext.txt"
    word_list = open(filename, encoding="latin-1").read().split()
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

# b)
def top10(L):
    '''Takes in a list of 100 integers and returns a list of the 10 largest integers in L.'''
    top_list = []
    for i in range(10):
        max = 0

        for i in range(len(L)):
            if L[i] > max:
                max = L[i]

        L.remove(L[i])
        top_list.append(L[i])

    return top_list

# c)

def freq_words():
    words = {}
    filename = r"C:\Users\YamHo Jobs\PyZo Projects\Labs\Lab09\prideandprejudice.txt"
    word_list = open(filename, encoding="latin-1").read().split()
    for word in word_list:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    inverted_words = {}
    for key, value in words.items():
        inverted_words[value] = key

    sorted_list = sorted(inverted_words.items())

    top_list = []
    for i in range(-1, -11, -1):
        top_list.append(sorted_list[i][1])

    return top_list

# Problem 2

# Problem 3
import urllib.request
def get_results(variant):
    address = "https://ca.search.yahoo.com/search?p="
    thing = urllib.parse.quote(variant)
    address += thing
    f = urllib.request.urlopen(address)
    page = f.read().decode("utf-8")
    f.close()
    for i in range(len(page)):
        if page[i] == "A" and page[i+1] == "b" and page[i+2] == "o" and page[i+3] == "u" and page[i+4] == "t":
            n = i+6
            results = ""
            while page[n].isdigit() or page[n] == ",":
                n += 1
                if page[n-1] == ",":
                    continue
                results += page[n-1]
            return results
    return

def choose_variants(variants):
    empty_list = []
    for variant in variants:
        value = int(get_results(variant))
        empty_list.append((variant, value))

    while len(empty_list) > 1:
        if empty_list[0][1] < empty_list[1][1]:
            del empty_list[0]
        elif empty_list[0][1] > empty_list[1][1]:
            del empty_list[1]

    return empty_list[0][0]

print(choose_variants(["five-year anniversary", "fifth anniversary"]))
print(choose_variants(["top ranked school uoft", "top ranked school waterloo"]))