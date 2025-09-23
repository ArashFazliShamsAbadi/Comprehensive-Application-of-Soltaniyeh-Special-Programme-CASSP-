import streamlit as st

col1, col2 = st.columns(2)
col1.page_link(label= "**Soltaniyeh page on UNESCO website**", 
             page="https://whc.unesco.org/en/list/1188/", icon=":material/home:")
col1.page_link(label= "**Soltaniyeh Municipality website**",
               page = "https://www.soltaniyeh.ir/", icon= ":material/villa:")
col2.page_link(label = "**GD of Roads and Urban Development of Zanjan Province website**",
                page= "https://zanjan.mrud.ir/", icon=":material/forum:")
col2.page_link(label="**GD of Cultural Heritage, Tourism and Handicrafts of Zanjan Province website**",
               page="https://zanjan.mcth.ir/", icon=":material/castle:")

st.title("Synopsis")
text = st.write("""The site of Soltaniyeh with its impressive dome and monuments reveals an outstanding 
                example of human use of a favourable environment. Moreover, it is an exemplar testimony of an important 
                achievement in the course of human architectural innovations. In spite of the fact that the man’s attraction 
                for the lush meadow lands of Soltaniyeh, which is displayed by its vast and fertile pasture, goes back to 
                Prehistoric times, it was in the fourteenth century when the pasture was selected to become the capital par 
                excellence of an empire. It was the Mongol Ilkhan Oljaytu, recently converted to Shi’ism (and chose the name 
                of Soltan Mohammad Khodābandeh), who decided to build his capital city marked with a huge monument that 
                would become his sepulchre. The sites reveals the exemplar type of a successful unity between the Mongol 
                way of life, that is the horse breeding and nomadic way, and the sedentary society prevailing in Iran. 
                The rapid but astonishingly successful construction of the mausoleum and the structures of the city in a span of 
                less than ten years (from A.D. 1305 to 1313) was a culminating point in the history of Persian architecture. 
                The central monument of Soltaniyeh was built as the mausoleum of the Ilkhān Oljaytu adjacent to the pasture. 
                The mausoleum towered with a huge brick dome, which soon gave its name to the whole edifice. The monument is 
                known today as the Gonbad-e Soltaniyeh (the Imperial Dome). The presence of the highest dome ever constructed on 
                an octagonal plan at Soltaniyeh, which became possible merely by the ingenious constructing of a double shelled 
                structure, shows an innovation that inspired the construction of the high dome of Santa Maria del Fiore in Florence 
                almost a century later. The other significant aspect of Oljaytu’s mausoleum is its remarkable interior decorations 
                in the form of glazed tiles, brickwork, marquetry, stuccos and frescoes. The decorated surface in the monument was 
                estimated to 9000 square metres, and is one of the most decorated monuments in Iran. In this way, the monument 
                is a rich “museum” of applied decorative arts and their use in architecture. The spiritual significance of the 
                mausoleum is revealed by its ample decorative and calligraphic designs which bespeak of the builder’s attachment 
                to Shi’ism faith. According to a tradition, the monument had originally been designed to receive the relics of 
                Shi’i imams, Ali and his son, Hoseyn. The site lies in a plain adjacent to the pasture land that was the primary
                reason of its creation and existence. The whole area is in a large landscape buffer zone (4547.38 hectares), which 
                includes monuments with their core and buffer zones. The buffer zone comprises two major areas: first class and 
                second class buffer zones. Soltaniyeh is proposed as a single nomination within its landscape buffer zone 
                including the core and two relevant buffer zones.""")

col1 , col2 = st.columns(2)
col1.image("Soltaniyeh_Heritag_Sites.png")
col2.image("Heritage_Official_Map.jpg")
