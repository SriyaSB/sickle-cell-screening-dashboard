import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_ind

with open('analysis_output.txt', 'w') as f:
    def write_line(line):
        print(line)
        f.write(line + '\n')

    df = pd.read_csv('scd_screening_data.csv')

    write_line("total patients: " + str(len(df)))

    write_line("\nGenotype wise count:")
    for k, v in df['genotype'].value_counts().items():
        write_line(f"  {k}: {v}")

    write_line("\nAwareness (%):")
    aw = df['awareness'].value_counts()
    for k, v in aw.items():
        write_line(f"  {k}: {round(v/len(df)*100,1)}%")

    yes_screened = df[df['screened']=='Yes']
    pct = len(yes_screened)/len(df)*100
    write_line(f"\nOverall screened: {round(pct,1)}%")

    write_line("\nDistrict wise screening %:")
    for dist, grp in df.groupby('district'):
        s = round((grp['screened']=='Yes').sum()/len(grp)*100, 1)
        write_line(f"  {dist}: {s}%")

    hbss = df[df['genotype']=='HbSS']
    hu_pct = round((hbss['hydroxyurea']=='Yes').sum()/len(hbss)*100, 1) if len(hbss)>0 else 0
    write_line(f"\nHydroxyurea among HbSS: {hu_pct}%")

    ltfu_pct = round((df['follow_up_status']=='Lost to follow-up').sum()/len(df)*100, 1)
    write_line(f"\nLost to follow-up: {ltfu_pct}%")

    # Stats
    df['heard_scd'] = df['awareness'].apply(lambda x: 0 if x=='Never heard' else 1)

    ct1 = pd.crosstab(df['gender'], df['heard_scd'])
    c1, p1, d1, e1 = chi2_contingency(ct1)
    write_line(f"\nChi-square (gender vs awareness):")
    write_line(f"  chi2 = {round(c1,3)}, p = {round(p1,4)}, df = {d1}")

    age_ss = df[df['genotype']=='HbSS']['age'].dropna()
    age_sa = df[df['genotype']=='HbSA']['age'].dropna()
    t1, pt = ttest_ind(age_ss, age_sa)
    write_line(f"\nIndependent t-test (age: HbSS vs HbSA):")
    write_line(f"  mean HbSS = {round(age_ss.mean(),1)}, mean HbSA = {round(age_sa.mean(),1)}")
    write_line(f"  t = {round(t1,3)}, p = {round(pt,4)}")

    ct2 = pd.crosstab(df['belief_black_magic'], df['screened'])
    c2, p2, d2, e2 = chi2_contingency(ct2)
    write_line(f"\nChi-square (black magic belief vs screened):")
    write_line(f"  chi2 = {round(c2,3)}, p = {round(p2,4)}, df = {d2}")