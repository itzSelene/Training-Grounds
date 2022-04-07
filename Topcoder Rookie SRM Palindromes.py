#   Topcoder, Rookie SRM 10 Rookie 10 - Division I, Level Three

#   Solution by Selene (HttpRichie) 


from math import floor

s = input(); # reiceves the input

substrings = [s[i:j+1] for i in range(len(s)) for j in range(i+1, len(s))] # creates a list of substrings of "string" whose lenght is at least 2


def checkPalindrome(substr): # function to look for palindromes

    l = len(substr)

    if l%2==0:
        for i in range(0, int(l/2)): # Will check for equality over all symmetrical indexes in relation to the center of the string

            if substr[i] != substr[l-i-1]:
                return 1
    else:
        for j in range(0, floor(l/2)+1): # Will check for equality over all symmetrical indexes in relation to the center of the string
            if substr[j] != substr[l-j-1]:
                return 1

    return 0
        

palindromeCandidates = list(map(checkPalindrome, substrings)) # map from the set of substrings to {0, 1}

current = 1;
for x in palindromeCandidates: current = current*x; # If there is any palindrome whitin the set of substrings, then "current" will be always 0.


if current == 0:
    print("good")
else:
    print("not good")
                