import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

sub_font = "<style>body {font-family: 'Times New Roman', Times, serif;} </style>"

st.write(f"{sub_font}<h2><u>VISUALIZATION: Project 1</u>    [PAGE 4]</h2>", unsafe_allow_html = True)
st.subheader("% Breakthrough Analysis : HeatMap")
st.write("For more information, data, and visualization code: [Github link](https://github.com/AliceLiu17/VIsualization-Covid-Efficacy)")
st.write("**HOVER FOR 2 ARROW PINCHING BUTTON: TO ENTER FULL SCREEN TO VIEW FULL DATA!**")
st.write('---')

st.write(f"{sub_font}<h4> <u>Overview HeatMap Breakthrough Analysis) </u> </h4>", unsafe_allow_html = True)
st.write(r""" 
Analyzing % of breakthrough cases for each country to see countries with high breakthrough rates and other 
countries who use the same vaccine. We want to filter based on strains, WHO_region, and Company of the vaccine.
The company of the vaccine are a list of companies that came out with multiple vaccines. 

By visualizing the data in this way, it is easier to identify countries that have a high percentage of breakthrough 
cases and determine whether the vaccine used is less effective against a particular strain or in a particular region. 

Effectiveness can give some sort of indication of reaction to contracting COVID-19, and the risk levels of 
death from COVID-19.
""")

st.write(f"{sub_font}<h4><u>Features:</u></h4>", unsafe_allow_html = True)
st.write(""" 
- Filtering: filter the data based on the selected WHO region and strain, respectively. These functions update the heatmap
to display only the data that meets the selected criteria.
- Heatmap:
    - The x-axis is the unique country string object values that will filter based on WHO_region
    - The y-axis is the unique vaccine string object whose values will filter based on Company selected
- Hovering: when you hover over part of the heat map you'll get the:
    - Country name
    - Vaccine
    - Strain 
- Color: color-scale; the higher the percentage the more red, the lower the percentage the more blue.
- Navigating this chart: click on full-screen button (2 arrow pinching) when hovering over the chart to have a better view of the data
""")

st.write(f"{sub_font}<h4><u>Some Observations:</u></h4>", unsafe_allow_html = True)
st.write(r"""
- Realize that the percentages are based on all the unique vaccines together in 1 column. What I mean is that
say country China uses vaccine1, vaccine2, vaccine3. Those 3 vaccines have % suceptible for x strain is 10%. 

- But what we can observe is that countries with Pfizer BioNTech - Comirnaty, AstraZeneca - Vaxzevria, 
Moderna - Spikevax, and/or Janssen - Ad26.COV 2-S as part of their vaccine list are shaded in BLUE and/or 
WHITE. Meaning low suceptibility rate.

- What this tells us is that those who are vaccined with specific companies tend to have lower 
suceptibility percentage, which indicates more effectiveness of the vaccine. Low susceptibility means:
    - Smaller proportion of vaccinated individuals are getting infected
    - Indicates that the vaccine is providing good protection against the virus. 
    - Even if a vaccinated individual gets infected, the symptoms are likely to be milder and less severe, 
    and the likelihood of hospitalization and death is greatly reduce

- Therefore, low susceptibility to breakthrough infection is a **positive sign** for vaccine efficacy and shows that 
the vaccine is performing as intended.
""")

st.write(f"{sub_font}<h4><u>Next Steps:</u></h4>", unsafe_allow_html = True)
st.write(""" 
Now we examine the different levels of protection gainst severe disease and infection for each country, and how it 
relates to the size of the population, which would provide additional insights to the vaccination status of each country. 
Run file `bubble_scatter_protection_susceptible.py`  
""")
st.write('---')


def display_heatmap(df, strain_selected, who_selected):
    df = df.dropna(subset=['VACCINES_USED'])
    df_pivot = df.pivot(index='VACCINES_USED', columns='COUNTRY', values=strain_selected)
    fig = px.imshow(df_pivot,
                    labels = dict(y = 'Vaccines', x = 'Countries', color = strain_selected),
                    color_continuous_scale='RdBu_r')
    fig.update_layout(title='Breakthrough Cases by Vaccine and Country',
                    width = 1800,
                    height = 1000,
                    margin=dict(l=100, r=100))
    st.plotly_chart(fig)

