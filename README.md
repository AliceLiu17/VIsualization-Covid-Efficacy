# Covid-Visualization-Project

---

Utilize streamlit application to provide a user interface with the visualization. 

To run streamlit, on the terminal enter: `streamlit run ___` (the ___ is the file path/python file)
- For instance: to run `interactive_map.py` enter `streamlit run streamlit-fileinteractive_map.py`

**PLEASE NOTE: The screen for streamlit can be small, and scrolling can be tiring. Which is why when you hover over the graphs you see options to zoom, pan, etc. Best viewing option is to click on the 2 arrow button to enter FULL SCREEN MODE**

**If you want to filter, please exit FULL SCREEN mode and adjust filter**

---
### Overview of each streamlit file:
Please run and view these files in the order it is listed below (the story progresses this way):

1. `population_analysis.py` = bar chart that shows % of population vaccinated and not vaccinated in each country this will help us see the overall vaccination coverage in different regions and countries
  - To run `population_analysis.py` enter `streamlit run streamlit_files/population_analysis.py` 

2. `interactive_map.py` = where the vaccines are administered globally; users are able to filter the vaccine on the map to see where each vaccine is located. User has the ability to zoom in and out of the map
  - To run `interactive_map.py` enter `streamlit run streamlit_files/interactive_map.py`
  - **WARNING:** The GeoJson file is 24.1 MB. Therefore, the application may be slow to run it. Make sure you don't have many files open.

3. `bubble_chart.py` = bubble chart where the relative size of the bubble is indicated by the number of countries that uses each vaccine. 
  - To run `bubble_chart.py` enter `streamlit run streamlit_files/bubble_chart.py`

4. `heatmap_breakthrough.py` = Analyzing % of breakthrough cases for each country based on vaccine used analyzing to see countries with high breakthrough rates and other countries who use the same vaccine. We want to filter based on strains, WHO_region, and Brand
  - To run `heatmap_breakthrough.py` enter `streamlit run streamlit_files/heatmap_breakthrough.py`

5. `bubble_scatter_protection_susceptible.py` = Analyzing which countries have low and high levels of protection against severe disease and infection, and how these levels of protection relation to the size of the population. The size of the bubbles will help us understand which countries have larger populations that are potentially at risk for breakthrough infections. The color coding of the bubbles by WHO region can help you understand how different regions of the world are performing in terms of vaccine efficacy and breakthrough infections. It can also help you identify areas where more attention or resources may be needed to improve vaccine distribution or effectiveness. 
  - To run `bubble_scatter_protection_susceptible.py` enter `streamlit run streamlit_files/bubble_scatter_protection_susceptible.py`