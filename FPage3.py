import streamlit as st



st.image("Rahbordyimage.jpg", width=300)

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

vision_toggle = st.sidebar.toggle("بیانیه چشم انداز")
if vision_toggle:
    st.markdown('<p class="persian-text">بیانیه چشم انداز</p>', unsafe_allow_html=True)
    ":orange[----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.write('<p class="persian-text">شهر-منطقه تاریخی-فرهنگی معروف جهانیان، به عنوان یکی از حلقه­های نمادین واسط میان دو کلان-محور تمدنی البرز و زاگرس در میان مرغزار زیبا و شاداب سلطانیه – به عنوان اعضای یک پیکر – محلی است خودبسنده برای سکونت اقشار مختلف که از طریق فعالیت­های متنوع گردشگری، کشاورزی و فعالیت­های صنعتی دوستدار محیط زیست روزگار می­گذرانند. اهالی سلطانیه با پیشینه تاریخی کم­بدیل خود به مدد آموزش مستمر و موثر مردمانی دوستدار شهر و ثروت تاریخی و محیط زیست خود بوده و با آگاهی از اهمیت این عناصر به دنبال معرفی آن به جهانیان هستند. محیط سرزنده و امن این شهر که از حضور دوشادوش و مشارکت تمامی گروه­های سنی و جنسی شاداب شده، پذیرای انواع گردشگران و محققان و دانشجویان علوم و هنر و تاریخ این سرزمین از هر گوشه و کنار کشور و دنیا است و برای ماندگاری و آسایش آن­ها در شهر امکانات درخوری مهیا کرده است. کهن­شهر پاک سلطانیه – که سوادش از هر سو تا دوردست­ها پیداست – نشانی از فرسودگی ندارد و کالبد او با احترام به تاریخ معماری و شهرسازی خود متناسب با زندگی معاصر است.</p>', unsafe_allow_html=True)
    st.image("IMG_6072.JPG")
