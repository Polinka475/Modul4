# def strcounter(s): # O(N*M); 
    #for sym in set(s): #set - множество
    #    counter = 0
    #    for sub_sym in s:  # N - уникальные элементы; M - все
    #        if sym == sub_sym:
    #            counter += 1
    #   print(sym, counter)

 #strcounter('abc')   


def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items():
        print(sym, count)

strcounter('ajghskghskab')