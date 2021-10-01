def n_letter(my_string):
    sample_dictionary={}
    for word in my_string:
        words=len(word)
        if words in sample_dictionary:
            sample_dictionary[words].add(word)
        else:
            sample_dictionary[words] = {word}
    print(sample_dictionary)
    return sample_dictionary
n_letter(['Lorem', 'ele', 'sit', 'incididunt', 'a', 'su', 'dom', 'ouch', 'ipsum'])
