import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt 
from streamlit_folium import st_folium as stf
from shapely import Point, Polygon
import pandas as pd
import shutil
import os
import folium
from folium.plugins import MeasureControl
import utm
from pyproj import CRS
import networkx as nx
import json


@st.cache_data
def load_data(path):
    return gpd.read_file(path)

# my directory
main_directory = r'D:\Arash\StreamLit\Other_Try\Multipage'


# basic files for working with
parcels = r"D:\Arash\StreamLit\Other_Try\Multipage\geojsons\Parcel1401.geojson"
gdf_parcels = load_data(parcels)
gdf_parcels_check = gdf_parcels.set_index("ObjectID", drop=False)

@st.cache_data
def find_parcel(id):
    try:
        return gdf_parcels_check.loc[[id]]
    except KeyError:
        return None

city_zones = r"D:\Arash\StreamLit\Other_Try\Multipage\geojsons\City_Zoning.geojson"
city_zoning = load_data(city_zones)
functions_list = []
with open("Functions1.txt") as file:
    for row in file:
        functions_list.append(row)

gdf_parcels = gdf_parcels.to_crs('EPSG:32639')

axial_map_json = r"D:\Arash\StreamLit\Other_Try\Multipage\geojsons\Axial_Map.geojson"
axial_map = load_data(axial_map_json) 


# to find residential rate in each zone
@st.cache_data
def zone_res(zone):
    zone_f = city_zoning.loc[city_zoning["ZirPahne"]==zone]
    zone_join = gdf_parcels.sjoin(zone_f, predicate="intersects", how="left")
#     if "Landuse" in zone_join.columns:
    zone_join = zone_join.loc[zone_join["ZirPahne"] == zone]
    b_f = zone_join.loc[zone_join["Landuse"]==1].count() / zone_join.count()
    res_rate = b_f.iloc[0]
    return res_rate

historical_sites_path = r"D:\Arash\StreamLit\Other_Try\Multipage\geojsons\Historical_sites_boundaries.geojson"
historical_sites = load_data(historical_sites_path)

parcel_width = r"D:\Arash\StreamLit\Other_Try\Multipage\geojsons\Parcel_width.geojson"
parcel_width_road = load_data(parcel_width)

parcel_angle = r"D:\Arash\StreamLit\Other_Try\Multipage\geojsons\parcel_angle.geojson"
parcel_angle_gdf = load_data(parcel_angle)

@st.cache_data
def read_pd_file(path):
    return pd.read_excel(path)

# a function to convert landuse codes to descriptions
def landuse_current(a):
    if a==1:
        return "مسکونی"
    elif a==2:
        return "آموزش تحقیقات و فناوری"
    elif a==3:
        return "آموزشی"
    elif a==4:
        return "اداری انتظامی"
    elif a==5:
        return "تجاری خدماتی"
    elif a==6:
        return "ورزشی"
    elif a==7:
        return "درمانی"
    elif a==8:
        return "فرهنگی هنری"
    elif a==9:
        return "پارک و فضای سبز"
    elif a==10:
        return "مذهبی"
    elif a==11:
        return "تاسیسات شهری"
    elif a==12:
        return "تجهیزات شهری"
    elif a==13:
        return "حمل و نقل و انبارداری"
    elif a==14:
        return "نظامی"
    elif a==15:
        return "باغات و کشاورزی"
    elif a==16:
        return "میراث تاریخی"
    elif a==17:
        return "طبیعی"
    elif a==18:
        return "صنعتی"
    elif a==19:
        return "حریم"
    elif a==20:
        return "تفریحی توریستی"
    elif a==21:
        return "مختلط مسکونی-تجاری"
    elif a==28:
        return "فاقد بنا و استفاده"
    else:
        return "خارج از محدوده و یا در مسیر معابر"

# to show the residential rate in zone
basic_rates = r"D:\Arash\StreamLit\Other_Try\Multipage\Residential_Rates.xlsx"
basic_rates_df = read_pd_file(basic_rates).set_index("title", drop=False)

city_blocks = r"D:\Arash\StreamLit\Other_Try\Multipage\geojsons\City_New_Blocks.geojson"
city_blocks_gdf = load_data(city_blocks)
city_blocks_gdf = city_blocks_gdf.to_crs('EPSG:32639')

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
    residential_functions = ["یک یا دوخانواری", "آپارتمان", "مسکونی موقت (استفاده فصلی)"]
    if zone == "R121":
        b = 0.7
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "R122":
        b = 0.7
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "R211":
        b = 0.7
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "R212":
        b = 0.75
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "R311":
        b = 0.65
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "R321":
        b = 0.75
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "R322":
        b = 0.65
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "M111":
        b = 0.6
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "M121":
        b = 0.55
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "M311":
        b = 0.4
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "M321":
        b = 0.45
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "M322":
        b = 0.45
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "S111":
        b = 0.3
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "S112":
        b = 0.2
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    elif zone == "S211":
        b = 0.35
        r = zone_res(zone)
        if (b >= r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request not in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این امر عملکرد مورد درخواست مورد حمایت است .</p>'
        elif (b < r and plot_request in residential_functions) :
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} درصد است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت انتخاب سایر عملکردهای غیرسکونتی مجاز در پهنه مورد حمایت است .</p>'
        else:
            return f'<p class="persian-text">نسبت سکونت به فعالیت در این پهنه در حال حاضر {round(r*100,1)} است. نسبت بهینه برای این پهنه {round(b*100,1)} درصد است. با توجه به این نسبت استقرار عملکرد سکونتی نیز مورد حمایت است .</p>'
    else:
        return '<p class="persian-text">نسبت سکونت و فعالیت در این پهنه قابل ارائه نمی باشد</p>'
