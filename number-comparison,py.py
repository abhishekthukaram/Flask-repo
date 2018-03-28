def numbercompare(n):
    newlist = set(n)
    if len(newlist)== len(n):
        print "The numbers are unique"
    else:
        print "the number is repeated"

numbercompare([1,2,3,4,5])
numbercompare([1,1,2,2,3,4,5])


