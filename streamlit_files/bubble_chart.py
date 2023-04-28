import streamlit as st
import pandas as pd
import plotly.express as px

sub_font = "<style>body {font-family: 'Times New Roman', Times, serif;} </style>"

st.write(f"{sub_font}<h2><u>VISUALIZATION: Project 1</u>    [PAGE 3]</h2>", unsafe_allow_html = True)
st.subheader("Vaccine Global Analysis : Bubble Chart")
st.write("For more information, data, and visualization code: [Github link](https://github.com/AliceLiu17/VIsualization-Covid-Efficacy)")
st.write("**HOVER FOR 2 ARROW PINCHING BUTTON: TO ENTER FULL SCREEN TO VIEW FULL DATA!**")
st.write('---')

st.write(f"{sub_font}<h4> <u>Overview of Vaccine Global Analysis (Bubble Chart) </u> </h4>", unsafe_allow_html = True)
st.write("Analysis on where vaccines are administered globally (based on what the user filters) through the view of bubble chart")
st.write("The idea behind this chart is the same as `interactive_map.py` but easier visualization of the size differences.")

st.write(f"{sub_font}<h4><u>Features:</u></h4>", unsafe_allow_html = True)
st.write(""" 
- No Filtering: the goal of this visualization is to see what vaccine is the most popular by examining the size of the bubble
- Bubbles: when you hover over each bubble you'll see the vaccine name followed by its corresponding # of countries who use it
    - The x-axis is the unique vaccine string object values from column VACCINES_USED 
    - The y-axis is the # of countries that use that corresponding vaccine
    - Size of bubble is the # of countries that use that corresponding vaccine (the bigger the bubble, the higher distribution of the vaccine)
- Color: All 41 vaccines correspond to a color as indicated by the legend on the right-hand side
- Navigating this chart: click on full-screen button (2 arrow pinching) when hovering over the chart to have a better view of the data
- List: a list of where each vaccine is administered and the total vaccines administered by country
""")
         
st.write(f"{sub_font}<h4><u>Some Observations:</u></h4>", unsafe_allow_html = True)
st.write(r"""
As stated before: My hypothesis remains the same, the more effective the vaccine is, the more popular distribution it is. 

- AstraZeneca - Vaxzevria, Moderna - Spikevax, Janssen - Ad26.COV 2-S, and Pfizer BioNTech - Comirnaty are the widest 
distributed vaccine in the world with Pfizer taking the top maximum. 
""")
         
st.write(f"{sub_font}<h4><u>Next Steps:</u></h4>", unsafe_allow_html = True)
st.write(""" 
Let's examine if our hypothesis is correct. Analyzing the percentage of breakthrough cases for each country can provide additional 
information on the effectiveness of the vaccines in that country. Run file `heatmap_breakthrough.py`  
""")
st.write('---')


def main():
    df_original = pd.read_csv("data/Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")
    df_vaccine_total_country = pd.read_csv("data/Vaccine_total_countries.csv")

    df_vaccine_total_country["WHO Region"] = df_original["WHO_REGION"]

    custom_colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', 
                     '#e5c494', '#b3b3b3', '#8dd3c7', '#bebada', '#fb8072', '#80b1d3', 
                     '#fdb462', '#b15928', '#ccebc5', '#ffed6f', '#ffffb3', '#b2df8a', 
                     '#1f78b4', '#33a02c', '#fb9a99', '#6a3d9a', '#cab2d6', '#fdbf6f', 
                     '#ff7f00', '#bcbd22', '#17becf', '#f03b20', '#1f77b4', '#aec7e8', 
                     '#ffbb78', '#2ca02c', '#ff9896', '#98df8a', '#d62728', '#ff9896', 
                     '#9467bd', '#c5b0d5', '#8c564b', '#c49c94', '#e377c2', '#7f7f7f', 
                     '#bcbd22', '#dbdb8d', '#17becf']


    fig = px.scatter(df_vaccine_total_country, x = 'Vaccine', y = '# of countries use vaccine',
                     size_max = 90, size = '# of countries use vaccine', 
                     color = 'Vaccine',
                     color_discrete_sequence=custom_colors,
                     color_continuous_scale='Greens',
                     range_color=[20, 100],
                     title = 'Total Number of Countries Using Each Vaccine')
    
    fig.update_layout(xaxis_title='Vaccine', yaxis_title='Number of Countries',
                      legend_title='Number of Countries', font=dict(size=12),
                      xaxis_tickfont_size=12, width=1000, height=800,
                      margin=dict(l=50, r=0, b=300), xaxis_tickangle=45)
    
    st.plotly_chart(fig)

    st.write("\n")
    st.write("Dataset: ")
    st.write("\n")
    st.write(df_vaccine_total_country)