@st.cache_data
# for historical part
def historical_zone(zone):
    if zone == "H111" or zone == "H211":
        return True
    else:
        return False
   
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    .persian-text {
        font-family: 'Vazirmatn', sans-serif;
        font-size: 20px
        direction: rtl;
        text-align: right;
        }
    </style>
    """,
    unsafe_allow_html=True
    )
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    .persian-titr1 {
        font-family: 'Vazirmatn', sans-serif;
        font-size: 100px;
        direction: rtl;
        text-align: right;
        color: red;
        }
    </style>
    """,
    unsafe_allow_html=True
    )
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    .persian-titr2 {
        font-family: 'Vazirmatn', sans-serif;
        direction: rtl;
        text-align: right;
        color: blue;
        }
    </style>
    """,
    unsafe_allow_html=True
    )  
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    .persian-titr3 {
        font-family: 'Vazirmatn', sans-serif;
        direction: rtl;
        text-align: right;
        color: orange;
        }
    </style>
    """,
    unsafe_allow_html=True
    )               
# creating the page with a title
st.image("Law.jpg", width=400)   

# about this page and its purposes
col1, col2 = st.columns(2)
col2.markdown('<p class="persian-text">این بخش از نرم افزار جامع طرح ویژه سلطانیه برای ساکنان شهر، توسعه‌دهندگان، سازندگان، کارکنان شهرداری و کسانی است که می‌خواهند در مورد ضوابط و مقررات حاکم بر ملک خود بدانند. این بخش شامل موارد زیر است:</p>',
              unsafe_allow_html=True)
col1.image("IMG_7451.jpg", width=450)
col1.image("IMG_7453.jpg", width=450)
col2.write('<p class="persian-titr2">پهنه دربرگیرنده قطعه زمین را مشخص می کند.</p>',
           unsafe_allow_html=True)
col2.write('<p class="persian-titr2">عرض معبر دسترسی ملک را تعیین می کند. </p>',
           unsafe_allow_html=True)
col2.write('<p class="persian-titr2">چنانچه ملک دارای کاربری خدمات عمومی غیرانتفاعی باشد، ضمن اعلام ضوابط کاربری مذکور را ارائه می دهد .</p>',
           unsafe_allow_html=True)
col2.write('<p class="persian-titr2">حداکثر ارتفاع قانونی ساختمان قابل احداث را ارائه می دهد.</p>',
           unsafe_allow_html=True)
col2.write('<p class="persian-titr2">موقعیت ملک را نسبت به طرحهای موضعی پیشنهادی مشخص می کند.</p>',
           unsafe_allow_html=True)
col2.write('<p class="persian-titr2">در صورت لزوم بهترین عملکرد/ها را برای اجرا در آن بخش از شهر پیشنهاد می دهد.</p>',
           unsafe_allow_html=True)
col2.write('<p class="persian-titr2">بهترین نوع فرم توده گذاری ساختمان در سطح قطعه را تعیین می کند.</p>',
           unsafe_allow_html=True)
col2.write('<p class="persian-text">اگر نیاز به دانستن در مورد این مجموعه ضوابط و مقررات دارید، باید از قبل اطلاعاتی را در فرم زیر وارد کنید. اولین مورد، کد نوسازی است که برای هر قطعه زمین منحصر به فرد است. نرم افزار با استفاده از این کد می‌تواند ملک را پیدا کند و اطلاعات مربوطه را بر اساس مباحث فوق‌الذکر بازگرداند. مورد دیگر که باید تکمیل شود، مساحت و ابعاد قطعه زمین بر اساس سند ملکی (یا اسناد قانونی مشابه) است. این بخش باید با دقت نوشته شود، زیرا برنامه محاسباتی روی اعداد وارد شده انجام می‌دهد و در صورت وجود هرگونه ارتباط نادرست بین آنها، خطای مذکور را گوشزد می کند. </p>',
           unsafe_allow_html=True)
col2.write('<p class="persian-titr1">نکته مهم: به دلیل شرایط حفظ حریم خصوصی، نیازی به ارائه نام یا شماره ملی خود به برنامه ندارید.</p>',
           unsafe_allow_html=True)
col2.write('<p class="persian-text">با این اطلاعات و تعیین عملکرد مورد نظر برای راه اندازی در ملک، پس از بررسی لازم بر روی نقشه ها و ضوابط طرح ویژه، ضوابط و مقررات اصلی مربوط به قطعه زمین مورد نظر استخراج و ارائه می شود</p>',
           unsafe_allow_html=True)
st.write('<p class="persian-titr2">اگر می‌خواهید قوانین و مقررات شهری مربوط به ملک خود را دریافت کنید، بر روی این فرم کلیک کنید.</p>',
         unsafe_allow_html=True)


# creating a form to give initial info
owner_form = st.expander("بر روی فرم کلیک کنید")

plot_code = owner_form.number_input("کد نوسازی ملک را وارد نمایید", min_value=0,
                        placeholder="Enter the code", value=None, key="code")

