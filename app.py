

# ==================================================
# IMPORT LIBRARY
# ==================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import pickle
import os



# ==================================================
# SETTING HALAMAN
# ==================================================

st.set_page_config(

    page_title="Jelajah Wisata Jawa Timur",

    page_icon="icon.png",

    layout="wide"

)



# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv(
    "hasil_labeling_sentimen.csv"
)


kolom_wisata = "Nama Wisata"

kolom_sentimen = "sentiment"








# ==================================================
# KOLOM WILAYAH FINAL
# ==================================================

def cari_wilayah(nama):

    nama = str(nama).lower()


    wilayah = {




        # MOJOKERTO
        "trawas":"Kabupaten Mojokerto",
        "sumber gempong":"Kabupaten Mojokerto",
        "claket":"Kabupaten Mojokerto",


        # PROBOLINGGO
        "gili ketapang":"Kabupaten Probolinggo",
        "paiton":"Kabupaten Probolinggo",
        "randutatah":"Kabupaten Probolinggo",


        # BONDOWOSO
        "tasnan":"Kabupaten Bondowoso",
        "kawah wurung":"Kabupaten Bondowoso",
        "blawan":"Kabupaten Bondowoso",
        "sampean":"Kabupaten Bondowoso",


        # BANYUWANGI
        "kalibendo":"Kabupaten Banyuwangi",
        "jagir":"Kabupaten Banyuwangi",
        "tabuhan":"Kabupaten Banyuwangi",
        "bangsring":"Kabupaten Banyuwangi",
        "mustika":"Kabupaten Banyuwangi",


        # JOMBANG
        "wonosalam":"Kabupaten Jombang",
        "sumber biru":"Kabupaten Jombang",
        "kedung cinet":"Kabupaten Jombang",


        # SAMPANG
        "aeng sareh":"Kabupaten Sampang",
        "camplong":"Kabupaten Sampang",
        "nepa":"Kabupaten Sampang",
        "mandangin":"Kabupaten Sampang",
        "toroan":"Kabupaten Sampang",


        # TULUNGAGUNG
        "klatak":"Kabupaten Tulungagung",
        "sine":"Kabupaten Tulungagung",
        "pacar":"Kabupaten Tulungagung",
        "goa pasir":"Kabupaten Tulungagung",


        # TRENGGALEK
        "damas":"Kabupaten Trenggalek",
        "pelang":"Kabupaten Trenggalek",
        "prigi":"Kabupaten Trenggalek",


        # NGAWI / MAGETAN
        "srambang":"Kabupaten Ngawi",
        "jamus":"Kabupaten Ngawi",
        "lawu":"Kabupaten Magetan",
        "sarangan":"Kabupaten Magetan",


        # PONOROGO
        "mloko sewu":"Kabupaten Ponorogo",
        "waduk bendo":"Kabupaten Ponorogo",


        # NGANJUK
        "ngetos":"Kabupaten Nganjuk",
        "pringitan":"Kabupaten Nganjuk",


        # GRESIK
        "bawean":"Kabupaten Gresik",
        "kastoba":"Kabupaten Gresik",
        "mengare":"Kabupaten Gresik",


        # SITUBONDO
        "tampora":"Kabupaten Situbondo",
        "baluran":"Kabupaten Situbondo",
        "bama":"Kabupaten Situbondo",
        "banongan":"Kabupaten Situbondo",
        "bekol":"Kabupaten Situbondo",
        "pasir putih":"Kabupaten Situbondo",


        # SUMENEP
        "slopeng":"Kabupaten Sumenep",
        "lombang":"Kabupaten Sumenep",
        "sembilan":"Kabupaten Sumenep",
        "saronggi":"Kabupaten Sumenep",
        "ponjuk":"Kabupaten Sumenep",


        # LAMONGAN
        "maharani":"Kabupaten Lamongan",
        "wisata bahari":"Kabupaten Lamongan",


        # MADIUN
        "pandan wilis":"Kota Madiun",


        # KEDIRI
        "selomangleng":"Kota Kediri",
        "ongakan":"Kabupaten Kediri",


        # PASURUAN
        "kakek bodo":"Kabupaten Pasuruan",
        "grati":"Kabupaten Pasuruan",


        # JEMBER
        "gambir":"Kabupaten Jember",
        "tancak":"Kabupaten Jember",
        "teluk love":"Kabupaten Jember",
        "bandealit":"Kabupaten Jember",





        # SISA MAPPING FINAL

        "hawai":"Kota Malang",
        "kampung blekok":"Kabupaten Situbondo",
        "blekok":"Kabupaten Situbondo",
        "almour":"Kabupaten Bangkalan",
        "alassumur":"Kabupaten Bangkalan",
        "klampis":"Kabupaten Bangkalan",
        "paralayang megasari":"Kabupaten Tulungagung",
        "megasari":"Kabupaten Tulungagung",
        "marparan":"Kabupaten Sampang",
        "tanjung gheen":"Kabupaten Sampang",
        "gunung geger":"Kabupaten Bangkalan",

        "bukit sekipan":"Kabupaten Magetan",
        "sekipan":"Kabupaten Magetan",
        "pasir berbisik":"Kabupaten Probolinggo",
        "roro kuning":"Kabupaten Nganjuk",
        "damar wulan":"Kabupaten Kediri",
        "pelalangan":"Kabupaten Bangkalan",
        "kapur suci":"Kabupaten Gresik",
        "mayangkara":"Kabupaten Blitar",
        "banyulawe":"Kabupaten Nganjuk",

        "sendang made":"Kabupaten Jombang",
        "tirto galuh":"Kabupaten Blitar",
        "kapas biru":"Kabupaten Lumajang",
        "kusuma agro":"Kota Batu",
        "candi lor":"Kabupaten Nganjuk",
        "goa jepang":"Kota Batu",
        "ropet":"Kabupaten Sumenep",

        "watu karung":"Kabupaten Pacitan",
        "cemara":"Kabupaten Tuban",
        "welirang":"Kabupaten Pasuruan",
        "arjuno":"Kabupaten Pasuruan",
        "ngampiran":"Kabupaten Trenggalek",
        "umbul tuk":"Kabupaten Blitar",
        "teletubies":"Kabupaten Probolinggo",
        "mangrove spot":"Kabupaten Sampang",

        "pantai boom":"Kabupaten Banyuwangi",
        "waduk jambe":"Kabupaten Ponorogo",
        "sangiran":"Kabupaten Ngawi",
        "kampung inggris":"Kabupaten Kediri",
        "kedungbrubus":"Kabupaten Madiun",
        "atlantis":"Kota Surabaya",

        "siring kemuning":"Kabupaten Bangkalan",
        "payaman":"Kabupaten Lamongan",
        "karang bolong":"Kabupaten Pacitan",
        "pantai duta":"Kabupaten Probolinggo",
        "lekok":"Kabupaten Pasuruan",
        "paseban":"Kabupaten Jember",
        "bendungan bendo":"Kabupaten Ponorogo",
        "dampar":"Kabupaten Lumajang",
        "rongkang":"Kabupaten Bangkalan",


        # SURABAYA
        "surabaya":"Kota Surabaya",
        "bungkul":"Kota Surabaya",
        "flora":"Kota Surabaya",
        "kenjeran":"Kota Surabaya",
        "sampoerna":"Kota Surabaya",
        "tugu pahlawan":"Kota Surabaya",
        "harmoni":"Kota Surabaya",


        # MALANG
        "malang":"Kota Malang",
        "sengkaling":"Kabupaten Malang",
        "coban":"Kabupaten Malang",
        "balekambang":"Kabupaten Malang",
        "goa cina":"Kabupaten Malang",
        "sendiki":"Kabupaten Malang",
        "ngliyep":"Kabupaten Malang",
        "semeru":"Kabupaten Malang",


        # BATU
        "batu":"Kota Batu",
        "jatim park":"Kota Batu",
        "selecta":"Kota Batu",
        "angkut":"Kota Batu",
        "songgoriti":"Kota Batu",
        "cangar":"Kota Batu",
        "omah kayu":"Kota Batu",


        # BLITAR
        "blitar":"Kabupaten Blitar",
        "bung karno":"Kabupaten Blitar",
        "gebang":"Kabupaten Blitar",
        "tambak rejo":"Kabupaten Blitar",
        "serang":"Kabupaten Blitar",


        # BANYUWANGI
        "ijen":"Kabupaten Banyuwangi",
        "banyuwangi":"Kabupaten Banyuwangi",
        "pulau merah":"Kabupaten Banyuwangi",
        "djawatan":"Kabupaten Banyuwangi",
        "watudodol":"Kabupaten Banyuwangi",
        "sukamade":"Kabupaten Banyuwangi",
        "teluk hijau":"Kabupaten Banyuwangi",


        # PROBOLINGGO
        "bromo":"Kabupaten Probolinggo",
        "madakaripura":"Kabupaten Probolinggo",
        "bentar":"Kabupaten Probolinggo",


        # LUMAJANG
        "tumpak":"Kabupaten Lumajang",
        "ranu":"Kabupaten Lumajang",


        # JEMBER
        "jember":"Kabupaten Jember",
        "papuma":"Kabupaten Jember",
        "watu ulo":"Kabupaten Jember",
        "rembangan":"Kabupaten Jember",


        # KEDIRI
        "kediri":"Kabupaten Kediri",
        "gumul":"Kabupaten Kediri",
        "sekartaji":"Kabupaten Kediri",
        "dolo":"Kabupaten Kediri",


        # MADIUN
        "madiun":"Kota Madiun",


        # NGANJUK
        "nganjuk":"Kabupaten Nganjuk",
        "sedudo":"Kabupaten Nganjuk",
        "rorokuning":"Kabupaten Nganjuk",


        # PACITAN
        "pacitan":"Kabupaten Pacitan",
        "klayar":"Kabupaten Pacitan",
        "goa gong":"Kabupaten Pacitan",
        "srau":"Kabupaten Pacitan",


        # TUBAN
        "tuban":"Kabupaten Tuban",


        # SUMENEP
        "sumenep":"Kabupaten Sumenep",
        "gili labak":"Kabupaten Sumenep",
        "gili iyang":"Kabupaten Sumenep",


        # LAMONGAN
        "lamongan":"Kabupaten Lamongan",


        # PASURUAN
        "prigen":"Kabupaten Pasuruan",
        "purwodadi":"Kabupaten Pasuruan",


        # BANGKALAN
        "bangkalan":"Kabupaten Bangkalan",
        "jaddhih":"Kabupaten Bangkalan",


        # TRENGGALEK
        "trenggalek":"Kabupaten Trenggalek",

    }



    for key,value in wilayah.items():

        if key in nama:

            return value


    return "Lainnya"



