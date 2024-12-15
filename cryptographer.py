def encrypt(text):
    plain_upper=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    ceaser_upper=('D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C')
    plain_lower=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    ceaser_lower=('d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c')
    plain_numbers=('0','1','2','3','4','5','6','7','8','9')
    ceaser_numbers=('3','4','5','6','7','8','9','0','1','2')
    length=len(text)
    final=""
    for i in range(0,length):
        character=text[i]
        if(character in plain_upper):    
            for j in range(0,26):
                if(character==plain_upper[j]):
                    final=final+ceaser_upper[j]
        elif(character in plain_lower):
            for k in range(0,26):
                if(character==plain_lower[k]):
                    final=final+ceaser_lower[k]
        elif(character in plain_numbers):
            for l in range(0,9):
                if(character==plain_numbers[l]):
                    final=final+ceaser_numbers[l]
        else:
            final=final+character
    return(final)


def decrypt(text):
    plain_upper=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    ceaser_upper=('D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C')
    plain_lower=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    ceaser_lower=('d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c')
    plain_numbers=('0','1','2','3','4','5','6','7','8','9')
    ceaser_numbers=('3','4','5','6','7','8','9','0','1','2')
    length=len(text)
    final=""
    for i in range(0,length):
        character=text[i]
        if(character in ceaser_upper):    
            for j in range(0,26):
                if(character==ceaser_upper[j]):
                    final=final+plain_upper[j]
        elif(character in ceaser_lower):
            for k in range(0,26):
                if(character==ceaser_lower[k]):
                    final=final+plain_lower[k]
        elif(character in ceaser_numbers):
            for l in range(0,9):
                if(character==ceaser_numbers[l]):
                    final=final+plain_numbers[l]
        else:
            final=final+character
    return(final)