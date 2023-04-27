import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Population analysis: 
# bar chart that shows % of population vaccinated and not vaccinated in each country
# this will help us see the overall vaccination coverage in different regions and countries
# we will filter the bar chart through filtering the WHO_region

st.title("Visualization: Project 1")
st.subheader("Population Analysis : Bar Chart")
st.write("For more information, data, and visualization code: [Github link](https://github.com/AliceLiu17/VIsualization-Covid-Efficacy)")
st.write("\n")
st.write("Bubble chart of unique vaccines and amount of countries using each vaccine")
st.write("HOVER FOR 2 ARROW PINCHING BUTTON: TO ENTER FULL SCREEN TO VIEW FULL DATA!")

def display_population_bar(df, WHO_region):
    filtered_df = df[df["WHO_REGION"] == WHO_region]
    colors = {'% Population NOT VACCINATED': '#1f77b4', '% Population vaccinated': '#ff7f0e'}

    fig = px.bar(filtered_df, 
                 y = "COUNTRY", 
                 x = [r"% Population NOT VACCINATED", r"% Population vaccinated"], 
                 barmode="group",
                 color_discrete_map = colors,
                 hover_name="COUNTRY",
                 labels={
                     r"% Population NOT VACCINATED": "% Population Not Vaccinated",
                     r"% Population vaccinated": "% Population Vaccinated",
                 })
    fig.update_traces(hovertemplate="<b>%{x}</b><br>" +
                                     "%{customdata[0]} of population not vaccinated<br>" +
                                     "%{customdata[1]} of population vaccinated<br>")
    fig.update_traces(customdata=np.stack((filtered_df[r"% Population NOT VACCINATED"], 
                                            filtered_df[r"% Population vaccinated"]), axis=-1))

    fig.update_layout(height = 1800, 
                      width = 1200, 
                      margin=dict(l=50, r=20, t=50, b=50),
                      )
    st.plotly_chart(fig)

def WHO_region_filter(df):
    WHO_region_list = df["WHO_REGION"].astype(str).unique().tolist()
    WHO_region_sb = st.selectbox('WHO Region:', sorted(WHO_region_list))
    st.subheader(f'Selected WHO Region: {WHO_region_sb}')
    return WHO_region_sb

def main():
    df_original = pd.read_csv("data/Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")

    df_population = df_original.iloc[:, 0:3].copy()
    df_population["Number of vaccine types used"] = df_original["NUMBER_VACCINES_TYPES_USED"]
    df_population["TOTAL Population"] = df_original["TOTAL Population"]
    df_population["Population Vaccinated"] = df_original["Population Vaccinated"]
    df_population[r"% Population vaccinated"] = df_original[r"% Population vaccinated"]
    df_population[r"% Population NOT VACCINATED"] = df_original[r"% Population NOT VACCINATED"]

    WHO_region = WHO_region_filter(df_original)
    display_population_bar(df_original, WHO_region)


if __name__ == "__main__":
    main()









# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px

# # Population analysis: 
# # bar chart that shows % of population vaccinated and not vaccinated in each country
# # this will help us see the overall vaccination coverage in different regions and countries
# # we will filter the bar chart through filtering the WHO_region

# def display_population_bar(df, WHO_region):
#     filtered_df = df[df["WHO_REGION"] == WHO_region]
#     colors = {'% Population NOT VACCINATED': '#1f77b4', '% Population vaccinated': '#ff7f0e'}


#     fig = px.bar(filtered_df, 
#                  y = "COUNTRY", 
#                  x = [r"% Population NOT VACCINATED", r"% Population vaccinated"], 
#                  barmode="group",
#                  color_discrete_map = colors,
#                  hover_name="COUNTRY",
#                  labels={
#                      r"% Population NOT VACCINATED": "% Population Not Vaccinated",
#                      r"% Population vaccinated": "% Population Vaccinated",
#                  })
#     fig.update_traces(hovertemplate="<b>%{x}</b><br>" +
#                                      "%{customdata[0]} of population not vaccinated<br>" +
#                                      "%{customdata[1]} of population vaccinated<br>")
#     fig.update_traces(customdata=np.stack((filtered_df[r"% Population NOT VACCINATED"], 
#                                             filtered_df[r"% Population vaccinated"]), axis=-1))
#     fig.update_traces(
#         width = 0.3 # increase the thickness of the bar outlines
#     )

