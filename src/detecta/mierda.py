'''
Created on 06/03/2017

@author: ernesto
'''
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    nodo_caca=head
    nodo_caca_doble=head
    primera_vuelta=True
    
    while(nodo_caca and nodo_caca_doble):
        if(id(nodo_caca)==id(nodo_caca_doble) and not primera_vuelta):
            return 1
        primera_vuelta=False
        nodo_caca=nodo_caca.next
        nodo_caca_doble=nodo_caca_doble.next
        if(nodo_caca_doble):
            if(id(nodo_caca)==id(nodo_caca_doble)):
                return 1
            nodo_caca_doble=nodo_caca_doble.next
        else:
            return 0
    
    return 0


def has_cycle_conejo_pendejo(head):
    ya_visto=set()
    nodo_caca=head
    
    while(nodo_caca):
        if(id(nodo_caca) in ya_visto):
            return 1
        ya_visto.add(id(nodo_caca))
        nodo_caca=nodo_caca.next
    
    return 0

