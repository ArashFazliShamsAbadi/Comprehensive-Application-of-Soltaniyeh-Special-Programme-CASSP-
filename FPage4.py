import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium as stf
import geopandas as gpd
import matplotlib.pyplot as plt  
import zipfile
import io

st.image("InteractiveMap.jpg", width=400)

# def to colorise the layers
def buffer_fill_colour(text):
    if text == "First Buffer Zone":
        return "#64AFFF"
    else:
        return "#FF197D"
    
def ancient_road_colour(text):
    if text == "Silk Road":
        return "#EBCF00"
    elif text == "Maritime Silk Route":
        return "#005CE6"
    elif text == "Other Route":
        return "#828282"
    elif text == "Eurasian Steppe Route":
        return "#E69800"
    elif text == "Incense Road":
        return "#AA66CD"
    else:
        return "#48C72C"

def ancient_Eu_road_colour(text):
    if text == "Land route":
        return "#B66054"
    else:
        return "#3863E7"

def zoneregion_fill_colour(text):
    if text == "Agricultural Tourism":
        return "#00FF00"
    elif text == "Agriculture Sport tourism":
        return "#32FF96"
    elif text == "Agriculture and Cultural Tourism":
        return "#96FF96"
    elif text == "Agriculture and Natural Tourism":
        return "#C8FF96"
    elif text == "Agriculture and Natural-Cultural Tourism":
        return "#C8FFC8"
    elif text == "Agriculture and Sport Tourism":
        return "#C8C8C8"
    elif text == "Agriculture and high techs":
        return "#FFC8C8"
    elif text == "Agriculture and tranformative industries":
        return "#FFAFE1"
    elif text == "Agriculture, sport, and natural tourism":
        return "#AFE1AF"
    elif text == "Industrial":
        return "#FF00FF"
    elif text == "Conservation, Sport tourism":
        return "#7D9619"
    elif text == "Conservation, Cultural Tourism":
        return "#FF9664"
    elif text == "Rural Areas":
        return "#FFFF00"
    elif text == "Agriculture & agricultural tourism, natural tourism":
        return "#32E17D"
    else:
        return "#00C819"
    
def vision_zones_colour(text):
    if text == "No construction permission 1":
        return "#AAAAAA"
    elif text == "No construction permission 2":
        return "#7D7D7D"
    elif text == "North hinterland":
        return "#FFC864"
    elif text == "Other Zones":
        return "#C8C864"
    elif text == "Sensetive to construction - up to 10.5m":
        return "#C8FFC8"
    elif text == "Sensetive to construction - up to 4.5m":
        return "#9696C8"
    elif text == "Sensetive to construction - up to 7.5m":
        return "#AFAFE1"
    elif text == "Sensetive to construction - up to 7.5m, elevation<1800m":
        return "#AF6496"
    else:
        return "#E1AF7D"
    
def height_zones_colour(text):
    if text == "No construction permition":
        return "#969696"
    elif text == "Up to 10 m":
        return "#E1AF32"
    else:
        return "#E1FA32"
    
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
    
def currentplan_colour(text):
    if text == "maskuni2":
        return "#FFFF00"
    elif text == "amuzesh_ali":
        return "#260394"
    elif text in ["amuzeshi mantaghe","amuzeshi_mahale","amuzeshi_nahie","amuzeshi_shahr2"]:
        return "#6699CD"
    elif text == "edari2":
        return "#686868"
    elif text == "tejari2":
        return "#EB4D52"
    elif text == "varzeshi2":
        return "#F57AB6"
    elif text == "darmani2":
        return "#2769BA"
    elif text == "farhangi2":
        return "#7AB6F5"
    elif text == "park2":
        return "#4CE600"
    elif text == "mazhabi2":
        return "#7AF5CA"
    elif text == "tasisat2":
        return "#E69800"
    elif text == "tajhizat2":
        return "#755913"
    elif text == "hamlonaghl2":
        return "#FFFFAF"
    elif text == "arazi zakhire":
        return "#343434"
    elif text == "bagh2":
        return "#008B43"
    elif text == "tarikhi":
        return "#D1BA90"
    elif text == "khadamat poshtiban":
        return "#847D94"
    elif text == "jahangardi2":
        return "#A6D900"
    else:
        return "#CCCCCC"
    