#     fig.update_layout(height = 1800, 
#                       width = 1200, 
#                       margin=dict(l=50, r=20, t=50, b=50),
#                       bargap=0.5)
#     st.plotly_chart(fig)

# def WHO_region_filter(df):
#     WHO_region_list = df["WHO_REGION"].astype(str).unique().tolist()
#     WHO_region_sb = st.selectbox('WHO Region:', sorted(WHO_region_list))
#     st.subheader(f'Selected WHO Region: {WHO_region_sb}')
#     return WHO_region_sb

# def main():
#     df_original = pd.read_csv("Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")

#     df_population = df_original.iloc[:, 0:3].copy()
#     df_population["Number of vaccine types used"] = df_original["NUMBER_VACCINES_TYPES_USED"]
#     df_population["TOTAL Population"] = df_original["TOTAL Population"]
#     df_population["Population Vaccinated"] = df_original["Population Vaccinated"]
#     df_population[r"% Population vaccinated"] = df_original[r"% Population vaccinated"]
#     df_population[r"% Population NOT VACCINATED"] = df_original[r"% Population NOT VACCINATED"]

#     WHO_region = WHO_region_filter(df_original)
#     display_population_bar(df_original, WHO_region)


# if __name__ == "__main__":
#     main()








# vertical
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px

# # Population analysis: 
# # stacked bar chart that shows % of population vaccinated and not vaccinated in each country
# # this will help us see the overall vaccination coverage in different regions and countries
# # we will filter the stacked bar chart through filtering the WHO_region

# def display_population_stack(df, WHO_region):
#     filtered_df = df[df["WHO_REGION"] == WHO_region]
#     colors = {'% Population NOT VACCINATED': '#1f77b4', '% Population vaccinated': '#ff7f0e'}


#     fig = px.bar(filtered_df, 
#                  y = "COUNTRY", 
#                  x = [r"% Population NOT VACCINATED", r"% Population vaccinated"], 
#                  barmode="stack",
#                  color_discrete_map = colors,
#                  hover_name="COUNTRY",
#                  labels={
#                      r"% Population NOT VACCINATED": "% Population Not Vaccinated",
#                      r"% Population vaccinated": "% Population Vaccinated",
#                  })
#     fig.update_traces(hovertemplate="<b>%{x}</b><br>" +
#                                      "%{customdata[0]} of population not vaccinated<br>" +
#                                      "%{customdata[1]} of population vaccinated<br>")
#     fig.update_traces(customdata=np.stack((filtered_df[r"% Population NOT VACCINATED"], 
#                                             filtered_df[r"% Population vaccinated"]), axis=-1))

#     fig.update_layout(height = 1100, width = 1200, margin=dict(l=50, r=20, t=50, b=50))
#     st.plotly_chart(fig)

# def WHO_region_filter(df):
#     WHO_region_list = df["WHO_REGION"].astype(str).unique().tolist()
#     WHO_region_sb = st.selectbox('WHO Region:', sorted(WHO_region_list))
#     st.subheader(f'Selected WHO Region: {WHO_region_sb}')
#     return WHO_region_sb

# def main():
#     df_original = pd.read_csv("Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")

#     df_population = df_original.iloc[:, 0:3].copy()
#     df_population["Number of vaccine types used"] = df_original["NUMBER_VACCINES_TYPES_USED"]
#     df_population["TOTAL Population"] = df_original["TOTAL Population"]
#     df_population["Population Vaccinated"] = df_original["Population Vaccinated"]
#     df_population[r"% Population vaccinated"] = df_original[r"% Population vaccinated"]
#     df_population[r"% Population NOT VACCINATED"] = df_original[r"% Population NOT VACCINATED"]

#     WHO_region = WHO_region_filter(df_original)
#     display_population_stack(df_original, WHO_region)


# if __name__ == "__main__":
#     main()
