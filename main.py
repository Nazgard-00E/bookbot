def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        words_count = len(words)
        #return words_count
    number_characters = counting_characters(file_contents)
    character_filtered = aggregate(file_contents)
    character_sorted = sort_on(character_filtered)
    #print(character_sorted)
    print_outcome(words_count, character_sorted)
    
def counting_characters(input_string):
    character_counting = {}
    lowered_strings = input_string.lower()
    for character in lowered_strings:
        if character in character_counting: 
            character_counting[character]+= 1
        else:
            character_counting[character] = 1
    return character_counting

def aggregate(input_string):
    import string
    character_output = {}
    character_input = counting_characters(input_string)
    for character in string.ascii_lowercase:
        character_output[character] = character_input[character] 
    return character_output

def sort_on(character_to_filter):
    sorted_characters = dict(sorted(character_to_filter.items(), key=lambda item: item[1], reverse=True))
    return sorted_characters

def print_outcome(length, outcome):
    print("--- Begin report of books/frankenstein.txt ---")
    print(length," words found in the document\n")
    #print(outcome)
    
    for key, value in outcome.items():
        #print(outcome)
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

    
    
        

main()   