df["Kabupaten/Kota"] = (

    df["Nama Wisata"]

    .apply(cari_wilayah)

)


kolom_kota = "Kabupaten/Kota"



# ==================================================
# HITUNG SENTIMEN PER WISATA
# ==================================================

hasil = (

    df.groupby(

        [

        kolom_wisata,

        kolom_kota

        ]

    )


    [kolom_sentimen]


    .value_counts()


    .unstack(fill_value=0)


    .reset_index()

)




for s in [

    "positif",

    "netral",

    "negatif"

]:


    if s not in hasil.columns:


        hasil[s]=0




hasil["total_ulasan"] = (


    hasil["positif"]

    +

    hasil["netral"]

    +

    hasil["negatif"]

)




hasil["persen_positif"] = (


    hasil["positif"]

    /

    hasil["total_ulasan"]

    *

    100

).round(1)




hasil["persen_netral"] = (


    hasil["netral"]

    /

    hasil["total_ulasan"]

    *

    100

).round(1)




hasil["persen_negatif"] = (


    hasil["negatif"]

    /

    hasil["total_ulasan"]

    *

    100

).round(1)






# ==================================================
# FOTO WISATA (REVISI FINAL)
# ==================================================

foto = {


    "Gunung Bromo":"bromo.jpg",


    "Kawah Ijen":"kawah_ijen.jpg",


    "Air Terjun Tumpak Sewu":"tumpak_sewu.jpg",


    "Pantai Papuma":"papuma.jpg",


    "Pantai Balekambang":"balekambang.jpg"


}





