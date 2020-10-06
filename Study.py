import itertools

def ItertoolsChain():
    #need import itertools

    print("##################################################")

    print("""
    import itertools

    for item in itertools.chain([1,2],['a','b']):
        print(item)
    """)

    print("##################################################")

    print("If you understand the code, hit any key!")
    AnyKey = input()

    for item in itertools.chain([1,2],['a','b']):
        print(item)

    

#スペースで区切られた数値をリストに変換する
def ConvertSpaceSeparatedNumbersToAList():

    print("##################################################")

    print("""
    InputElement = list(map(int, input().split()))
    """)

    print("##################################################")

    print("If you understand the code, hit any key!")
    AnyKey = input()

    InputElement = list(map(int, input().split()))

    print(InputElement)

    







########## main ##########
ItertoolsChain()
ConvertSpaceSeparatedNumbersToAList()



##########################