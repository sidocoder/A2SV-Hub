# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E


from collections import Counter
def issubs(s,t):
    index = 0
    for char in s:
        index = t.find(char,index)
        if index == -1:
            return False
        index+=1
    return True
        



def transform(s, t, p):
    if not issubs(s,t):
        return 'NO'
    
    hashh_s = Counter(s)
    hashh_p = Counter(p)
    needed = Counter()

    for char in t:
        if char not in hashh_s:
            needed[char]+=1
        else:
            hashh_s[char]-=1
            if hashh_s[char] == 0:
                del hashh_s[char]
    for val,fre in needed.items():
        if val in hashh_p:
            if fre > hashh_p[val]:
                return 'NO'
        else:

            return 'NO'
    return 'YES'

    

    




for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    print(transform(s,t,p))

