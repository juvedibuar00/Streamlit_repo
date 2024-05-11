import streamlit as st


tab1, tab2, tab3 = st.tabs(['pagina 1', 'pagina 2', 'pagina 3'])


with tab3:
    st.map()



tab4, tab5 = st.tabs(['pagina 4', 'pagina 5'])

with tab4:
    st.video('https://www.youtube.com/watch?v=ncUzxOFibgA')

with tab5:
    st.image('https://images.pexels.com/photos/20147082/pexels-photo-20147082/free-photo-of-neve-leve-luz-light.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')