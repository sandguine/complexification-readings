#!/usr/bin/env python3
"""Exact finite illustration, not a new theorem or an organizational experiment.

Three possible co-policies C,D,E (uniform prior); a focal person chooses A or B.
Separate an authorized objective change from a restriction of action rights.
Inspired by Lauffer et al. (ICML 2023), but payoffs and comparisons are ours.
Run from any directory. Uses only Python standard library; writes no files.
"""
from fractions import Fraction as F
from itertools import product
import json

TYPES=('C','D','E'); ACTIONS=('A','B')
PAYOFF={
 'routine':{'A':(4,0,4),'B':(2,3,2)},
 'revised':{'A':(4,0,0),'B':(2,3,2)},
}

def best_responses(context,kind,actions=ACTIONS):
    j=TYPES.index(kind)
    best=max(PAYOFF[context][a][j] for a in actions)
    return tuple(a for a in actions if PAYOFF[context][a][j]==best)

def partition(contexts,actions=ACTIONS):
    groups={}
    for t in TYPES:
        key=tuple(best_responses(q,t,actions) for q in contexts)
        groups.setdefault(key,[]).append(t)
    return list(groups.values())

def value(context,groups,actions=ACTIONS):
    # Maximize conditional expected payoff within each report cell.
    # Multiply through by uniform prior to avoid conditional denominators.
    return sum((max(sum(F(PAYOFF[context][a][TYPES.index(t)],len(TYPES)) for t in cell)
                    for a in actions) for cell in groups),F(0))

def all_partitions():
    seen=set()
    for labels in product(range(3),repeat=3):
        cells=tuple(sorted(tuple(t for t,l in zip(TYPES,labels) if l==j)
                           for j in set(labels)))
        if cells not in seen:seen.add(cells);yield cells

def run():
    routine=partition(['routine']); revised=partition(['revised']); joint=partition(['routine','revised'])
    assert routine==[['C','E'],['D']]
    assert revised==[['C'],['D','E']]
    assert joint==[['C'],['D'],['E']]
    # Exhaust every deterministic report partition on the three co-policies.
    count=0
    for cells in all_partitions():
        count+=1
        for q in PAYOFF:
            assert value(q,cells)<=value(q,[[t] for t in TYPES])
        preserves=all(len({best_responses(q,t) for t in cell})==1
                      for q in PAYOFF for cell in cells)
        assert preserves == all(len(cell)==1 for cell in cells)
    assert count==5
    full=value('revised',joint); coarse=value('revised',routine)
    locked=partition(['routine','revised'],actions=('A',))
    assert full==3 and coarse==F(7,3) and full-coarse==F(2,3)
    assert locked==[['C','D','E']] and value('revised',locked,('A',))==F(4,3)
    # Same observed action at baseline can hide different mechanism responses.
    # Two systems have A=0 when actuation reversal g=0; desired outcome Y=1.
    # Y = 1 XOR A XOR g. Adaptive chooses A=g; frozen always A=0.
    response=[{'g':g,'adaptive_action':g,'frozen_action':0,
               'adaptive_outcome':1 ^ g ^ g,'frozen_outcome':1 ^ 0 ^ g} for g in (0,1)]
    assert response[0]['adaptive_outcome']==response[0]['frozen_outcome']==1
    assert response[1]['adaptive_outcome']==1 and response[1]['frozen_outcome']==0
    return {'status':'exact analytical illustration; no empirical study',
            'payoffs':PAYOFF,'routine_partition':routine,'revised_partition':revised,
            'both_contexts_partition':joint,'partitions_checked':count,
            'routine_full_and_routine_report_value':str(value('routine',routine)),
            'revised_full_value':str(full),'revised_routine_report_value':str(coarse),
            'revised_report_regret':str(full-coarse),
            'only_A_partition':locked,'only_A_revised_value':str(value('revised',locked,('A',))),
            'mechanism_response_example':response}

if __name__=='__main__':print(json.dumps(run(),indent=2))
