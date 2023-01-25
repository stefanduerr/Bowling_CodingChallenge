def bowling(throws, set):
    list_of_throws = list()
    
    # insert zeros after strikes
    for throw in range(20):
        if throw < len(set):
            if set[throw] == 10:
                set.insert(throw+1, 0)

    # iterate over set of throws
    for x in range(1, len(set), 2):

        # determine what kind of case it is
        if set[x-1] == 10 and x+1 < throws*2 and set[x+1] == 10:
            list_of_throws.append([sum(set[x-1:x+4]), "multi-strike"])
        elif set[x-1] == 10 and x+1 < throws*2:
            if set[x+1] != 0:
                list_of_throws.append([sum(set[x-1:x+3]), "strike"])
            else:
                list_of_throws.append([sum(set[x-1:x+1]), "failed_strike"])
        elif set[x]+set[x-1] == 10 and x+1 < throws*2:
            list_of_throws.append([sum(set[x-1:x+2]), "spare"])
        else:
            list_of_throws.append([sum(set[x-1:x+1]), "regular"])

        # handle first throw
        if x != 1:
            list_of_throws[-1][0] += list_of_throws[-2][0]

    # handle extra turns, earned by strikes or spares
    if len(list_of_throws) > throws:
        list_of_throws[-2][0] += list_of_throws[-1][0] - list_of_throws[-2][0]
        del list_of_throws[-1]
    elif len(set) > throws*2:
        list_of_throws[-1][0] += set[-1]
        
    # format result
    result = []
    for i in range(len(list_of_throws)):
        result.append(list_of_throws[i][0])
    result = ",".join(map(str, result))

    print(list_of_throws)
    print(result)
   

bowling(4, [2, 7, 10, 4, 6, 4, 5])
#9,29,43,52
bowling(4, [2, 7, 4, 6, 10, 4, 5])
#9,29,48,57
bowling(3, [2, 7, 4, 6, 10, 4, 5])
#9,29,48
bowling(10, [1,4,4,5,6,4,5,5,10,0,1,7,3,6,4,10,2,8,6])

bowling(10, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

bowling(10, [10,10,10,10,10,10,10,10,10,10,10,10])

bowling(10, [7,2,1,9,6,4,5,5,10,3,7,7,3,6,4,10,2,8,6])
# def test():