def detailed_projects_colour(text):
    if text == "Amadesazi Arazi Shargh":
        return "#E1FF32"
    elif text == "Darvaze Tabiat":
        return "#4BFF32"
    elif text == "Designing Neighbourhood Centre":
        return "#960000"
    elif text == "EnsejamBakhshi Shargh va Gharb":
        return "#969696"
    elif text == "Tarrahi Darvazehaye Tarikhi":
        return "#7D4BFA"
    elif text == "Tarrahi Mabadi Voroudi Shahr":
        return "#FF4B94"
    elif text == "Tarrahi Mehvar Did Be Gonbad":
        return "#80FF4B"
    elif text == "Tarrahi Mehvar Molla Hasan":
        return "#00C8C8"
    elif text == "Tarrahi Mehvar Piramoun Arg":
        return "#7D1919"
    else:
        return "#96E119"
    
def facilities_colour(text):
    if text == "Art-Culture":
        return "#7AB6F5"
    elif text == "Educational":
        return "#6699CD"
    elif text == "Hospital":
        return "#2769BA"
    elif text == "Mosque":
        return "#7AF5CA"
    elif text == "Official":
        return "#686868"
    elif text == "Park":
        return "#4CE600"
    elif text == "Public Facilities":
        return "#755913" 
    elif text == "Sport Facilities":
        return "#F57AB6"
    else:
        return "#E69800"
    
def road_color(text):
    if text == "Jam Pakhsh":
        return "orange"
    elif text == "Mahalli":
        return "green"
    else:
        return "blue"
    
                                
zone_fill_colour = {"H111":"#B2B2B2", "H211":"#E69800", "R121":"#FFFF00",
                    "R122":"#E6E600","R211":"#FFEBAF","R212":"#FFD37F",
                    "R311":"#FFAA00","R321":"#A87000","R322":"#734C00",
                   "M111":"#D7B09E","M121":"#9EBBD7","M311":"#CD6666",
                   "M321":"#D7D79E","M322":"#D69DBC","S111":"#FF7F7F",
                   "S112":"#E64C00","S211":"#A80000","G111":"#98E600",
                   "G121":"#D1FF73","G311":"#A3FF73"}

# popups
popup01 = folium.GeoJsonPopup(fields=["Name"])
popup02 = folium.GeoJsonPopup(fields = ["Hoze", "Zir_Hoze", "Pahne", "ZirPahne", "Shape_Area"])
popup03 = folium.GeoJsonPopup(fields=["Name","Area"])
popup04 = folium.GeoJsonPopup(fields=["Name","Shape_Area"])
popup05 = folium.GeoJsonPopup(fields=["Eng_Name","Shape_Area"])
popup06 = folium.GeoJsonPopup(fields=["Height", "Elevation", "Shape_Area"])
popup07 = folium.GeoJsonPopup(fields=["Name","Floor","Shape_Area"])
popup08 = folium.GeoJsonPopup(fields=["N_Name", "Jamiat", "Pop_Dens"])
popup09 = folium.GeoJsonPopup(fields=["Layer","Shape_Area"])
popup10 = folium.GeoJsonPopup(fields=["Route_Name"])
popup11 = folium.GeoJsonPopup(fields=["Arz_Mojood", "Selsele", "width"])
popup16 = folium.GeoJsonPopup(fields=["Site_Name","Historical_Period"])
popup20 = folium.GeoJsonPopup(fields=["CATEGORY","CITY_1","CITY_2"])



map1 = folium.Map(control_scale=False,
    
    location=[36.4342609,48.7952043], zoom_control=True,
    tiles = "OpenStreetMap", zoom_start=11)

tile_layers = st.sidebar.expander("انتخاب نقشه زمینه")

imagery1 = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
attribution1 = ('Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community')
imagery2 = 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png'
attribution2 = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'

toggle_otm = tile_layers.toggle("Open Topo Map")
if toggle_otm:
    folium.TileLayer("opentopomap").add_to(map1)

toggle_img = tile_layers.toggle("CartodbPositron")
if toggle_img:
    folium.TileLayer("cartodbpositron").add_to(map1)

toggle_sat = tile_layers.toggle("Satellite Image")
if toggle_sat:
    folium.TileLayer(imagery1,attr=attribution1).add_to(map1)

