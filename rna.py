def transcribe(s):
    result = ''
    for i in range(0, len(s)):
        if (s[i] == 'T'):
            # s[i] = 'U'
            result += 'U'
        else:
            result += s[i]
    return result
