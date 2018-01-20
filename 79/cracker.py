import sys

def index_or_else(list_, value, default):
    try:
        return list_.index(value)
    except ValueError:
        return default

def is_good_guess(guess, codes):
    for code in codes:
        minimum = 0
        for character in guess:
            idx = index_or_else(code, character, None)
            if idx is not None:
                if minimum < idx:
                    return False
                minimum += 1
    return True

with open(sys.argv[1]) as codefile:
    codes = set((code.strip() for code in codefile.readlines()))
    candidates = set(''.join(codes))
    print(codes)
    guess = ''
    for i in range(len(candidates)):
        for i in candidates:
            if i in guess:
                continue
            if is_good_guess(guess + i, codes):
                print(f'{guess + i}')
                guess = guess + i
                break