def check_plot_code(code):
    if plot_code is not None:
        if len(str(st.session_state.code)) != 5:
            st.error("کد وارد شده صحیح نمی باشد. لطفا کد صحیح را وارد کنید.", icon="🚨") 
        else:
            if len(find_parcel(st.session_state.code)) != 1:
                st.error("کد وارد شده در سامانه کدهای نوسازی شهر سلطانیه ثبت نشده است. لطفا از درستی کد اطمینان حاصل فرمایید", icon="🚨")
            else:
                return st.session_state.code
    else:
        st.info("لطفا ابتدا کد نوسازی ملک مورد استعلام را وارد کنید")


if plot_code is not None and check_plot_code(plot_code) == plot_code:
    plot_location = find_parcel(st.session_state.code).to_crs('EPSG:32639')
    plot_location_point = gpd.points_from_xy(plot_location.centroid.x, plot_location.centroid.y,
                                             crs='EPSG:32639')
    plot_location = plot_location.reset_index(drop=True)

    join_info = plot_location.sjoin(city_zoning, predicate ="intersects", how="left")
    main_zone = ""
    for zone in list(join_info['ZirPahne']):
        zone1 = city_zoning.loc[city_zoning["ZirPahne"]==zone]
        for poly in zone1.geometry:
            m = Polygon(poly)
            if plot_location_point.within(m):
                main_zone = zone

                
                
    plot_area = owner_form.number_input("مساحت ملک را بر اساس سند رسمی و به مترمربع وارد کنید",
                            placeholder="Enter the area", value=None, key="area", disabled=historical_zone(main_zone),
                            step=1.0)
    plot_width = owner_form.number_input("میزان طول قطعه را بر حسب متر و بر اساس سند رسمی وارد کنید",
                            placeholder="Enter the dimention", value=None, key="width", disabled=historical_zone(main_zone))
    plot_depth = owner_form.number_input("میزان عمق قطعه را بر حسب متر و بر اساس سند رسمی وارد کنید",
                            placeholder="Enter the dimention", value=None, key="depth", disabled=historical_zone(main_zone))




    acceptable_functions = []

    base_law = r"D:\Arash\StreamLit\Other_Try\Multipage\Plot_area_road_width.xlsx"
    base_law_df = pd.read_excel(base_law)

    if main_zone != "":
        if main_zone != "H111" and main_zone != "H211":
            for idx,row in base_law_df.iterrows():
                if row[f"{main_zone}"] == "a":
                    acceptable_functions.append(row["persian title"])

        else:
    # to show the historical sites and the bans dominationg them
            st.markdown('<p class="persian-titr2">نتایج بررسی قطعه</p>', unsafe_allow_html=True)
            st.write('<p class="persian-text">به سبب آن که ملک مورد نظر در عرصه تاریخی قرار گرفته است، هر گونه اقدام مستلزم استعلام از اداره کل میراث فرهنگی، گردشگری و صنایع دستی استان است.</p>',
                    unsafe_allow_html=True)
            historical_map = historical_sites.explore()
            plot_location.explore(m = historical_map, color="#EB4D52")
            show_map = stf(historical_map)
        
        
    # a list of all functions to select from
    list_functions = []
    for idx,row in base_law_df.iterrows():
        list_functions.append(row["persian title"])

    plot_request = owner_form.selectbox("عملکرد موردنظر را بر اساس این فهرست انتخاب کنید", options = list_functions,
                                        placeholder="Select from this list", index=None, key = "request", 
                                        disabled=historical_zone(main_zone))


    # to find relevant local project
    base_local_projects = r"D:\Arash\StreamLit\Other_Try\Multipage\geojsons\Detailed_Projects.geojson.geojson"
    local_projects = load_data(base_local_projects)
    local_projects = local_projects.to_crs('EPSG:32639')


    # to find if the plot has a public facility laduse
    public_facilities = r"D:\Arash\StreamLit\Other_Try\Multipage\geojsons\Public_Facilities.geojson"
    public_facilities_gdf = load_data(public_facilities)  
    public_facilities_gdf = public_facilities_gdf.to_crs('EPSG:32639')  


    # to show a picture taken around the plot
    photos = r'D:\Arash\ArcGis_Pro_Manual\Folium_Map_Interactive\Shp\new_photos.shp'
    photo_points = load_data(photos)
    photo_points = photo_points.to_crs('EPSG:32639')
    closest_photo = plot_location.sjoin_nearest(photo_points, distance_col="Distance")

    # basic file to assess if a plot is inside a historical site or buffer zone
    historical_buffers = r"D:\Arash\StreamLit\Other_Try\Multipage\geojsons\Historical_Buffer_Boundaries.geojson"
    historical_buffer_gdf = load_data(historical_buffers)
    historical_buffer_gdf = historical_buffer_gdf.to_crs('EPSG:32639')
    def building_height(point):
        msg7 = ""
        for idx,area in historical_buffer_gdf.iterrows():
            if point.within(Polygon(area.geometry)) == True:
                msg7 = f"{area['Name']}"
        if msg7 == "" or msg7 == "Second Buffer Zone":
            return f'<p class="persian-text">بر اساس نقشه پهنه بندی نظام ارتفاعی، حداکثر ارتفاع ساختمان در این ملک برابر 10.5 متر است.</p>'
        elif msg7 == "First Buffer Zone":
            return f'<p class="persian-text">بر اساس نقشه پهنه بندی نظام ارتفاعی، حداکثر ارتفاع ساختمان در این ملک برابر 7.5 متر است.</p>'
        else:
            return f'<p class="persian-text">به سبب قرارگیری در عرصه تاریخی نیازمند استعلام از اداره کل میراث فرهنگی، گردشگری و صنایع دستی استان زنجان است.</p>'
            

    # to assess the information whether it is true or needs corrections
    # assessment_button = st.toggle("بررسی و اعلام نتایج")
    # if assessment_button:
    assessment = []
    if st.session_state.code is not None and st.session_state.area is not None and st.session_state.depth is not None and st.session_state.width is not None and st.session_state.request is not None:
        if len(str(st.session_state.code)) != 5:
            st.error("کد وارد شده صحیح نمی باشد. لطفا کنترل نمایید.", icon="🚨") 
        else:
            assessment.append(1)
        if len(gdf_parcels.loc[gdf_parcels["ObjectID"]== int(st.session_state.code)]) == 1:
            assessment.append(1)
        else:
            st.error("کد وارد شده مربوط به املاک شهر سلطانیه نیست. از صحت کد اطمینان حاصل فرمایید.", icon="🚨")
        if abs(st.session_state.area - (st.session_state.depth * st.session_state.width)) >= 5:
            st.error("مساحت وارد شده می بایست با حاصل ضرب ابعاد وارد شده تقریبا برابر باشد. لطفا اطلاعات وارد شده را کنترل کنید.", icon="🚨")
        else:
            assessment.append(1)
        if st.session_state.area <= 0 or st.session_state.depth <=0 or st.session_state.width <=0:
            st.error("مساحت و ابعاد می بایست اعداد مثبت باشند.", icon="🚨")
        else:
            assessment.append(1)
        if len(st.session_state.request) !=0:
            assessment.append(1)
        else:
            st.error("شما می بایست عملکردی را به عنوان درخواست به سامانه اعلام فرمایید. لطفا ردیف مربوطه را تکمیل فرمایید.", icon="🚨")


    # final step; to show the law and regulations about the plot  
    if sum(assessment) == 5:
        msg1, msg2, msg3, msg4 = "", "", "", ""
            
        st.info("اطلاعات وارد شده قابل بررسی است. ضوابط و مقررات مربوط به ملک در موارد زیر ارائه شده است. همچنین بر روی نقشه موقعیت ملک در شهر سلطانیه نشان داده شده است.")

        # to show current condition
        st.markdown('<p class="persian-titr2">وضعیت موجود ملک</p>', unsafe_allow_html=True)
        msg7 = False
        for idx,area in historical_buffer_gdf.iterrows():
            if plot_location_point.within(Polygon(area.geometry)):
                if area["Name"] == "Second Buffer Zone":
                    msg7 = True
                    st.write(f'<p class="persian-text">. ملک در حریم درجه 2 عرصه های تاریخی قرار گرفته است </p>', unsafe_allow_html=True)
                elif area["Name"] == "First Buffer Zone":
                    msg7 = True
                    st.write(f'<p class="persian-text">. ملک در حریم درجه 1 عرصه های تاریخی قرار گرفته است </p>', unsafe_allow_html=True)
                elif area["Name"] == "Landscape Buffer Zone" or area["Name"] == "":
                    msg7 = True
                    st.write(f'<p class="persian-text">. ملک در خارج از حرایم درجه 1 و 2 عرصه های تاریخی (و در داخل حریم منظری) قرار گرفته است </p>', unsafe_allow_html=True)
                else:
                    msg7 = True
                    st.write(f'<p class="persian-text">. این ملک در محدوده عرصه تاریخی قرار گرفته است. هر گونه اقدام مستلزم استعلام از اداره کل میراث فرهنگی، گردشگری و صنایع دستی استان زنجان است </p>', unsafe_allow_html=True)
        if msg7 == False:
            st.write(f'<p class="persian-text">. ملک در خارج از محدوده و حرایم درجه 1 و 2 عرصه های تاریخی (و در داخل حریم منظری) قرار گرفته است </p>', unsafe_allow_html=True)
                       
        st.write(f'<p class="persian-text"> . کاربری ملک در وضع موجود {landuse_current(list(plot_location["Landuse"])[0])} است</p>' , unsafe_allow_html=True)
        if int(list(plot_location['Floor'])[0]) >0:
            st.write(f'<p class="persian-text">. بنای موجود در ملک {list(plot_location["Floor"])[0]} طبقه است</p>', unsafe_allow_html=True)
        st.write(f'<p class="persian-text">. مساحت قطعه بر اساس نقشه سامانه {round(list(plot_location.area)[0],2)} مترمربع است</p>',
                 unsafe_allow_html=True)
             
        parcel_image = shutil.copyfile(closest_photo["Path"].values[0], os.path.join(main_directory, closest_photo["Name"].values[0]))
        st.image(parcel_image, width=400, caption="تصویری از ملک و موقعیت و همجواریهای آن")
        
        
        
        # to find rules and regulations    
        st.markdown('<p class="persian-titr2">ضوابط و مقررات</p>', unsafe_allow_html=True)
        st.markdown('<p class="persian-titr1">موقعیت در پهنه بندی و عرض معبر دسترسی</p>', unsafe_allow_html=True)
        
        road_width = parcel_width_road.loc[parcel_width_road["ObjectID"] == st.session_state.code]["Arz_Gozar"].values[0]
        
        st.write(f'<p class="persian-text">. قرار گرفته است  {main_zone} قطعه مورد استعلام در پهنه </p>', unsafe_allow_html=True)
        st.markdown(f'<p class="persian-text">. عرض معبر دسترسی ملک بر اساس طرح تفصیلی برابر {road_width} متر می باشد </p>', unsafe_allow_html=True)
        
        # to find area after being editted by the road network
        parcel = gdf_parcels.loc[gdf_parcels["ObjectID"] == plot_code].to_crs('EPSG:32639')
        clipped_parcel = gpd.clip(parcel, city_blocks_gdf).to_crs('EPSG:32639')
        # epsg = findtheutm(clipped_plot.geometry.iloc[0]) #Input the dfs first geometry to the function and get utm epsg code back
        # clipped_plot['correctArea'] = clipped_plot.to_crs(epsg).area # /1e6 for km2
        

        editted_area = list(parcel.area)[0] - list(clipped_parcel.area)[0]
        if editted_area > 0:
            st.write(f'<p class="persian-text">. مساحت قطعه پس از اصلاح ناشی از شبکه معابر پیشنهادی طرح برابر {round(list(clipped_parcel.area)[0],2)} می باشد</p>',
                     unsafe_allow_html=True)
        else:
            st.write('<p class="persian-text">. مطابق نقشه طرح تفصیلی قطعه مورد نظر نیازمند اصلاح از نظر شبکه معابر نمی باشد</p>',
                     unsafe_allow_html=True)

        
        #to find parcel on facilities map before function assessment
        st.markdown('<p class="persian-titr1">موقعیت نسبت به کاربریهای خدمات عمومی غیرانتفاعی</p>', unsafe_allow_html=True)
        facilities_join = plot_location.sjoin(public_facilities_gdf, predicate="intersects", how="left")
        for item in list(facilities_join["Khadamat_P"]):
            if item == " " :
                msg6 = ""
                landuse = ""
            else:
                msg6 = f'<p class="persian-text">این قطعه دارای کاربری {item} می باشد . هر گونه اقدام مستلزم رعایت ضوابط و مقررات این کاربری است .</p>'
                landuse = item
        if msg6 != "":
            st.write(msg6, unsafe_allow_html=True)

        else:
            st.write('<p class="persian-text">. قطعه مورد استعلام از کاربری های خدمات عمومی غیرانتفاعی موجود یا پیشنهادی نمی باشد</p>',
                     unsafe_allow_html=True)
            #st.write(f"The minimum area of plot for running {plot_request} is {base_law_df.loc[base_law_df['english_title'] == plot_request]['s_area'].values}")
            st.markdown('<p class="persian-titr1">بررسی امکان استقرار عملکرد</p>', unsafe_allow_html=True)
            # st.markdown('<p class="persian-titr3">بررسی بر اساس نسبت سکونت به فعالیت در پهنه</p>', unsafe_allow_html=True)
            st.write(residential_rate(main_zone), unsafe_allow_html=True)

            if st.session_state.request in acceptable_functions:
                r_function = True
            else:
                r_function = False
                st.markdown('<p class="persian-titr3">بررسی بر اساس فهرست عملکردهای مجاز</p>', unsafe_allow_html=True)
                st.write(f'<p class="persian-text">. قرار ندارد {main_zone} عملکرد مورد نظر در فهرست عملکردهای مجاز به استقرار در پهنه </p>',
                         unsafe_allow_html=True)
                #st.write(f'<p class="persian-text">عملکردهای مجاز به استقرار در پهنه {main_zone} شامل {acceptable_functions} می باشد .</p>', unsafe_allow_html=True)
                st.write('<p class="persian-text">: فهرست عملکردهای مجاز به استقرار در این پهنه شامل موارد زیر است</p>',
                         unsafe_allow_html=True)
                st.write(f'<p class="persian-text">{"، ".join(acceptable_functions)}</p>',
                         unsafe_allow_html=True)
                #st.write(f"{acceptable_functions}")
            
            minimum_area = float(base_law_df.loc[base_law_df["persian title"] == st.session_state.request]["s_area"])
            
            if float(st.session_state.area) < minimum_area:
                r_area = False
            else:
                r_area = True
                
            minimum_road = float(base_law_df.loc[base_law_df["persian title"] == st.session_state.request]["s_road_width"])
            
            if float(road_width) < minimum_road:
                r_road_width = False
            else:
                r_road_width = True

            if r_function == True and r_area == True and r_road_width == True:
                msg1 = st.write('<p class="persian-text">. بر اساس پهنه فراگیر، عرض گذر دسترسی و مساحت قطعه مورد استعلام، استقرار عملکرد مورد درخواست مجاز است </p>', unsafe_allow_html=True)

            if r_function == True and r_area == True and r_road_width == False:
                msg2 = st.write('<p class="persian-text">. علی رغم آن که عملکرد مورد درخواست در فهرست عملکردهای مجاز پهنه فوق الذکر قرار دارد و مساحت قطعه مورد استعلام نیز برای این منظور مناسب است، به سبب کمتر بودن عرض گذر دسترسی از مقدار استاندارد موردنیاز عملکرد مذکور، استقرار این عملکرد امکانپذیر نمی باشد </p>', unsafe_allow_html=True)

            
            if r_function == True and r_road_width == True and r_area == False:
                msg3 = st.write('<p class="persian-text">. علی رغم آن که عملکرد مورد درخواست در فهرست عملکردهای مجاز به استقرار پهنه فوق الذکر است و عرض گذر دسترسی نیز برای راه اندازی عملکرد مذکور مناسب است، به سبب آن که مساحت قطعه از حداقل لازم برای راه اندازی عملکرد مذکور کمتر است، استقرار این عملکرد مجاز نمی باشد </p>', unsafe_allow_html=True)

            if r_function == True and r_road_width == False and r_area == False:
                msg4 = st.write('<p class="persian-text">. عملکرد مذکور در فهرست عملکردهای مجاز به استقرار در پهنه قرار دارد لیکن به سبب کمتر بودن مساحت قطعه از حداقل لازم برای راه اندازی این عملکرد و همچنین کمتر بودن عرض گذر دسترسی از حداقل استاندارد مدنظر ضوابط، استقرار این عملکرد در این قطعه مجاز نمی باشد </p>', unsafe_allow_html=True)

            if msg2 != "" or msg3 != "" or msg4 != "":
                suggestions1 = []
                for idx,row in base_law_df.iterrows():
                    if row["persian title"] in acceptable_functions and float(st.session_state.area)>= row["s_area"] and float(plot_location['Arz_Pishna'])>= row["s_road_width"]:
                        suggestions1.append(row["persian title"]) 

                #st.write(f'<p class="persian-text">بر اساس پهنه فراگیر قطعه مورد استعلام، مساحت ملک و عرض گذر دسترسی، عملکردهای قابل استقرار شامل : {" ، ".join(suggestions1)} می باشد .</p>', unsafe_allow_html=True)
                if len(suggestions1) != 0:
                    st.write('<p class="persian-text">: بر اساس پهنه فراگیر، مساحت و عرض گذر دسترسی قطعه مورد استعلام، عملکردهای قابل استقرار شامل موارد زیر است</p>',
                             unsafe_allow_html=True)
                    st.write(f'<p class="persian-text">{"، ".join(suggestions1)}</p>', unsafe_allow_html=True)
        st.markdown('<p class="persian-titr1">موقعیت نسبت به طرح های موضعی</p>', unsafe_allow_html=True)
        local_prs_join = plot_location.sjoin(local_projects, predicate="intersects", how="left")
        projects_names = ["طراحی دروازه های طبیعت", "طراحی محورهای دید به گنبد", "طراحی مبادی ورودی شهر",
                          "طراحی دروازه های تاریخی", "طراحی محورهای پیرامون ارگ", "طراحی محور طبیعت گردی",
                          "انسجام بخشی محدوده های شرق و غرب بلوار آزادی", "آماده سازی اراضی توسعه شرقی",
                          "طراحی مراکز محلات", "طراحی محور ملاحسن کاشی"]
        for project in list(local_prs_join["Prn_name"]):
            if project in projects_names:
            #if Polygon(project).contains(plot_location_point) == True:
                #msg5 = f'<p class="persian-text">این قطعه در محدوده طرح موضعی {project} قرار دارد .</p>'
                msg5 = f'<p class="persian-text">. این قطعه در محدوده طرح موضعی "{project}" قرار دارد </p>'
            else:
                msg5 = ""
        
        if len(msg5) > 0 :
            st.write(msg5, unsafe_allow_html=True)
        else:
            st.write('<p class="persian-text">. این قطعه در محدوده هیچ کدام از طرح های موضعی قرار ندارد </p>', unsafe_allow_html=True)
        

        # to write urban law and regulations based on landuse or zoning  
        st.markdown('<p class="persian-titr1">ضوابط و مقررات عمومی ساخت و ساز</p>', unsafe_allow_html=True)
        if landuse == "آموزشی":
            st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\L_Educational.pdf")
        elif landuse == "ورزشی":
            st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\L_Varzeshi.pdf")
        elif landuse == "فرهنگی هنری":
            st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\L_Farhangi.pdf")
        elif landuse == "پارک و فضای سبز":
            st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\L_Park.pdf")
        elif landuse == "اداری انتظامی":
            st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\L_Edari.pdf")
        elif landuse == "تاسیسات شهری":
            st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\L_Tasisat.pdf")
        elif landuse == "تجهیزات شهری":
            st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\L_Tajhizat.pdf")
        elif landuse == "درمانی":
            st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\L_Darmani.pdf")
        elif landuse == "مذهبی":
            st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\L_Mazhabi.pdf")
        else:
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
                        building_kind1 = st.write('<p class="persian-text">الگوی توده گذاری مورد حمایت در قطعه مذکور با توجه به شرایط آن دوطرفه منفصل است .</p>', unsafe_allow_html=True, key="twoparts")
                        st.write(f'<p class="persian-text">در صورت انتخاب الگوی فوق الذکر حداکثر سطح اشغال برابر با {floor_coverage2} در نظر گرفته می شود .</p>', unsafe_allow_html=True)
                        st.write(building_height(plot_location_point), unsafe_allow_html=True)
                        st.image("Twosided.jpg", width=500)
                    else:
                        building_kind2 =st.write('<p class="persian-text">الگوی توده گذاری بهینه بر اساس شرایط قطعه یک طرفه است .</p>', unsafe_allow_html=True, key="onesided1")
                        st.write(f'<p class="persian-text">حداکثر سطح اشغال بنا در این قطعه برابر {floor_coverage1} می باشد .</p>',
                                unsafe_allow_html=True)
                        st.write(building_height(plot_location_point), unsafe_allow_html=True)

                elif dimention_ratio >= 1 and dimention_ratio <= 1.8:
                    if st.session_state.area>=300 and (depth-6)/2>=4 and (width-6)/2>=4:
                        building_kind3 =st.write('<p class="persian-text">الگوی توده گذاری مورد حمایت در قطعه مذکور با توجه به شرایط آن الگوی چهار طرفه (حیاط مرکزی) است .</p>',
                                                unsafe_allow_html=True, key="foursided1")
                        st.write(f'<p class="persian-text">در صورت انتخاب الگوی فوق الذکر حداکثر سطح اشغال برابر با {floor_coverage2} در نظر گرفته می شود .</p>', unsafe_allow_html=True)
                        st.write(building_height(plot_location_point), unsafe_allow_html=True)
                        st.image("Foursided.png", width=500)
                    elif st.session_state.area>=300 and ((depth-6)/2<4 or (width-6)/2<4):
                        building_kind4 =st.write(f'<p class="persian-text">الگوی توده گذاری مورد حمایت در قطعه مذکور با توجه به شرایط آن الگوی سه طرفه است .</p>',
                                                unsafe_allow_html=True, key="uform1")
                        st.write(f'<p class="persian-text">در صورت انتخاب الگوی فوق الذکر حداکثر سطح اشغال برابر با {floor_coverage2} در نظر گرفته می شود .</p>', unsafe_allow_html=True)
                        st.write(building_height(plot_location_point), unsafe_allow_html=True)
                        st.image("Threesided.jpg", width=500)
                    elif st.session_state.area>=150 and st.session_state.area<300 and ((depth-6)/2>=4 or (width-6)/2>=4):
                        building_kind5 =st.write(f'<p class="persian-text">الگوی توده گذاری مورد حمایت در قطعه مذکور با توجه به شرایط آن الگوی سه طرفه است .</p>',
                                                unsafe_allow_html=True, key="uform2")
                        st.write(f'<p class="persian-text">در صورت انتخاب الگوی فوق الذکر حداکثر سطح اشغال برابر با {floor_coverage2} در نظر گرفته می شود .</p>', unsafe_allow_html=True)
                        st.write(building_height(plot_location_point), unsafe_allow_html=True)
                        st.image("Threesided.jpg", width=500)
                    elif st.session_state.area>=150 and st.session_state.area<300 and ((depth-6)/2<4 and (width-6)/2<4):
                        building_kind6 =st.write('<p class="persian-text">الگوی توده گذاری مورد حمایت در قطعه مذکور با توجه به شرایط آن الگوی دوطرفه متصل می باشد .</p>',
                                                unsafe_allow_html=True, key="lform1")
                        st.write(f'<p class="persian-text">در صورت انتخاب الگوی فوق الذکر حداکثر سطح اشغال برابر با {floor_coverage2} در نظر گرفته می شود .</p>', unsafe_allow_html=True)
                        st.write(building_height(plot_location_point), unsafe_allow_html=True)
                        st.image("Lshape.jpg", width=500)
                    elif st.session_state.area<150 and st.session_state.area>=75:
                        building_kind7 =st.write('<p class="persian-text">الگوی توده گذاری مورد حمایت در قطعه مذکور با توجه به شرایط آن الگوی دوطرفه متصل می باشد .</p>',
                                                unsafe_allow_html=True, key="lform2")
                        st.write(f'<p class="persian-text">در صورت انتخاب الگوی فوق الذکر حداکثر سطح اشغال برابر با {floor_coverage2} در نظر گرفته می شود .</p>', unsafe_allow_html=True)
                        st.write(building_height(plot_location_point), unsafe_allow_html=True)
                        st.image("Lshape.jpg", width=500)
                    else:
                        building_kind8 =st.write('<p class="persian-text">الگوی توده گذاری بهینه بر اساس شرایط قطعه یک طرفه است .</p>', 
                                                unsafe_allow_html=True, key="onesided2")
                        st.write(f'<p class="persian-text">حداکثر سطح اشغال بنا در این قطعه برابر {floor_coverage1} می باشد .</p>', 
                                unsafe_allow_html=True)
                        st.write(building_height(plot_location_point), unsafe_allow_html=True)
                elif dimention_ratio >= 3:
                    building_kind9 =st.write('<p class="persian-text">الگوی توده گذاری بهینه بر اساس شرایط قطعه یک طرفه است .</p>', 
                                            unsafe_allow_html=True, key="onesided3")
                    st.write(f'<p class="persian-text">حداکثر سطح اشغال بنا در این قطعه برابر {floor_coverage1} می باشد .</p>', 
                            unsafe_allow_html=True)
                    st.write(building_height(plot_location_point), unsafe_allow_html=True)
                else:
                    st.write('<p class="persian-text">درباره الگوی توده گذاری موردی برای ارائه وجود ندارد .</p>',
                            unsafe_allow_html=True)
            elif main_zone[0] == "S" and msg1 !="":
                building_kind10 =st.write('<p class="persian-text">الگوی توده گداری به صورت یک طرفه در نظر گرفته شود. ضمنا می بایست نمای اصلی بنا متصل به معبر اصلی دسترسی در نظر گرفته شود .</p>',
                                        unsafe_allow_html=True, key="onesidedcommercial")
                st.write(f'<p class="persian-text">حداکثر سطح اشغال بنا در این قطعه برابر {floor_coverage3} می باشد .</p>', 
                        unsafe_allow_html=True)
                st.write(building_height(plot_location_point), unsafe_allow_html=True)
                st.image("Commercial_facade.jpg", width=500)
            elif main_zone[:2] == "G2" and msg1 != "":
                st.write('<p class="persian-text">هر گونه مداخله و ساخت و ساز در این قطعه تابع ماده 14 قانون زمین شهری است .</p>',
                        unsafe_allow_html=True)
            elif main_zone[:2]== "G1" and msg1 != "":
                st.write('<p class="persian-text">با توجه به کاربری پارک و فضای سبز هر گونه اقدام ساختمانی مستلزم رعایت ضوابط و مقررات این کاربری است .</p>',
                        unsafe_allow_html=True)
            else:
                st.write('<p class="persian-text>ابتدا می بایست یکی از عملکردهای مجاز به استقرار در قطعه را بر اساس پهنه فراگیر امتخاب نمایید. لیست پیشنهادی ارائه شده در این بخش راهنمای خوبی در ابن راستا است .</p>',
                        unsafe_allow_html=True)
            # to show the location of the under investigated plot  
            angle = parcel_angle_gdf.loc[parcel_angle_gdf["ObjectID"] == st.session_state.code]["MBG_Orientation"].values[0]
            if building_kind1 != "":
                st.write('<p class="persian-text">در این الگو فضای باز قطعه (حیاط) مابین دو توده منفصل قرار می گیرد .</p>',
                        unsafe_allow_html=True) 
            if building_kind2 != "" or building_kind8 != "" or building_kind9 != "":
                st.write('<p class="persian-text">در این الگو فضای باز (حیاط) در یک سمت قطعه قرار می گیرد .</p>',
                        unsafe_allow_html=True)
            if building_kind3 != "":
                st.write('<p class="persian-text">در این الگو فضای باز (حیاط) در بخش مرکزی قطعه جانمایی می گیرد .</p>',
                        unsafe_allow_html=True)
            if building_kind4 != "" or building_kind5 != "":
                if float(angle) <= 20:
                    st.write('<p class="persian-text">فضای باز بهتر است در سمت شرق قطعه جانمایی گردد .</p>',
                            unsafe_allow_html=True)
                elif float(angle) > 20 and float(angle) <= 40:
                    st.write('<p class="persian-text">فضای باز می تواند در یکی از سمت های شرق یا غرب قطعه جانمایی گردد .</p>',
                            unsafe_allow_html=True)
                elif float(angle) > 40 and float(angle) <= 140:
                    st.write('<p class="persian-text">فضای باز بهتر است در سمت جنوب قطعه جانمایی گردد .</p>',
                            unsafe_allow_html=True)
                elif float(angle) > 140 and float(angle) <= 160:
                    st.write('<p class="persian-text">فضای باز می تواند در یکی از سمت های شرق یا غرب قطعه جانمایی گردد .</p>',
                            unsafe_allow_html=True)
                else:
                    st.write('<p class="persian-text">فضای باز بهتر است در سمت غرب قطعه جانمایی گردد .</p>',
                            unsafe_allow_html=True)
            if building_kind6 != "" or building_kind7 != "":
                if float(angle) <= 100:
                    st.write('<p class="persian-text">فضای باز می تواند در یکی از سمت های جنوب شرق یا جنوب غرب قطعه جانمایی گردد .</p>',
                            unsafe_allow_html=True)
                elif float(angle) > 100 and float(angle) <= 120:
                    st.write('<p class="persian-text">فضای باز می تواند در یکی از سمت های شمال شرق یا جنوب غرب قطعه جانمایی گردد .</p>',
                            unsafe_allow_html=True)
                else:
                    st.write('<p class="persian-text">فضای باز بهتر است در سمت جنوب غرب قطعه جانمایی گردد .</p>',
                            unsafe_allow_html=True)
        
            
    st.markdown('<p class="persian-titr1">موقعیت قطعه</p>', unsafe_allow_html=True)   
        
    map1 = folium.Map(zoom_start=18)
    folium.GeoJson(plot_location, color="#FF2828", popup = folium.GeoJsonPopup(fields=["Landuse", "Floor",
                                                                                "Shape_Area"])).add_to(map1)
    
    
    map1.add_child(MeasureControl(position="bottomleft",collapesed=False))
    folium.FitOverlays().add_to(map1)
    map_town = stf(map1, width=1000)
            


document_toggle = st.sidebar.toggle("گزارش ضوابط و مقررات طرح ویژه سلطانیه")   
if document_toggle:
    st.markdown('<p class="persian-titr2">گزارش کامل ضوابط و مقررات طرح ویژه سلطانیه</p>', unsafe_allow_html=True)
    st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\06_1_Zavabet_AsasTarh.pdf", height=800)