def tampil_foto(nama):


    nama = str(nama).lower()



    if "bromo" in nama:

        st.image(
            "bromo.jpg",
            use_container_width=True
        )



    elif "ijen" in nama:

        st.image(
            "kawah_ijen.jpg",
            use_container_width=True
        )



    elif "tumpak" in nama:

        st.image(
            "tumpak_sewu.jpg",
            use_container_width=True
        )



    elif "papuma" in nama:

        st.image(
            "papuma.jpg",
            use_container_width=True
        )



    elif "balekambang" in nama:

        st.image(
            "balekambang.jpg",
            use_container_width=True
        )



# ==================================================
# SIDEBAR
# ==================================================


daftar_kota = [

    "Kabupaten Bangkalan",
    "Kabupaten Banyuwangi",
    "Kabupaten Blitar",
    "Kabupaten Bojonegoro",
    "Kabupaten Bondowoso",
    "Kabupaten Gresik",
    "Kabupaten Jember",
    "Kabupaten Jombang",
    "Kabupaten Kediri",
    "Kabupaten Lamongan",
    "Kabupaten Lumajang",
    "Kabupaten Madiun",
    "Kabupaten Magetan",
    "Kabupaten Malang",
    "Kabupaten Mojokerto",
    "Kabupaten Nganjuk",
    "Kabupaten Ngawi",
    "Kabupaten Pacitan",
    "Kabupaten Pamekasan",
    "Kabupaten Pasuruan",
    "Kabupaten Ponorogo",
    "Kabupaten Probolinggo",
    "Kabupaten Sampang",
    "Kabupaten Sidoarjo",
    "Kabupaten Situbondo",
    "Kabupaten Sumenep",
    "Kabupaten Trenggalek",
    "Kabupaten Tuban",
    "Kabupaten Tulungagung",

    "Kota Batu",
    "Kota Blitar",
    "Kota Kediri",
    "Kota Madiun",
    "Kota Malang",
    "Kota Mojokerto",
    "Kota Pasuruan",
    "Kota Probolinggo",
    "Kota Surabaya"

]


