def reverseComplement(s):
    result = ''
    for i in range(0, len(s)):
        if (s[i] == 'A'):
            result += 'T'
        elif (s[i] == 'T'):
            result += 'A'
        elif (s[i] == 'C'):
            result += 'G'
        elif (s[i] == 'G'):
            result += 'C'
    return result[::-1]
