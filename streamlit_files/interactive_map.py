### REAL-TIME FILTERING: 
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

sub_font = "<style>body {font-family: 'Times New Roman', Times, serif;} </style>"

st.write(f"{sub_font}<h2><u>VISUALIZATION: Project 1</u>    [PAGE 2]</h2>", unsafe_allow_html = True)
st.subheader("Vaccine Global Analysis : Interactive Map Chart")
st.write("For more information, data, and visualization code: [Github link](https://github.com/AliceLiu17/VIsualization-Covid-Efficacy)")
st.write("Feel free to ZOOM IN/ZOOM OUT of the map")
st.write('---')

st.write(f"{sub_font}<h4> <u>Overview of Vaccine Global Analysis </u> </h4>", unsafe_allow_html = True)
st.write("Analysis on where vaccines are administered globally (based on what the user filters) through an interactive map")
st.write(""" 
As stated before, the world rushed to develop and distribute vaccines to the population in order to combat the spread of the virus. 
As a result, from the data we're given, there has been approximately 41 vaccines. An interactive map is developed to indicate where vaccines 
are administered globally.  
""")

st.write(f"{sub_font}<h4><u>Features:</u></h4>", unsafe_allow_html = True)
st.write(""" 
- Filtering: User can filter on the left-hand side by choosing what vaccine they'd like to view in the map.
- Title: will indicate what vaccine was filtered
- Total count: counts the total countries where the filtered vaccine is administered
- Color: Based on the filter you select, the map will color Green for regions where this vaccine is administered
- Hover Feature: interact with the map to see what/where each country is
- Navigating this map: you may zoom in and out of the map
- List: a list of where each vaccine is administered and the total vaccines administered by country

**IMPORTANT FEATURE:** The GeoJson file is 24.1 MB, therefore it will take a few seconds to pull the map with every 
feature and adjustment of the map
""")

st.write(""" 
Overall, this map can help you understnad and visualize the global distribution of vaccines and the impact they have 
in different regions of the world.
""")
         
st.write(f"{sub_font}<h4><u>Some Observations:</u></h4>", unsafe_allow_html = True)
st.write(r"""
- AstraZeneca - Vaxzevria, Moderna - Spikevax, Janssen - Ad26.COV 2-S, and Pfizer BioNTech - Comirnaty are the widest 
distributed vaccine in the world with Pfizer taking the top maximum. 

This now graples the question. What causes the vaccines to be more popularily distributed in comparison to others?

My hypothesis will be based on some basic assumption, which is, the vaccine can be more effective. How will we know?
We can examine columns where it shows % susceptibility. Meaning % of the population who are vaccinated but can still 
be infected. The lower the % the more effective the vaccine is. The higher the % the less effective the vaccine is. 
""")
         
st.write(f"{sub_font}<h4><u>Next Steps:</u></h4>", unsafe_allow_html = True)
st.write(""" 
Viewing what are the widely distributed vaccine can be difficult to view in map, since it is difficult to remember every
value as we filter. 

**NEXT STEPS:** Run file `bubble_chart.py` for easier visualization of vaccine distribution. 
""")
st.write('---')



