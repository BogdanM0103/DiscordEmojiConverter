import sys

emojiDictionary = {
    "A": [':regional_indicator_a:', ':a:',':arrow_up_small:', '::'],
    "B": [':regional_indicator_b:', ':b:'],
    "C": [':regional_indicator_c:', ':star_and_crescent:'],
    "D": [':regional_indicator_d:', ':leftwards_arrow_with_hook:'],
    "E": [':regional_indicator_e:', ':email:'],
    "F": [':regional_indicator_f:', ':flags:'],
    "G": [':regional_indicator_g:'],
    "H": [':regional_indicator_h:'],
    "I": [':regional_indicator_i:', ':information:', ':clock1230:'],
    "J": [':regional_indicator_j:', ':japan:'],
    "K": [':regional_indicator_k:'],
    "L": [':regional_indicator_l:', ':clock3:'],
    "M": [':regional_indicator_m:', ':m:', ':part_alternation_mark:', ':scorpio:'],
    "N": [':regional_indicator_n:', ':capricorn:'],
    "O": [':regional_indicator_o:', ':o2:', ':o:', ':no_entry_sign:'],
    "P": [':regional_indicator_p:', ':parking:'],
    "Q": [':regional_indicator_q:'],
    "R": [':regional_indicator_r:'],
    "S": [':regional_indicator_s:'],
    "T": [':regional_indicator_t:', ':cross:', ':orthodox_cross:'],
    "U": [':regional_indicator_u:'],
    "V": [':regional_indicator_v:'],
    "W": [':regional_indicator_w:'],
    "X": [':regional_indicator_x:', ':x:', ':negative_squared_cross_mark:'],
    "Y": [':regional_indicator_y:'],
    "Z": [':regional_indicator_z:', ':zzz:'],
    "0": [':zero:'],
    "1": [':one:', ':first_place:'],
    "2": [':two:', ':second_place:'],
    "3": [':three:', ':third_place:'],
    "4": [':four:'],
    "5": [':five:'],
    "6": [':six:'],
    "7": [':seven:'],
    "8": [':eight:', ':8ball:'],
    "9": [':nine:'],
}

def EmojiConverter(input):
    #initialize empty list
    word = []

    #occurences dictionary
    occurences = {}

    #check if input string is empty
    if not input:
        print("Input String is empty.")
        return

    #loop through each character of the input string
    for ch in input:
        #capitalize the characters
        upper_ch = ch.upper()

        if upper_ch in occurences:
            occurences[upper_ch] += 1
        else:
            occurences[upper_ch] = 0
        
        #append the emoji to the list
        if upper_ch in emojiDictionary:
            #append the emoji that was not yet used in case we have more than 1 character of the same type in the word
            word.append(emojiDictionary[upper_ch][occurences[upper_ch]])

    print(word)

    
EmojiConverter("aaabbcc");
