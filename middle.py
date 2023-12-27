import streamlit as st 
#from end import ImageFolderViewer as ifv

st.set_page_config(layout="wide")

#st.markdown("<h1 style='text-align: center;'>Archmage Streamer</h1> <br>", unsafe_allow_html=True)
ftr=st.container()
with ftr:
    col1, col2 = st.columns((1, 2))
    with col1:
        st.image('solo-leveling.png', width=350)
    with col2:
        st.header("Solo Leveling")
        st.write('Komik ini mengisahkan tentang Im Dajun, seorang siswa SMA yang setiap hari menjadi korban bully di sekolahnya. Suatu hari, ketika hampir menyerah pada kehidupannya, dia melihat wawancara di TV dengan seorang pembunuh yang membalas dendam atas penggertakan terhadap teman-temannya. Dajun terinspirasi oleh apa yang dia saksikan dan memutuskan untuk ikut membalas dendam. Meskipun balas dendamnya berhasil, hidupnya malah berubah menjadi arah yang tidak diinginkan. Im Dajun meninggalkan sekolah dan bergabung dengan kelompok aneh bernama Runaway Fam.Sebagai anggota kelompok ini, Dajun tidak lagi menjadi korban pengganggu di sekolah, namun sekarang dia harus bertahan melawan preman yang lebih ganas di jalanan.')
        

st.markdown("<br>", unsafe_allow_html=True)

btn_chp=st.container()
btn_chp.subheader('RELEASES')
with btn_chp:
    col1,col2,col3=st.columns(3)
    with col1:
        col1.link_button('Chapter 1', 'http://localhost:8503', use_container_width=True)
        col1.link_button('Chapter 2', 'http://localhost:8504', use_container_width=True)
        col1.link_button('Chapter 3', 'http://localhost:8505', use_container_width=True)
        col1.link_button('Chapter 4', 'http://localhost:8506', use_container_width=True)
        col1.link_button('Chapter 5', 'http://localhost:8507', use_container_width=True)



    with col2:
        col2.link_button('Chapter 6', 'http://localhost:8508', use_container_width=True)
        col2.link_button('Chapter 7', 'http://localhost:8509', use_container_width=True)
        col2.link_button('Chapter 8', 'http://localhost:8510', use_container_width=True)
        col2.link_button('Chapter 9', 'http://localhost:8511', use_container_width=True)
        col2.link_button('Chapter 10', 'http://localhost:8512', use_container_width=True)


    with col3:
        col3.link_button('Chapter 11', 'http://localhost:8502', use_container_width=True)
        col3.link_button('Chapter 12', 'http://localhost:8502', use_container_width=True)
        col3.link_button('Chapter 13', 'http://localhost:8502', use_container_width=True)
        col3.link_button('Chapter 14', 'http://localhost:8502', use_container_width=True)
        col3.link_button('Chapter 15', 'http://localhost:8502', use_container_width=True)