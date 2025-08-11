# resolução O(n)

def formar_palindromo_com_uma_troca(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s
    if s == s[::-1]:
        return s

    # encontra o primeiro par de posições (l, r) que não batem
    l, r = 0, n - 1
    while l < r and s[l] == s[r]:
        l += 1
        r -= 1

    # tentar trocar s[l] com s[l+1]
    if l + 1 < n:
        t = s[:l] + s[l+1] + s[l] + s[l+2:]
        if t == t[::-1]:
            return t

    # tentar trocar s[r-1] com s[r]
    if r - 1 >= 0:
        t = s[:r-1] + s[r] + s[r-1] + s[r+1:]
        if t == t[::-1]:
            return t

    return '-1'


print(formar_palindromo_com_uma_troca("racecra"))
