import numpy as np

def get_new_page_rankings(PRA, PRB, PRC, linkings, c, damping_factor=0.8):
    PRA= damping_factor + ((1-damping_factor)*(PRB/c['B']) * (PRC/c['C']))

    PRB= damping_factor + ((1-damping_factor)* (PRA/c['A']))

    PRC= damping_factor + ((1-damping_factor)* (PRA/c['A']))

    return PRA, PRB, PRC



linkings= ['A-B', 'A-C', 'B-A', 'C-A']
c={'A':2,'B':1, 'C':1}
PRA, PRB, PRC= 1,1,1
old_PRA, old_PRB, old_PRC= 1,1,1

PRA, PRB, PRC= get_new_page_rankings(PRA, PRB, PRC, linkings,c)
iterations_to_converge=1

while abs(old_PRA-PRA)>0.000001 or abs(old_PRB-PRB)>0.000001 or abs(old_PRC-PRC)>0.000001:
    old_PRA, old_PRB, old_PRC= PRA, PRB, PRC
    PRA, PRB, PRC= get_new_page_rankings(PRA, PRB, PRC, linkings,c)
    iterations_to_converge+=1

print(f'Page Rank A: {PRA}')
print(f'Page Rank B: {PRB}')
print(f'Page Rank C: {PRC}')
print(f'Converged in {iterations_to_converge} iterations')