def display_map(df, vaccine_filter):
    country_filtered = []
    for column in df.iloc[:, 4:15]:
        matching_rows = df[df[column] == vaccine_filter]
        country_filtered.extend(matching_rows["COUNTRY"].unique().tolist())
    country_filtered = list(set(country_filtered)) # remove duplicates
    
    df_country_filtered = pd.DataFrame(country_filtered, columns = ["COUNTRY"])
    df_country_filtered["ISO3"] = df["ISO3"]
    df_country_filtered["Filtered Vaccine Used"] = vaccine_filter

    df_country_filtered_premap = df_country_filtered.copy()
    
    # mapping dictionary
    country_vaccine_dictionary_mapping_for_map = {
        "Anhui ZL - Zifivax" : 0,
        "AstraZeneca - AZD1222" : 1,
        "AstraZeneca - Vaxzevria" : 2,
        "Beijing CNBG - BBIBP-CorV" : 3,
        "Bharat - Covaxin" : 4,
        "Biological E - Corbevax" : 5,
        "CIGB - CIGB-66" : 6,
        "CanSino - Convidecia" : 7,
        "Chumakov - Covi-Vac" : 8,
        "Finlay - Soberana Plus" : 9,
        "Finlay - Soberana-02" : 10,
        "Gamaleya - Gam-Covid-Vac" : 11,
        "Gamaleya - Sputnik V" : 12,
        "Gamaleya - Sputnik-Light" : 13,
        "IMB - Covidful" : 14,
        "Janssen - Ad26.COV 2-S" : 15,
        "Julphar - Hayat-Vax" : 16,
        "Moderna" : 17,
        "Moderna - Spikevax" : 18,
        "Moderna - mRNA-1273" : 19,
        "Moderna Spikevax Bivalent Original/Omicron - Generic" : 20,
        "Moderna Spikevax Bivalent Original/Omicron BA.1" : 21,
        "Novavax - Covavax" : 22,
        "Novavax-NUVAXOVID" : 23,
        "Pfizer BioNTech - Comirnaty" : 24,
        "Pfizer BioNTech - Comirnaty Bivalent Original/Omicron - Generic" : 25, 
        "Pfizer BioNTech - Comirnaty Bivalent Original/Omicron - BA.1" : 26, 
        "Pfizer BioNTech - Comirnaty Bivalent Original/Omicron - BA.4/BA.5" : 27,
        "Pfizer/BioNTech" : 28,
        "RIBSP - QazVac" : 29,
        "SII - Covishield" : 30,
        "SII - Covovax" : 31,
        "SRCVB - EpiVacCorona" : 32,
        "Shenzhen - LV-SMENP-DC" : 33,
        "Shifa - COVIran Barakat" : 34,
        "Sinovac - CoronaVac" : 35,
        "Turkovac" : 36,
        "Unknown Vaccine" : 37,
        "Valneva - VLA2001" : 38,
        "Wuhan CNBG - Inactivated" : 39,
        "Zydus - ZyCov-D" : 40
    }
    # convert string values into int
    df_country_filtered["Filtered Vaccine Used"] = df_country_filtered["Filtered Vaccine Used"].map(country_vaccine_dictionary_mapping_for_map)
    
    map = folium.Map(location = [32, -28], zoom_start = 1, scrollWheelZoom = False, tiles = "CartoDB positron")
    
    choropleth = folium.Choropleth(
        geo_data = "data/countries.geojson",
        data = df_country_filtered,
        columns = ["COUNTRY", "Filtered Vaccine Used"],
        key_on = 'properties.ADMIN',
        fill_color = "YlGn",
        fill_opacity = 0.7,
        line_opacity = 0.4,
        legend_name = 'Filtered Vaccine Used',
        highlight = True
    ).add_to(map)

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['ADMIN'], labels = False)
    )
    st_map = st_folium(map, width = 700, height = 450) # display map
    folium.LayerControl().add_to(map)
    st.write(df_country_filtered_premap)


def filter_vaccine(df):
    # filter on map: filtering based on vaccine type
    # return vaccine list
    vaccine_list = []
    for column in df.iloc[:, 4:15]:
        df[column] = df[column].str.strip()
        vaccine_list.extend(df[column].unique().tolist())
    vaccine_list = list(set(vaccine_list)) # remove duplicates

    # filter side bar: vaccines:
    for column in df.iloc[:, 4:15]: # FIX: spacing issues!!!
        df[column] = df[column].str.strip()
    vaccine_list_for_sidebar = df.iloc[:, 4:15].stack().astype(str).unique().tolist()
    vaccine_sidebar = st.sidebar.selectbox('Vaccine Used:', sorted(vaccine_list_for_sidebar))

    st.subheader(f'Vaccine: {vaccine_sidebar}')
    return vaccine_sidebar


def display_countries_total(df, vaccine_filter):
    country_filtered = []
    for column in df.iloc[:, 4:15]:
        matching_rows = df[df[column] == vaccine_filter]
        country_filtered.extend(matching_rows["COUNTRY"].unique().tolist())
    country_filtered = list(set(country_filtered)) # remove duplicates
    # returns countries that use that specific vaccine
    
    df_country_filtered = pd.DataFrame(country_filtered, columns = ["COUNTRY"])
    df_country_filtered["ISO3"] = df["ISO3"]
    df_country_filtered["Filtered Vaccine Used"] = vaccine_filter

    num_countries = len(df_country_filtered)
    st.write(f'{num_countries} countries')


