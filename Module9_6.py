def all_variants(text):

    
    inc=1
    a=0
    var=text[a:a+inc]
    while inc<=len(text)-1:
        if a+inc>len(text)-1:
            inc+=1
            a=0
        yield var
        a+=1
        

        


            
a = all_variants("abc")
for i in a:
    print(i)
    
print(len('abc'))
