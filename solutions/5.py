while 1:
    print(sorted(map(lambda x:(x,"-"+x[:-1])["-" in x],input()[::-1].split()),key=int)[1])

