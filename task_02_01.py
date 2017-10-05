def is_palindrome(s):
    def trim(chars, src):
        chars = list(str(chars))
        for c in chars:
            src = src.replace(c, '')
        return src
    s = list(trim(' ,.!?:/\\-;\'\"', str(s)).lower())
    return True if s == s[::-1] else False