with st.sidebar:


    st.image(

        "icon.png",

        width=140

    )



    st.title(

        "Jelajah Wisata"

    )



    menu = st.radio(

        "☰ MENU",

        [

            "🏠 Beranda",

            "⭐ Wisata Terbaik",

            "🔍 Cari Wisata",

            "📊 Analisis Sentimen",

            "💬 Prediksi Sentimen",

            "ℹ️ Tentang Sistem"

        ]

    )




    pilih_kota = st.selectbox(

        "📍 Filter Wilayah",


        ["Semua Kabupaten/Kota"]

        +

        list(daftar_kota)

    )






# ==================================================
# BERANDA
# ==================================================

if menu == "🏠 Beranda":




    # ==================================================
    # FILTER WILAYAH
    # ==================================================

    if pilih_kota != "Semua Kabupaten/Kota":



        data_filter = (

            hasil[

                (

                    hasil[kolom_kota]

                    .str.replace("Kabupaten ","",regex=False)

                    .str.replace("Kota ","",regex=False)

                    .str.lower()

                    ==

                    pilih_kota

                    .replace("Kabupaten ","")

                    .replace("Kota ","")

                    .lower()

                )

                |

                (

                    hasil[kolom_wisata]

                    .str.lower()

                    .str.contains(

                        pilih_kota

                        .replace("Kabupaten ","")

                        .replace("Kota ","")

                        .lower(),

                        na=False

                    )

                )

            ]


            .sort_values(

                by="persen_positif",

                ascending=False

            )


            .reset_index(drop=True)

        )




        st.title(

            f"📍 Wisata {pilih_kota}"

        )




        st.info(

            "Wisata diurutkan berdasarkan sentimen positif tertinggi"

        )




        if data_filter.empty:



            st.warning(

                "Belum ada data wisata pada wilayah ini"

            )




        else:



            for nomor,row in data_filter.iterrows():



                st.markdown("---")



                st.subheader(

                    f"{nomor+1}. {row[kolom_wisata]}"

                )




                c1,c2,c3,c4 = st.columns(

                    [2,1,1,1]

                )




                with c1:



                    tampil_foto(

                        row[kolom_wisata]

                    )



                    st.write(

                        f"💬 Total Ulasan : {row['total_ulasan']}"

                    )





                with c2:



                    st.metric(

                        "🟢 Positif",

                        f"{row['persen_positif']}%"

                    )





                with c3:



                    st.metric(

                        "🟡 Netral",

                        f"{row['persen_netral']}%"

                    )





                with c4:



                    st.metric(

                        "🔴 Negatif",

                        f"{row['persen_negatif']}%"

                    )








    # ==================================================
    # DASHBOARD UTAMA BERANDA
    # ==================================================

    else:



        st.image(

            "background.jpg",

            use_container_width=True

        )



        st.markdown(

            """

            <h1 style='font-size:50px;font-weight:800;'>

            Jelajah<br>
            Wisata<br>
            Jawa Timur

            </h1>


            <p>

            Temukan destinasi wisata terbaik
            berdasarkan analisis sentimen pengunjung.

            </p>


            """,

            unsafe_allow_html=True

        )





        total = len(df)


        positif = len(

            df[df[kolom_sentimen]=="positif"]

        )


        netral = len(

            df[df[kolom_sentimen]=="netral"]

        )


        negatif = len(

            df[df[kolom_sentimen]=="negatif"]

        )






        c1,c2,c3,c4,c5 = st.columns(5)
                # ==================================================
        # CARD STATISTIK KLIK
        # ==================================================


        with c1:


            if st.button(

                "🏔️\n\nTotal Wisata\n\n404 Tempat"

            ):


                st.dataframe(

                    hasil,

                    use_container_width=True

                )





        with c2:


            if st.button(

                f"💬\n\nTotal Ulasan\n\n{total:,}"

            ):


                st.dataframe(

                    df,

                    use_container_width=True

                )





        with c3:


            if st.button(

                f"😊\n\nPositif\n\n{positif}"

            ):


                st.dataframe(

                    df[

                        df[kolom_sentimen]=="positif"

                    ],

                    use_container_width=True

                )





        with c4:


            if st.button(

                f"😐\n\nNetral\n\n{netral}"

            ):


                st.dataframe(

                    df[

                        df[kolom_sentimen]=="netral"

                    ],

                    use_container_width=True

                )






        with c5:


            if st.button(

                f"😞\n\nNegatif\n\n{negatif}"

            ):


                st.dataframe(

                    df[

                        df[kolom_sentimen]=="negatif"

                    ],

                    use_container_width=True

                )






        st.markdown("---")






        # ==================================================
        # REKOMENDASI 5 WISATA UTAMA
        # ==================================================


        kiri,kanan = st.columns(

            [2,1]

        )





        with kiri:



            st.subheader(

                "⭐ Rekomendasi Wisata Berdasarkan Sentimen Positif"

            )



            st.caption(

                "Wisata unggulan berdasarkan hasil analisis sentimen."

            )






            wisata_utama = [

                "bromo",

                "ijen",

                "tumpak",

                "papuma",

                "balekambang"

            ]





            top5 = pd.DataFrame()





            for w in wisata_utama:



                ambil = hasil[


                    hasil[kolom_wisata]

                    .str.lower()

                    .str.contains(

                        w,

                        na=False

                    )


                ]




                top5 = pd.concat(

                    [

                        top5,

                        ambil.head(1)

                    ]

                )





            top5 = (

                top5

                .sort_values(

                    by="persen_positif",

                    ascending=False

                )

                .reset_index(

                    drop=True

                )

            )






            kol = st.columns(5)





            for i,(_,row) in enumerate(

                top5.iterrows()

            ):




                with kol[i]:




                    st.markdown(

                        f"### {i+1}"

                    )




                    tampil_foto(

                        row[kolom_wisata]

                    )





                    st.write(

                        f"**{row[kolom_wisata]}**"

                    )





                    st.caption(

                        row[kolom_kota]

                    )





                    st.write(

                        f"🟢 Positif {row['persen_positif']}%"

                    )





                    st.write(

                        f"🟡 Netral {row['persen_netral']}%"

                    )





                    st.write(

                        f"🔴 Negatif {row['persen_negatif']}%"

                    )





                    st.caption(

                        f"Total Ulasan : {row['total_ulasan']}"

                    )






        # ==================================================
        # RINGKASAN SENTIMEN
        # ==================================================


        with kanan:



            st.subheader(

                "📊 Ringkasan Analisis Sentimen"

            )





            jumlah = (

                df[kolom_sentimen]

                .value_counts()

            )





            fig = go.Figure(

                data=[

                    go.Pie(

                        labels=jumlah.index,

                        values=jumlah.values,

                        hole=0.55,

                        textinfo="percent"

                    )

                ]

            )





            fig.add_annotation(

                text=f"<b>{total:,}</b><br>Total Ulasan",

                x=0.5,

                y=0.5,

                showarrow=False

            )





            st.plotly_chart(

                fig,

                use_container_width=True

            )





            st.info(

                "Distribusi sentimen diperoleh dari hasil labeling seluruh ulasan wisata."

            )






        st.markdown(

            """

            ---

            <center>

            🏔️ <b>Jelajah Wisata Jawa Timur</b><br>

            © 2026 All rights reserved.

            </center>

            """,

            unsafe_allow_html=True

        )
        # ==================================================
