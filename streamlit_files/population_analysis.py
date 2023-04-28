import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

sub_font = "<style>body {font-family: 'Times New Roman', Times, serif;} </style>"

st.write(f"{sub_font}<h2><u>VISUALIZATION: Project 1</u>    [PAGE 1]</h2>", unsafe_allow_html = True)
st.subheader("Population Analysis : Bar Chart")
st.write("For more information, data, and visualization code: [Github link](https://github.com/AliceLiu17/VIsualization-Covid-Efficacy)")
st.write("**HOVER FOR 2 ARROW PINCHING BUTTON: TO ENTER FULL SCREEN TO VIEW FULL DATA!**")
st.write('---')

st.write(""" 
In the year of 2020, the world was thrusted a global pandemic caused by COVID-19. COVID-19 has made signficant impact on 
daily life around the world, causing a worldwide lockdown of public spaces and closure of businesses. The disease was fatal 
to ones health. One's health varied with mild symptoms and/or death. Since then there has been strain variations from the 
original variation. Such strains are BA1.n which was is a sub-lineage of SAR-CoV-2 and Omicron. 

As the world continues to fight the COVID-19 pandemic, vaccines have been developed and distributed to countries around 
the globe. While the vaccines have shown to be effective in reducing the number of severe cases, hospitalizations, and 
deaths from the virus, breakthrough infections have been reported in some vaccinated individuals.

A possible explanation for breakthrough infections is the percentage of the population that has not been vaccinated.
""")

st.write(f"{sub_font}<h4> <u>Overview of % Vaccinated vs. Non-Vaccinated </u> </h4>", unsafe_allow_html = True)
st.write(r""" 
The Population analysis: the bar chart that shows % of population vaccinated and % not vaccinated in each country
this will help us see the overall vaccination coverage in different regions and countries. 
""")
         
st.write(f"{sub_font}<h4><u>Features:</u></h4>", unsafe_allow_html = True)
st.write(""" 
- Filtering: User can filter by choosing which WHO_region they'd like to view in the map.
- Legend: 
    - Blue = % population not vaccinated
    - Orange = % population vaccinated
- Hover: % population information of each country
""")
         
st.write(f"{sub_font}<h4><u>Some Observations:</u></h4>", unsafe_allow_html = True)
st.write(r"""
It's important for countries to prioritize the efforts in vaccinating the general public to increase the number
of vaccination to reduce the breakthrough infections. The following are observations of the bar chart and personal
speculations:

**AFRO Region:**

- Many regions have a higher % of being non-vaccinated in comparison to being vaccinated
- Seycellas, Saint Helena, Mauritius are the countries who has a higher % of being vaccinated than non-vaccinated
- One can speculate: 
    - Supply: many countries in this region had less vaccinated people due to struggles to secure adequate vaccine 
    supplies and therefore have a lower vaccination rate.
    - Pharamcuetical location: majority of the COVID-19 vaccines are produced by a small number of pharmaceutical companies, 
    many of which are located in high-income countries. These companies have limited production capacity 
    and have prioritized meeting the demand in their own countries before exporting vaccines to other regions.
        - Ex. Moderna, Pfizer, Janseen are popular vaccines produced by US (AMRO region)
        - Ex. AstraZeneca another popular vaccine produced by England (EURO region)
    - Health Systems: some countries in the AFRO region have weak health systems, which can make it challenging 
    to distribute and administer vaccines efficiently. This can impact the ability to secure adequate vaccine supplies.
    - Country Wealth: wealth of the countries in this region could struggle with accessing secure vaccine supplies. 
    
**AMRO Region:**

- Many regions have a higher % of being vaccinated in comparison to being non-vaccinated
- Sint Maarten, Saba, Puerto Rico, Martinique, Haiti, Guadeloupe, and Bahamas are the countries that has a higher %
of being non-vaccinated
- One can speculate:
    - Pharamcuetical location: as supported from the speculation above, many of the pharamceutical companies will 
    produce and distribute to meet the demands of their own countries. Therefore, we see countries in the AMRO 
    region have a higher % of their population being vaccinated. 
    - Rapid response: many countries in the AMRO region acted early to secure vaccine supplies and develop distribution plans. 
    For example, Chile negotiated early and aggressively with vaccine manufacturers and has one of the highest 
    vaccination rates in the world.
    - Manufacturing capacity: several countries in the AMRO region, such as Brazil and Mexico, have a strong pharmaceutical 
    industry and manufacturing capacity, which has allowed them to produce vaccines domestically or enter into manufacturing 
    partnerships with vaccine developers.
    - Country Wealth: the countries in the AMRO region generally have higher incomes and stronger economies than countries
    in other regions, which allows them to invest more in healthcare and vaccine procurement.

**EMRO Region:**

- The countries in this region is pretty evenly split in terms of % vaccinated vs. % non-vaccinated
- One can speculate:
    - Vaccine Accessibility: countries in the EMRO region may have relatively equal access to vaccines, with neither the 
    wealthy nor the poor having a significant advantage in terms of vaccine distribution. This could result in a more even 
    split in terms of who is vaccinated and who is not.
    - Hesitancy: individuals may be hesitant or unwilling to get vaccinated due to various reasons such as mistrust, fear, or 
    misinformation

**EURO Region:**

- Countries in this region have higher % of being vaccinated in comparison to being non-vaccinated
- Bulgaria, Republic of Moldavia, Romania, Kyrgyzstan, Bosnia are the countires has a higher % of being
non-vaccinated
- One can speculate:
    - Healthcare Accessibility: many countries in the EURO region have centralized healthcare systems and universal healthcare 
    coverage, which has made it easier to reach and vaccinate large portions of the population.
    - Vaccine Accessibility: many of these countries were able to secure a large number of vaccine doses early on in the vaccine rollout.
    For example, in early of the pandemic, France was heavily impacted by the virus before US was. Vaccine rollout was probably a high 
    priority for the French government. 

**OTHER Region:**

- Liechtenstein's population has a higher % of being vaccinated with 68.01%

**SEARO Region:**

- All countries in this region has their population being more vaccinated than non-vaccinated

**WPRO Region:**

- Countries in this region have higher % of being vaccinated in comparison to being non-vaccinated
- Papua New Guinea, Palau, Northen Mariana Islands,Micronesia, Marshall Islands, Guam, and Samoa are 
the countires has a higher % of being non-vaccinated
""")
         
st.write(f"{sub_font}<h4><u>Next Steps:</u></h4>", unsafe_allow_html = True)
st.write(""" 
Now let's examine what vaccines were popularly distributed. Run file `interactive_map.py`  
""")
st.write('---')


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
                                    "Country: %{customdata[2]}<br>" +
                                    "Total Population: %{customdata[3]}<br>" +
                                    "%{customdata[0]} of population not vaccinated<br>" +
                                    "%{customdata[1]} of population vaccinated")
    fig.update_traces(customdata=np.stack((filtered_df[r"% Population NOT VACCINATED"], 
                                            filtered_df[r"% Population vaccinated"],
                                            filtered_df["COUNTRY"],
                                            filtered_df["TOTAL Population"]), axis=-1))

    fig.update_layout(height = 2200, 
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