def main():
    df_original = pd.read_csv("data/Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")
    df_vaccine = pd.read_csv("data/Covid Vaccine Split [FINAL].csv")

    # filter on map: filtering based on vaccine type
    vaccine_filter = filter_vaccine(df_vaccine)
    display_countries_total(df_vaccine, vaccine_filter)
    display_map(df_vaccine, vaccine_filter) # display map

if __name__ == "__main__":
    main()








##### DUMMY VARIABLE WITH MAP:
# import streamlit as st
# import pandas as pd
# import folium
# from streamlit_folium import st_folium

# st.title("Visualization: Project 1")
# st.write("Data and Visualization Code: [Github link](https://github.com/AliceLiu17/Visualization-Project-1)")

# def display_map(df, vaccine_filter):
#     # df_map_filtered = df[df["Vaccine 1"] == vaccine_filter]
#     # df_map_filtered = df[(df["Vaccine 1"] == vaccine_filter) or (df["Vaccine 2"] == vaccine_filter) or (df["Vaccine 3"] == vaccine_filter) or (df["Vaccine 4"] == vaccine_filter) or (df["Vaccine 5"] == vaccine_filter) or (df["Vaccine 6"] == vaccine_filter) or (df["Vaccine 7"] == vaccine_filter) or (df["Vaccine 8"] == vaccine_filter) or (df["Vaccine 9"] == vaccine_filter) or (df["Vaccine 10"] == vaccine_filter) or (df["Vaccine 11"] == vaccine_filter) or (df["Vaccine 12"] == vaccine_filter)]

#     country_filtered = []
#     for column in df.iloc[:, 4:15]:
#         matching_rows = df[df[column] == vaccine_filter]
#         country_filtered.extend(matching_rows["COUNTRY"].unique().tolist())
#     country_filtered = list(set(country_filtered)) # remove duplicates
    
#     df_country_filtered = pd.DataFrame(country_filtered, columns = ["COUNTRY"])
#     df_country_filtered["Filtered Vaccine Used"] = vaccine_filter

#     # mapping dictionary
#     country_vaccine_dictionary_mapping_for_map = {
#         "Anhui ZL - Zifivax" : 0,
#         "AstraZeneca - AZD1222" : 1,
#         "AstraZeneca - Vaxzevria" : 2,
#         "Beijing CNBG - BBIBP-CorV" : 3,
#         "Bharat - Covaxin" : 4,
#         "Biological E - Corbevax" : 5,
#         "CIGB - CIGB-66" : 6,
#         "CanSino - Convidecia" : 7,
#         "Chumakov - Covi-Vac" : 8,
#         "Finlay - Soberana Plus" : 9,
#         "Finlay - Soberana-02" : 10,
#         "Gamaleya - Gam-Covid-Vac" : 11,
#         "Gamaleya - Sputnik V" : 12,
#         "Gamaleya - Sputnik-Light" : 13,
#         "IMB - Covidful" : 14,
#         "Janssen - Ad26.COV 2-S" : 15,
#         "Julphar - Hayat-Vax" : 16,
#         "Moderna" : 17,
#         "Moderna - Spikevax" : 18,
#         "Moderna - mRNA-1273" : 19,
#         "Moderna Spikevax Bivalent Original/Omicron - Generic" : 20,
#         "Moderna Spikevax Bivalent Original/Omicron BA.1" : 21,
#         "Novavax - Covavax" : 22,
#         "Novavax-NUVAXOVID" : 23,
#         "Pfizer BioNTech - Comirnaty" : 24,
#         "Pfizer BioNTech - Comirnaty Bivalent Original/Omicron - Generic" : 25, 
#         "Pfizer BioNTech - Comirnaty Bivalent Original/Omicron - BA.1" : 26, 
#         "Pfizer BioNTech - Comirnaty Bivalent Original/Omicron - BA.4/BA.5" : 27,
#         "Pfizer/BioNTech" : 28,
#         "RIBSP - QazVac" : 29,
#         "SII - Covishield" : 30,
#         "SII - Covovax" : 31,
#         "SRCVB - EpiVacCorona" : 32,
#         "Shenzhen - LV-SMENP-DC" : 33,
#         "Shifa - COVIran Barakat" : 34,
#         "Sinovac - CoronaVac" : 35,
#         "Turkovac" : 36,
#         "Unknown Vaccine" : 37,
#         "Valneva - VLA2001" : 38,
#         "Wuhan CNBG - Inactivated" : 39,
#         "Zydus - ZyCov-D" : 40
#     }
#     # convert string values into int
#     df_country_filtered["Filtered Vaccine Used"] = df_country_filtered["Filtered Vaccine Used"].map(country_vaccine_dictionary_mapping_for_map)



