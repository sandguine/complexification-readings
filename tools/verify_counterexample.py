"""Exact enumeration for the proposal's constructed example; no empirical data."""
from fractions import Fraction as F

rows=[]
for z in (0,1):
    for r in (0,1):
        # Passive transition: Z'=1-Z, R'=R. Switch: Z'=R.
        # Loss: 1-Z' plus a switch cost of 1/5.
        full_losses=[F(z),F(1-r)+F(1,5)]
        summary_losses=[F(z),F(1,2)+F(1,5)]
        action=min(range(2),key=lambda u:summary_losses[u])
        regret=full_losses[action]-min(full_losses)
        rows.append((z,r,action,regret))
for row in rows: print('Z=%d R=%d summary_action=%d regret=%s'%row)
assert sum(row[3] for row in rows)/4 == F(1,20)
assert sum(row[3] for row in rows if row[0]==1)/2 == F(1,10)
print('Overall regret: 0.05; regret conditional on Z=1: 0.10')
