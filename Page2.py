import streamlit as st
import pandas as pd
import geopandas as gpd 

def landuse_colour(text):
    if text == 1:
        return "#FFFF00"
    elif text == 3:
        return "#6699CD"
    elif text == 4:
        return "#686868"
    elif text == 5:
        return "#EB4D52"
    elif text == 6:
        return "#F57AB6"
    elif text == 7:
        return "#2769BA"
    elif text == 8:
        return "#7AB6F5"
    elif text == 9:
        return "#4CE600"
    elif text == 10:
        return "#7AF5CA"
    elif text == 11:
        return "#E69800"
    elif text == 12:
        return "#755913"
    elif text == 13:
        return "#FFFFAF"
    elif text == 14:
        return "#343434"
    elif text == 15:
        return "#008B43"
    elif text == 16:
        return "#D1BA90"
    elif text == 18:
        return "#8400A8"
    elif text == 20:
        return "#A6D900"
    elif text == 21:
        return "#FBD900"
    else:
        return "#CCCCCC"
    
st.title("Current Condition; Town and surrounding")

env_expander = st.sidebar.expander("Environmental Condition")


population = pd.read_excel("Demography_pop.xlsx")
population_rate = pd.read_excel("Demography_poprate.xlsx")
age_sex85 = pd.read_excel("85_agesex.xlsx")
age_sex90 = pd.read_excel("90_agesex.xlsx")
age_sex95 = pd.read_excel("95_agesex.xlsx")
interpersonal_trust = pd.read_excel("interpersonal_trust.xlsx")
instutitional_trust = pd.read_excel("instutitional_trust.xlsx")
all_trust = pd.read_excel("all_trust.xlsx")
communication = pd.read_excel("communication.xlsx")
formal_participation = pd.read_excel("formal_participation.xlsx")
informal_participation = pd.read_excel("informal_participation.xlsx")
all_participation = pd.read_excel("all_participation.xlsx")
social_capital = pd.read_excel("social_capital.xlsx")
resilience = pd.read_excel("resilience.xlsx")
people_issues_file = pd.read_excel("people_issues.xlsx")


general_economic_table = "General_Economic.xlsx"
economic_sectors_table = "Economic_Sectors.xlsx"
tourists_table = "Tourists.xlsx"
hotels = "Hotels.xlsx"

landcover_file = pd.read_excel("Landcover.xlsx")
landcover_df = pd.DataFrame(landcover_file)
landcover_df["percentage (%)"] = landcover_df["percentage (%)"]*100
water_file = pd.read_excel("water_supply.xlsx")
water_consumption = pd.read_excel("water_consumption.xlsx")
precipitation = pd.read_excel("precipitation.xlsx")
landuse_raw_table = "landuse.xlsx"
parcels = "Parcels.xls"
building_direction = "Building_Direction.xlsx"
building_toode = "Building_Toodeh.xlsx"
building_toode_dimension = "Building_Toodeh_Dimension.xlsx"
roads_traffic = "Roads_Traffic.xlsx"
roads_traffic_barchart = "Roads_Traffic_BarChart.xlsx"
roads_width = "Roads_Width.xlsx"
roads_slop = "Roads_Slop.xlsx"


landcover = env_expander.toggle("Land Cover")
if landcover:
    st.header("Land Cover", divider="orange")

    st.markdown("""**84% of the area's land is covered by agriculture.
                Tree cover and water surface have the lowest percentage of coverage.
                :green[Soltaniyeh pasture] with 721 hectares covers approximately 3.1% of the area.**""")
    st.image("Harim_Mojoud_C.jpg")
    #st.table(landcover_df)
    st.bar_chart(landcover_df, x="land cover", y="percentage (%)")

