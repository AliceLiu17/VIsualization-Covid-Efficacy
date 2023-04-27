# Covid-Visualization-Project

---

Utilize streamlit application to provide a user interface with the visualization. 

To run streamlit, on the terminal enter: `streamlit run ___` (the ___ is the file path/python file)
- For instance: to run `interactive_map.py` enter `streamlit run streamlit-fileinteractive_map.py`

Overview of each streamlit file:
- `interactive_map.py` = where the vaccines are administered globally; users are able to filter the vaccine on the map to see where each vaccine is located. User has the ability to zoom in and out of the map
  - To run `interactive_map.py` enter `streamlit run streamlit_files/interactive_map.py`
  - **WARNING:** The GeoJson file is 24.1 MB. Therefore, the application may be slow to run it. Make sure you don't have many files open.

- `bubble_chart.py` = bubble chart where the relative size of the bubble is indicated by the number of countries that uses each vaccine. 
  - To run `bubble_chart.py` enter `streamlit run streamlit_files/bubble_chart.py`

- `population_analysis.py` = stacked bar chart that shows % of population vaccinated and not vaccinated in each country this will help us see the overall vaccination coverage in different regions and countries
  - To run `population_analysis.py` enter `streamlit run streamlit_files/population_analysis.py`
