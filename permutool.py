#loads .txt file containing all english words into main memory
def build_dictionary():
    dictionary_file = open("all_words.txt")
    return set(dictionary_file.read().split())

def permutations(string, all_perms, step = 0):
    # base case
    if step == len(string):
        all_perms.add("".join(string))

    # postfix of the string hasn't been permuted
    for i in range(step, len(string)):
        # make a copy of the str
        copy = [character for character in string]
        # swap the current index with the step
        copy[step], copy[i] = copy[i], copy[step]
        # recurse over the postfix of the string that hasn't been permuted
        permutations(copy, all_perms, step + 1)

# driver
if __name__ == '__main__':
    english_dictionary = build_dictionary()
    while True:
        user_str = input("Enter String to permute (or 1 to exit): ")
        try: 
            if int(user_str) == 1 : break
        except ValueError:
            print("running...")
        all_unique_permutations = set()
        permutations(user_str, all_unique_permutations) 
        for x in all_unique_permutations:
            if x in english_dictionary:
                print(x)
