from collections import Counter
from functools import reduce
from operator import mul

def pt_count(slowa, l_d, slowa_w_zdaniu):

    return [
        [slowa_w_zdaniu[i][j] / l_d[j] for j in range(len(slowa_w_zdaniu[i]))]
        for i in range(len(slowa))
    ]

def pq_count(pt_lista):

    return [reduce(mul, column) for column in zip(*pt_lista)]

def p_count(slowa, l_d, pt_lista, lam):
    return [
        [
            lam * pt_lista[i][j] + (1 - lam) * pt_lista[i][-1]
            for j in range(len(pt_lista[i]) - 1)
        ]
        for i in range(len(slowa))
    ]

def sort_and_get_indices(values):
    
    sorted_indices = sorted(range(len(values)), key=lambda i: values[i], reverse=True)
    
    return sorted_indices

def zadanie():

    n = int(input())
    zdania = [input().translate(str.maketrans('', '', ',.!?')).strip().lower() for _ in range(n)]
    slowa = input().split(' ')

    zdania.append(' '.join(zdania))

    lam = 0.5

    l_d = [len(zd.split(" ")) for zd in zdania]

    slowa_w_zdaniu = [
    [Counter(zdanie.split())[slowo] for zdanie in zdania]
    for slowo in slowa
    ]

    pt_lista = pt_count(slowa, l_d, slowa_w_zdaniu)

    pq_lista = pq_count(pt_lista)

    p_lista = p_count(slowa, l_d, pt_lista, lam)
    
    p_lista_mult = pq_count(p_lista)
    sorted_indices = sorted(range(len(p_lista_mult)), key=lambda i: p_lista_mult[i], reverse=True)

    return sorted_indices

print(zadanie())