#     st.write(df_country_filtered)
    
#     map = folium.Map(location = [32, -28], zoom_start = 1, scrollWheelZoom = False, tiles = "CartoDB positron")
    
#     choropleth = folium.Choropleth(
#         geo_data = "countries.geo.json",
#         data = df_country_filtered,
#         columns = ["COUNTRY", "Filtered Vaccine Used"],
#         key_on = 'properties.name',
#         fill_color = "YlGn",
#         fill_opacity = 0.7,
#         line_opacity = 0.4,
#         legend_name = 'Filtered Vaccine Used',
#         highlight = True
#     ).add_to(map)

#     choropleth.geojson.add_child(
#         folium.features.GeoJsonTooltip(['name'], labels = False)
#     )

#     st_map = st_folium(map, width = 700, height = 450) # display map

#     folium.LayerControl().add_to(map)


# def filter_vaccine():
#     # filter on map: filtering based on vaccine type
#     # attempt 1: 
#     vaccine_filter_1 = "Sinovac - CoronaVac"
#     # return the country value from column COUNTRY that corresponds to that value
#     country_filtered = []
#     for column in df_vaccine.iloc[:, 4:15]:
#         matching_rows = df_vaccine[df_vaccine[column] == vaccine_filter_1]
#         country_filtered.extend(matching_rows["COUNTRY"].unique().tolist())
#     country_filtered = list(set(country_filtered)) # remove duplicates
#     st.write(country_filtered)



# def main():
#     df_original = pd.read_csv("Covid Protection Efficacy By Country - Averaged Out (FINAL DATASET).csv")
#     df_vaccine = pd.read_csv("Covid Vaccine Split [FINAL].csv")

#     # filter side bar: vaccines:
#     # FIX: spacing issues!!!
#     for column in df_vaccine.iloc[:, 4:15]:
#         df_vaccine[column] = df_vaccine[column].str.strip()

#     vaccine_list = df_vaccine.iloc[:, 4:15].stack().astype(str).unique().tolist()
#     st.sidebar.selectbox('Vaccine Used:', sorted(vaccine_list))
#     # st.write(vaccine_list)

#     # filter on map: filtering based on vaccine type
#     # attempt 1: 
#     vaccine_filter_1 = "Moderna - Spikevax"
#     # return the country value from column COUNTRY that corresponds to that value
#     country_filtered = []
#     for column in df_vaccine.iloc[:, 4:15]:
#         matching_rows = df_vaccine[df_vaccine[column] == vaccine_filter_1]
#         country_filtered.extend(matching_rows["COUNTRY"].unique().tolist())
#     country_filtered = list(set(country_filtered)) # remove duplicates
#     # st.write(country_filtered)

#     #filter_vaccine_df = df_vaccine[(df_vaccine["Vaccine 1"] == vaccine_filter_1) or (df_vaccine["Vaccine 2"] == vaccine_filter_1) or (df_vaccine["Vaccine 3"] == vaccine_filter_1) or (df_vaccine["Vaccine 4"] == vaccine_filter_1) or (df_vaccine["Vaccine 5"] == vaccine_filter_1) or (df_vaccine["Vaccine 6"] == vaccine_filter_1) or (df_vaccine["Vaccine 7"] == vaccine_filter_1) or (df_vaccine["Vaccine 8"] == vaccine_filter_1) or (df_vaccine["Vaccine 9"] == vaccine_filter_1) or (df_vaccine["Vaccine 10"] == vaccine_filter_1) or (df_vaccine["Vaccine 11"] == vaccine_filter_1) or (df_vaccine["Vaccine 12"] == vaccine_filter_1)]
#     display_map(df_vaccine, vaccine_filter_1) # display map

# if __name__ == "__main__":
#     main()
