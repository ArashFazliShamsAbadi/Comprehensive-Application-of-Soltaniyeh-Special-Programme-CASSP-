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
st.image("CurrentImage.jpg", width=400)
":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

env_expander = st.sidebar.expander("اقلیم، طبیعت و محیط زیست")


fpopulation = pd.read_excel("fDemography_pop.xlsx")
fpopulation_rate = pd.read_excel("fDemography_poprate.xlsx")
fage_sex85 = pd.read_excel("f85_agesex.xlsx")
fage_sex90 = pd.read_excel("f90_agesex.xlsx")
fage_sex95 = pd.read_excel("f95_agesex.xlsx")

finterpersonal_trust = pd.read_excel("finterpersonal_trust.xlsx")
finstutitional_trust = pd.read_excel("finstutitional_trust.xlsx")

fall_trust = pd.read_excel("fall_trust.xlsx")
fcommunication = pd.read_excel("fcommunication.xlsx")
fformal_participation = pd.read_excel("fformal_participation.xlsx")
finformal_participation = pd.read_excel("finformal_participation.xlsx")
fall_participation = pd.read_excel("fall_participation.xlsx")
fsocial_capital = pd.read_excel("fsocial_capital.xlsx")
fresilience = pd.read_excel("fresilience.xlsx")
fpeople_issues_file = pd.read_excel("fpeople_issues.xlsx")


fgeneral_economic_table = "fGeneral_Economic.xlsx"
feconomic_sectors_table = "fEconomic_Sectors.xlsx"
ftourists_table = "fTourists.xlsx"
fhotels = "fHotels.xlsx"

landcover_file = pd.read_excel("Landcover.xlsx")
landcover_df = pd.DataFrame(landcover_file)
landcover_df["percentage (%)"] = landcover_df["percentage (%)"]*100
fwater_file = pd.read_excel("fwater_supply.xlsx")
fwater_consumption = pd.read_excel("fwater_consumption.xlsx")
precipitation = pd.read_excel("precipitation.xlsx")
flanduse_raw_table = "flanduse.xlsx"
fparcels = "fParcels.xls"
fbuilding_direction = "fBuilding_Direction.xlsx"
fbuilding_toode = "fBuilding_Toodeh.xlsx"
fbuilding_toode_dimension = "fBuilding_Toodeh_Dimension.xlsx"
froads_traffic = "fRoads_Traffic.xlsx"
froads_traffic_barchart = "fRoads_Traffic_BarChart.xlsx"
froads_width = "fRoads_Width.xlsx"
froads_slop = "fRoads_Slop.xlsx"


landcover = env_expander.toggle("پوشش زمین")
if landcover:
    st.markdown('<p class="persian-titr1">پوشش زمین</p>', unsafe_allow_html=True)

    st.markdown('<p class="persian-text">۸۴٪ از زمین‌های این منطقه تحت پوشش کشاورزی است. پوشش درختی و سطوح آبی کمترین درصد پوشش را دارند. چمن سلطانیه با ۷۲۱ هکتار تقریباً ۳.۱٪ از منطقه را پوشش می‌دهد.</p>',
                unsafe_allow_html=True)
    st.image("Harim_Mojoud_C.jpg")
    #st.table(landcover_df)
    st.bar_chart(landcover_df, x="persian", y="percentage (%)",
                 x_label="پوشش زمین", y_label="درصد مساحت")

water_resource = env_expander.toggle("منابع آب")
if water_resource:
    st.markdown('<p class="persian-titr1">منابع آب</p>', unsafe_allow_html=True)

    st.markdown('<p class="persian-text">طبق آخرین گزارش شرکت آب و فاضلاب استان زنجان، منابع آب شهری شهر سلطانیه (که تنها نقطه شهری در شهرستان سلطانیه است) یک چاه است. حجم منابع آب زیرزمینی برای تأمین آب شهری (در سال 2022) 0.94 میلیون متر مکعب در سال ذکر شده است.</p>',
                unsafe_allow_html=True)
    st.write('<p class="persian-text">این جدول حجم کل منابع آب و میزان تولید شده در سال‌های اخیر را نشان می‌دهد.</p>', 
             unsafe_allow_html=True)
    st.table(fwater_file)
    st.markdown('<p class="persian-text">طبق اطلاعات موجود، بخش عمده و اصلی منابع آب در بخش کشاورزی مصرف می‌شود.</p>',
                unsafe_allow_html=True)
    st.table(fwater_consumption)
    st.markdown('<p class="persian-text">این نقشه نشان می‌دهد که چگونه سطح ایستابی در سال‌های اخیر کاهش یافته است</p>',
                unsafe_allow_html=True)
    st.image("Kahesh_Salane_SathAab.jpg")
    