def filter_columns(df, strain_selected, who_selected):
    if strain_selected == '% SUCEPTIBLE for BREAKTHROUGH ORGINAL SEVERE':
        df = df[['COUNTRY', 'WHO_REGION', 'VACCINES_USED', '% SUCEPTIBLE for BREAKTHROUGH ORGINAL SEVERE']]
    elif strain_selected == '% SUCEPTIBLE for BREAKTHROUGH ORIGINAL INFECTION':
        df = df[['COUNTRY', 'WHO_REGION', 'VACCINES_USED', '% SUCEPTIBLE for BREAKTHROUGH ORIGINAL INFECTION']]
    elif strain_selected == '% SUCEPTIBLE for BREAKTHROUGH OMICRON SEVERE':
        df = df[['COUNTRY', 'WHO_REGION', 'VACCINES_USED', '% SUCEPTIBLE for BREAKTHROUGH OMICRON SEVERE']]
    elif strain_selected == '% SUCEPTIBLE for BREAKTHROUGH OMICRON INFECTION':
        df = df[['COUNTRY', 'WHO_REGION', 'VACCINES_USED', '% SUCEPTIBLE for BREAKTHROUGH OMICRON INFECTION']]
    if who_selected != "ALL":
        df = df[df['WHO_REGION'] == who_selected]  # add filter for WHO_REGION column
    df = df[df[strain_selected].notna()]
    return df

def filter_strain():
    strain_list = ['% SUCEPTIBLE for BREAKTHROUGH ORGINAL SEVERE', 
           '% SUCEPTIBLE for BREAKTHROUGH ORIGINAL INFECTION', 
           '% SUCEPTIBLE for BREAKTHROUGH OMICRON SEVERE', 
           '% SUCEPTIBLE for BREAKTHROUGH OMICRON INFECTION']
    strain_sb = st.sidebar.selectbox('Select Strain:', strain_list)
    st.subheader(f'Selected Strain: {strain_sb}')
    return strain_sb

def WHO_region_filter(df):
    WHO_region_list = df["WHO_REGION"].astype(str).unique().tolist()
    WHO_region_list.append("ALL")
    WHO_region_sb = st.sidebar.selectbox('WHO Region:', sorted(WHO_region_list))
    st.subheader(f'Selected WHO Region: {WHO_region_sb}')
    return WHO_region_sb

def filter_brand(df, brand_selected):
    df['BRAND'] = df['VACCINES_USED'].str.split('-').str[0].str.strip()
    if brand_selected != 'All':
        df = df.loc[df['BRAND'] == brand_selected]
    return df

def main():
    df_original = pd.read_csv("data/Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")
    
    df_original = df_original.assign(VACCINES_USED = df_original["VACCINES_USED"].str.split(',')).explode('VACCINES_USED')

    # filtering the column, if the column is equal to strain_selected return the column
    df_heatmap = pd.DataFrame()
    df_heatmap["COUNTRY"] = df_original["COUNTRY"]
    df_heatmap["WHO_REGION"] = df_original["WHO_REGION"]
    df_heatmap["VACCINES_USED"] = df_original["VACCINES_USED"]
    df_heatmap['VACCINES_USED'] = df_heatmap['VACCINES_USED'].str.strip()
    
    df_heatmap["% SUCEPTIBLE for BREAKTHROUGH ORGINAL SEVERE"] = df_original.iloc[:, 17]
    df_heatmap["% SUCEPTIBLE for BREAKTHROUGH ORIGINAL INFECTION"] = df_original.iloc[:, 18]
    df_heatmap["% SUCEPTIBLE for BREAKTHROUGH OMICRON SEVERE"] = df_original.iloc[:, 19]
    df_heatmap["% SUCEPTIBLE for BREAKTHROUGH OMICRON INFECTION"] = df_original.iloc[:, 20]
 
    brand_list = ['All', 'Moderna', 'Pfizer BioNTech', 'AstraZeneca', 'Finlay', 'Gamaleya', 'Novavax', 'SII']
    brand_sb = st.sidebar.selectbox('Select Company:', sorted(brand_list))
    st.subheader(f'Selected Brand: {brand_sb}')
    
    df_heatmap = filter_brand(df_heatmap, brand_sb)
    strains = filter_strain()
    WHO_region = WHO_region_filter(df_heatmap)
    df_heatmap = filter_columns(df_heatmap, strains, WHO_region)
    display_heatmap(df_heatmap, strains, WHO_region)

if __name__ == "__main__":
    main()


















# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import seaborn as sns
# import matplotlib.pyplot as plt

# st.markdown(
#     """
#     <style>
#     .sidebar .sidebar-content {
#         width: 20px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # analyzing % of breakthrough cases for each country based on vaccine used
# # analyzing to see countries with high breakthrough rates and other countries who use the same vaccine
# # we want to filter based on strains

