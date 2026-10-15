empty_list = []
print()

numbers = [1, 2, 3, 4, 5]
print(numbers)

triples = [1, 2, 3] * 3
print(triples)

aList = [200, 600, 400, 500, 300]
aList = aList[::-1]
print(aList, "\n")

print("------------------------------------------------------------------------------------------")

def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word [0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of words with first and last character same\n", lst)
    return ctr

count = match_words(['aba', 'cfb', 'xyx', '414', '1223'])
print("Number of words containing the first and last character same: ", count)

print("------------------------------------------------------------------------------------------")

L = [10, 6, 2, 3, 5, 4, 9, 8]
print("Original List: ", L)

count = 0

for b in L:
    count += b

    avg = count/len(L)

    print("Sum = ", count)
    print("Average = ", avg)

    L.sort()

    print("Tiniest element is: ", L[0])
    print("Biggest element is: ", L[-1])