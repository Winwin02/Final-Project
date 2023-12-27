import streamlit as st 
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")


image = Image.open('logo.png')
st.image(image, width=150)
 

navbar = option_menu(
    menu_title=None,
    options=("Home", "Semua Komik", "Donasi"),
    icons=["house", "book", "donate"],
    orientation = ("horizontal")
)

st.header=('ETIKOMIK')
if navbar == "Home":
#    rkm = 'rekomendasi'
    rkm = st.container()
    with rkm:
        gbr = Image.open('h3.jpg')
        st.image(gbr)
        rkm.header("L O O K I S M")
        rkm.write("Mengisahkan tentang seorang remaja laki-laki bernama Park Hyung Seok yang mengalami bully penampilannya yang dianggap tidak menarik. Bully yang begitu parah membuatnya memutuskan untuk pindah rumah dan sekolah.Tak disangka, keputusan pindah itu ternyata benar-benar mengubah kehidupan Park Hyung Seok.")


    populer = st.container()
    with populer:
        st.subheader("Populer Hari Ini", divider=True)
        kom1, kom2, kom3, kom4, kom5, kom6, kom7, kom8 = st.columns(8)
        with kom1: 
            kom1.image('lookism.jpg', width=135)
            kom1.write('Lookism')
            kom1.link_button("Mulai Baca", "www.google.com", use_container_width=True)
        with kom2:
            kom2.image('nano-machine.jpg', width=135)
            kom2.write('Nano Machine')
            kom2.link_button("Mulai Baca", "www.google.com", use_container_width=True)
        with kom3:
            kom3.image('killer-peter.png')
            kom3.write('Killer Peter')
            kom3.link_button("Mulai Baca", "www.google.com", use_container_width=True)
        with kom4:
            kom4.image('warble.png', width=135)
            kom4.write('Warble')
            kom4.link_button("Mulai Baca", "www.google.com", use_container_width=True)
        with kom5:
            kom5.image('how-to-fight.jpg', width=135)
            kom5.write('How To Fight')
            kom5.link_button("Mulai Baca", "www.google.com", use_container_width=True)
        with kom6:
            kom6.image('solo-leveling.png', width=135)
            kom6.write('Solo Leveing')
            kom6.link_button("Mulai Baca", "http://localhost:8502/", use_container_width=True)
        with kom7:
            kom7.image('to-not-die.png', width=135)
            kom7.write('To Not Die')
            kom7.link_button("Mulai Baca", "www.google.com", use_container_width=True)
        with kom8:
            kom8.image('overlord.png', width=135)
            kom8.write('Overlord')
            kom8.link_button("Mulai Baca", "www.google.com", use_container_width=True)

    st.subheader("Update Komik Terbaru", divider=True)
    seka = st.container( border = None)
    with seka:
        tu1, tu2, tu3= st.columns(3)
        with tu1:
            kol1, kol2 = st.columns(2)
            with kol1:                                           
                c1 = st.container(border=None)
                c1.image('drifting-moon.jpg', caption='Reaper Of The Drifting Moon', width=200)
                c1.link_button("Mulai Baca", "./chapter/killer-peter-chapter-01/1.kiryuu.id.jpg", use_container_width=True)
                c2 = st.container(border=None)
                c2.image('nano-machine.jpg', caption='Nano Machine', width=200)
                c2.link_button("Mulai Baca", "chapter/ArcStrm1", use_container_width=True)
                c3 = st.container(border=None)
                c3.image('infinite-mage.jpg', caption='Infinite Mage', width=200)
                c3.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c4 = st.container(border=None)
                c4.image('boundless-necromancer.jpg', caption='Boundless Necromancer', width=200)
                c4.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                
                
            with kol2:
                c1 = st.container(border=None)
                c1.image('lookism.jpg', caption='Lookism', width=200)
                c1.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c2 = st.container(border=None)
                c2.image('eleceed.png', caption='Eleceed', width=200)
                c2.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c3 = st.container(border=None)
                c3.image('how-to-fight.jpg', caption='How To Fight', width=200)
                c3.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c4 = st.container(border=None)
                c4.image('killer-peter.png', caption='Killer Peter', width=200)
                c4.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                
                
        with tu2:
            kol3, kol4 = st.columns(2)
            with kol3:
                c1 = st.container(border=None)
                c1.image('magic-emperor.png', caption='Magic Emperor', width=200)
                c1.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c2 = st.container(border=None)
                c2.image('merciless.png', caption='Merciless', width=200)
                c2.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c3 = st.container(border=None)
                c3.image('overlord.png', caption='Overlord', width=200)
                c3.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c4 = st.container(border=None)
                c4.image('secret-player.png', caption='Secret Player', width=200)
                c4.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                
            with kol4:
                c1 = st.container(border=None)
                c1.image('quest-supremacy.png', caption='Quest Supremacy', width=200)
                c1.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c2 = st.container(border=None)
                c2.image('solo-leveling.png', caption='Solo Leveling', width=200)
                c2.link_button("Mulai Baca", "http://localhost:8502", use_container_width=True)
                c3 = st.container(border=None)
                c3.image('warble.png', caption='Warble', width=200)
                c3.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c4 = st.container(border=None)
                c4.image('to-not-die.png', caption='To Not Die', width=200)
                c4.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                
        
    with tu3:
        ame = st.container()
        ame.subheader('ABOUT ME')
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            col1.image('logoig.png', width=80)
            col1.link_button('Instagram', 'https://www.instagram.com/')
        with col2:
            col2.image('logotw.png', width=50)
            col2.link_button('X / Twetter', 'https://twitter.com/?lang=en')
        with col3:
            col3.image('logowa.png', width=50)
            col3.link_button('WhatsApp', 'https://web.whatsapp.com/' )\
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        kata2=st.container(border=True)
        with kata2:
            kata2.write('Selamat datang di dunia ETIKOMIK, di mana setiap garis tangan adalah langkah dalam petualangan teknologi dan seni yang tak terbatas. Di balik layar, kami bukan hanya seniman dan penulis, tetapi juga pengembang web yang penuh semangat. ETIKOMIK bukan hanya tentang cerita-cerita hebat, tetapi juga tentang keterlibatan teknologi yang mendalam.Dalam setiap panel, kami menarik inspirasi dari dunia pengembangan web untuk menciptakan pengalaman unik bagi Anda. Kami tidak hanya bercerita melalui kata-kata dan gambar, tetapi juga melibatkan elemen interaktif , dan antarmuka yang ramah pengguna. Setiap halaman adalah proyek kolaboratif antara seni dan teknologi, sebuah sinergi yang menciptakan dunia komik yang lebih hidup.Tim kami terdiri dari Frumentios David Ivan Satria, Muhammad Taufiq Budianto, Erwin Eka Saputra yang terdiri dari pengembang frontend, dan penggemar komik yang menyatu dalam visi kami untuk menciptakan pengalaman web yang tak terlupakan. Di ETIKOMIK, kami tidak hanya bercerita tentang karakter-karakter fantastis, tetapi juga tentang kemampuan teknologi untuk membawa mereka lebih dekat ke pembaca.Melalui setiap detail, dari animasi halaman hingga efek transisi yang mulus, kami berusaha memberikan pengalaman yang menggugah dan mendalam. Bergabunglah dengan kami di ETIKOMIK, di mana tulisan tangan kami yang unik dan keterampilan pengembangan web kami bersatu untuk membentuk dunia komik digital yang penuh keajaiban.Terima kasih telah menjadi bagian dari perjalanan ini. Bersama-sama, mari kita merayakan cerita, seni, dan teknologi dalam setiap klik dan gulir. Selamat menikmati petualangan, dan selamat datang di dunia ETIKOMIK, di mana seni bertemu dengan kode.Selamat membaca! Salam hangat Tim ETIKOMIK')

