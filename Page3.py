import streamlit as st



st.title("Soltaniyeh Strategic Plan (SSP)")

vision_toggle = st.sidebar.toggle("Vision Statement")

if vision_toggle:
    st.subheader("Vision Statement:", divider="orange")
    st.write("""**The world-famous historical-cultural city-region, as one of the symbolic links between the two 
                 civilisational mega-axis of Alborz and Zagros, in the midst of the beautiful and lush meadows 
                 of Soltaniyeh - as members of one body - is a self-sufficient place for the residence of different lasses 
                 who spend their lives through various tourism, agricultural and environmentally friendly industrial activities.
                 The Soltaniyeh dwellers, with their rich historical background, are people who love the city, its historical 
                 wealth and its environment, with the help of continuous and effective education, and are aware of the importance 
                 of these elements, and seek to introduce it to the world.The lively and safe environment of this city, which is 
                 refreshed by the presence and participation of all age and gender groups, welcomes all kinds of tourists, 
                 researchers and students of science, art and history of this land from every corner of the country and the world, 
                 and has provided suitable facilities for their stay and comfort in the city. The clean old city of 
                 Soltaniyeh - whose architecture is visible from all sides and even far away - shows no signs of deterioration, 
                 and its structure, while respecting its architectural and urban history, is appropriate for contemporary life.**""")
    st.image("IMG_6072.JPG")
goals_toggle = st.sidebar.toggle("Main Goals")
if goals_toggle:
    st.subheader("Main Goals:", divider="orange")
    st.markdown("**Deservedly introducing Soltaniyeh to people around the world.**")
    st.markdown("**Improving the town and dwellres' economic condition.**")
    st.markdown("**Improving the living conditions for dwellres not only for themselves, but also to prevent them from leaving Soltaniyeh.**")
    st.markdown("**Considering regenerational approach as the main referenced idea to conservation and development.**")
    st.markdown("**Sustainable conservation of Soltaniyeh Pasture and its environment.**")
    st.markdown("**Improving tourism industry and tourist infrastructure.**")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.image("IMG_6224.JPG")
    col2.image("IMG_6231.JPG")
    col3.image("IMG_7306.JPG")
    col4.image("IMG_7961.JPG")
    col5.image("IMG_6081.JPG")
    col6.image("IMG_6109.JPG")
detailed_goals = st.sidebar.toggle("Other Goals")
if detailed_goals:
    st.subheader("Other Goals:", divider="orange")
    col1 , col2 = st.columns(2)
    col1.markdown("Upgrading Soltaniyeh to the historical city of Soltaniyeh and a centre for education and research in Ilkhanid arts and sciences.")
    col1.markdown("Improving the agricultural sector based on the principles of sustainable development.")
    col1.markdown("Providing the conditions for developing tourism chain activities in various fields — historical, natural, agricultural, sports, etc. — within the city and its surroundings, in competition with the provincial centre.")
    col1.markdown("Improving conditions for employment, business activities, and investment in the city, and preventing the outflow of human capital.")
    col1.markdown("Ensuring sustainable revenue sources for urban management.")
    col1.markdown("Sustainable protection of historical areas with a view to urban development and modernisation.")
    col1.markdown("Integration and coherence of historical areas with the city, reconciling the city with its own history.")
    col1.markdown("Strengthening the sense of citizenship and belonging to Soltaniyeh among the people.")
    col1.markdown("Enhancing residents’ awareness and knowledge of their natural, historical, and identity-related heritage.")
    col1.markdown("Improving the city’s service delivery to residents in all areas, befitting its status as a county centre.")
    col2.image("IMG_6310.JPG")
strategies = st.sidebar.toggle("Strategies")
if strategies:
    st.subheader("Strategies:", divider = "orange")
    col1 , col2 , col3 = st.columns(3)
    col1.subheader("Strategies based on combination of strengths (S) and opportunities (O)", divider="green")
    col1.markdown(":orange[**SO1**]: Active protection of the historical city (world heritage sites and surrounding).")
    col1.markdown(":orange[**SO2**]: Enhancing and improving tourist infrastructure in competition with the provincial centre.")
    col1.markdown(":orange[**SO3**]: Sustaining the agricultural sector and farmland in the county.")
    col1.markdown(":orange[**SO4**]: Bringing new invesment opportunities in the city and surrounding.")
    col1.markdown(":orange[**SO5**]: Strengthening the sense of citizenship and historical identity among dwellers.")
    col2.image("IMG_7315.JPG")
    col3.subheader("Strategies based on combination of weaknesses (W) and opportunities (O)", divider="green")
    col3.markdown(":blue[**WO1**]: Protection of Soltaniyeh Pasture")
    col3.markdown(":blue[**WO2**]: Implementing the principles of sustainable development in physical expansion.")
    col3.markdown(":blue[**WO3**]: Improving the Zanjan-Hamedan distinctive tourist corridor to the Corridor of Dialogue Among Civilazations.")
    col3.markdown(":blue[**WO4**]: Shaping and strengthening the interconnected network of historical quarters.")
    col3.markdown(":blue[**WO5**]: Strengthening the spirit of hope and foresight among people.")
    col3.markdown(":blue[**WO6**]: Improving the living conditions of residents.")
    
document_toggle = st.sidebar.toggle("Full report of the strategic plan")   
if document_toggle:
    st.header("Strategic Plan Report", divider="orange") 
    st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\04_05_RhbordiSakhtari.pdf", height=800)
    
    
