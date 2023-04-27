import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        width: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Visualization: Project 1")
st.subheader("% Breakthrough Analysis : HeatMap")
st.write("For more information, data, and visualization code: [Github link](https://github.com/AliceLiu17/VIsualization-Covid-Efficacy)")
st.write("\n")
st.write(r"Analyzing % of breakthrough cases for each country based on vaccine used analyzing to see countries with high breakthrough rates and other countries who use the same vaccine. We want to filter based on strains, WHO_region, and Brand")
st.write("HOVER FOR 2 ARROW PINCHING BUTTON: TO ENTER FULL SCREEN TO VIEW FULL DATA!")

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
    brand_sb = st.sidebar.selectbox('Select Brand:', sorted(brand_list))
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

