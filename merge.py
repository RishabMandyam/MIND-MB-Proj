import pandas as pd
import os

os.chdir("/Users/rishabmandyam/Desktop/Akane Sano Lab/MIND-MB Proj/cleaned datasets")
print(os.getcwd())

# load datasets
beh = pd.read_csv('all_behavior_extracted.csv')      # 'RSRCHNO'
fmri = pd.read_csv('fMRI_extracted.csv')             # 'Subject.ID'
meds = pd.read_csv('medications_edited.csv')         # 'RESEARCHID'
pgs = pd.read_csv('pgs_extracted.csv')               # 'sample'

beh = beh.rename(columns={'RSRCHNO': 'Subject.ID'})
meds = meds.rename(columns={'RESEARCHID': 'Subject.ID'})
pgs = pgs.rename(columns={'sample': 'Subject.ID'})

print("Duplicates in beh:", beh.index.duplicated().sum())
print("Duplicates in fmri:", fmri.index.duplicated().sum())
print("Duplicates in meds:", meds.index.duplicated().sum())
print("Duplicates in pgs:", pgs.index.duplicated().sum())

beh = beh[~beh.index.duplicated(keep='first')]
fmri = fmri[~fmri.index.duplicated(keep='first')]
meds = meds[~meds.index.duplicated(keep='first')]
pgs = pgs[~pgs.index.duplicated(keep='first')]

combined = pd.concat([beh, fmri, meds, pgs], axis=1).reset_index()

# remove duplicate columns
combined = combined.loc[:, ~combined.columns.duplicated()]

combined.to_csv('MINDMB_dataset.csv', index=False)
print("MINDMB_dataset.csv created successfully.")