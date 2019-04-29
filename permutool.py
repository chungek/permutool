#loads .txt file containing all english words into main memory
def build_dictionary():
    dictionary_file = open("all_words.txt")
    return set(dictionary_file.read().split())

# permutes a string
def permutations(str):
    runs_tracker = _set_up(str)
    output = []
    _permute(runs_tracker, "", len(str), output)
    return output

# helper function
def _permute(runs_tracker, permuted_segment, remainder, output):
    # base case
    if remainder == 0:
        output.append(permuted_segment)
        return
    # run on remaining chars that follow
    for curr_char in runs_tracker.keys(): 
        runs_left = runs_tracker[curr_char]
        if runs_left > 0:
            runs_tracker[curr_char] -= 1
            _permute(runs_tracker, permuted_segment + curr_char, remainder - 1, output)
            runs_tracker[curr_char] = runs_left 

# helper function
def _set_up(str):
    runs_tracker = {}
    for c in str:
        if c not in runs_tracker:
            runs_tracker[c] = 0
        runs_tracker[c] += 1
    return runs_tracker

# driver
if __name__ == '__main__':
    english_dictionary = build_dictionary()
    while True:
        user_str = input("Enter String to permute (or 1 to exit): ")
        try: 
            if int(user_str) == 1 : break
        except ValueError:
            print("running...")
        all_unique_permutations = permutations(user_str) 
        # append to list if a permutation passes the check
        valid_words = []
        for x in range(len(all_unique_permutations)):
            if all_unique_permutations[x] in english_dictionary:
                valid_words.append(all_unique_permutations[x])
        for y in range(len(valid_words)):
            print(valid_words[y])
