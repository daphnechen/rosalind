def nucleotideCount(s):
    acount = 0
    tcount = 0
    gcount = 0
    ccount = 0
    for i in range(0, len(s)):
        if (s[i] == 'A'):
            acount += 1
        elif (s[i] == 'T'):
            tcount += 1
        elif (s[i] == 'G'):
            gcount += 1
        elif (s[i] == 'C'):
            ccount += 1
    resultlist = [acount, tcount, gcount, ccount]
    return resultlist


