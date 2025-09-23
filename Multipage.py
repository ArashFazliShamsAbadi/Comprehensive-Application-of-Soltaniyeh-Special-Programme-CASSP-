import streamlit as st


st.set_page_config(layout ="wide")

language = st.sidebar.selectbox("Language", options=["English", "فارسی"])
if language == "English":
    page0 = st.Page("Page0.py", title= "About the application")
    page1 = st.Page("Page1.py", title="Synopsis")
    page2 = st.Page("Page2.py", title="Current Condition")
    page3 = st.Page("Page3.py", title="Strategic Plan")
    page3_1 = st.Page("Page3_1.py" , title = "Structure Planning")
    page4 = st.Page("Page4.py", title = "Soltaniyeh Interactive Map")
    page5 = st.Page("Page5.py", title = "Ueban Law and Regulations")

    pg = st.navigation([page0, page1, page2, page3, page3_1, page4, page5])

    pg.run()
else:
    page0 = st.Page("FPage0.py", title= "درباره اپلیکیشن")
    page1 = st.Page("FPage1.py", title="پیش گفتار")
    page2 = st.Page("FPage2.py", title="وضعیت موجود")
    page3 = st.Page("FPage3.py", title="برنامه راهبردی")
    page3_1 = st.Page("FPage3_1.py" , title = "طرح ساختاری")
    page4 = st.Page("FPage4.py", title = "نقشه تعاملی سلطانیه")
    page5 = st.Page("FPage5.py", title = "سامانه ضوابط و مقررات")

    pg = st.navigation([page0, page1, page2, page3, page3_1, page4, page5])

    pg.run()    
