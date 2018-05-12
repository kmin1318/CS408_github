def process_line(words, word_dict):
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

def word_count(filename, max_to_min=False):
    with open(filename, "rU") as f:
        word_dict = {}
        for line in f:
            if line.replace(" ", "") != ("\n" or None):
                process_line(filter(None, split("[^a-zA-Z']+", line.lower())), word_dict)

    final_list = process_dict(word_dict)
    format_print(final_list, max_to_min, len(word_dict))