# WISATA TERBAIK
# ==================================================

elif menu == "⭐ Wisata Terbaik":



    st.title(

        "⭐ Wisata Terbaik Berdasarkan Sentimen Positif"

    )




    wisata_utama = [

        "bromo",

        "ijen",

        "tumpak",

        "papuma",

        "balekambang"

    ]





    utama = pd.DataFrame()





    for w in wisata_utama:



        ambil = hasil[


            hasil[kolom_wisata]

            .str.lower()

            .str.contains(

                w,

                na=False

            )


        ]





        utama = pd.concat(

            [

                utama,

                ambil.head(1)

            ]

        )





    lainnya = hasil[


        ~

        hasil[kolom_wisata]

        .isin(

            utama[kolom_wisata]

        )


    ]





    lainnya = lainnya.sort_values(

        by="persen_positif",

        ascending=False

    )






    ranking = pd.concat(

        [

            utama,

            lainnya

        ]

    ).reset_index(

        drop=True

    )






    st.dataframe(


        ranking[

            [

                kolom_wisata,

                kolom_kota,

                "positif",

                "netral",

                "negatif",

                "total_ulasan",

                "persen_positif",

                "persen_netral",

                "persen_negatif"

            ]

        ],


        use_container_width=True

    )







# ==================================================
# CARI WISATA
# ==================================================

