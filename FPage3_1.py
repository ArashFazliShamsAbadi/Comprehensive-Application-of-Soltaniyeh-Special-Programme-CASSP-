import streamlit as st
import os

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    .persian-text {
        font-family: 'Vazirmatn', sans-serif;
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

st.image("Albume.jpg", width=400)
":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

st.markdown('<p class="persian-titr2">در این صفحه می‌توانید خروجی‌های طرح ساختاری و تفصیلی ویژه سلطانیه را مشاهده کنید. برای اطلاعات بیشتر، می توانید به اصل گزارش ها که در همین اپلیکیشن ارائه شده مراجعه فرمایید.</p>',
            unsafe_allow_html=True)
":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

planning_map = st.sidebar.toggle("نقشه های طرح ساختاری")
if planning_map:
    st.markdown('<p class="persian-titr1">نقشه های طرح ساختاری</p>',
                unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.caption('<p class="persian-text">اساس طرح در مقیاس حریم</p>', unsafe_allow_html=True)
    col1.image("AsasTarhHarim.jpg")
    col2.caption('<p class="persian-text">اساس طرح در مقیاس شهر</p>', unsafe_allow_html=True)
    col2.image("AsasTarhShahr.jpg")
    col3.caption('<p class="persian-text">پهنه بندی پتانسیل عملکردی در حریم شهر</p>', unsafe_allow_html=True)
    col3.image("HarimDetailedZoning.jpg")
    col1.caption('<p class="persian-text">پهنه بندی اراضی حریم شهر</p>', unsafe_allow_html=True)
    col1.image("HarimMainZoning.jpg")
    col2.caption('<p class="persian-text">پهنه بندی ساماندهی حریم منظری</p>', unsafe_allow_html=True)
    col2.image("HarimManzari.jpg")
    col3.caption('<p class="persian-text">محدوده و حریم پیشنهادی</p>', unsafe_allow_html=True)
    col3.image("MahdoudeHarim.jpg")
    col1.caption('<p class="persian-text">محدوده پیشنهادی، مقایسه با محدوده موجود</p>', unsafe_allow_html=True)
    col1.image("MoqayeseMahdoodeh.jpg")
    col2.caption('<p class="persian-text">نقشه راه سلطانیه 1420</p>', unsafe_allow_html=True)
    col2.image("RoadMap.jpg")
    col3.caption('<p class="persian-text">سلسله مراتب شبکه معابر پیشنهادی</p>', unsafe_allow_html=True)
    col3.image("ShahrRoads.jpg")
    col1.caption('<p class="persian-text">پهنه بندی پیشنهادی نحوه استفاده از اراضی شهر</p>', unsafe_allow_html=True)
    col1.image("ShahrZoning.jpg")
    col2.caption('<p class="persian-text">موقعیت طرح های موضعی پیشنهادی</p>', unsafe_allow_html=True)
    col2.image("TarhHayeMozeyi.jpg")
    col3.caption('<p class="persian-text">پهنه بندی پیشنهادی استفاده از اراضی شهر بر اساس مقیاس عملکردی</p>', unsafe_allow_html=True)
    col3.image("ZoningShahrScales.jpg")
detailed_map = st.sidebar.toggle("نقشه های تفصیلی 1:2000")
if detailed_map:
    st.markdown('<p class="persian-titr1">نقشه های طرح تفصیلی در مقیاس 1:2000</p>',
                unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    for i in range(1,13,3):
        col1.image(os.path.join(r"D:\Arash\StreamLit\Other_Try\Multipage\Map2000", f"0{i}.jpg"))
        col2.image(os.path.join(r"D:\Arash\StreamLit\Other_Try\Multipage\Map2000", f"0{i+1}.jpg"))
        col3.image(os.path.join(r"D:\Arash\StreamLit\Other_Try\Multipage\Map2000", f"0{i+2}.jpg"))
        
        
    # for i in range(2,15,3):
    #     col2.image(os.path.join(r"D:\Arash\StreamLit\Other_Try\Multipage\Map2000", f"0{i}.jpg"))    
    # for i in range(3,15,3):
    #     col3.image(os.path.join(r"D:\Arash\StreamLit\Other_Try\Multipage\Map2000", f"0{i}.jpg"))  
document_toggle = st.sidebar.toggle("گزارش طرح تفصیلی")   
if document_toggle:
    st.markdown('<p class="persian-titr1">گزارش کامل طرح تفصیلی شهر</p>',
                unsafe_allow_html=True)
    st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\06_TarhTafsili_EslahiOstan.pdf", height=800)