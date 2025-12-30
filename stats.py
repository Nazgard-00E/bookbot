def get_num_words(text):
    return len(text)

def get_character_count(text):
    final_result = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in final_result:
            final_result[char] += 1
        else:
            final_result[char] = 1
    return final_result

def sorted_character_count(text):
    char_count = get_character_count(text)
    char_list = list(char_count.items())
    char_list.sort(key=lambda x: x[1], reverse=True)
    char_list_dict = dict(char_list)
    return char_list_dict
    