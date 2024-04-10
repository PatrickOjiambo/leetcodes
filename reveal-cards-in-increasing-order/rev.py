#!/usr/bin/env python3
def deckRevealedIncreasing(deck):
    """
    :type deck: List[int]
    :rtype: List[int]
    """
    if len(deck) == 1:
        return deck
    deck.sort(reverse = True)
    sorted_list = []
    for i, number in enumerate(deck):
        if i <= 1:
            sorted_list.insert(0, number)
            
        else:
            sorted_list.insert(0, number)
            last_number = sorted_list[-1]
            sorted_list.insert(1, last_number)
            sorted_list.pop()
    return sorted_list

test_list = [1,2,3]
print(deckRevealedIncreasing(test_list))
