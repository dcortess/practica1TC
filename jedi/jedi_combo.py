#!/bin/python3

"""Methods to obtain the jedi combination."""

import sys


class LudusDeck():

    '''Deck'''

    def __init__(self):
        self.deck = []

    def read_file(self, file):
        """Init deck from a text file"""
        _file = open(file, "r")
        for line in _file.readlines():
            parsed_line = line.split()
            self.deck.append((parsed_line[0], int(parsed_line[1])))

    def read_from_input(self):
        """Init deck from a stdin"""
        deck = []
        print("Introdueix cartes (tipus, valor). Per finalitzar Control+D")
        inp = sys.stdin.readlines()
        for line in inp:
            parse = line.split()
            self.deck.append((parse[0], int(parse[1])))

        print("------------------------------------------------------------------")
        return deck




class Strategy():
    """Strategy """

    def __init__(self):
        self.combination = []

    def combo(self, deck, last_increase):
        '''combo'''
        raise NotImplementedError()

    def patch_out(self):
        '''Method to run to stdout with the right format'''
        for card in self.combination:
            print(card[0], card[1])


class RecursiveStrategy(Strategy):
    """Recursive function immplementation"""

    def combo(arr):
        n = len(arr)   
        lis = [1]*n 
        
        llistaindex = [0]*n
        for i in range(0, n):
            llistaindex[i] = i
        
        for i in range (1 , n): 
            for j in range(0 , i): 
                if (arr[i] > arr[j] and lis[i]< lis[j] + 1): 
                    lis[i] = lis[j]+1
                    llistaindex[i] = j
    
        maxim = 0
        index = 0
        
        for i in range(n): 
            if (maxim < lis[i]):
                maxim = lis[i]
                index = i
            
        seq = [arr[index]]
        while (index != llistaindex[index]):
            index = llistaindex[index]
            seq.append(arr[index])
            
            
        llistafinal = seq[::-1]
        return llistafinal


class IterativeStrategy(Strategy):
    """Iterative function immplementation"""

    def combo(self, deck, last_increase=0):

        """Recursive combo"""

        return []


if __name__ == '__main__':

    DECK = LudusDeck()
    if len(sys.argv) == 1:
        sys.exit()
    elif len(sys.argv) == 2:
        DECK.read_from_input()
    else:
        DECK.read_file(sys.argv[2])

    S = Strategy()

    if sys.argv[1] == 'r':
        S = RecursiveStrategy()
    elif sys.argv[1] == 'i':
        S = IterativeStrategy()
    else:
        sys.exit()

    S.combination = S.combo(DECK.deck)
    S.patch_out()
