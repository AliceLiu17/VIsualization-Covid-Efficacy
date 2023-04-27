import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Visualization: Project 1")
st.subheader("Trends in vaccine efficacy and breakthrough infections : Bubble Chart")
st.write("For more information, data, and visualization code: [Github link](https://github.com/AliceLiu17/VIsualization-Covid-Efficacy)")
st.write("\n")
st.write(r"Analyzing which countries have low and high levels of protection against severe disease and infection. Can understand how different regions of the world are performing in terms of vaccine efficacy and breakthrough infections. It can also help you identify areas where more attention or resources may be needed to improve vaccine distribution or effectiveness.")
st.write("\n")
st.write("HOVER FOR 2 ARROW PINCHING BUTTON: TO ENTER FULL SCREEN TO VIEW FULL DATA!")
st.write("\n")

def display_bubble(df, WHO_selected, strain_selected):
    if WHO_selected != "ALL":
        df = df[df['WHO_REGION'] == WHO_selected]
    if strain_selected != "ALL":
        # Define the columns to use for x and y based on the selected strain
        x_col = f"% People Protected for {strain_selected} SEVERE"
        y_col = f"% People Protected for {strain_selected} INFECTION"
    else:
        # Use the original columns if "ALL" strains are selected
        x_col = "% People Protected for ORGINAL SEVERE"
        y_col = "% People Protected for ORGINAL INFECTION"

    fig = px.scatter(df, x= x_col, y=y_col, 
                     size="TOTAL Population", 
                     size_max = 60,
                     color="WHO_REGION", 
                     hover_name="COUNTRY")

    # Update the layout
    fig.update_layout(title="COVID Protection Efficacy by Country",
                      xaxis_title="% People Protected for Severe Disease",
                      yaxis_title="% People Protected for Infection",
                      font=dict(size=14),
                      width=1000, height=800,
                      margin=dict(l=50, r=0, b=300), xaxis_tickangle=45)
    
    # Display the chart
    st.plotly_chart(fig)

def WHO_region_filter(df):
    WHO_region_list = df["WHO_REGION"].astype(str).unique().tolist()
    WHO_region_list.append("ALL")
    WHO_region_sb = st.sidebar.selectbox('WHO Region:', sorted(WHO_region_list))
    st.subheader(f'Selected WHO Region: {WHO_region_sb}')
    return WHO_region_sb

def strain_filter(df):
    strain_list = ['ORIGINAL', 'OMICRON']
    strain_sb = st.sidebar.selectbox('Strains:', sorted(strain_list))
    st.subheader(f'Selected Strain: {strain_sb}')
    return strain_sb

def main():
    df_original = pd.read_csv("data/Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")

    df_scatter = pd.DataFrame()
    df_scatter["COUNTRY"] = df_original["COUNTRY"]
    df_scatter["WHO_REGION"] = df_original["WHO_REGION"]
    df_scatter["TOTAL Population"] = df_original["TOTAL Population"]

    df_scatter[r"% People Protected for ORIGINAL SEVERE"] = df_original[r"% People Protected for ORGINAL SEVERE"]
    df_scatter[r"% People Protected for ORIGINAL INFECTION"] = df_original[r"% People Protected for ORGINAL INFECTION"]
    df_scatter[r"% People Protected for OMICRON SEVERE"] = df_original[r"% People Protected for OMICRON SEVERE"]
    df_scatter[r"% People Protected for OMICRON INFECTION"] = df_original[r"% People Protected for OMICRON INFECTION"]

    df_scatter[r"% SUCEPTIBLE for BREAKTHROUGH ORIGINAL SEVERE"] = df_original.iloc[:, 17]
    df_scatter[r"% SUCEPTIBLE for BREAKTHROUGH ORIGINAL INFECTION"] = df_original.iloc[:, 18]
    df_scatter[r"% SUCEPTIBLE for BREAKTHROUGH OMICRON SEVERE"] = df_original.iloc[:, 19]
    df_scatter[r"% SUCEPTIBLE for BREAKTHROUGH OMICRON INFECTION"] = df_original.iloc[:, 20]

    df_scatter = df_scatter.dropna(axis = 0)
    WHO_region = WHO_region_filter(df_scatter)
    strain_selected = strain_filter(df_scatter)
    display_bubble(df_scatter, WHO_region, strain_selected)

if __name__ == '__main__':
    main()


















# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import seaborn as sns
# import matplotlib.pyplot as plt

