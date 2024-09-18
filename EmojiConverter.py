import sys

def EmojiConverter(input):
    characters = [];
    for character in input:
        characters.append(character)
    for item in characters:
        itemIndex = characters.index(item)
        match item:
            case 'a':
                characters[itemIndex] = ':a:'
            case 'b':
                characters[itemIndex] = ':b:'
            case 'c':
                characters[itemIndex] = ':arrow_right_hook:'
            case 'd':
                characters[itemIndex] = ':leftwards_arrow_with_hook:'
            case 'e':
                characters[itemIndex] = ':e_mail:'
            case 'f':
                characters[itemIndex] = ':flags:'
            case 'g':
                caracters[itemIndex] = ':fuelpump:'
            case 'h':
                characters[itemIndex] = ':pisces:'
            case 'i':
                characters[itemIndex] = ':information:'
            case 'j':
                characters[itemIndex] = ':japan:'
            case 'k':
                characters[itemIndex] = ':leg:'
            case 'l':
                characters[itemIndex] = ':muscle:'
            case 'm':
                characters[itemIndex] = ':part_alternation_mark:'
            case 'n':
                characters[itemIndex] = ':capricorn:'
            case 'o':
                characters[itemIndex] = ':o2:'
            case 'p':
                characters[itemIndex] = ':parking:'
            case 'q':
                characters[itemIndex] = ':postal_horn:'
            case 'r':
                characters[itemIndex] = ':registered:'
            case 's':
                characters[itemIndex] = ':heavy_dollar_sign:'
            case 't':
                characters[itemIndex] = ':cross:'
            case 'u':
                characters[itemIndex] = ':ophiuchus:'
            case 'v':
                characters[itemIndex] = ':aries:'
            case 'w':
                characters[itemIndex] = ':regional_indicator_w:'
            case 'x':
                characters[itemIndex] = ':negative_squared_cross_mark:'
            case 'y':
                characters[itemIndex] = ':v:'
            case 'z':
                characters[itemIndex] = ':zzz:'
            case '0':
                characters[itemIndex] = ':zero:'
            case '1':
                characters[itemIndex] = ':one:'
            case '2':
                characters[itemIndex] = ':two:'
            case '3':
                characters[itemIndex] = ':three:'
            case '4':
                characters[itemIndex] = ':four:'
            case '5':
                characters[itemIndex] = ':five:'
            case '6':
                characters[itemIndex] = ':six:'
            case '7':
                characters[itemIndex] = ':seven:'
            case '8':
                characters[itemIndex] = ':eight:'
            case '9':
                characters[itemIndex] = ':nine:'
                
    print(characters);

    
EmojiConverter("Hella");
