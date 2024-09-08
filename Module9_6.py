def all_variants(text):
    inc = 1
    a = 0
    while inc <= (len(text) - 1):
        if a + inc > len(text):
            inc += 1
            a = 0
        yield text[a:a + inc]
        a += 1


a = all_variants("abc")
for i in a:
    print(i)

