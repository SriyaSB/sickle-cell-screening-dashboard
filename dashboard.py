import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

st.set_page_config(page_title="SCD Dashboard", layout="wide")

# load data
df = pd.read_csv('scd_screening_data.csv')

st.title("Sickle Cell Disease Screening - Field Data Dashboard")
st.write("Data collected from field sites in Odisha and Assam")

# sidebar
st.sidebar.write("### Filter Records")
dist_list = sorted(df['district'].dropna().unique().tolist())
geno_list = sorted(df['genotype'].dropna().unique().tolist())

sel_dist = st.sidebar.multiselect("District", dist_list, default=dist_list)
sel_geno = st.sidebar.multiselect("Genotype", geno_list, default=geno_list)

# apply filter
fdf = df[df['district'].isin(sel_dist) & df['genotype'].isin(sel_geno)].copy()

st.write(f"Showing {len(fdf)} records after filter")
st.write("---")

# metrics row
c1, c2, c3, c4 = st.columns(4)

total = len(fdf)
screened_pct = round((fdf['screened']=='Yes').sum()/total*100, 1) if total > 0 else 0

hbss_df = fdf[fdf['genotype']=='HbSS']
if len(hbss_df) > 0:
    hu_pct = round((hbss_df['hydroxyurea']=='Yes').sum()/len(hbss_df)*100, 1)
else:
    hu_pct = 0

ltfu_pct = round((fdf['follow_up_status']=='Lost to follow-up').sum()/total*100, 1) if total > 0 else 0

c1.metric("Total Patients", total)
c2.metric("Screened (%)", f"{screened_pct}%")
c3.metric("HbSS on HU (%)", f"{hu_pct}%")
c4.metric("Lost to Follow-up (%)", f"{ltfu_pct}%")

st.write("---")

# screening by district
st.write("### Screening Coverage by District")
dist_screen = {}
for d, grp in fdf.groupby('district'):
    pct = round((grp['screened']=='Yes').sum()/len(grp)*100, 1)
    dist_screen[d] = pct

dist_screen_df = pd.Series(dist_screen).sort_values()
fig1, ax1 = plt.subplots(figsize=(8,4))
dist_screen_df.plot(kind='barh', ax=ax1, color='steelblue')
ax1.set_xlabel("Screened (%)")
ax1.set_title("District-wise Screening %")
plt.tight_layout()
st.pyplot(fig1)

st.write("---")

# awareness
st.write("### Awareness of SCD among Patients")
aw_counts = fdf['awareness'].value_counts()
fig2, ax2 = plt.subplots(figsize=(7,4))
aw_counts.plot(kind='bar', ax=ax2, color='teal')
ax2.set_ylabel("No. of patients")
ax2.set_title("Awareness levels")
ax2.tick_params(axis='x', rotation=30)
plt.tight_layout()
st.pyplot(fig2)

st.write("---")

# cascade of care
st.write("### Cascade of Care (Step-wise)")
stage    = ['Total enrolled', 'Ever screened', 'HbSS genotype', 'HbSS on hydroxyurea', 'Active follow-up']
counts   = [
    total,
    (fdf['screened']=='Yes').sum(),
    (fdf['genotype']=='HbSS').sum(),
    (hbss_df['hydroxyurea']=='Yes').sum(),
    (fdf['follow_up_status']=='Active').sum()
]
cas_df = pd.DataFrame({'Stage': stage, 'Count': counts})
st.dataframe(cas_df, use_container_width=True)

st.write("---")

# lost to follow up list
st.write("### Lost to Follow-up Patients")
ltfu_df = fdf[fdf['follow_up_status']=='Lost to follow-up'][['patient_id','age','gender','district','genotype']]
st.write(f"Total LTFU: {len(ltfu_df)}")
st.dataframe(ltfu_df.reset_index(drop=True), use_container_width=True)

st.write("---")

# chi square
st.write("### Association: Black Magic Belief vs Screening")
tab = pd.crosstab(fdf['belief_black_magic'], fdf['screened'])
st.write("Contingency table:")
st.dataframe(tab)

if tab.shape[0] >= 2 and tab.shape[1] >= 2:
    chi2, p, dof, ex = chi2_contingency(tab)
    st.write(f"Chi-square = {round(chi2,3)}, df = {dof}, p-value = {round(p,4)}")
    if p < 0.05:
        st.success("Significant association found (p < 0.05)")
    else:
        st.info("No significant association (p >= 0.05)")
else:
    st.warning("Not enough data for chi-square test with current filters")