if __name__ == "__main__":
    main()








# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.title("Visualization: Project 1")
# st.write("For more information, data, and visualization code: [Github link](https://github.com/AliceLiu17/Visualization-Project-1)")
# st.write("Bubble chart of unique vaccines and amount of countries using each vaccine")

# def main():
#     df_original = pd.read_csv("Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")
#     df_vaccine_total_country = pd.read_csv("Vaccine_total_countries.csv")
#     st.write(df_vaccine_total_country)

#     df_vaccine_total_country["WHO Region"] = df_original["WHO_REGION"]

#     fig = px.scatter(df_vaccine_total_country, x = 'Vaccine', y = '# of countries use vaccine',
#                      size_max = 90, size = '# of countries use vaccine', 
#                      color = '# of countries use vaccine',
#                      color_continuous_scale='Greens',
#                      range_color=[20, 100],
#                      title = 'Total Number of Countries Using Each Vaccine')
    
#     fig.update_layout(xaxis_title='Vaccine', yaxis_title='Number of Countries',
#                       legend_title='Number of Countries', font=dict(size=12),
#                       xaxis_tickfont_size=12, width=1000, height=800,
#                       margin=dict(l=50, r=0, b=300), xaxis_tickangle=45)
    
#     fig.show()

# if __name__ == "__main__":
#     main()




# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.title("Visualization: Project 1")
# st.write("For more information, data, and visualization code: [Github link](https://github.com/AliceLiu17/Visualization-Project-1)")
# st.write("Bubble chart of unique vaccines and amount of countries using each vaccine")

# def filter_vaccine(df):
#     # filter on map: filtering based on vaccine type
#     # return vaccine list
#     vaccine_list = []
#     for column in df.iloc[:, 4:15]:
#         df[column] = df[column].str.strip()
#         vaccine_list.extend(df[column].unique().tolist())
#     vaccine_list = list(set(vaccine_list)) # remove duplicates

#     # filter side bar: vaccines:
#     for column in df.iloc[:, 4:15]: # FIX: spacing issues!!!
#         df[column] = df[column].str.strip()
#     vaccine_list_for_sidebar = df.iloc[:, 4:15].stack().astype(str).unique().tolist()
#     vaccine_sidebar = st.sidebar.selectbox('Vaccine Used:', sorted(vaccine_list_for_sidebar))

#     return vaccine_sidebar

# def main():
#     df_original = pd.read_csv("Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")
#     df_vaccine = pd.read_csv("Covid Vaccine Split [FINAL].csv")

#     # filter on map: filtering based on vaccine type
#     vaccine_filter = filter_vaccine(df_vaccine)

#     country_filtered = []
#     for column in df_vaccine.iloc[:, 4:15]:
#         matching_rows = df_vaccine[df_vaccine[column] == vaccine_filter]
#         country_filtered.extend(matching_rows["COUNTRY"].unique().tolist())
#     country_filtered = list(set(country_filtered)) # remove duplicates
    
#     df_country_filtered = pd.DataFrame(country_filtered, columns = ["COUNTRY"])
#     df_country_filtered["ISO3"] = df_vaccine["ISO3"]
#     df_country_filtered["Filtered Vaccine Used"] = vaccine_filter

#     df_bubble = df_country_filtered.groupby("Filtered Vaccine Used")["COUNTRY"].nunique().reset_index()
#     df_bubble = df_bubble.rename(columns={"Filtered Vaccine Used": "unique vaccine", "COUNTRY": "total countries"})

#     st.write(df_bubble)

# if __name__ == "__main__":
#     main()