water_resource = env_expander.toggle("Water Resource")
if water_resource:
    st.header("Water Resources", divider="orange")

    st.markdown("""According to the latest report of the Zanjan Province Water and Wastewater Company, the urban water resources of 
                Soltaniyeh city (which is the only urban point in Soltaniyeh county) are a borehole.
                The volume of groundwater resources for urban water supply (in 2022) is stated to be :orange[**0.94 million cubic meters 
                per year**].""")
    st.write("This table demonstrates the volume of total water resources and the amount produced in recent years.")
    st.table(water_file)
    st.markdown("According to accessible information, the main part of the water resources is used for agriculture.")
    st.table(water_consumption)
    st.markdown("**This map depicts how :blue[phreatic surface] has been decreasing during recent years**.")
    st.image("Kahesh_Salane_SathAab.jpg")
    
climatic_factors = env_expander.toggle("Climatic Factors")
if climatic_factors:
    st.header("Climatic Factors", divider="orange")
    st.write("**The average maximum daily temperature between 2006 and 2017 was :red[*+17.9 C*].**")
    st.write("**The average daily temperature between 2006 and 2017 was :orange[*+11.8 C*].**") 
    st.write("**The average minimum daily temperature between 2006 and 2017 was :gray[*+2.5 C*].**") 
    st.write("**The average daily precipitation between 2006 and 2017 was :blue[*0.8 mm*].**") 
    st.write("**:green[***Spring***] is the rainiest season of the year.**") 
    st.write("This line graph shows yearly precipitation over a period of 2006-2017.")
    st.line_chart(precipitation, x="year", y="precipitation (mm)", y_label="Total precipitation during a year (mm)")
    st.divider()
    st.write("**The average total number of annual frost days between 2006 and 2017 was :blue[***137 days***].**")
    st.write("**The average annual relative humidity percentage between 2006 and 2017 was :red[***52 percent***].**")
    st.write("**The average daily wind speed between 2006 and 2017 was :violet[***3.8 knots***].**")
    st.divider()
    st.image("Jauary.jpg", caption="Shadows in the January mornings in plots with a northeast-southwest extension (approximate direction of the Qibla)")
    st.image("January_afternoon.jpg", caption="Shadows in the January evenings in plots with a east-west extension (approximate direction of the Kerman)")
    
    # st.markdown("""**The distance from the :red[Soltaniyeh fault] (approximately 140 km long) to the town is almost 8 km. 
    #             This fault is located in the south and southeast of Soltaniyeh.**""")
    
demographic_expander = st.sidebar.expander("Sociodemographic Condition")
general_info = demographic_expander.selectbox("General Demographic Information", options=["Population", "Population Trends",
                                                                              "Age-Sex Pyramid", "Population Density"], 
                                              index=None,
                               placeholder="Select the item from this list")
if general_info == "Population":
    st.header("Population", divider="orange")
    colors=["#E64C00", "#2769BA", "#7D1919", "#7AF5CA"]
    st.table(population)
    columns = st.columns(4)
    for idx,row in population.iterrows():
        columns[idx].line_chart(row, x_label=row["Title"], color=colors[idx])
if general_info == "Population Trends":
    st.header("Population Trends", divider="orange")
    colors=["#E64C00", "#2769BA", "#7D1919", "#7AF5CA"]
    st.table(population_rate)
    columns = st.columns(4)
    for idx,row in population_rate.iterrows():
        columns[idx].line_chart(row, x_label=row["Title"], color=colors[idx])    
if general_info == "Age-Sex Pyramid":
    st.header("Age-Sex Pyramids", divider="orange")
    st.caption("**Age-Sex Pyramid - 2005**")
    age_sex_85_table = st.table(age_sex85)
    age_sex_85_chart = st.bar_chart(age_sex85, x="Age groups", y=["Men (population)", "Women (population)"], 
                                    x_label="Population", color=["#7D1919", "#2769BA"], horizontal=True, stack="center")
    st.caption("**Age-Sex Pyramid - 2010**")
    age_sex_90_table = st.table(age_sex90)
    age_sex_90_chart = st.bar_chart(age_sex90, x="Age groups", y=["Men (population)", "Women (population)"], 
                                    x_label="Population", color=["#7D1919", "#2769BA"], horizontal=True, stack="center")  
    st.caption("**Age-Sex Pyramid - 2015**")
    age_sex_95_table = st.table(age_sex95)
    age_sex_95_chart = st.bar_chart(age_sex95, x="Age groups", y=["Men (population)", "Women (population)"], 
                                    x_label="Population", color=["#7D1919", "#2769BA"], horizontal=True, stack="center") 