goals_toggle = st.sidebar.toggle("اهداف کلان")
if goals_toggle:
    st.markdown('<p class="persian-text">اهداف کلان و اصلی</p>', unsafe_allow_html=True)
    ":orange[----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.markdown('<p class="persian-text">معرفی درخور شهر سلطانیه به ایرانیان و جهانیان</p>', unsafe_allow_html=True)
    st.markdown('<p class="persian-text">ارتقاء وضعیت اقتصادی شهر و ساکنان</p>', unsafe_allow_html=True)
    st.markdown('<p class="persian-text">ارتقاء شرایط زیست و ماندگاری ساکنان در شهر</p>', unsafe_allow_html=True)
    st.markdown('<p class="persian-text">رجوع به الگوی شهرسازی اولیه به مثابه ایده ساختاری مرجع</p>', unsafe_allow_html=True)
    st.markdown('<p class="persian-text">حفاظت پایدار از عرصه طبیعی و محیط زیست سلطانیه</p>', unsafe_allow_html=True)
    st.markdown('<p class="persian-text"بهبود شرایط گردشگری و گردشگرپذیری</p>', unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.image("IMG_6224.JPG")
    col2.image("IMG_6231.JPG")
    col3.image("IMG_7306.JPG")
    col4.image("IMG_7961.JPG")
    col5.image("IMG_6081.JPG")
    col6.image("IMG_6109.JPG")
detailed_goals = st.sidebar.toggle("اهداف خرد")
if detailed_goals:
    st.markdown('<p class="persian-text">اهداف خرد</p>', unsafe_allow_html=True)
    ":orange[----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    col1 , col2 = st.columns(2)
    col2.markdown('<p class="persian-text">ارتقاء سلطانیه به شهر تاریخی سلطانیه و مرکز آموزش و پژوهش هنرها و علوم ایلخانی</p>',
                  unsafe_allow_html=True)
    col2.markdown('<p class="persian-text">ارتقاء وضعیت کشاورزی بر مبنای اصول توسعه پایدار</p>', unsafe_allow_html=True)
    col2.markdown('<p class="persian-text">مهیاسازی شرایط توسعه فعالیت­های زنجیره گردشگری (در انواع مختلف تاریخی، طبیعی، کشاورزی، ورزشی، ...) در شهر و پیرامون در رقابت با مرکز استان</p>',
                  unsafe_allow_html=True)
    col2.markdown('<p class="persian-text">بهبود شرایط اشتغال، فعالیت و سرمایه­ گذاری در شهر و جلوگیری از فرار سرمایه انسانی و ریالی</p>',
                  unsafe_allow_html=True)
    col2.markdown('<p class="persian-text">بهره­ مندی مدیریت شهر از منابع پایدار درآمدی</p>', unsafe_allow_html=True)
    col2.markdown('<p class="persian-text">حفاظت پایدار از محدوده­ های تاریخی با نگاه به توسعه و معاصرسازی شهر</p>', 
                  unsafe_allow_html=True)
    col2.markdown('<p class="persian-text">همپیوندی و انسجام محدوده­ های تاریخی با شهر؛ آشتی شهر با تاریخ خود</p>',
                  unsafe_allow_html=True)
    col2.markdown('<p class="persian-text">تقویت روحیه شهروندی و شهروند سلطانیه بودن در مردم</p>', unsafe_allow_html=True)
    col2.markdown('<p class="persian-text">ارتقاء وضعیت آگاهی و دانش ساکنان نسبت به مواریث طبیعی، تاریخی و هویتی خود</p>',
                  unsafe_allow_html=True)
    col2.markdown('<p class="persian-text">ارتقاء شرایط خدمات­ رسانی شهر به ساکنان در همه زمینه­ ها و درخور مرکز شهرستان</p>',
                  unsafe_allow_html=True)
    col1.image("IMG_6310.JPG")
strategies = st.sidebar.toggle("راهبردها")
if strategies:
    st.markdown('<p class="persian-text">راهبردها</p>', unsafe_allow_html=True)
    ":orange[----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    col1 , col2 , col3 = st.columns(3)
    col1.markdown('<p class="persian-text">راهبردهای منتج از ترکیب نقاط قوت و فرصت</p>', unsafe_allow_html=True)
    col1.divider()
    col1.markdown('<p class="persian-text">SO1: حفاظت فعال از شهر تاریخی</p>', unsafe_allow_html=True)
    col1.markdown('<p class="persian-text">SO2: تقویت و ارتقاء زیرساخت ­های گردشگری در رقابت با مرکز استان</p>',
                  unsafe_allow_html=True)
    col1.markdown('<p class="persian-text">SO3 : پایدارسازی کشاورزی در پیرامون شهر و شهرستان</p>', 
                  unsafe_allow_html=True)
    col1.markdown('<p class="persian-text">SO4 : ایجاد فرصت­های سرمایه­ گذاری در شهر و پیرامون</p>', unsafe_allow_html=True)
    col1.markdown('<p class="persian-text">SO5 : تقویت روحیه شهروندی و حس تعلق و هویت به شهر</p>', unsafe_allow_html=True)
    col2.image("IMG_7315.JPG")
    col3.markdown('<p class="persian-text">راهبردهای منتج از ترکیب نقاط ضعف و فرصت</p>', unsafe_allow_html=True)
    col3.divider()
    col3.markdown('<p class="persian-text">WO1 : حفاظت از عرصه طبیعی چمن سلطانیه</p>', unsafe_allow_html=True)
    col3.markdown('<p class="persian-text">WO2 : پایدارسازی توسعه کالبدی شهر</p>', unsafe_allow_html=True)
    col3.markdown('<p class="persian-text">WO3 : ارتقاء محور ممتاز گردشگری استان به محور تعاطی تمدن­ها</p>',
                  unsafe_allow_html=True)
    col3.markdown('<p class="persian-text">WO4 : شکل­ دهی و تقویت شبکه همپیوند عرصه ­های تاریخی</p>',
                  unsafe_allow_html=True)
    col3.markdown('<p class="persian-text">WO5 : تقویت روحیه امید و آینده­ نگری در مردم</p>', unsafe_allow_html=True)
    col3.markdown('<p class="persian-text">WO6 : ارتقاء شرایط زیستی ساکنان</p>', unsafe_allow_html=True)
    
document_toggle = st.sidebar.toggle("گزارش برنامه راهبردی")   
if document_toggle:
    st.markdown('<p class="persian-text">متن کامل برنامه راهبردی</p>', unsafe_allow_html=True)
    ":orange[----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]"
    st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\04_05_RhbordiSakhtari.pdf", height=800)
    
    