toggle_osmh = tile_layers.toggle("Open Street Map Hot")
if toggle_osmh:
    folium.TileLayer(imagery2,attr=attribution2).add_to(map1)



main_layers = st.sidebar.expander("عرصه های تاریخی و حرایم آنها")

chaman_toggle = main_layers.toggle("چمن سلطانیه")
if chaman_toggle:
    chaman_file = "Chaman.geojson"
    folium.GeoJson(
        chaman_file,
        style_function=lambda feature: {
            "fillColor": "green",
            "color": "black",
            "weight": 2,
            "dashArray": "5, 5",}
    ).add_to(map1)
historical_toggle = main_layers.toggle("عرصه های تاریخی")
if historical_toggle:
    historical_marker = r"geojsons\Historical_Sites.geojson"
    historical_sites = r"geojsons\Historical_sites_boundaries.geojson"
    folium.GeoJson(historical_marker, popup = popup01).add_to(map1)
    folium.GeoJson(historical_sites).add_to(map1)

buffer_toggle = main_layers.toggle("حرایم مصوب")
if buffer_toggle:
    buffer_zones_json = r"geojsons\Buffer_Zones.geojson"

    folium.GeoJson(
        buffer_zones_json,
        style_function=lambda feature: {
            "fillColor": buffer_fill_colour(feature["properties"]["Layer"]),
            "color": "black",
            "weight": 2,
            "dashArray": "5, 5",}
        ).add_to(map1)
    
ancient_hill_file = r"geojsons\Ancient_Hills.geojson"
toggle_hill_zanjan = main_layers.toggle("تپه های تاریخی استان زنجان")
if toggle_hill_zanjan:
    folium.GeoJson(
        ancient_hill_file,
        color="black",
        popup=folium.GeoJsonPopup(fields = ["Name1", "DateBack"])
        ).add_to(map1)    


programme_layers = st.sidebar.expander("لایه های طرح ویژه سلطانیه")
boundaries_toggle = programme_layers.toggle("محدوده ها")
if boundaries_toggle:
    officials = programme_layers.checkbox("مرز تقسیمات کشوری")
    if officials:
        officials_file = r"geojsons\Official_Boundaries.geojson"
        folium.GeoJson(officials_file).add_to(map1)
    current_border = programme_layers.checkbox("محدوده ملاک عمل فعلی (تا 1404)")
    if current_border:
        current_city_border = r"geojsons\Current_City_Border.geojson"
        folium.GeoJson(current_city_border, style_function=lambda feature:{
            "color":"blue",
            "fillcolor": "gray",
            "dashArray" : "7, 7",
        }).add_to(map1)
    current_region = programme_layers.checkbox("حریم ملاک عمل فعلی (تا 1404)")
    if current_region:
        current_region = r"geojsons\Harim_Manzar.geojson"
        folium.GeoJson(current_region, color="green").add_to(map1)
    proposed_border = programme_layers.checkbox("محدوده پیشنهادی شهر")
    if proposed_border:
        proposed_city_border = r"geojsons\Mahdoodeh.geojson"
        folium.GeoJson(proposed_city_border).add_to(map1)
    proposed_region = programme_layers.checkbox("مرز حریم پیشنهادی شهر")
    if proposed_region:
        proposed_region_border = r"geojsons\Marz_Harim_Pishnahadi.geojson"
        folium.GeoJson(proposed_region_border, color="grey").add_to(map1)