# st.title("Visualization: Project 1")
# st.subheader("Trends in vaccine efficacy and breakthrough infections : Bubble Chart")
# st.write("For more information, data, and visualization code: [Github link](https://github.com/AliceLiu17/VIsualization-Covid-Efficacy)")
# st.write("\n")
# st.write(r"Analyzing which countries have low and high levels of protection against severe disease and infection. Can understand how different regions of the world are performing in terms of vaccine efficacy and breakthrough infections. It can also help you identify areas where more attention or resources may be needed to improve vaccine distribution or effectiveness.")
# st.write("\n")
# st.write(r"Will also add another layer of gradient color scheme to represent the % of susceptible population which can help us understand the relationship between vaccine efficacy and susceptibility to COVID-19.")
# st.write("\n")
# st.write("HOVER FOR 2 ARROW PINCHING BUTTON: TO ENTER FULL SCREEN TO VIEW FULL DATA!")
# st.write("\n")

# def display_bubble(df, WHO_selected, strain_selected):
#     if WHO_selected != "ALL":
#         df = df[df['WHO_REGION'] == WHO_selected]
#     if strain_selected != "ALL":
#         columns = [col for col in df.columns if strain_selected in col]
#         df = df[['COUNTRY', 'WHO_REGION', 'TOTAL Population'] + columns]

#     fig = px.scatter(df, x="% People Protected for ORIGINAL SEVERE", y="% People Protected for ORIGINAL INFECTION", 
#                      size="TOTAL Population", 
#                      size_max = 60,
#                      color="WHO_REGION", 
#                      hover_name="COUNTRY", )

#     # Add a gradient color scheme to represent the percentage of susceptible population
#     # fig.for_each_trace(lambda trace: trace.update(marker=dict(sizemode='diameter', 
#     #                                                            sizeref=0.2*max(df["% SUCEPTIBLE for BREAKTHROUGH ORIGINAL SEVERE"])/100, 
#     #                                                            color=df["% SUCEPTIBLE for BREAKTHROUGH ORIGINAL SEVERE"], 
#     #                                                            colorscale='Viridis', 
#     #                                                            colorbar=dict(thickness=15, 
#     #                                                                          xanchor='left', 
#     #                                                                          title=dict(text='% Susceptible for Breakthrough Infection', 
#     #                                                                                     font=dict(size=14))))))

#     # Update the layout
#     fig.update_layout(title="COVID Protection Efficacy by Country",
#                       xaxis_title="% People Protected for Severe Disease",
#                       yaxis_title="% People Protected for Infection",
#                       font=dict(size=14),
#                       width=1000, height=800,
#                       margin=dict(l=50, r=0, b=300), xaxis_tickangle=45)
    
#     # Display the chart
#     st.plotly_chart(fig)

# def WHO_region_filter(df):
#     WHO_region_list = df["WHO_REGION"].astype(str).unique().tolist()
#     WHO_region_list.append("ALL")
#     WHO_region_sb = st.sidebar.selectbox('WHO Region:', sorted(WHO_region_list))
#     st.subheader(f'Selected WHO Region: {WHO_region_sb}')
#     return WHO_region_sb

# def strain_filter(df):
#     strain_list = ['ALL', 'ORIGINAL', 'OMICRON']
#     strain_sb = st.sidebar.selectbox('Strains:', sorted(strain_list))
#     st.subheader(f'Selected Strain: {strain_sb}')
#     return strain_sb

# def main():
#     df_original = pd.read_csv("data/Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")

#     df_scatter = pd.DataFrame()
#     df_scatter["COUNTRY"] = df_original["COUNTRY"]
#     df_scatter["WHO_REGION"] = df_original["WHO_REGION"]
#     df_scatter["TOTAL Population"] = df_original["TOTAL Population"]

#     df_scatter[r"% People Protected for ORIGINAL SEVERE"] = df_original[r"% People Protected for ORGINAL SEVERE"]
#     df_scatter[r"% People Protected for ORIGINAL INFECTION"] = df_original[r"% People Protected for ORGINAL INFECTION"]
#     df_scatter[r"% People Protected for OMICRON SEVERE"] = df_original[r"% People Protected for OMICRON SEVERE"]
#     df_scatter[r"% People Protected for OMICRON INFECTION"] = df_original[r"% People Protected for OMICRON INFECTION"]

#     df_scatter[r"% SUCEPTIBLE for BREAKTHROUGH ORIGINAL SEVERE"] = df_original.iloc[:, 17]
#     df_scatter[r"% SUCEPTIBLE for BREAKTHROUGH ORIGINAL INFECTION"] = df_original.iloc[:, 18]
#     df_scatter[r"% SUCEPTIBLE for BREAKTHROUGH OMICRON SEVERE"] = df_original.iloc[:, 19]
#     df_scatter[r"% SUCEPTIBLE for BREAKTHROUGH OMICRON INFECTION"] = df_original.iloc[:, 20]

#     df_scatter = df_scatter.dropna(axis = 0)
#     # st.write(df_scatter)
#     WHO_region = WHO_region_filter(df_scatter)
#     strain_selected = strain_filter(df_scatter)
#     display_bubble(df_scatter, WHO_region, strain_selected)

# if __name__ == '__main__':
#     main()