if navbar == "Semua Komik":
    seka = st.container( border = None)
    with seka:
        tu1, tu2, tu3= st.columns(3)
        with tu1:
            kol1, kol2 = st.columns(2)
            with kol1:                                           
                c1 = st.container(border=None)
                c1.image('drifting-moon.jpg', caption='Reaper Of The Drifting Moon', width=200)
                c1.link_button("Mulai Baca", "./chapter/ArcStrm1/5.jpg", use_container_width=True)
                c2 = st.container(border=None)
                c2.image('nano-machine.jpg', caption='Nano Machine', width=200)
                c2.link_button("Mulai Baca", ("chapter/ArcStrm1"), use_container_width=True)
                c3 = st.container(border=None)
                c3.image('infinite-mage.jpg', caption='Infinite Mage', width=200)
                c3.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c4 = st.container(border=None)
                c4.image('boundless-necromancer.jpg', caption='Boundless Necromancer', width=200)
                c4.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                
            with kol2:
                c1 = st.container(border=None)
                c1.image('lookism.jpg', caption='Lookism')
                c1.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c2 = st.container(border=None)
                c2.image('eleceed.png', caption='Eleceed')
                c2.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c3 = st.container(border=None)
                c3.image('how-to-fight.jpg', caption='How To Fight')
                c3.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c4 = st.container(border=None)
                c4.image('killer-peter.png', caption='Killer Peter')
                c4.link_button("Mulai Baca", "www.google.com", use_container_width=True)
        with tu2:
            kol3, kol4 = st.columns(2)
            with kol3:
                c1 = st.container(border=None)
                c1.image('magic-emperor.png', caption='Magic Emperor')
                c1.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c2 = st.container(border=None)
                c2.image('merciless.png', caption='Merciless')
                c2.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c3 = st.container(border=None)
                c3.image('overlord.png', caption='Overlord')
                c3.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c4 = st.container(border=None)
                c4.image('secret-player.png', caption='Secret Player')
                c4.link_button("Mulai Baca", "www.google.com", use_container_width=True)
            with kol4:
                c1 = st.container(border=None)
                c1.image('quest-supremacy.png', caption='Quest Supremacy')
                c1.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c2 = st.container(border=None)
                c2.image('solo-leveling.png', caption='Solo Leveling')
                c2.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c3 = st.container(border=None)
                c3.image('warble.png', caption='Warble')
                c3.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c4 = st.container(border=None)
                c4.image('to-not-die.png', caption='To Not Die')
                c4.link_button("Mulai Baca", "www.google.com", use_container_width=True)
        with tu3:
            kol5, kol6 = st.columns(2)
            with kol5:
                c1 = st.container(border=None)
                c1.image('magic-emperor.png', caption='Magic Emperor')
                c1.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c2 = st.container(border=None)
                c2.image('merciless.png', caption='Merciless')
                c2.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c3 = st.container(border=None)
                c3.image('overlord.png', caption='Overlord')
                c3.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c4 = st.container(border=None)
                c4.image('secret-player.png', caption='Secret Player')
                c4.link_button("Mulai Baca", "www.google.com", use_container_width=True)
            with kol6:
                c1 = st.container(border=None)
                c1.image('quest-supremacy.png', caption='Quest Supremacy')
                c1.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c2 = st.container(border=None)
                c2.image('solo-leveling.png', caption='Solo Leveling')
                c2.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c3 = st.container(border=None)
                c3.image('warble.png', caption='Warble')
                c3.link_button("Mulai Baca", "www.google.com", use_container_width=True)
                c4 = st.container(border=None)
                c4.image('to-not-die.png', caption='To Not Die')
                c4.link_button("Mulai Baca", "www.google.com", use_container_width=True)

if navbar == "Donasi":
    st.subheader('QRCODE DANA')
    st.image('qrcode.jpeg')
    st.subheader('Donasi yang banyak yaa !!')