zoning_toggle = programme_layers.toggle("لایه های پهنه بندی")
if zoning_toggle:
    city_zoning = programme_layers.checkbox("پهنه بندی نحوه استفاده از اراضی شهر")
    if city_zoning:
        zoning_file = "Town_Zoning.geojson"
        folium.GeoJson(zoning_file, 
                       style_function=lambda feature: {
                           "color": zone_fill_colour[feature["properties"]["ZirPahne"]],
                           "weight": 1}, popup=popup02).add_to(map1)
    region_zoning = programme_layers.checkbox("پهنه بندی اراضی حریم پیشنهادی")
    if region_zoning:
        region_zones = r"geojsons\Haim_Zones.geojson"
        folium.GeoJson(region_zones,
                       style_function = lambda feature: {
                           "fillColor": zoneregion_fill_colour(feature["properties"]["Name"]),
                           "color": "black",
                           "weight": 2,
                           "dashArray": "5, 5",
                       }, popup = popup03).add_to(map1)
    landscape_zoning = programme_layers.checkbox("پهنه های ساماندهی حریم منظری")
    if landscape_zoning:
        landscape_buffer_zones = r"geojsons\Soltanieh_Dome_Vision.geojson"
        folium.GeoJson(landscape_buffer_zones, style_function=lambda feature: {
            "fillColor": vision_zones_colour(feature["properties"]["Name"]),
            "color": "black",
            "weight": 2,
            "dashArray": "5, 5"}, popup = popup04).add_to(map1) 
    height_zoning = programme_layers.checkbox("نظام ارتفاعی پیشنهادی")
    if height_zoning:
        height_zones = r"geojsons\Height_Zones.geojson"
        folium.GeoJson(height_zones, style_function=lambda feature: {
            "fillColor": height_zones_colour(feature["properties"]["Eng_Name"]),
            "color": "black",
            "weight": 2,
            "dashArray": "5, 5"}, popup = popup05).add_to(map1)
    
other_layer_toggle = programme_layers.toggle("سایر لایه ها")
if other_layer_toggle:
    current_buildings = programme_layers.checkbox("ابنیه موجود - اعیان")
    if current_buildings:
        buildings_layer = r"geojsons\Buildings.geojson"
        folium.GeoJson(buildings_layer, fill_color = "grey", color="black",
                       weight = 1, popup=popup06).add_to(map1)
    current_landuse = programme_layers.checkbox("کاربری وضع موجود اراضی شهر")
    if current_landuse:
        current_landuse_file = r"geojsons\Parcels.geojson"
        folium.GeoJson(current_landuse_file, style_function=lambda feature: {
            "fillColor": landuse_colour(feature["properties"]["Landuse"]),
            "color": "black",
            "weight": 1}, popup=popup07).add_to(map1)
    neighbourhoods = programme_layers.checkbox("محدوده محلات")
    if neighbourhoods:
        neighbourhoods_file = r"geojsons\Mahallat_Ejtemayi.geojson"
        folium.GeoJson(neighbourhoods_file, color= "black", dashArray= "5,5", 
                       fill_color= "#728944", fill_opacity= 0.2, popup=popup08).add_to(map1)
    current_plan = programme_layers.checkbox("طرح تفصیلی ملاک عمل (تا 1404)")
    if current_plan:
        current_implemented_plan = r"geojsons\Current_Implemented_Plan.geojson"
        folium.GeoJson(current_implemented_plan, style_function=lambda feature: {
            "fillColor": currentplan_colour(feature["properties"]["Layer"]),
            "color": "black","weight": 1}
                       , popup=popup09).add_to(map1)
    detailed_project = programme_layers.checkbox("موقعیت طرح های موضعی پیشنهادی")
    if detailed_project:
        detailed_plans = r"geojsons\Detailed_Projects.geojson"
        folium.GeoJson(detailed_plans, style_function=lambda feature: {
            "fillColor": detailed_projects_colour(feature["properties"]["Name"]),
            "color": "black",
            "weight": 2,"dashArray": "5, 5"}, popup=popup04).add_to(map1)
    public_facilities = programme_layers.checkbox("موقعیت خدمات عمومی غیرانتفاعی پیشنهادی")
    if public_facilities:
        public_amenities = r"geojsons\Public_Amenities.geojson"
        folium.GeoJson(public_amenities, style_function=lambda feature: {
            "fillColor": facilities_colour(feature["properties"]["Eng_Name"]),
            "color": "black",
            "weight": 1,
        }
                       , popup=popup05).add_to(map1)
    city_roads = programme_layers.checkbox("شبکه معابر پیشنهادی")
    if city_roads:
        roads_file = r"geojsons\City_Roads.geojson"
        pouste = r"geojsons\Pousteh_Pish.geojson"
        folium.GeoJson(roads_file,style_function=lambda feature: {
            "color": road_color(feature["properties"]["Selsele"]),
            "weight": 2}, 
                       popup=popup11).add_to(map1)
        folium.GeoJson(pouste, style_function= lambda features: {"color" : "#292B27",
                                                                  "weight" : 2}).add_to(map1)
  
  
  