if general_info == "Population Density":
    st.header("Population Density", divider = "orange")

    st.subheader("Gross Population Density - 2015")
    st.image("Tarakom_Jamiati_Nakhales.jpg")
    st.subheader("Gross Population Density - 2005")
    st.image("Tarakom_Jamiati_Nakhales85.jpg")
    st.subheader("Gross Population Density in Neighbourhoods") 
    st.image("Tarakom_Jamiati_Mahallat.jpg") 

social_info = demographic_expander.selectbox("Societal Information", options=["Trust Index", "Social Communication",
                                                                              "Social Participation", "Social Capital",
                                                                              "Resilience Index"],
                                             placeholder="Select from this list", index=None)

if social_info == "Trust Index":
    st.header("Trust Index", divider="orange")
    st.write("This index is made up of two indices: **interpersonal trust** and **institutional trust**. Interpersonal trust refers to trust in friends, acquaintances, and family, and institutional trust refers to trust in government officials and institutions (both governmental and public).")
    col1, col2 = st.columns(2)
    col1.caption("**Interpersonal Trust**")
    col1.bar_chart(interpersonal_trust, x="title", y="Interpersonal Trust", x_label="Interpersonal Trust Level",
                 y_label="Percentage of interviewees", color=["#2769BA"])
    col2.caption("**Institutional Trust**")
    col2.bar_chart(instutitional_trust, x="title", y="Institutional Trust", x_label="Institutional Trust Level",
                 y_label="Percentage of interviewees", color=["#E64C00"])
    st.write("The **trust index** is a combination of interpersonal and institutional trust level.")
    st.bar_chart(all_trust, x="title", y="Trust", x_label="Trust Level",
                 y_label="Percentage of interviewees", color=["#7AF5CA"])

if social_info == "Social Communication":
    st.header("Social Communication", divider="orange")
    st.write("This index is made up of the sum of the items of communication with neighbours and family. According to the chart below, this index is evaluated as above average in Soltaniyeh city.")
    st.bar_chart(communication, x="title", y="Communication", x_label="Social Communication Level",
                 y_label="Percentage of interviewees", color=["#2769BA"])

if social_info == "Social Participation":
    st.header("Social Participation", divider="orange")
    st.write("This index is made up of the sum of the formal and informal participation indices; formal participation refers to participation in urban decision-making and participation in metropolitan affairs. Informal participation also refers to participation in religious affairs, local decisions, etc.")
    col1, col2 = st.columns(2)
    col1.caption("Informal Participation Level")
    col1.bar_chart(informal_participation, x="title", y="Informal Participation", x_label="Informal Participation Level",
                 y_label="Percentage of interviewees", color=["#E64C00"])
    col2.caption("Formal Participation Level")
    col2.bar_chart(formal_participation, x="title", y="Formal Participation", x_label="Formal Participation Level",
                 y_label="Percentage of interviewees", color=["#2769BA"])
    st.markdown("**Conclusion**: Participation among citizens of Soltaniyeh city has been assessed as low or very low.")
    st.bar_chart(all_participation, x="title", y="Participation", x_label="Participation Level",
                 y_label="Percentage of interviewees", color=["#7AF5CA"])
    
if social_info == "Social Capital":
    st.header("Social Capital", divider="orange")
    st.write("This index is made up of the sum of the indicators of **participation**, **trust** and **communication**, and **urban identity** and **belonging**. Based on this index, the level of social capital is assessed as average.")
    st.bar_chart(social_capital, x="title", y="Social Capital", x_label="Social Capital Level",
                 y_label="Percentage", color=["#7AF5CA"])
    