# def display_heatmap(df, strain_selected, who_selected):
#     df = df.dropna(subset=['VACCINES_USED'])
#     df_pivot = df.pivot(index='VACCINES_USED', columns='COUNTRY', values=strain_selected)
#     fig = px.imshow(df_pivot,
#                     labels = dict(y = 'Vaccines', x = 'Countries', color = strain_selected),
#                     color_continuous_scale='RdBu_r')
#     fig.update_layout(title='Breakthrough Cases by Vaccine and Country',
#                     width = 1800,
#                     height = 1000,
#                     margin=dict(l=100, r=100))
#     st.plotly_chart(fig)

# def filter_columns(df, strain_selected, who_selected):
#     if strain_selected == '% SUCEPTIBLE for BREAKTHROUGH ORGINAL SEVERE':
#         df = df[['COUNTRY', 'WHO_REGION', 'VACCINES_USED', '% SUCEPTIBLE for BREAKTHROUGH ORGINAL SEVERE']]
#     elif strain_selected == '% SUCEPTIBLE for BREAKTHROUGH ORIGINAL INFECTION':
#         df = df[['COUNTRY', 'WHO_REGION', 'VACCINES_USED', '% SUCEPTIBLE for BREAKTHROUGH ORIGINAL INFECTION']]
#     elif strain_selected == '% SUCEPTIBLE for BREAKTHROUGH OMICRON SEVERE':
#         df = df[['COUNTRY', 'WHO_REGION', 'VACCINES_USED', '% SUCEPTIBLE for BREAKTHROUGH OMICRON SEVERE']]
#     elif strain_selected == '% SUCEPTIBLE for BREAKTHROUGH OMICRON INFECTION':
#         df = df[['COUNTRY', 'WHO_REGION', 'VACCINES_USED', '% SUCEPTIBLE for BREAKTHROUGH OMICRON INFECTION']]
#     df = df[df['WHO_REGION'] == who_selected]  # add filter for WHO_REGION column
#     df = df[df[strain_selected].notna()]
#     return df

# def filter_strain():
#     strain_list = ['% SUCEPTIBLE for BREAKTHROUGH ORGINAL SEVERE', 
#            '% SUCEPTIBLE for BREAKTHROUGH ORIGINAL INFECTION', 
#            '% SUCEPTIBLE for BREAKTHROUGH OMICRON SEVERE', 
#            '% SUCEPTIBLE for BREAKTHROUGH OMICRON INFECTION']
#     strain_sb = st.sidebar.selectbox('Select Strain:', strain_list)
#     st.subheader(f'Selected Strain: {strain_sb}')
#     return strain_sb

# def WHO_region_filter(df):
#     WHO_region_list = df["WHO_REGION"].astype(str).unique().tolist()
#     WHO_region_sb = st.sidebar.selectbox('WHO Region:', sorted(WHO_region_list))
#     st.subheader(f'Selected WHO Region: {WHO_region_sb}')
#     return WHO_region_sb

# def main():
#     df_original = pd.read_csv("data/Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")
    
#     df_original = df_original.assign(VACCINES_USED = df_original["VACCINES_USED"].str.split(',')).explode('VACCINES_USED')

#     # filtering the column, if the column is equal to strain_selected return the column
#     df_heatmap = pd.DataFrame()
#     df_heatmap["COUNTRY"] = df_original["COUNTRY"]
#     df_heatmap["WHO_REGION"] = df_original["WHO_REGION"]
#     df_heatmap["VACCINES_USED"] = df_original["VACCINES_USED"]
#     df_heatmap['VACCINES_USED'] = df_heatmap['VACCINES_USED'].str.strip()
#     df_heatmap["% SUCEPTIBLE for BREAKTHROUGH ORGINAL SEVERE"] = df_original.iloc[:, 17]
#     df_heatmap["% SUCEPTIBLE for BREAKTHROUGH ORIGINAL INFECTION"] = df_original.iloc[:, 18]
#     df_heatmap["% SUCEPTIBLE for BREAKTHROUGH OMICRON SEVERE"] = df_original.iloc[:, 19]
#     df_heatmap["% SUCEPTIBLE for BREAKTHROUGH OMICRON INFECTION"] = df_original.iloc[:, 20]
 
#     strains = filter_strain()
#     WHO_region = WHO_region_filter(df_heatmap)
#     df_heatmap = filter_columns(df_heatmap, strains, WHO_region)
#     display_heatmap(df_heatmap, strains, WHO_region)

# if __name__ == "__main__":
#     main()

