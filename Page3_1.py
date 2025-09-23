import streamlit as st
import os


st.title("Soltaniyeh Structure Planning (SStP)")
st.markdown("""In this page you can visit the :blue[**outputs of structure planning for Soltaniyeh**]. For further information,
            please read the printed documants.""")


planning_map = st.sidebar.toggle("Planning Maps")
if planning_map:
    planning_maps = st.subheader("Planning Maps", divider="orange")
    col1, col2, col3 = st.columns(3)
    col1.caption("The main body of the region planning")
    col1.image("AsasTarhHarim.jpg")
    col2.caption("The main body of the city planning")
    col2.image("AsasTarhShahr.jpg")
    col3.caption("Surrounding area detailed zones")
    col3.image("HarimDetailedZoning.jpg")
    col1.caption("Surrounding area main zones")
    col1.image("HarimMainZoning.jpg")
    col2.caption("Landscape buffer zone policies")
    col2.image("HarimManzari.jpg")
    col3.caption("Proposed Boudaries")
    col3.image("MahdoudeHarim.jpg")
    col1.caption("City boundary: Comparison with the current boundary")
    col1.image("MoqayeseMahdoodeh.jpg")
    col2.caption("Soltaniyeh 2040 Road Map")
    col2.image("RoadMap.jpg")
    col3.caption("Proposed Road network")
    col3.image("ShahrRoads.jpg")
    col1.caption("City functional zoning")
    col1.image("ShahrZoning.jpg")
    col2.caption("Proposed local projects")
    col2.image("TarhHayeMozeyi.jpg")
    col3.caption("City zoning; Scales")
    col3.image("ZoningShahrScales.jpg")
detailed_map = st.sidebar.toggle("Detailed planning Maps")
if detailed_map:
    st.subheader("Dtailed Planning Map", divider="orange")
    col1, col2, col3 = st.columns(3)
    for i in range(1,13,3):
        col1.image(os.path.join(r"D:\Arash\StreamLit\Other_Try\Multipage\Map2000", f"0{i}.jpg"))
        col2.image(os.path.join(r"D:\Arash\StreamLit\Other_Try\Multipage\Map2000", f"0{i+1}.jpg"))
        col3.image(os.path.join(r"D:\Arash\StreamLit\Other_Try\Multipage\Map2000", f"0{i+2}.jpg"))
        
        
    # for i in range(2,15,3):
    #     col2.image(os.path.join(r"D:\Arash\StreamLit\Other_Try\Multipage\Map2000", f"0{i}.jpg"))    
    # for i in range(3,15,3):
    #     col3.image(os.path.join(r"D:\Arash\StreamLit\Other_Try\Multipage\Map2000", f"0{i}.jpg"))  
document_toggle = st.sidebar.toggle("Full report of the structure plan")   
if document_toggle:
    st.header("Structure Plan Report", divider="orange") 
    st.pdf(r"D:\Arash\StreamLit\Other_Try\Multipage\06_TarhTafsili_EslahiOstan.pdf", height=800)