if social_info == "Resilience Index":
    st.header("Resilience Index", divider="orange")
    st.write("The characteristic of community resilience allows communities to be compared with each other in terms of their ability to adapt positively to hardships and problems. The resilience index is composed of indicators such as trust and communication, participation, which is also known as social capital in this research. Another indicator of social resilience is the urban identity and belonging index. As can be seen in the chart below, the status of this indicator is assessed as average.")
    st.bar_chart(resilience, x="title", y="Resilience", x_label="Resilience Level",
                 y_label="Percentage", color=["#7AF5CA"])        
    
people_issues = demographic_expander.toggle("People's Issues")  
if people_issues:
    st.header("People's Issues and Questions", divider="orange") 
    st.write("One of the most important questions in social survey is to find people's opinion about their city and the issues they have to deal with. In other words, what the urgent problems are when it comes to live in Soltaniyeh. Soltaniyeh dwellers said:")
    col1, col2, col3 = st.columns(3)
    col1.markdown("**- :red[Lack of health and welfare services]**")
    col1.markdown("**- :red[Improper management of city capacities]**")
    col1.markdown("**- :red[Unemployment rate]**")
    col1.markdown("**- :red[Inadequate public transportation]**")
    col1.markdown("**- :red[Lack of communication between officials and citizens]**")
    col1.markdown("**- :red[Emigration from Soltaniyeh (particularly young people and experts)]**")
    col1.markdown("**- :red[Destruction of historical monuments]**")
    col1.markdown("**- :red[Non-native urban management]**")
    col1.markdown("**- :red[Environmental problems such as dust]**")
    col1.markdown("**- :red[Poor education]**")
    col1.markdown("**- :red[Poor road conditions]**")
    col1.markdown("**- :red[Problems related to women's presence in public spaces]**")
    col1.markdown("**- :red[Strict laws and regulations for development]**")
    col1.markdown("**- :red[Lack of tourism infrastructure]**")
    col2.image("IMG_6079.jpg")
    # col4.image("IMG_6080.jpg")
    col2.image("IMG_6338.jpg")
    # col4.image("IMG_6340.jpg")
    col3.image("IMG_6343.jpg")
    col3.image("IMG_6349.jpg")
    # col3.image("IMG_7412.jpg")
    # #col3.image("IMG_7418.jpg")
    st.bar_chart(people_issues_file, x="Issues", y="Number of Interviewees", color=["#7AF5CA"])

economic_expander = st.sidebar.expander("Economic Condition")
general_economic = economic_expander.toggle("General Economic Structure")
if general_economic:
    st.header("General Economic Structure of the City", divider="orange")
    st.subheader("General Information")
    df_economic = pd.read_excel(general_economic_table)
    st.dataframe(df_economic, hide_index=True)
    economic_sectors = pd.read_excel(economic_sectors_table)
    st.bar_chart(economic_sectors, x="Sector", y="Shares of total employment", color="#00FF00")
    st.divider()
    st.write("The most important crops in Soltaniyeh are :green[***potato, wheat, barley, beans, hay, canola and corn fodder***].")
    st.write("The amount of :orange[***potato***] harvested each year is :blue[***almost 110 tons***] per hectare. This figure in Zanjan province is approximately 42 tons.")
    st.write("The most important products in gardens is :green[***apple***]. The apples harvested in :grey[***Gozal Darreh***] have a special taste and smell.")
    st.write("After apple, there are :blue[***pear, peach and walnut***] in the second to forth ranks, respectively.")
    st.write("Soltanieh is a centre for agricultural support services and the supply and repair of agricultural equipment for the surrounding villages.")
    st.write("In the field of :red[***wheat***], there are processing industries related to the production of :orange[***bread flour, confectionery, and industrial bran***] in the city.")
economic_opportunities = economic_expander.toggle("Economic Opportunities")
if economic_opportunities:
    st.header("Economic Opportunities mentioned in other researches", divider="orange")
    st.write("Placement near the Tehran - Bazargan international commercial Corridor")
    st.write("Surrounded by agricultural land which can be cultivated in various ways")
    st.write("Placement in the intersection of two tourist corridors (Tehran-Tabriz and Zanjan-Hamedan)")
    st.write("Placement in the industrial corridor of Zanjan province (Zanjan - Abhar)")
    col1, col2, col3 = st.columns(3)
    col1.image("Industry.png")
    col2.image("Mining.png")
    col3.image("Service.png")
    