climatic_factors = env_expander.toggle("مهمترین داده های اقلیمی")
if climatic_factors:
    st.markdown('<p class="persian-titr1">مهمترین داده های اقلیم و آب و هوا</p>', unsafe_allow_html=True)
    st.write('<p class="persian-text">میانگین حداکثر دمای روزانه بین سال‌های ۲۰۰۶ تا ۲۰۱۷  میلادی برابر 17.9+ درجه سانتیگراد بوده است.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">میانگین دمای روزانه بین سال‌های ۲۰۰۶ تا ۲۰۱۷ میلادی، ۱۱.۸+ درجه سانتیگراد بوده است.</p>',
             unsafe_allow_html=True) 
    st.write('<p class="persian-text">میانگین حداقل دمای روزانه بین سال های فوق الذکر، 2.5+ درجه سانتیگراد بوده است.</p>',
             unsafe_allow_html=True) 
    st.write('<p class="persian-text">میانگین بارندگی روزانه بین سال‌های ۲۰۰۶ تا ۲۰۱۷ میلادی، ۰.۸ میلی‌متر بوده است.</p>',
             unsafe_allow_html=True) 
    st.write('<p class="persian-text">بهار در سلطانیه پرباران‌ترین فصل سال است.</p>', unsafe_allow_html=True) 
    st.write('<p class="persian-text">این نمودار، میزان بارندگی سالانه را در بازه زمانی ۲۰۰۶ تا ۲۰۱۷ میلادی نشان می‌دهد.</p>',
             unsafe_allow_html=True)
    st.line_chart(precipitation, x="year", y="precipitation (mm)", x_label="سال", y_label="کل بارش سالانه (میلیمتر)")
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.write('<p class="persian-text">میانگین تعداد کل روزهای یخبندان سالانه بین سال‌های ۲۰۰۶ تا ۲۰۱۷ میلادی، ۱۳۷ روز بوده است.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">میانگین درصد رطوبت نسبی سالانه در بازه فوق الذکر، ۵۲ درصد بوده است.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">میانگین سرعت باد روزانه بین سال‌های ۲۰۰۶ تا ۲۰۱۷ میلادی، ۳.۸ گره دریایی بوده است.</p>',
             unsafe_allow_html=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.markdown('<p class="persian-text">سایه‌ها در صبحگاهان دی ماه در قطعاتی با امتداد شمال شرقی-جنوب غربی (رون تقریبی قبله)</p>',
                unsafe_allow_html=True)
    st.image("Jauary.jpg")
    st.markdown('<p class="persian-text">سایه‌ها در عصرگاهان دی ماه در قطعاتی با امتداد شرقی-غربی (رون تقریبی کرمان)</p>',
                unsafe_allow_html=True)
    st.image("January_afternoon.jpg")
    
    # st.markdown("""**The distance from the :red[Soltaniyeh fault] (approximately 140 km long) to the town is almost 8 km. 
    #             This fault is located in the south and southeast of Soltaniyeh.**""")
    
demographic_expander = st.sidebar.expander("جمعیت و اجتماع")
general_info = demographic_expander.selectbox("اطلاعات عمومی جمعیتی", options=["جمعیت", "نرخ رشد جمعیت",
                                                                              "هرم سنی-جنسی", "تراکم جمعیتی"], 
                                              index=None,
                               placeholder="از این فهرست انتخاب کنید")
if general_info == "جمعیت":
    st.markdown('<p class="persian-titr2">جمعیت</p>', unsafe_allow_html=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    colors=["#E64C00", "#2769BA", "#7D1919", "#7AF5CA"]
    st.table(fpopulation)
    columns = st.columns(4)
    for idx,row in fpopulation.iterrows():
        columns[idx].line_chart(row, x_label=row["عنوان"], color=colors[idx])
if general_info == "نرخ رشد جمعیت":
    st.markdown('<p class="persian-titr2">نرخ رشد جمعیت</p>', unsafe_allow_html=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    colors=["#E64C00", "#2769BA", "#7D1919", "#7AF5CA"]
    st.table(fpopulation_rate)
    columns = st.columns(4)
    for idx,row in fpopulation_rate.iterrows():
        columns[idx].line_chart(row[1:4], x_label=row["عنوان"], color=colors[idx])    
if general_info == "هرم سنی-جنسی":
    st.markdown('<p class="persian-titr2">هرم سنی-جنسی</p>', unsafe_allow_html=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.markdown('<p class="persian-titr1">هرم سنی-جنسی در سال 1385</p>', unsafe_allow_html=True)
    age_sex_85_table = st.table(fage_sex85)
    age_sex_85_chart = st.bar_chart(fage_sex85, x="گروه های سنی", y=["مردان (جمعیت)", "زنان (جمعیت)"], 
                                    x_label="جمعیت", color=["#7D1919", "#2769BA"], horizontal=True, stack="center")
    st.markdown('<p class="persian-titr1">هرم سنی-جنسی در سال 1390</p>', unsafe_allow_html=True)
    age_sex_90_table = st.table(fage_sex90)
    age_sex_90_chart = st.bar_chart(fage_sex90, x="گروه های سنی", y=["مردان (جمعیت)", "زنان (جمعیت)"], 
                                    x_label="جمعیت", color=["#7D1919", "#2769BA"], horizontal=True, stack="center")  
    st.markdown('<p class="persian-titr1">هرم سنی-جنسی در سال 1395</p>', unsafe_allow_html=True)
    age_sex_95_table = st.table(fage_sex95)
    age_sex_95_chart = st.bar_chart(fage_sex95, x="گروه های سنی", y=["مردان (جمعیت)", "زنان (جمعیت)"], 
                                    x_label="جمعیت", color=["#7D1919", "#2769BA"], horizontal=True, stack="center") 
if general_info == "تراکم جمعیتی":
    st.markdown('<p class="persian-titr2">تراکم جمعیتی</p>', unsafe_allow_html=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.markdown('<p class="persian-titr1">تراکم ناخالص جمعیتی در سال 1395</p>', unsafe_allow_html=True)
    st.image("Tarakom_Jamiati_Nakhales.jpg")
    st.markdown('<p class="persian-titr1">تراکم ناخالص جمعیتی در سال 1385</p>', unsafe_allow_html=True)
    st.image("Tarakom_Jamiati_Nakhales85.jpg")
    st.markdown('<p class="persian-titr1">تراکم ناخالص جمعیتی در سطح محلات</p>', unsafe_allow_html=True)
    st.image("Tarakom_Jamiati_Mahallat.jpg") 

social_info = demographic_expander.selectbox("اطلاعات جامعه شناسی", options=["شاخص اعتماد", "مراودات اجتماعی",
                                                                              "مشارکت اجتماعی", "سرمایه اجتماعی",
                                                                              "شاخص تاب آوری"],
                                             placeholder="از این فهرست انتخاب کنید", index=None)

if social_info == "شاخص اعتماد":
    st.markdown('<p class="persian-titr2">شاخص اعتماد</p>', unsafe_allow_html=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-text">این شاخص از دو شاخص اعتماد بین فردی و اعتماد نهادی تشکیل شده است. اعتماد بین فردی به اعتماد به دوستان، آشنایان و خانواده اشاره دارد و اعتماد نهادی به اعتماد به مسئولان و نهادهای دولتی (اعم از دولتی و عمومی) اشاره دارد.</p>',
             unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.markdown('<p class="persian-titr1">اعتماد بین فردی</p>', unsafe_allow_html=True)
    col1.bar_chart(finterpersonal_trust, x="مقدار", y="اعتماد بین فردی", x_label="میزان اعتماد بین فردی",
                 y_label="درصد از کل مصاحبه شوندگان", color=["#2769BA"])
    col2.markdown('<p class="persian-titr1">اعتماد نهادی</p>', unsafe_allow_html=True)
    col2.bar_chart(finstutitional_trust, x="مقدار", y="اعتماد نهادی", x_label="میزان اعتماد نهادی",
                 y_label="درصد از کل مصاحبه شوندگان", color=["#E64C00"])
    st.write('<p class="persian-text">شاخص اعتماد ترکیبی از سطح اعتماد بین فردی و اعتماد نهادی است.</p>',
             unsafe_allow_html=True)
    st.bar_chart(fall_trust, x="مقدار", y="اعتماد", x_label="میزان اعتماد",
                 y_label="درصد از کل مصاحبه شوندگان", color=["#7AF5CA"])

if social_info == "مراودات اجتماعی":
    st.markdown('<p class="persian-titr2">مراودات اجتماعی</p>', unsafe_allow_html=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-text">این شاخص از مجموع گویه‌های ارتباط با همسایگان و خانواده تشکیل شده است. طبق نمودار زیر، این شاخص در شهر سلطانیه بالاتر از حد متوسط ​​ارزیابی می‌شود.</p>',
             unsafe_allow_html=True)
    st.bar_chart(fcommunication, x="مقدار", y="مراودات اجتماعی", x_label="میزان ارتباط اجتماعی",
                 y_label="درصد از مصاحبه شوندگان", color=["#2769BA"])

if social_info ==  "مشارکت اجتماعی":

    st.markdown('<p class="persian-titr2">مشارکت اجتماعی</p>', unsafe_allow_html=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-text">این شاخص از مجموع شاخص‌های مشارکت رسمی و غیررسمی تشکیل شده است؛ مشارکت رسمی به مشارکت در تصمیم‌گیری‌های شهری و مشارکت در امور کلان‌شهری اشاره دارد. مشارکت غیررسمی نیز به مشارکت در امور مذهبی، تصمیم‌گیری‌های محلی و غیره اشاره دارد.</p>',
             unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.markdown('<p class="persian-titr1">میزان مشارکت غیررسمی</p>', unsafe_allow_html=True)
    col1.bar_chart(finformal_participation, x="مقدار", y="مشارکت غیررسمی", x_label="میزان مشارکت غیررسمی",
                 y_label="درصد از مصاحبه شوندگان", color=["#E64C00"])
    col2.markdown('<p class="persian-titr1">میزان مشارکت رسمی</p>', unsafe_allow_html=True)
    col2.bar_chart(fformal_participation, x="مقدار", y="مشارکت رسمی", x_label="میزان مشارکت رسمی",
                 y_label="درصد از مصاحبه شوندگان", color=["#2769BA"])
    st.markdown('<p class="persian-text">نتیجه‌گیری: مشارکت در بین شهروندان شهر سلطانیه کم یا خیلی کم ارزیابی شده است.</p>',
                unsafe_allow_html=True)
    st.bar_chart(fall_participation, x="مقدار", y="مشارکت", x_label="میزان مشارکت",
                 y_label="درصد از مصاحبه شوندگان", color=["#7AF5CA"])
    
if social_info == "سرمایه اجتماعی":

    st.markdown('<p class="persian-titr2">سرمایه اجتماعی</p>', unsafe_allow_html=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-text">این شاخص از مجموع شاخص‌های مشارکت، اعتماد و ارتباط و هویت و تعلق شهری تشکیل شده است. بر اساس این شاخص، میزان سرمایه اجتماعی متوسط ​​ارزیابی می‌شود.</p>',
             unsafe_allow_html=True)
    st.bar_chart(fsocial_capital, x="مقدار", y="سرمایه اجتماعی", x_label="میزان سرمایه اجتماعی",
                 y_label="درصد", color=["#7AF5CA"])
    
if social_info == "شاخص تاب آوری":

    st.markdown('<p class="persian-titr2">شاخص تاب آوری</p>', unsafe_allow_html=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-text">ویژگی تاب‌آوری جامعه این امکان را فراهم می‌کند که جوامع از نظر توانایی سازگاری مثبت با سختی‌ها و مشکلات با یکدیگر مقایسه شوند. شاخص تاب‌آوری از شاخص‌هایی مانند اعتماد و ارتباط، مشارکت که در این تحقیق با عنوان سرمایه اجتماعی نیز شناخته می‌شود، تشکیل شده است. یکی دیگر از شاخص‌های تاب‌آوری اجتماعی، شاخص هویت و تعلق شهری است. همانطور که در نمودار زیر مشاهده می‌شود، وضعیت این شاخص متوسط ​​ارزیابی می‌شود.</p>',
             unsafe_allow_html=True)
    st.bar_chart(fresilience, x="مقدار", y="تاب آوری", x_label="میزان تاب آوری",
                 y_label="درصد", color=["#7AF5CA"])        
    
people_issues = demographic_expander.toggle("مشکلات، مسائل و راه حلها از نظر مردم")  
if people_issues:

    st.markdown('<p class="persian-titr2">مشکلات، خواسته ها و انتظارات مردم</p>', unsafe_allow_html=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-text">یکی از مهمترین سوالات در نظرسنجی اجتماعی، یافتن نظر مردم در مورد شهرشان و مسائلی است که باید با آنها دست و پنجه نرم کنند. به عبارت دیگر، مشکلات زندگی در سلطانیه چیست؟ ساکنان سلطانیه می گویند:</p>',
             unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col2.markdown('<p class="persian-titr1">رفع کمبودها در زمینه خدمات بهداشتی و درمانی و عمران شهری</p>', unsafe_allow_html=True)
    col2.markdown('<p class="persian-titr1">حل و فصل مسئله حفاظت از آثار و کم کردن تاثیر سوء آنها بر نظام و کارکرد شهری</p>', unsafe_allow_html=True)
    col2.markdown('<p class="persian-titr1">رفع مشکلات نظام اداری (با تکیه بر ارتقاء نظام مدیریتی از طریق جذب نیروهای متخصص و دلسوز مخصوصا محلی و بومی)</p>', unsafe_allow_html=True)
    col2.markdown('<p class="persian-titr1">تدوین مدل مشارکتی برای ایجاد ارتباط مستمر و سازنده میان مردم و مسئولان و امکان رصد و نظارت بر کار مسئولان</p>', unsafe_allow_html=True)
    col2.markdown('<p class="persian-titr1">اعتمادسازی و احیاء اعتماد مردم به مسئولین به عنوان پیش زمینه پیشرفت و توسعه</p>', unsafe_allow_html=True)
    col2.markdown('<p class="persian-titr1">افزایش زیرساخت های گردشگری برای افزایش حضورپذیری توریست و بهره مند شدن شهر از رونق گردشگری (اعم از فضاهای اقامتی، فضاهای تجاری و عرضه محصولات، مسیرهای گردشگری، حمل و نقل گردشگر، ...)</p>', unsafe_allow_html=True)
    col2.markdown('<p class="persian-titr1">ارتباط مناسب و دوباره مجموعه ارگ با شهر (آشتی این مجموعه با پیرامون، حذف حصار و به هم پیوستگی ارگ با شهر)</p>', unsafe_allow_html=True)
    col2.markdown('<p class="persian-titr1">اجرای پروژه های طراحی و معماری برای اتصال محدوده های تاریخی با تعریف عملکردهای مناسب به سبک شهرهای توریستی برتر کشور</p>', unsafe_allow_html=True)
    col2.markdown('<p class="persian-titr1">تهیه برنامه های تبلیغاتی، برگزاری سمینارها و همایش های مرتبط، استفاده از ظرفیت مدارس و دانشگاه ها برای معرفی و تبلیغ سلطانیه</p>', unsafe_allow_html=True)

    col1.image("IMG_6079.jpg")
    col1.image("IMG_6338.jpg")
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.bar_chart(fpeople_issues_file, x="عنوان", y="تعداد پاسخ ها", color=["#7AF5CA"])

economic_expander = st.sidebar.expander("شرایط اقتصادی")
general_economic = economic_expander.toggle("اطلاعات کلی ساختار اقتصادی")
if general_economic:
    st.write('<p class="persian-titr2">اطلاعات کلی درباره ساختار اقتصادی</p>',
             unsafe_allow_html=True)  
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-titr1">اطلاعات عمومی</p>',
             unsafe_allow_html=True)  

    fdf_economic = pd.read_excel(fgeneral_economic_table)
    st.dataframe(fdf_economic, hide_index=True)
    feconomic_sectors = pd.read_excel(feconomic_sectors_table)
    st.bar_chart(feconomic_sectors, x="بخش", y="سهم از اشتغال کل (درصد)", color="#00FF00")
    # st.divider()
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-text">مهم‌ترین محصولات زراعی سلطانیه سیب‌زمینی، گندم، جو، لوبیا، یونجه، کلزا و ذرت علوفه‌ای هستند.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">میزان برداشت سیب‌زمینی در هر سال تقریباً ۱۱۰ تن در هکتار است. این رقم در استان زنجان تقریباً ۴۲ تن در هکتار است.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">مهم‌ترین محصول باغی، سیب است. سیب‌های برداشت شده در گوزل دره طعم و بوی خاصی دارند.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">پس از سیب، گلابی، هلو و گردو به ترتیب در رتبه‌های دوم تا چهارم قرار دارند.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">سلطانیه مرکز خدمات پشتیبانی کشاورزی و تأمین و تعمیر تجهیزات کشاورزی برای روستاهای اطراف است.</p>',
             unsafe_allow_html=True) 
    st.write('<p class="persian-text">در زمینه گندم، صنایع فرآوری مربوط به تولید آرد سوخاری، شیرینی‌جات و سبوس صنعتی در این شهر وجود دارد.</p>',
             unsafe_allow_html=True) 
economic_opportunities = economic_expander.toggle("فرصتهای اقتصادی")
if economic_opportunities:
    st.write('<p class="persian-titr2">مهمترین فرصت های اقتصادی - برگرفته از سایر مطالعات</p>',
             unsafe_allow_html=True)  
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.write('<p class="persian-text">قرارگیری شهرستان در منطقه برنامه‌ریزی محور شهرستان‌های زنجان- ابهر- خرمدره و سلطانیه</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">قرارگیری در کریدور اصلی و مجهز بازرگان- تهران با عملکرد ملی و بین‌المللی</p>',
             unsafe_allow_html=True) 
    st.write('<p class="persian-text">قرارگیری در پهنه اصلی توسعه کشاورزی آبی، دیم و طیور</p>',
             unsafe_allow_html=True)  
    st.write('<p class="persian-text">محور گردشگری سطح یک عبوری شرقی- غربی در پیوند با تهران و تبریز</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">منطقه پیشاهنگی توسعه گردشگری استان با توسعه زیرساخت‌ها و خدمات اقامت و پذیرایی</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">اولویت استقرار خدمات لجستیک، حمل‌ونقل و پشتیبان گردشگری</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">محور گردشگری ممتاز سطح یک در پیوند با استان گیلان و همدان (گردشگری تاریخی و بومگردی در سلطانیه)</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">محور سطح دو صنعتی در پیوند با قیدار و زرین رود با استقرار صنایع پشتیبان کشاورزی</p>',
             unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.image("Industry.png")
    col2.image("Mining.png")
    col3.image("Service.png")
    
tourists = economic_expander.toggle("صنعت گردشگری")
if tourists:
    st.write('<p class="persian-titr2">گردشگران و صنعت گردشگری در سلطانیه</p>',
             unsafe_allow_html=True)  
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-text">این جدول اطلاعات کلی گردشگران سلطانیه را نشان می‌دهد.</p>',
             unsafe_allow_html=True)
    fdf_tourists = pd.read_excel(ftourists_table)
    st.table(fdf_tourists)
    st.divider()
    st.write('<p class="persian-text">سلطانیه از کمبود انواع اقامتگاه‌ها برای گردشگران رنج می‌برد. این شهر تنها دو مکان دارد که برخی از زیرساخت‌های گردشگری را برای بازدیدکنندگان فراهم می‌کنند.</p>',
             unsafe_allow_html=True)
    fdf_hotels = pd.read_excel(fhotels)
    st.table(fdf_hotels)
    
    st.image("IMG_7960.jpg", width=1200)
    st.caption("باغ ایلخانی؛ عکس از آرش فضلی شمس آبادی")
    
    
    
    

physical_expander = st.sidebar.expander("ساختار کالبدی")
landuse = physical_expander.toggle("کاربری اراضی")
if landuse:
    st.write('<p class="persian-titr2">کاربری اراضی در وضع موجود</p>',
             unsafe_allow_html=True) 
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.image("Current Landuse.jpg")
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    flanduse_df = pd.read_excel(flanduse_raw_table)
    flanduse_df["سهم مساحت از کل (درصد)"] = flanduse_df["سهم مساحت از کل (درصد)"]*100
    st.dataframe(flanduse_df, hide_index=True)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.bar_chart(flanduse_df, x="عنوان کاربری", y="سهم مساحت از کل (درصد)",
                 x_label="کاربری ها", y_label="سهم مساحتی از کل")
buildings = physical_expander.toggle("وضعیت ابنیه")
if buildings:
    st.write('<p class="persian-titr2">وضعیت کالبدی - ابنیه</p>',
             unsafe_allow_html=True) 
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    fbuildings_table = pd.read_excel(fparcels)
    fbase_floors = fbuildings_table.groupby(by=["طبقات"])["count"].count()  
    fbase_structure = fbuildings_table.groupby(by=["سازه"])["count"].count()
    fbase_oldness = fbuildings_table.groupby(by=["قدمت"])["count"].count() 
    fbase_quality = fbuildings_table.groupby(by=["کیفیت"])["count"].count() 
    col1, col2 = st.columns(2)
    col1.write('<p class="persian-titr1">تعداد طبقات</p>', unsafe_allow_html=True) 
    col1.bar_chart(fbase_floors, x_label="تعداد طبقات", y_label="تعداد بناها",
                   horizontal=False)
    col1.image("Tabaqat_Abnieh.jpg")
    col1.divider()
    col2.write('<p class="persian-titr1">سازه ابنیه</p>', unsafe_allow_html=True) 
    col2.bar_chart(fbase_structure, x_label="سازه ابنیه", y_label="تعداد بناها", color=["#E64C00"],
                   horizontal=False)
    col2.image("Saze_Abnie.jpg")
    col2.divider()
    col1.write('<p class="persian-titr1">قدمت ابنیه</p>', unsafe_allow_html=True) 
    col1.bar_chart(fbase_oldness, x_label="قدمت ابنیه", y_label="تعداد بناها",
                   horizontal=False)
    col1.image("Omr_Bana.jpg")
    col2.write('<p class="persian-titr1">کیفیت ابنیه</p>', unsafe_allow_html=True) 
    col2.bar_chart(fbase_quality, x_label="کیفیت ابنیه", y_label="تعداد بناها", color=["#E64C00"],
                   horizontal=False)
    col2.image("Quality.jpg")

urban_fabric = physical_expander.toggle("بافت شهری")
if urban_fabric:
    st.write('<p class="persian-titr2">بافت شهری</p>',
             unsafe_allow_html=True) 
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    
    st.write('<p class="persian-titr1">درباره قطعات با کاربری مسکونی</p>', unsafe_allow_html=True) 
    col1, col2 = st.columns(2)
    col2.write('<p class="persian-text">متوسط مساحت قطعات با کاربری مسکونی در شهر سلطانیه 221.1 مترمربع است. </p>',
             unsafe_allow_html=True)   
    col2.write('<p class="persian-text">در توسعه های جدید شهر (شهرک طالبیه) متوسط دانه بندی 252.5 مترمربع و در بخش قدیمی شهر این مقدار 217.1 مترمربع است. </p>',
             unsafe_allow_html=True) 
    col2.write('<p class="persian-text">در حوزه کاربری مسکونی و خانه ها، متوسط سطح اشغال ابنیه در کل شهر سلطانیه قریب 60 درصد (دقیقا 59.61 درصد) است.</p>',
             unsafe_allow_html=True) 
    col2.write('<p class="persian-text">متوسط تراکم ساختمانی در کاربری مسکونی در شهر سلطانیه حدود 78 درصد است. </p>',
             unsafe_allow_html=True) 
    col2.write('<p class="persian-text">متوسط زیربنا در کاربری مسکونی در شهر سلطانیه 145.5 مترمربع است. </p>',
             unsafe_allow_html=True)
    col2.write('<p class="persian-text">بر اساس اطلاعات مرکز آمار متوسط واحد مسکونی در شهر سلطانیه 119 مترمربع است لذا متوسط سهم مشاعات (شامل راه پله، ورودی و ...) در خانه ها حدود 18.2 درصد محاسبه می شود. </p>',
             unsafe_allow_html=True)
    col1.image("Urban Fabric1.jpg")
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.write('<p class="persian-titr1">درباره معماری بناهای مسکونی</p>', unsafe_allow_html=True) 
    
    st.write('<p class="persian-text">توده گذاری و جهت گیری ابنیه دو عامل مهم در تعیین نوع کلی معماری در قطعات هستند. برای استفاده حداکثر از نور خورشید در زمستان و پرهیز از گرما در تابستان (خاصه در فلات ایران) این دو عامل نقش تعیین کننده ای دارند.</p>',
             unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    ftoodeha = pd.read_excel(fbuilding_toode)
    col2.bar_chart(ftoodeha, x="نوع", y="سهم تعداد از کل", horizontal=True,
                   height=350, color=["#E64C00"], x_label="سهم از کل")
    col1.image("fToudeh.jpg", width = 1200) 

    col1,col2,col3 = st.columns(3)
    col2.image("fNS.jpg", width=300)
    col2.image("fQibla.jpg", width=300)
    col3.image("fKerman.jpg", width=300)
    col3.image("fIsfehan.jpg", width=300)
    fdirections = pd.read_excel(fbuilding_direction)
    col1.bar_chart(fdirections, x="جهت گیری بنا", y="سهم تعداد از کل",
                   x_label="نوع جهت گیری بنا", y_label="سهم از کل",
                   height=500)
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.write('<p class="persian-text">جدول زیر اطلاعات مربوط به نسیت ابعاد قطعات را در انواع جهت گیری های شناسایی شده در اختیار قرار می دهد.</p>',
             unsafe_allow_html=True)
    ftoode_dimension = pd.read_excel(fbuilding_toode_dimension)
    fdf_styled = ftoode_dimension.style.map(lambda x: f"background-color:{'#E69800' if x>2 else '#96FF96'}",
                                          subset="نسبت ابعاد")
    st.dataframe(fdf_styled, hide_index=True) 
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.write('<p class="persian-titr1">درجه ارگانیک بودن معابر</p>', unsafe_allow_html=True) 
    st.write('<p class="persian-text">شاخص ارگانیک بودن معابر نشان می دهد که تا چه اندازه یک مسیر حرکتی به شکل تاریخی خود نزدیک است. در شهرسازی تاریخی ایران زمین، شکل گیری معابر با پیچ و خم های فراوان به دلایل مختلفی از جمله بحث های اقلیمی، دفاعی، مالکیت اراضی، صبغه اجتماعی و ... بسیار معمول بوده است. با این حال این شاخص در اکثر معابر سلطانیه به 1 نزدیک است. از زمان خریداری و پاکسازی اراضی اطراف گنبد سلطانیه و گسترش شهر به جوانب، نوع خیابان کشی ها نیز از حالت قدیم خود خارج شده اند.</p>',
             unsafe_allow_html=True)    
    st.image("Road_Sinuosity.jpg")
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.write('<p class="persian-titr1">شاخص های تحلیل چیدمان فضا</p>', unsafe_allow_html=True)     
    st.markdown('<p class="persian-text">این نقشه‌ها جنبه‌های مختلف تحلیل چیدمان فضا در سلطانیه را نشان می‌دهند. برای کاربردی‌تر بودن، همه آنها وضعیت فعلی را با وضعیت قبل از آزادسازی اراضی اطراف گنبد سلطانیه، مقایسه می‌کنند.</p>',
                unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.image("Control1343.jpg", caption=":blue[**کنترل**]")
    col1.image("Hampeyvandi1343 (2).jpg", caption=":blue[**همپیوندی**]")
    col2.image("Hampeyvandi1343.jpg", caption=":blue[**همپیوندی (HH)**]")
    col2.image("Harkat_TabiE1343.jpg", caption=":blue[**انتخاب**]")
    col3.image("Omgh1343.jpg", caption=":blue[**عمق نهایی**]")
    col3.image("Vozooh1343.jpg", caption=":blue[**ارتباط**]")
    
      
roads = physical_expander.toggle("شبکه معابر")
if roads:
    st.write('<p class="persian-titr2">شبکه معابر شهر</p>',
             unsafe_allow_html=True) 
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-titr1">حجم تردد وسایل نقلیه بین سلطانیه و سایر شهرها</p>', unsafe_allow_html=True) 
    st.write('<p class="persian-text">جدول زیر اطلاعات مربوط به تعداد وسایل نقلیه در حال تردد در امتداد جاده‌های متصل به سلطانیه را ارائه می‌دهد. این اطلاعات مربوط به آبان ماه سال 1398، قبل از همه‌گیری کووید-۱۹ و اعمال شرایط قرنطینه‌ است.</p>',
             unsafe_allow_html=True)
    froads = pd.read_excel(froads_traffic)
    froads["سهم (درصد)"] = froads["سهم (درصد)"] * 100
    st.dataframe(froads, hide_index=True)
    froads_bar = pd.read_excel(froads_traffic_barchart)
    st.bar_chart(froads_bar, x="جهت", y="متوسط تعداد وسیله نقلیه در ساعات اوج", horizontal=True,
                 y_label="جهت", color= "#4B17B4")
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.write('<p class="persian-titr1">سلسله مراتب راه های شهری</p>', unsafe_allow_html=True) 
    st.markdown('<p class="persian-text">این نقشه سلسله مراتب راه ها در شهر سلطانیه را در وضع موجود نشان می دهد. همان طور که پیداست عمده راه ها از جنس معابر دسترسی محلی هستند.</p>',
                unsafe_allow_html=True) 
    st.image("Road_Hierarchy.jpg")   
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.write('<p class="persian-titr1">عرض و شیب معابر</p>', unsafe_allow_html=True) 
    st.write('<p class="persian-text">عرض شبکه معابر</p>', unsafe_allow_html=True)
    froadswidth = pd.read_excel(froads_width)
    st.dataframe(froadswidth, hide_index=True)
    st.image("DarajeBandi_Arz_Mabar.jpg")
    st.write('<p class="persian-text">شیب شبکه معابر</p>', unsafe_allow_html=True)
    froadslop = pd.read_excel(froads_slop)
    st.dataframe(froadslop, hide_index=True)
    st.image("Shib_Mabar.jpg")

conclusion_expander = st.sidebar.expander("ارزش ها، ظرفیت ها، مسائل")
values = conclusion_expander.toggle("ارزش ها")
if values:
    st.write('<p class="persian-titr2">ارزش ها</p>',
             unsafe_allow_html=True) 
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-text">سلطانیه به عنوان یک شهر تاریخی بی‌نظیر که طی یک دهه ساخته شده، تقریباً ۷۰ سال پابرجا ماند. آثار تاریخی باقی مانده در کنار بناهای دیدنی، به ویژه گنبد سلطانیه، ارزش این شهر را دو چندان می‌کند.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">چمن سلطانیه پوشش گیاهی منحصر به فردی است که شایسته است به عنوان میراث طبیعی مورد حفاظت قرار گیرند.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">چشمه شاه بلاغی یکی از مقاصد گردشگری استان زنجان است که به طبیعت و تاریخ این منطقه ارزش دوچندانی می‌بخشد.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text"> داش کسن (معبد اژدها) در ویر یکی دیگر از مکان‌های تاریخی نزدیک سلطانیه است که به همراه سایر مکان‌ها می‌تواند شبکه‌ای از مقاصد گردشگری مختلف را تشکیل دهد.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">چشم‌انداز بکر این منطقه با بناهای شگرف و خارق العاده، مانند گنبد سلطانیه و آرامگاه چلبی اوقلو، آن را از نظر طراحی شهری کم‌نظیر می‌کند.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">حس شاداب زندگی در میان ساکنان شهر به آنها کمک می‌کند تا با مشکلات فراوانی که هر روز با آنها روبرو هستند، کنار بیایند.</p>',
             unsafe_allow_html=True)
capasities = conclusion_expander.toggle("ظرفیت ها")
if capasities:
    st.write('<p class="persian-titr2">ظرفیت ها</p>',
             unsafe_allow_html=True) 
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-text">سلطانیه فرصت مناسبی برای بهبود اقتصاد خود از طریق کشاورزی دارد. وضعیت خاک، منابع آب و نیروی کار سه ضلع یک مثلث هستند که این بخش اقتصادی را شکل می‌دهند.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">تنوع امکان سفر به و از شهر، از جمله راه آهن، بزرگراه و سایر جاده‌ها، می‌تواند صنعت گردشگری، کشاورزی، فعالیت‌های معدنی و مناطق صنعتی را تقویت کند.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">سلطانیه می‌تواند دروازه شمالی مسیر گردشگری زنجان-همدان باشد و انواع گردشگری مانند گردشگری تاریخی، کشاورزی، طبیعی، ورزشی و موضوعی را ارائه دهد.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">محور صنعتی در بخش شمالی این منطقه یکی از مهمترین محدوده ها و محورهای صنعتی در ایران است، زیرا شامل برخی از شرکت‌ها و تولیدکنندگان برجسته مانند شرکت دخانیات جی تی، شرکت مینو، و مانند آن است.</p>',
             unsafe_allow_html=True)
issues = conclusion_expander.toggle("مسائل")
if issues:
    st.write('<p class="persian-titr2">مسائل</p>',
             unsafe_allow_html=True) 
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.write('<p class="persian-text">چمن سلطانیه به دلیل مصرف بیش از حد منابع آب در حالت بحرانی فرو رفته است.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">به دلیل مصرف بیش از حد آب در زمین‌های کشاورزی، سطح منابع آب زیرزمینی سالانه به طور متوسط 0.94 متر کاهش می یابد.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">صنایع اطراف سلطانیه آلودگی هوای زیادی ایجاد می‌کنند و منابع آب را آلوده می‌کنند. این صنایع علاوه بر آلودگی به سبب تامین منابع اولیه به محیط زیست آسیب فراوانی می رسانند.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">با وجود اینکه سلطانیه شهر اصلی شهرستان است، برخی از بخش‌های آن با مشکلات کالبدی، اجتماعی و اقتصادی دست و پنجه نرم می‌کند.</p>',
             unsafe_allow_html=True)
    st.write('<p class="persian-text">برخی از عرصه های تاریخی و حرایم آنها توسط ساخت و سازهای جدید مورد هجوم قرار گرفته‌اند. این پدیده مانع از اجرای پروژه‌های حفاظتی در این محدوده ها می‌شود.</p>',
             unsafe_allow_html=True)

documents_expander = st.sidebar.expander("گزارش ها و مدارک")
documents_toggle = documents_expander.toggle("مدارک")
reports_toggle = documents_expander.toggle("گزارش ها")
if documents_toggle:
    st.write('<p class="persian-titr2">پرونده ثبت جهانی سلطانیه</p>',
             unsafe_allow_html=True) 
    ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

    st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\Parvande_Sabt_Jahani.pdf", height = 800)

if reports_toggle:
    background = st.sidebar.checkbox("مطالعات زمینه ای")
  
    if background:
        st.write('<p class="persian-titr2">مطالعات زمینه ای</p>',
                unsafe_allow_html=True) 
        ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"

        st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\01_ZamineHa.pdf", height = 800) 
    current_report = st.sidebar.checkbox("مطالعات تفصیلی شهر")
    if current_report:
        st.write('<p class="persian-titr2">مطالعات تفصیلی شهر</p>',
                unsafe_allow_html=True)
        ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
 
        st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\02_MotaleAt_Tafsili_Shahr.pdf", height=800)
    analysis = st.sidebar.checkbox("تجزیه و تحلیل")
    if analysis:
        st.write('<p class="persian-titr2">تجزیه و تحلیل و استنتاج از مطالعات</p>',
                unsafe_allow_html=True)
        ":orange[-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
 
        st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\03_Tahlil.pdf", height=800)