world_layers = st.sidebar.expander("لایه های مربوط به میراث جهانی بشر")
historical_roads = world_layers.toggle("راه های تاریخی")
if historical_roads:
    ancient_road_json = r"geojsons\Ancient_Road.geojson"
    folium.GeoJson(
        ancient_road_json,
        style_function=lambda feature: {
            "color": ancient_road_colour(feature["properties"]["Route_Name"]),
            "weight": 6,
            "dashArray": "12, 12",}, popup=popup10).add_to(map1)
    ancient_Eu_road_json = r"geojsons\Ancient_Road_European.geojson"
    folium.GeoJson(
        ancient_Eu_road_json,
        style_function=lambda feature: {
            "color": ancient_Eu_road_colour(feature["properties"]["CATEGORY"]),
            "weight": 6,
            "dashArray": "12, 12",}, popup=popup20).add_to(map1)
    
world_heritage_sites = world_layers.toggle("سایت های ثبت شده در میراث جهانی")
if world_heritage_sites:
    world_heritage_file = r"geojsons\World_Heritage_Sites.geojson"
    gdf = gpd.read_file(world_heritage_file)
    whs_locations=[]
    info=[]

    for idx, row in gdf.iterrows():
        whs_locations.append([row["element_la"], row["element_lo"]])
        info.append([row["element_na"], row["property_2"]])
    popups = ["Element Name:{}<br>Description:{}".format(name, desc) for (name, desc) in info]
    MarkerCluster(locations=whs_locations,
                  popups=popups,
                  name="1000 clustered icons",
                  overlay=True,
                  control=True).add_to(map1)

    
    
    
    
uploading = st.sidebar.selectbox("فرمت فایل موردنظر خود را انتخاب کنید", options=["shp", "json", "geojson"])
if uploading == "json" or uploading == "geojson":
    message = st.sidebar.info("فایل جی سان خود را آپلود کنید. فایل مذکور می بایست دارای ستون ژئومتری باشد.")
    uploaded_files = st.sidebar.file_uploader("Upload your file", type=["json", "geojson"],
                                              accept_multiple_files=True)
    if uploaded_files is not None:
        for file in uploaded_files:
            your_file = gpd.read_file(file)
            cols = list(your_file.columns)
            folium.GeoJson(your_file, popup = folium.GeoJsonPopup(fields = cols[:-1])).add_to(map1)
else:
    st.sidebar.warning("شیپ فایل مورد نظر خود را در قالب یک فایل زیپ شده (به همراه سایر فایلهای مرتبط) آپلود کنید.")
    uploaded_shp_files = st.sidebar.file_uploader("فایل خود را اینجا آپلود کنید", type=["zip"],
                                                  accept_multiple_files=True)
    if uploaded_shp_files is not None:
        for file in uploaded_shp_files:
    # Create a BytesIO object from the uploaded file
            zip_file_bytes = io.BytesIO(file.getvalue())

        # Extract the contents of the zip file
            with zipfile.ZipFile(zip_file_bytes, 'r') as zip_ref:
        # Find the .shp file within the zip archive
                shp_file = next((f.filename for f in zip_ref.infolist() if f.filename.endswith('.shp')), None)

            if shp_file:
                # Extract all files to a temporary directory or read directly if possible
                # For direct reading, geopandas can often handle paths within a zip file if specified correctly.
                
                try:
                    gdf = gpd.read_file(f"/vsizip/{file.name}/{shp_file}")
                except Exception as e:
                    st.error(f"Error reading shapefile: {e}")
                    st.info("مطمئن شوید که تمام فایلهای مرتبط با شیپ فایل تان به همراه فایل اصلی در پوشه زیپ شده قرار داشته باشد.")
                    gdf = None

                if gdf is not None:
                    cols = list(gdf.columns)
                    folium.GeoJson(gdf, popup = folium.GeoJsonPopup(fields = cols[:-1])).add_to(map1)
            else:
                st.error("شیپ فایلی در فایل زیپ بارگزاری شده یافت نشد. از زیپ شدن فایل اطمینان حاصل کنید.")
    

folium.FitOverlays().add_to(map1)

map_town = stf(map1, width=700, height=600, use_container_width=True)