tourists = economic_expander.toggle("Tourism and Tourists")
if tourists:
    st.header("Tourism and Tourists in Soltaniyeh", divider="orange")
    st.write("This table demonstrate the most relevant information about tourists in Soltaniyeh.") 
    df_tourists = pd.read_excel(tourists_table)
    st.table(df_tourists)
    st.divider()
    st.write("Soltaniyeh suffers from lack of deifferent kinds of accommodations for tourists. It has only two places providing some tourist infrastructure for visitors.")
    df_hotels = pd.read_excel(hotels)
    st.table(df_hotels)
    
    st.image("IMG_7960.jpg", width=1200)
    st.caption("Bagh Ilkhani; Photo by: Arash Fazli Shams Abadi")
    
    
    
    

physical_expander = st.sidebar.expander("Physical Condition")
landuse = physical_expander.toggle("Current Landuse")
if landuse:
    st.header("Current Landuse", divider = "orange")
    st.image("Current Landuse.jpg")
    st.divider()
    landuse_df = pd.read_excel(landuse_raw_table)
    landuse_df["Proportion (%)"] = landuse_df["Proportion (%)"]*100
    st.dataframe(landuse_df, hide_index=True)
    st.divider()
    st.bar_chart(landuse_df, x="Landuse Title", y="Proportion (%)",
                 x_label="Landuse Titles", y_label="Proportion of total")
buildings = physical_expander.toggle("Buildings")
if buildings:
    st.header("Buildings characteristics", divider="orange")
    buildings_table = pd.read_excel(parcels)
    base_floors = buildings_table.groupby(by=["Floor"])["count"].count()  
    base_structure = buildings_table.groupby(by=["Structure"])["count"].count()
    base_oldness = buildings_table.groupby(by=["Oldness"])["count"].count() 
    base_quality = buildings_table.groupby(by=["Quality"])["count"].count() 
    col1, col2 = st.columns(2)
    col1.caption(":blue[**Floors**]")
    col1.bar_chart(base_floors, x_label="Number of Floors", y_label="Number of Buildings",
                   horizontal=False)
    col1.image("Tabaqat_Abnieh.jpg")
    col1.divider()
    col2.caption("ُ:orange[**Structure**]")
    col2.bar_chart(base_structure, x_label="Structure", y_label="Number of Buildings", color=["#E64C00"],
                   horizontal=False)
    col2.image("Saze_Abnie.jpg")
    col2.divider()
    col1.caption(":blue[**Oldness**]")
    col1.bar_chart(base_oldness, x_label="Kind of Oldness", y_label="Number of Buildings",
                   horizontal=False)
    col1.image("Omr_Bana.jpg")
    col2.caption("ُ:orange[**Quality**]")
    col2.bar_chart(base_quality, x_label="Quality", y_label="Number of Buildings", color=["#E64C00"],
                   horizontal=False)
    col2.image("Quality.jpg")

