import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt 
from streamlit_folium import st_folium as stf
from shapely import Point, Polygon
import pandas as pd
import shutil
import os
import folium

@st.cache_data
def load_data(path):
    return gpd.read_file(path)

# my directory
# main_directory = r'D:\Arash\StreamLit\Other_Try\Multipage'

# basic files for working with
parcels = r"geojsons\Parcel1401.geojson"
gdf_parcels = load_data(parcels)
gdf_parcels_check = gdf_parcels.set_index("ObjectID", drop=False)

@st.cache_data
def find_parcel(id):
    try:
        return gdf_parcels_check.loc[[id]]
    except KeyError:
        return None

city_zones = r"geojsons\City_Zoning.geojson"
city_zoning = load_data(city_zones)
functions_list = []
with open("Functions1.txt") as file:
    for row in file:
        functions_list.append(row)

historical_sites_path = r"geojsons\Historical_sites_boundaries.geojson"
historical_sites = load_data(historical_sites_path)
parcel_width = r"geojsons\Parcel_width.geojson"
parcel_width_road = load_data(parcel_width)

parcel_angle = r"geojsons\parcel_angle.geojson"
parcel_angle_gdf = load_data(parcel_angle)

@st.cache_data
def read_pd_file(path):
    return pd.read_excel(path)

# a function to convert landuse codes to descriptions
def landuse_current(a):
    if a==1:
        return "Residential"
    elif a==2:
        return "Tertiary Education"
    elif a==3:
        return "Educational"
    elif a==4:
        return "Official"
    elif a==5:
        return "Commercial"
    elif a==6:
        return "Sport"
    elif a==7:
        return "Welfare"
    elif a==8:
        return "Art & Culture"
    elif a==9:
        return "Park"
    elif a==10:
        return "Religious"
    elif a==11:
        return "Urban Facilities"
    elif a==12:
        return "Urban Infrastructure"
    elif a==13:
        return "Transport"
    elif a==14:
        return "Military"
    elif a==15:
        return "Agriculture & Private Gardens"
    elif a==16:
        return "Historical building and area"
    elif a==17:
        return "Natural"
    elif a==18:
        return "Industrial"
    elif a==19:
        return "Buffer Zone"
    elif a==20:
        return "Tourist Infrastructure"
    elif a==21:
        return "Mixed Landuse"
    elif a==28:
        return "Without Building - Barren Field"
    else:
        return "Out of City Border or In Street Area"

# to show the residential rate in zone
basic_rates = "Residential_Rates.xlsx"
basic_rates_df = read_pd_file(basic_rates).set_index("title", drop=False)

@st.cache_data
def set_zone(zone_code):
    try:
        return basic_rates_df.loc[[zone_code]]
    except KeyError:
        return None

parcel_temp = gdf_parcels.set_index("ObjectID", drop = False)

@st.cache_data
def set_object_id(id):
    try:
        return parcel_temp.loc[[id]]
    except KeyError:
        return None 
     
