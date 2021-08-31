class simpleInfiniteSequece:
    a = range(5)
    print (list(a))

    def infiniteSeq():
        num = 0
        while True:
            yield num
            num +=1
    #for i in infiniteSeq():
        #print(i, end = " ")