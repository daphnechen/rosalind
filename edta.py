def align(s, t):
    sPrime = ''
    tPrime = ''
    editDistance = 0
    for i in range(0, min(len(s), len(t))):
        # First case: characters are equal
        if s[i] == t[i]:
            sPrime += s[i]
            tPrime += t[i]
        # Second case: characters are not equal and
        # first string s is shorter than second string t
        elif (s[i] != t[i]) & (len(s) < len(t)):
            sPrime += s[i]
            tPrime += '-'
            editDistance += 1
        # Third case: characters are not equal and
        # first string s is longer than second string t
        elif (s[i] != t[i]) & (len(s) > len(t)):
            sPrime += '-'
            tPrime += t[i]
            editDistance += 1
        # Fourth case: first string s has ended and
        # second string t has remaining characters
        elif t[i] & (s[i] is None):
            sPrime += '-'
            tPrime += t[i]
            editDistance += 1
        # Fifth case: first string s has remaining
        # characters and second string t has ended
        elif s[i] & t[i] is None:
            sPrime += s[i]
            tPrime += '-'
            editDistance += 1
    # Add remaining characters to the resulting strings
    for j in range(min(len(s), len(t)), max(len(s), len(t))):
        if len(s) > len(t):
            sPrime += s[j]
            tPrime += '-'
            editDistance += 1
        elif len(s) < len(t):
            sPrime += '-'
            tPrime += t[j]
            editDistance += 1
    print(editDistance)
    print(sPrime)
    print(tPrime)