@st.cache_data  
def residential_rate(zone):
    if zone == "R121":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone R121 is :green[**70%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s
    elif zone == "R122":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone R122 is :green[**70%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s        
    elif zone == "R211":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone R211 is :green[**70%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s  
    elif zone == "R212":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone R212 is :green[**75%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s  
    elif zone == "R311":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone R311 is :green[**65%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s  
    elif zone == "R321":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone R321 is :green[**75%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s      
    elif zone == "R322":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone R322 is :green[**65%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s   
    elif zone == "M111":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone M111 is :green[**60%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s        
    elif zone == "M121":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone M121 is :green[**55%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s  
    elif zone == "M311":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone M311 is :green[**40%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s   
    elif zone == "M321":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone M321 is :green[**45%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s     
    elif zone == "M322":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone M322 is :green[**45%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s     
    elif zone == "S111":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone S111 is :green[**30%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s      
    elif zone == "S112":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone S112 is :green[**20%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s 
    elif zone == "S212":
        r = set_zone(zone)["residential_rate"].values[0]
        s = f"The targeted ratio for residential use in zone S212 is :green[**35%**] of all plots. This ratio is currently almost :orange[**{r*100}%**] ."
        return s 
    else:
        return f"There is nothing about residential rate in {zone}."
@st.cache_data
# for historical part
def historical_zone(zone):
    if zone == "H111" or zone == "H211":
        return True
    else:
        return False
    
                
# creating the page with a title
st.title("Urban Law and Regulations")    

# about this page and its purposes
col1, col2 = st.columns(2)
col1.markdown("**This part of the CASSP is for ciry dwellers, developers, constructors, municipality staff and those wanting to know about the laws, regulations and principles dominationg their properties. It includes:**")
col2.image("IMG_7451.jpg", width=450)
col2.image("IMG_7453.jpg", width=450)
col1.write("- The zone surrounding the plot")
col1.write("- The width of a road providing accessibility to the plot")
col1.write("- The maximum legal height of buildings")
col1.write("- The relevant urban designing and planning projects")
col1.write("- The best function/s to run in that part of the city")
col1.write("- The best kind of occupation form of the buildings")
col1.write("**If you need to know about these sets of law and regulations, you must enter some information in advance. The first one is :blue[***Construction Code***], which is unique for every plot. By means of this code CASSP can find the property and return relevant information based on the aforementioned topics. The other one must be filled is the :green[***Area and the Dimentions***] of the plot. It must be written carefully, since the application does some calculations on them, and it returns an error if there was a misconnection between them (Area ~= the result of multiplying the dimentions).**")
col1.write("**Because of privacy terms you do not need to give :red[***your name or national ID number***] to the application.**")
col1.write("**With these compulsory information, CASSP brings the main law and regulations about the asked plot back.**")
st.write("If you want to receive the urban law and regulations about your property click on this expander.")


# creating a form to give initial info
owner_form = st.expander("Click and fill the form!")

plot_code = owner_form.number_input("Enter the Construction Code of your property", min_value=0,
                        placeholder="Enter the code", value=None, key="code")

def check_plot_code(code):
    if plot_code is not None:
        if len(str(st.session_state.code)) != 5:
            st.error("The code is not correct. Enter a correct one.", icon="🚨") 
        else:
            if len(find_parcel(st.session_state.code)) != 1:
                st.error("The entered code is not for Soltaniyeh plots. Let's check it and enter thr right one.", icon="🚨")
            else:
                return st.session_state.code
    else:
        st.info("Please enter your property code first.")


if plot_code is not None and check_plot_code(plot_code) == plot_code:
    plot_location = find_parcel(st.session_state.code).to_crs(crs=city_zoning.crs)
    plot_location_point = gpd.points_from_xy(plot_location.centroid.x, plot_location.centroid.y)
    plot_location = plot_location.reset_index(drop=True)
    join_info = plot_location.sjoin(city_zoning, predicate ="intersects", how="left")
    main_zone = ""
    for zone in list(join_info['ZirPahne']):
        zone1 = city_zoning.loc[city_zoning["ZirPahne"]==zone]
        for poly in zone1.geometry:
            m = Polygon(poly)
            if plot_location_point.within(m):
                main_zone = zone

                
                
    plot_area = owner_form.number_input("Enter the area of your property based on legal documents",
                            placeholder="Enter the area", value=None, key="area", disabled=historical_zone(main_zone))
    plot_width = owner_form.number_input("Enter the width of your property",
                            placeholder="Enter the dimention", value=None, key="width", disabled=historical_zone(main_zone))
    plot_depth = owner_form.number_input("Enter the depth of your property",
                            placeholder="Enter the dimention", value=None, key="depth", disabled=historical_zone(main_zone))




    acceptable_functions = []

    base_law = "Plot_area_road_width.xlsx"
    base_law_df = pd.read_excel(base_law)

    if main_zone != "" and main_zone != "H111" and main_zone != "H211":
        for idx,row in base_law_df.iterrows():
            if row[f"{main_zone}"] == "a":
                acceptable_functions.append(row["english_title"])


    # to show the historical sites and the bans dominationg them
    if main_zone == "H111" or main_zone == "H211":
        st.subheader(":orange[**Assessment Results**]")
        st.write("""Your property is in the historical sites. To find what you can run in that, you need to negotiate with GD of 
            Cultural Heritage, Tourism and Handicrafts of Zanjan Province.""")
        historical_map = historical_sites.explore()
        plot_location.explore(m = historical_map, color="#EB4D52")
        show_map = stf(historical_map)
        
        
    # a list of all functions to select from
    list_functions = []
    for idx,row in base_law_df.iterrows():
        list_functions.append(row["english_title"])

    plot_request = owner_form.selectbox("Select your requested function", options = list_functions,
                                        placeholder="Select from this list", index=None, key = "request", 
                                        disabled=historical_zone(main_zone))


    # to find relevant local project
    base_local_projects = r"geojsons\Detailed_Projects.geojson"
    local_projects = load_data(base_local_projects)
    local_projects = local_projects.to_crs(city_zoning.crs)


    # to find if the plot has a public facility laduse
    public_facilities = r"geojsons\Public_Amenities.geojson"
    public_facilities_gdf = load_data(public_facilities)  
    public_facilities_gdf = public_facilities_gdf.to_crs(city_zoning.crs)  


    # to show a picture taken around the plot
    # photos = r'D:\Arash\ArcGis_Pro_Manual\Folium_Map_Interactive\Shp\new_photos.shp'
    # photo_points = load_data(photos)
    # photo_points = photo_points.to_crs(crs = city_zoning.crs)
    # closest_photo = plot_location.sjoin_nearest(photo_points, distance_col="Distance")

    # basic file to assess if a plot is inside a historical site or buffer zone
    historical_buffers = r"geojsons\Historical_Buffer_Boundaries.geojson"
    historical_buffer_gdf = load_data(historical_buffers)
    historical_buffer_gdf = historical_buffer_gdf.to_crs(crs = city_zoning.crs)
    def building_height(point):
        msg7 = ""
        for idx,area in historical_buffer_gdf.iterrows():
            if point.within(Polygon(area.geometry)) == True:
                msg7 = f"{area['Name']}"
        if msg7 == "" or msg7 == "Second Buffer Zone":
            return "Based on building height zoning, **the maximum height of the building is 10.5 m**."
        elif msg7 == "First Buffer Zone":
            return "Based on building height zoning, **the maximum height of the building is 7.5 m**."
        else:
            return f"Because of locating in {area['Name']}; **it needs to be investigated by GD of Cultural Heritage, Tourism and Handicrafts of Zanjan Province**."
            

    # to assess the information whether it is true or needs corrections
    assessment = []
    if st.session_state.code is not None and st.session_state.area is not None and st.session_state.depth is not None and st.session_state.width is not None and st.session_state.request is not None:
        if len(str(st.session_state.code)) != 5:
            st.error("The code is not correct. Enter a correct one.", icon="🚨") 
        else:
            assessment.append(1)
        if len(gdf_parcels.loc[gdf_parcels["ObjectID"]== int(st.session_state.code)]) == 1:
            assessment.append(1)
        else:
            st.error("The entered code is not for Soltaniyeh plots. Let's check it and enter thr right one.", icon="🚨")
        if abs(st.session_state.area - (st.session_state.depth * st.session_state.width)) >= 5:
            st.error("The area and the multiplication of dimentions must be almost equal.", icon="🚨")
        else:
            assessment.append(1)
        if st.session_state.area <= 0 or st.session_state.depth <=0 or st.session_state.width <=0:
            st.error("The area and dimentions must be positive numbers. Please check them.", icon="🚨")
        else:
            assessment.append(1)
        if len(st.session_state.request) !=0:
            assessment.append(1)
        else:
            st.error("You must define a function as your request.", icon="🚨")


    # final step; to show the law and regulations about the plot  
    if sum(assessment) == 5:
        msg1, msg2, msg3, msg4 = "", "", "", ""
            
        st.info(f"""Tou've entered the needed information (Plot Code: {st.session_state.code}, Area: {st.session_state.area} m2, 
                Dimentions: {st.session_state.depth}m * {st.session_state.width}m and requested function: {st.session_state.request}), 
                and now you are to receive the relevant law and regulations. 
                The map below shows the location of your property.""")

        # to show current condition
        st.subheader(":orange[***Current Condition***]")
        for idx,area in historical_buffer_gdf.iterrows():
            if plot_location_point.within(Polygon(area.geometry)):
                st.write(f"This plot is inside {area['Name']}.")
                
        st.write(f"The current laduse is :blue[**{landuse_current(list(plot_location['Landuse'])[0])}**] .")
        if int(list(plot_location['Floor'])[0]) >0:
            st.write(f"The number of floor is :blue[**{list(plot_location['Floor'])[0]}**] .")
        # parcel_image = shutil.copyfile(closest_photo["Path"].values[0], os.path.join(main_directory, closest_photo["Name"].values[0]))
        # st.image(parcel_image, width=400, caption="Photo taken by: Arash Fazli Shams Abadi")
        
        
        
        # to find rules and regulations    
        st.subheader(":orange[***Law and Regulations***]")
        st.markdown("- **Zone & Road Width**")
        st.write(f"The zone surrounding the plot is :blue[**{main_zone}**] .")
        st.write(residential_rate(main_zone))
        road_width = parcel_width_road.loc[parcel_width_road["ObjectID"] == st.session_state.code]["Arz_Gozar"].values[0]
        st.write(f"The width of the road that provides accessibility to this plot is :blue[**{road_width} m**].")

        #st.write(f"The minimum area of plot for running {plot_request} is {base_law_df.loc[base_law_df['english_title'] == plot_request]['s_area'].values}")
        st.markdown("- **Function Assessment**")
        if st.session_state.request in acceptable_functions:
            r_function = True
        else:
            r_function = False
            st.write(f":red[Your requested function is not in the list of acceptable functions in {main_zone}.]")
            st.write(f"The list of acceptable functions in {main_zone} includes: :blue[*{acceptable_functions}*].")
            #st.write(f"{acceptable_functions}")
        
        minimum_area = float(base_law_df.loc[base_law_df["english_title"] == st.session_state.request]["s_area"])
        
        if float(st.session_state.area) < minimum_area:
            r_area = False
        else:
            r_area = True
            
        minimum_road = float(base_law_df.loc[base_law_df["english_title"] == st.session_state.request]["s_road_width"])
        
        if float(road_width) < minimum_road:
            r_road_width = False
        else:
            r_road_width = True

        if r_function == True and r_area == True and r_road_width == True:
            msg1 = st.write(":blue[Based on the surrounding zone, the area of your plot and the width of the near road, the requested function is acceptable.]")
        
        if r_function == True and r_area == True and r_road_width == False:
            msg2 = st.write("Although your requested function is in acceptable functions and its area surpasses the threshold, :violet[because of road width you cannot run that function.]")

        
        if r_function == True and r_road_width == True and r_area == False:
            msg3 = st.write("Although your requested function is in acceptable functions and the accessibility is provided, :violet[because of the area you cannot run that function.]")

        if r_function == True and r_road_width == False and r_area == False:
            msg4 = st.write(f"Your requested function is in the list of {zone} acceptable functions, :orange[but the area and road width prevent that function to be run.]")

        if msg2 != "" or msg3 != "" or msg4 != "":
            suggestions1 = []
            for idx,row in base_law_df.iterrows():
                if row["english_title"] in acceptable_functions and float(st.session_state.area)>= row["s_area"] and float(plot_location['Arz_Pishna'])>= row["s_road_width"]:
                    suggestions1.append(row["english_title"]) 

            st.write(f"**Suggestion** : You can choose one of the undermentioned functions based on the area of your plot and the width of near road: :blue[*{suggestions1}*].")
        
        st.markdown("- **About Local Projects**")
        for idx,project in local_projects.iterrows():
            if project.geometry.contains(plot_location_point) == True:
                msg5 = f"This plot is inside a local project: {project['Name']}."
            else:
                msg5 = ""
        
        if msg5 != "":
            st.write(msg5)
        else:
            st.write("This plot is not inside any local project.")
        
        st.markdown("- **About Public Facilities**")
        for idx,parcel in public_facilities_gdf.iterrows():
            if parcel.geometry.contains(plot_location_point) == True:
                msg6 = f"This plot is of public facilities with landuse : {parcel['Eng_Name']}."
            else:
                msg6 = ""
        
        if msg6 != "":
            st.write(msg6)
        else:
            st.write("There is no defined public facility for this plot.")
            
        st.markdown("- **About the Architecture**")
        building_kind1, building_kind2, building_kind3, building_kind4, building_kind5, building_kind6, building_kind7, building_kind8, building_kind9, building_kind10 = "", "", "", "", "", "", "", "", "", ""
        floor_coverage1, floor_coverage2 , floor_coverage3 = "60%" , "75%" , "80%"
        if (main_zone[0] == "R" or main_zone[0] == "M") and msg1 != "":
            if st.session_state.width >= st.session_state.depth:
                depth , width = st.session_state.width, st.session_state.depth
                dimention_ratio = st.session_state.width/st.session_state.depth
            else:
                width, depth = st.session_state.width, st.session_state.depth
                dimention_ratio = st.session_state.depth/st.session_state.width
            if dimention_ratio > 1.8 and dimention_ratio < 3:
                if st.session_state.area >= 140:
                    building_kind1 = st.write("The building should be designed in :blue[**two separated parts**].", key="twoparts")
                    st.write(f"If this form is used, the maximum floor coverage will be :blue[**{floor_coverage2}**] .")
                    st.write(building_height(plot_location_point))
                    st.image("Twosided.jpg", width=500)
                else:
                    building_kind2 =st.write("The building should be :blue[**one-sided**].", key="onesided1")
                    st.write(f"The maximum floor coverage is {floor_coverage1} .")
                    st.write(building_height(plot_location_point))

            elif dimention_ratio >= 1 and dimention_ratio <= 1.8:
                if st.session_state.area>=300 and (depth-6)/2>=4 and (width-6)/2>=4:
                    building_kind3 =st.write("The building should be designed in :blue[**4-sided form**].", key="foursided1")
                    st.write(f"If this form is used, the maximum floor coverage will be :blue[**{floor_coverage2}**] .")
                    st.write(building_height(plot_location_point))
                    st.image("Foursided.png", width=500)
                elif st.session_state.area>=300 and ((depth-6)/2<4 or (width-6)/2<4):
                    building_kind4 =st.write("The building should be designed in :blue[**U-form**].", key="uform1")
                    st.write(f"If this form is used, the maximum floor coverage will be :blue[**{floor_coverage2}**] .")
                    st.write(building_height(plot_location_point))
                    st.image("Threesided.jpg", width=500)
                elif st.session_state.area>=150 and st.session_state.area<300 and ((depth-6)/2>=4 or (width-6)/2>=4):
                    building_kind5 =st.write("The building should be designed in :blue[**U-form**].", key="uform2")
                    st.write(f"If this form is used, the maximum floor coverage will be :blue[**{floor_coverage2}**] .")
                    st.write(building_height(plot_location_point))
                    st.image("Threesided.jpg", width=500)
                elif st.session_state.area>=150 and st.session_state.area<300 and ((depth-6)/2<4 and (width-6)/2<4):
                    building_kind6 =st.write("The building should be designed in :blue[**L-form**].", key="lform1")
                    st.write(f"If this form is used, the maximum floor coverage will be :blue[**{floor_coverage2}**] .")
                    st.write(building_height(plot_location_point))
                    st.image("Lshape.jpg", width=500)
                elif st.session_state.area<150 and st.session_state.area>=75:
                    building_kind7 =st.write("The building should be designed in :blue[**L-form**].", key="lform2")
                    st.write(f"If this form is used, the maximum floor coverage will be :blue[**{floor_coverage2}**] .")
                    st.write(building_height(plot_location_point))
                    st.image("Lshape.jpg", width=500)
                else:
                    building_kind8 =st.write("The building should be :blue[**one-sided**].", key="onesided2")
                    st.write(f"The maximum floor coverage is {floor_coverage1} .")
                    st.write(building_height(plot_location_point))
            elif dimention_ratio >= 3:
                building_kind9 =st.write("The building should be :blue[**one-sided**].", key="onesided3")
                st.write(f"The maximum floor coverage is {floor_coverage1} .")
                st.write(building_height(plot_location_point))
            else:
                st.write("Nothing especial.")
        elif main_zone[0] == "S" and msg1 !="":
            building_kind10 =st.write("The building should be designed :blue[**one-sided and its main facade should be along the road**].",
                    key="onesidedcommercial")
            st.write(f"The maximum floor coverage is {floor_coverage3} .")
            st.write(building_height(plot_location_point))
            st.image("Commercial_facade.jpg", width=500)
        elif main_zone[:2] == "G2" and msg1 != "":
            st.write("Any design must be done under article 14 of Urban Land Law.")
        elif main_zone[:2]== "G1" and msg1 != "":
            st.write("This is a park and needs a special designing under the rules dominationg green spaces in cities.")
        else:
            st.write("You must select an acceptable function first. Have a look at suggestion above.")
        # to show the location of the under investigated plot  
        angle = parcel_angle_gdf.loc[parcel_angle_gdf["ObjectID"] == st.session_state.code]["MBG_Orientation"].values[0]
        if building_kind1 != "":
            st.write("In this form the open space (yard) must be between two building parts.") 
        if building_kind2 != "" or building_kind8 != "" or building_kind9 != "":
            st.write("The open spce must be located on one side.")
        if building_kind3 != "":
            st.write("The open spce must be located on the centre.")
        if building_kind4 != "" or building_kind5 != "":
            if float(angle) <= 20:
                st.write("The open space (yard) should be located on the east side of the plot.")
            elif float(angle) > 20 and float(angle) <= 40:
                st.write("The open space (yard) should be located on either the east or west side of the plot.")
            elif float(angle) > 40 and float(angle) <= 140:
                st.write("The open space (yard) should be located on the south side of the plot.")
            elif float(angle) > 140 and float(angle) <= 160:
                st.write("The open space (yard) should be located on either the east or west side of the plot.")
            else:
                st.write("The open space (yard) should be located on the west side of the plot.")
        if building_kind6 != "" or building_kind7 != "":
            if float(angle) <= 100:
                st.write("The open space (yard) should be located on either the southeast  or southwest side of the plot.")
            elif float(angle) > 100 and float(angle) <= 120:
                st.write("The open space (yard) should be located on either the southeast or northwest side of the plot.")
            else:
                st.write("The open space (yard) should be located on the soutwest side of the plot.")
        
            
    st.markdown("- **Plot Location**")       
    map1 = folium.Map(zoom_start=18)
    folium.GeoJson(plot_location, color="red", popup = folium.GeoJsonPopup(fields=["Landuse", "Floor",
                                                                                   "Shape_Area"])).add_to(map1)
    folium.FitOverlays().add_to(map1)
    map_town = stf(map1) 
    