urban_fabric = physical_expander.toggle("Urban Fabric")
if urban_fabric:
    st.header("Urban Fabric Characteristics", divider="orange")
    st.subheader("About Residential Plots")
    col1, col2 = st.columns(2)
    col1.markdown("The area of :blue[**residential plots**] is almost ***221 m2*** in average.")  
    col1.markdown("In :red[**new parts**] of the city - Shahrak Talebieh - this figure is approximately ***252 m2***, while in :orange[**older parts**] it drops to ***217 m2***.") 
    col1.markdown("The :green[**ground floor**] of houses occupy about ***60%*** of their plots in average. The figure for floor per capita in residential areas is exactly ***59.61%***.")
    col1.markdown("The :blue[**average of floor space ratio**] for those occupied by households is almost ***78%***.")
    col1.markdown("According to previous points, the :blue[**average of building area**] in residential parts is ***145.5 m2***.")
    col1.markdown("Based of the information recieved from the Office of Statistics, the :red[**mean area of residential units**] is nearly ***119 m2***, which is resonable due to the average of building area. The difference between those figure refers to :green[**the area of common places**] in the buildings.")
    col2.image("Urban Fabric1.jpg")
    "---"
    st.subheader("Architecture of Residential Buildings")
    st.markdown("The general occupation forms of buildings and their geographical direction are of utmost importance. These factors contribute to deal with climatic conditions, particularly in Iran Plateau with generally warm summers and dry winters.")

    col1, col2 = st.columns(2)
    toodeha = pd.read_excel(building_toode)
    col1.bar_chart(toodeha, x="Kind", y="Proportion (%)", horizontal=True,
                   height=350, color=["#E64C00"], x_label="Proportion of Total")
    col2.image("Building_Toodeh.png", width = 1200) 

    col1,col2,col3 = st.columns(3)
    col2.image("NS_D.png", width=300)
    col2.image("Qb_D.png", width=300)
    col3.image("Km_D.png", width=300)
    col3.image("Is_D.png", width=300)
    directions = pd.read_excel(building_direction)
    col1.bar_chart(directions, x="Building Direction", y="Proportion (%)",
                   x_label="Kind of Direction", y_label="Proportion of Total",
                   height=550)
    col1.divider()
    col2.divider()
    col3.divider()
    toode_dimension = pd.read_excel(building_toode_dimension)
    df_styled = toode_dimension.style.map(lambda x: f"background-color:{'#E69800' if x>2 else '#96FF96'}",
                                          subset="Aspect ratio")
    st.markdown("The undermentioned table provides information about the :orange[**aspect ratio**] of different forms of plot occupation.")
    st.dataframe(df_styled, hide_index=True) 
    st.divider()
    st.subheader("Roads Sinuosity Index")
    st.markdown("The :blue[**Siuosity Index**] shows how straight a road is. Due to :green[traditional principles] in Iran's historical cities, this index tends to increase. Despite that, in today's Soltaniyeh this index closes to 1 as most parts of the city have been constructed since 1995 (after the government sold the land around Soltaniyeh Dome and city dwellers had to move to neighbouring areas).")
    st.image("Road_Sinuosity.jpg")
    st.divider()
    st.subheader("Space Syntax Indices")
    st.markdown("These maps demonstrate various aspects of :red[***Space Syntax Analysis***] in Soltaniyeh. To be more practical, all of them compare current condition with before 1995 condition.")
    col1, col2, col3 = st.columns(3)
    col1.image("Control1343.jpg", caption=":blue[**Control**]")
    col1.image("Hampeyvandi1343 (2).jpg", caption=":blue[**Integration**]")
    col2.image("Hampeyvandi1343.jpg", caption=":blue[**Integration (HH)**]")
    col2.image("Harkat_TabiE1343.jpg", caption=":blue[**Choice**]")
    col3.image("Omgh1343.jpg", caption=":blue[**Total Depth**]")
    col3.image("Vozooh1343.jpg", caption=":blue[**Connectivity**]")
    
      
roads = physical_expander.toggle("Roads Network")
if roads:
    st.header("Roads Network", divider="orange")
    st.subheader("Traffic between Soltaniyeh and other cities")
    st.write("The table below gives information about the number of vehicles moving along the connected roads with Soltaniyeh. This information is from 2018, before the COVID-19 pandemic and lockdowns.")
    roads = pd.read_excel(roads_traffic)
    roads["Proportion (%)"] = roads["Proportion (%)"] * 100
    st.dataframe(roads, hide_index=True)
    roads_bar = pd.read_excel(roads_traffic_barchart)
    st.bar_chart(roads_bar, x="Direction", y="The average of traffic in rush hours (veh)", horizontal=True,
                 y_label="Roads direction", color= "#4B17B4")
    st.divider()
    st.subheader("Hierarchy of Urban Roads")
    
    st.divider()
    st.subheader("Roads Width and Slope")
    st.write(":blue[**Roads Width**]")
    roadswidth = pd.read_excel(roads_width)
    st.dataframe(roadswidth, hide_index=True)
    st.image("DarajeBandi_Arz_Mabar.jpg")
    st.write(":blue[**Roads Slope**]")
    roadslop = pd.read_excel(roads_slop)
    st.dataframe(roadslop, hide_index=True)
    st.image("Shib_Mabar.jpg")

