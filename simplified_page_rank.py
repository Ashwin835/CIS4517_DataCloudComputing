#program is desgined to run for specifically 3 pages
import numpy as np
from fractions import Fraction

def get_eigenvector(forward_links):
    eigenvector= np.zeros(shape=(3,3))
    a_forwardlinks, b_forwardlinks, c_forwardlinks = 0, 0, 0

    for cur in forward_links:
        if cur[0]=='A':
            a_forwardlinks+=1
        elif cur[0]=='B':
            b_forwardlinks+=1
        else:
            c_forwardlinks+=1
    
    
    for i in range(3):
        for j in range(3):
            mapping= f'{get_mapping(i)}-{get_mapping(j)}'
            if mapping in forward_links:
                if i==0:
                    eigenvector[i,j] = 1/a_forwardlinks
                elif i==1:
                    eigenvector[i,j] = 1/b_forwardlinks
                else:
                    eigenvector[i,j]=1/c_forwardlinks

    eigenvector= np.transpose(eigenvector)

    return eigenvector

def get_mapping(number):
    if number==0:
        return 'A'
    if number==1:
        return 'B'
    return 'C'

def new_ranking(page_rankings, eigenvector):
    return eigenvector @ page_rankings



page_rankings= np.full(shape= (3,1), fill_value=1/3)

forward_links= ['A-B','A-C', 'B-C', 'B-A','C-A']

eigenvector= get_eigenvector(forward_links)

page_rankings= new_ranking(page_rankings, eigenvector)

while ( 1- page_rankings[0,0] + page_rankings[1,0] + page_rankings[2,0] < .0000001):
    page_rankings= new_ranking(page_rankings, eigenvector)

print(page_rankings)