elif menu == "🔍 Cari Wisata":



    st.title(

        "🔍 Cari Wisata"

    )



    cari = st.text_input(

        "Masukkan nama wisata"

    )





    if cari:



        hasil_cari = hasil[


            hasil[kolom_wisata]

            .str.contains(

                cari,

                case=False,

                na=False

            )


        ]





        if hasil_cari.empty:



            st.warning(

                "Wisata tidak ditemukan"

            )



        else:



            st.dataframe(

                hasil_cari,

                use_container_width=True

            )
            # ==================================================
# ANALISIS SENTIMEN
# ==================================================

elif menu == "📊 Analisis Sentimen":



    st.title(

        "📊 Analisis Sentimen Wisata"

    )




    jumlah = (

        df[kolom_sentimen]

        .value_counts()

    )




    fig = go.Figure(


        data=[


            go.Pie(

                labels=jumlah.index,

                values=jumlah.values,

                hole=0.5,

                textinfo="percent+label"

            )


        ]

    )





    st.plotly_chart(

        fig,

        use_container_width=True

    )





    tabel = pd.DataFrame(

        {


            "Sentimen":

            jumlah.index,



            "Jumlah Data":

            jumlah.values,



            "Persentase (%)":

            (

                jumlah.values

                /

                len(df)

                *

                100

            ).round(1)


        }

    )





    st.dataframe(

        tabel,

        use_container_width=True

    )










# ==================================================
# PREDIKSI SENTIMEN
# ==================================================

elif menu == "💬 Prediksi Sentimen":




    st.title(

        "💬 Prediksi Sentimen Ulasan Wisata"

    )





    model = pickle.load(

        open(

            "model_logistic_regression.pkl",

            "rb"

        )

    )





    vectorizer = pickle.load(

        open(

            "tfidf_vectorizer.pkl",

            "rb"

        )

    )





    teks = st.text_area(

        "Masukkan ulasan wisata"

    )





    if st.button(

        "Prediksi"

    ):




        if teks:




            proses = vectorizer.transform(

                [teks]

            )




            prediksi = model.predict(

                proses

            )[0]






            st.success(

                f"Hasil Sentimen : {prediksi}"

            )





        else:




            st.warning(

                "Masukkan ulasan terlebih dahulu"

            )









# ==================================================
# TENTANG SISTEM
# ==================================================

elif menu == "ℹ️ Tentang Sistem":




    st.title(

        "ℹ️ Tentang Sistem"

    )






    st.write(

        """

        Sistem Rekomendasi Wisata Jawa Timur
        Berbasis Analisis Sentimen Pengunjung.


        Sistem ini dibuat untuk memberikan rekomendasi
        destinasi wisata berdasarkan opini pengunjung.


        Tahapan penelitian:


        1. Scraping data ulasan wisata


        2. Preprocessing data teks


        3. Labeling sentimen positif, netral, negatif


        4. Pembagian data


        5. Ekstraksi fitur TF-IDF


        6. Klasifikasi menggunakan Logistic Regression


        7. Evaluasi model


        8. Pengembangan website rekomendasi wisata


        """

    )