conclusion_expander = st.sidebar.expander("Values, Capasities, Issues")
values = conclusion_expander.toggle("Values")
if values:
    st.header("Values", divider="orange")
    st.write("""- Soltaniyeh as an unique historical city constructed during a decade, was surviving for almost 70 years.
             Remained historical sites alongside the spectacular buildings, particularly Soltaniyeh Dome,
             bring the worthiness for this city.""")
    st.write("- Soltaniyeh pasture is a distinctive vegetation that is deserved to be protected as a natural heritage.")
    st.write("""- Shah-Bolaqi spring is one of the tourist destinations in Zanjan province, which adds an extra value to 
             the nature and history of this region.""")
    st.write("""- Dash-Kasan (Deragon) temple in Vier is another historical site near Soltaniyeh, which with the other sites can
             form a network of various tourist destinations.""")
    st.write("""- The pristine landscape of this region with quaint buildings, such as Soltaniyeh Dome and Chalabi-Oqlou,
             makes it sparse when it comes to urban designing.""")
    st.write("""- The vivid sense of life among city dwellers helps them cope with the many difficulties thay face everyday.""")
capasities = conclusion_expander.toggle("Capasities")
if capasities:
    st.header("Capasities", divider="orange")
    st.write("""- Soltaniyeh has an opportunity to improve its economy through agriculture. The soil condition, water resources
             and labour force are three sides of one triangle, which shapes this economic sector.""")
    st.write("""- The variety of transportation modes including railroad, highway and other roads, can enhance the tourist industry,
             agriculture, mining activities, and industrial zones.""")
    st.write("""- Soltaniyeh can be the north gateway of Zanjan-Hamedan tourist path with providing various forms of tourism,
             such as historical tourism, agricultural, natural, sport and thematic tourism.""")
    st.write("""- The industrial zone at the northern part of this region is one of the most important ones in Iran, since
             it includes some outstanding firms and manufacturers.""")
issues = conclusion_expander.toggle("Issuses")
if issues:
    st.header("Issues", divider="orange")
    st.write("""- Soltaniyeh pasture is in crisis because of the overconsumption of water resources.""")
    st.write("""- Due to water overconsumption in farmlands, the volume of groundwater resources has been
             decreasing with 0.94 m per year.""")
    st.write("""- Industries around Soltaniyeh produce a wealth of air pollution, and contaminate 
             water resources.""")
    st.write("""- Despite being the main city in the county, some parts of Soltaniyeh struggle with physical, societal, and 
             economic difficulties.""")
    st.write("""- Some historical sites and buffer zones are invaded by new construction.
             This phenomenon prevents these areas from conservational projects.""")

documents_expander = st.sidebar.expander("Documents and Reports")
documents_toggle = documents_expander.toggle("Documents")
reports_toggle = documents_expander.toggle("Reports")
if documents_toggle:
    st.header("Nomination Document", divider="orange")
    st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\Parvande_Sabt_Jahani.pdf", height = 800)

if reports_toggle:
    background = st.sidebar.checkbox("Background & Setting")  
    if background:
        st.header("Nomination Document", divider="orange")
        st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\01_ZamineHa.pdf", height = 800) 
    current_report = st.sidebar.checkbox("Study and survey of current condition")
    if current_report:
        st.header("Meticulously study and survey the current condition", divider="orange")
        st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\02_MotaleAt_Tafsili_Shahr.pdf", height=800)
    analysis = st.sidebar.checkbox("Analysis Report")
    if analysis:
        st.header("Analysis", divider="orange")
        st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\03_Tahlil.pdf", height=800)

