
# ¡Hola, Aitaner!
# Autora: Lilian Venegas Torres (20232102)

# Este proyecto busca  es una página interactiva que muestra datos sobre la popularidad y relevancia de álbumes y canciones de la cantante Aitana en plataformas como YouTube, Spotify e Instagram 
# Los datos empleados fueron recopilados hasta (Junio de 2025*)

#Base de datos: https://docs.google.com/spreadsheets/d/1ayqWyBe5T1cvJ6DKzNkxDhoJKBccw7mXGffqSTfDx6Y/edit?usp=sharing


#ESTRUCTURA
#Importamos librerías importantes para 
import streamlit as st #Streamlit para la creación de la página
import pandas as pd #Para la manipulación de datos 
from IPython.display import display_html #para la procesar imágenes en HTML
from IPython.display import YouTubeVideo #para la visualización de videos de youtube
import seaborn as sns #Para gráficos/visualizaciones
import matplotlib.pyplot as plt #Para gráficos/visualizaciones
from matplotlib.ticker import FuncFormatter #para establecer una numeración amigable en gráfica


# Para abrir y leer el archivo Excel (base de datos)
# Asignamos una variable al archivo
# Usamos pd.read_excel por que es un archivo excel
basedatos = pd.read_excel('aitana_base_datos.xlsx')

#Dividimos la página de Streamlit en secciones
paginas = ['Inicio', 'Youtube', 'Spotify', 'Instagram', '¿Cantamos?']
#Creamos una barra de selección lateral, para que el usuario elija una sección
pagina_seleccionada = st.sidebar.selectbox('Bienvenido, Aitaner', paginas)



#Ingresamos una estructura if-elif-else, que responderá a la elección del usuario a parir de la barra de selección/selectbox

##PÁGINA DE "INICIO"
#En caso el usuario selecciones "Inicio" se ejecutará la siguiente sección:
if pagina_seleccionada == 'Inicio':
    # Para mostrar banner superior, st.image
    st.image("banner_hola_aitaner.png", width=900)

    #st.markdown para agregar una pequeña descripción del proyecto, en letras pequeñas
    st.markdown(
            f"<div style='text-align: justify; font-size: 11px;'>{"*Datos recopilados hasta el 30 de junio de 2025"}</div>",
            unsafe_allow_html=True)

    # Para mostrar un título, st.markdown
    st.markdown("<h1 style='text-align: left;'>Sobre Aitana...</h1>", unsafe_allow_html=True)


    # Creamos dos columnas para organizar contenido con st.columns
    col1, col2 = st.columns([2, 1]) 

    #Definimos contenido de primera columna
    with col1:
        #Ingresamos una variable (texto) y asignamos el texto que se quiere mostrar (descripción de artista)
        texto = """
        Aitana es una de las artistas pop más influyentes de la escena musical actual en España y Latinoamérica. Saltó a la fama con su participación en Operación Triunfo (Edición 2017). Desde allí, su carrera ha sido un recorrido que refleja su talento, carisma y una evolución artística constante. 
            Con éxitos como “Lo Malo”, “Teléfono” y “Formentera”, ha alcanzado múltiples discos de platino y millones de reproducciones en plataformas digitales.
            Con cuatro álbumes de estudio y una banda sonora (Spoiler, 11 RAZONES, La Última, alpha, CUARTO AZUL), Aitana ha explorado sonidos que van del pop clásico al electropop más moderno. Además de su carrera musical, ha protagonizado series, documentales y ha sido reconocida con premios como el MTV EMA, los Premios Odeón y nominaciones a los Latin Grammy. Aitana no solo canta: crea tendencia, conecta con su generación y emociona con cada paso.
        """
        #Para mostrar el texto en la columna, st.markdown. Contiene la variable que se ejecuta e imprime su contenido
        #Texto justificado, tamaño 15px
        st.markdown(
            f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>",
            unsafe_allow_html=True
        )

    #Definimos contenido de segunda columna
    with col2:
        #Usamos st.image para mostrar imagen a partir de un link (contenido HTML)
        #"caption" para string a modo de descripción de imagen
        st.image(
        "https://hips.hearstapps.com/hmg-prod/images/sb-hb-aitana-001-1632818812.jpg?resize=980:*",
        caption="Aitana Ocaña",
        use_container_width=True
        )

    #Título para separar una nueva sección con st.markdown
    #Título de buscador
    st.markdown("<h1 style='text-align: center;'>¿Empezamos con un Álbum?💿</h1>", unsafe_allow_html=True)
    
    #Creamos variable para búsqueda por álbum
    #st.texto_input para que el usuario pueda ingresar un texto de búsqueda
    busqueda_principal = st.text_input("🎵 Ingresa el nombre de un álbum aquí:")

    #Estructura de control para la búsqueda 
    #if para evaluar el contenido de la variable "busqueda_principal", texto ingresado por usuario
    if busqueda_principal:

        #Definimos los nombres de álbum que puede elegir el usuario para obtener un resultado de búsqueda
        #columna 'album' de la base de datos con funciones str.lower(), str.contains() y .lower() 
        # para homogeneizar el contenido de la columna y definir mejor posibles valores

        albumes_coincidentes = basedatos[
            basedatos['album'].str.lower().str.contains(busqueda_principal.lower())
        ]

        #Estructura de control para asegurar la coincidencia de la búsqueda
        #not y .empty para asegurarnos de que se ha ingresado algún contenido (*no está vacío)
        if not albumes_coincidentes.empty:
            # =True para señalar que sí se ha ingresado un valor de búsqueda
            encontrado = True

            #for e in para iterar sobre valores la columna de la tabla/base de datos
            #.unique para definir los valores únicos de la columna album

            for album in albumes_coincidentes['album'].unique():
                canciones_album = albumes_coincidentes[
                    albumes_coincidentes['album'] == album
                ]

                #st.image para mostrar imagen de álbum (columna url_album)
                ##caption para imprimir nombre de álbum como descripción de imagen
                st.image(
                    canciones_album.iloc[0]["url_album"],
                    width=200,
                    caption=f"Portada del álbum: {album}",
                )

                #st.markdown para imprimir el nombre de álgum
                st.markdown(f"### 🎼 Álbum: {album}")
                #st.write para i
                st.write("**Canciones:**")
                
                #for para iterar sobre valores de columna con nombres de canciones (que son parte del álbum buscado)
                for _, cancion in canciones_album.iterrows():

                    #st.write para imprimir el nombre de las canciones pertenecientes al álbum buscado
                    st.write(f"- {cancion['nombre_canciones']}")
        
        #Estructura else que se muestra si el usuario no ingresa un valor válido
        else:
            #st.warning para imprimir el mensaje de error en la búsqueda
            st.warning("No se encontraron álbumes que coincidan con tu búsqueda.")



## PÁGINA DE "YOUTUBE"
#En caso el usuario seleccione "Youtube" se ejecutará la siguiente sección:
elif pagina_seleccionada == 'Youtube':

    #Título de la sección con st.markdown
    st.markdown("<h1 style='text-align: center;'>Rankings de canciones de Aitana en Youtube</h1>", unsafe_allow_html=True)

    #st.selectbox para agregar una barra de selección que permita al usuario elegir qué ranking observar
    #Diccionario con posibles opciones de rankings a visualizar: Likes, Visualizaciones, Comentarios
    opcion = st.selectbox(
        "Selecciona un ranking para ver el Top 15:",
        ["Likes", "Visualizaciones", "Comentarios"]
    )

    #En caso el usuario elija la opción "Likes" del selectbox se ejecuta lo siguiente:
    if opcion == "Likes":
        #Subtítulo con el nombre del ranking que se visualiza (likes en Youtube)
        st.subheader("👍 Top 15 canciones con más likes en YouTube")

        #Ordenamos la base de datos en base a valores de columna likes_yt en orden descendente
        ranking_likesyt = basedatos.sort_values(by='likes_yt', ascending=False)
        #Tomamos los primeros 15 valores con head(15) a partir del ordenamiento
        #.reset_index para mostrar una numeración a partir del orden 
        top15 = ranking_likesyt.head(15).reset_index(drop=True)
       
        # Insertamos una nueva columna al principio del DataFrame llamada "#"
        # Esta columna numera las canciones del 1 al 15
        top15.insert(0, "#", range(1, len(top15)+1))
        # Seleccionamos solo las columnas deseadas del dataframe general y cambiamos nombres de encabezados
        tabla = top15[['#', 'nombre_canciones', 'album', 'likes_yt']].rename(
            columns={
                'nombre_canciones': 'Canción',
                'album': 'Álbum',
                'likes_yt': 'Likes'
            }
        )
        
        #Mostramos la tabla creada a partir de los filtros anteriores
        # hide_index=True oculta el índice adicional para que no aparezca una columna duplicada de números
        st.dataframe(tabla, hide_index=True)

    #En caso el usuario elija la opción "Visualizaciones" del selectbox se ejecuta lo siguiente:
    elif opcion == "Visualizaciones":
        #Subtítulo con el nombre del ranking que se visualiza (visualizaciones en Youtube)
        st.subheader("👀 Top 15 canciones con más visualizaciones en YouTube")

        #Ordenamos la base de datos en base a valores de columna vistas_yt en orden descendente
        ranking_vistasyt = basedatos.sort_values(by='vistas_yt', ascending=False)
        #Tomamos los primeros 15 valores con head(15) a partir del ordenamiento
        #.reset_index para mostrar una numeración a partir del orden 
        top15 = ranking_vistasyt.head(15).reset_index(drop=True)

        # Insertamos una nueva columna al principio del DataFrame llamada "#"
        # Esta columna numera las canciones del 1 al 15
        top15.insert(0, "#", range(1, len(top15)+1))
        # Seleccionamos solo las columnas deseadas del dataframe general y cambiamos nombres de encabezados
        tabla = top15[['#', 'nombre_canciones', 'album', 'vistas_yt']].rename(
            columns={
                'nombre_canciones': 'Canción',
                'album': 'Álbum',
                'vistas_yt': 'Visualizaciones'
            }
        )
        
        #Mostramos la tabla creada a partir de los filtros anteriores
        # hide_index=True oculta el índice adicional para que no aparezca una columna duplicada de números
        st.dataframe(tabla, hide_index=True)

    #En caso el usuario elija la opción "Visualizaciones" del selectbox se ejecuta lo siguiente:
    elif opcion == "Comentarios":
        #Subtítulo con el nombre del ranking que se visualiza (comentarios en Youtube)
        st.subheader("💬 Top 15 canciones con más comentarios en YouTube")

        #Ordenamos la base de datos en base a valores de columna comentarios_yt en orden descendente
        ranking_commentsyt = basedatos.sort_values(by='comentarios_yt', ascending=False)
        #Tomamos los primeros 15 valores con head(15) a partir del ordenamiento
        #.reset_index para mostrar una numeración a partir del orden 
        top15 = ranking_commentsyt.head(15).reset_index(drop=True)

        # Insertamos una nueva columna al principio del DataFrame llamada "#"
        # Esta columna numera las canciones del 1 al 15
        top15.insert(0, "#", range(1, len(top15)+1))
        # Seleccionamos solo las columnas deseadas del dataframe general y cambiamos nombres de encabezados
        tabla = top15[['#', 'nombre_canciones', 'album', 'comentarios_yt']].rename(
            columns={
                'nombre_canciones': 'Canción',
                'album': 'Álbum',
                'comentarios_yt': 'Comentarios'
            }
        )

        #Mostramos la tabla creada a partir de los filtros anteriores
        # hide_index=True oculta el índice adicional para que no aparezca una columna duplicada de números
        st.dataframe(tabla, hide_index=True)

    #Se agrega una imagen para mostrar al cierre de la sección  
    st.image("https://d21tucfpen3j82.cloudfront.net/wp-content/uploads/2025/01/24172641/Aitana-SegundoIntento.jpg", width=900)

   
##PÁGINA DE "SPOTIFY"
#En caso el usuario seleccione "Spotify" se ejecutará la siguiente sección: 
elif pagina_seleccionada == 'Spotify':
    # Para el título de la sección usamos st.markdown
    st.markdown("<h1 style='text-align: center;'>Rankings de canciones de Aitana en Spotify 🎵</h1>", unsafe_allow_html=True)

    st.subheader("📈 Top 3 canciones más reproducidas por álbum")
    # .unique() para definir lista con nombres de los álbumes (nombres como valores únicos)
    albumes_unicos = basedatos['album'].unique()

    #Creamos una barra de selección/selectbox para que el usuario seleccione álbum
    #Usamos variable albumes_unicos para mostrar opciones disponibles
    album_seleccionado = st.selectbox(
        "🎵 Selecciona un álbum", 
        sorted(albumes_unicos)
    )

    #Filtramos DataFrame, base de datos, por álbum seleccionado
    grupo_album = basedatos[basedatos['album'] == album_seleccionado]

    #Obtenmos el URL de portada del álbum de la columna url_album
    portada_url = grupo_album['url_album'].iloc[0]

    #Tomamos las Top 3 canciones más reproducidas
    #Ordenamos los valores del dataframe con .sort_values en orden descendente
    #Elegimos los primeros 3 valores del dataframe después del ordenamiento con .head(3)
    top3 = grupo_album.sort_values(
        by='reproduciones_spotify',
        ascending=False
    ).head(3)

    #Renombramos las columnas para un acabado más limpio con .rename()
    #Usamos .reset_index() para resetear los índices de las canciones en el dataframe
    tabla_top3 = top3[['nombre_canciones', 'reproduciones_spotify']].rename(
        columns={
            'nombre_canciones': 'Canción',
            'reproduciones_spotify': 'Reproducciones'
        }
    ).reset_index(drop=True)

    #.index+1 para que el índice reseteado inicie en 1
    tabla_top3.index = tabla_top3.index + 1

    #Creamos dos columnas para ordenar el contenido de la sección
    col1, col2 = st.columns([1, 2])  #Proporción más angosta para primera columna

    #Definimos contenido de primera columna (imagen de portada de álbum)
    with col1:
        #Mostramos imagen con st.image
        #Añadimos descripción a imagen en caption=
        st.image(
            portada_url, 
            caption=f"Portada del álbum: {album_seleccionado}", 
            width=200
        )

    #Definimos contenido de segunda columna (tabla de ranking)
    with col2:
        #Añadimos un subtítulo para denominar la tabla
        st.subheader("🎧 Top 3 canciones")
        #Mostramos el dataframe filtrado (tabla_top3)
        st.dataframe(
            tabla_top3,
            use_container_width=True
        )

    # Añadimos gráfica con seaborn
    # Creamos una nueva columna a la base de dato general con reproducciones en millones
    top3_plot = top3.copy()
    top3_plot['reproduc_millones'] = top3_plot['reproduciones_spotify'] / 1_000_000

    #Configuramos la gráfica realizada con seaborn
    fig, ax = plt.subplots(figsize=(8, 5))

    #Definimos el contenido del gráfico de barras
    sns.barplot(
            data=top3_plot,
            x='reproduc_millones', #número de reproducciones a partir de la nueva columna generada
            y='nombre_canciones', #nombre de cada canción perteneciente al top3 del álbum
            palette='Blues_d', #colores elegidos (azules)
            ax=ax    #especificamos el eje sobre el que se dibuja
        )

    #Definimos etiquetas y título, que irán cambiando de acuerdo al album seleccionado
    ax.set_xlabel("Reproducciones en Spotify (millones)", fontsize=12)
    ax.set_ylabel("Canción", fontsize=12)
    ax.set_title(f"Top 3 - {album_seleccionado}", fontsize=14, fontweight='bold')

    #Formateamos eje x para mostrar número de reproducciones en millones (como: 1.2M, 3.8M, etc.)
    ax.xaxis.set_major_formatter(
            FuncFormatter(lambda x, _: f"{x:.1f}M")
        )

    #Mostramos los valores numéricos junto a cada barra
    for i, v in enumerate(top3_plot['reproduc_millones']):
         ax.text(
                v, # Posición del texto con respecto al eje x
                i, # Posición del texto con respecto al eje y(índice de la canción)
                f"{v:.1f}M", # Texto que se mostrará (formato millones)
                color='black',
                va='center',
                fontweight='bold'
            )
    #Ajustamos los márgenes y distribución del gráfico
    plt.tight_layout()

    #Mostramos la gráfica, debajo de la división en columnas
    st.pyplot(fig)



##PÁGINA DE "INSTAGRAM"
#En caso el usuario seleccione "Instagram" se ejecutará la siguiente sección: 
elif pagina_seleccionada == 'Instagram':

    #Creamos un título con st.markdowm para denominar la sección
    st.markdown("<h1 style='text-align: center;'>📱 Posts promocionales en Instagram</h1>", unsafe_allow_html=True)

    # Creamos columna de "interacción" que sume el número de likes y el número de comentarios
    basedatos['interaccion_total'] = (
        basedatos['numlikes_ig'] + basedatos['numcomentarios_ig']
    )

    #Generamos un dataframe tomando en cuenta los valores de la nueva columna generada
    # Ordenamos el data frame en función a los valores de la columna interacción_total (Usamos .sort_values)
    #.head(10) para mostrar los primeros 10 valores a partir de este ordenamiento
    top_instagram = basedatos.sort_values(
        by='interaccion_total', ascending=False
    ).head(10)

    # Creamos una lista con urls de imágenes que se mostrarán para acompañar los 10 valores de resultado
    imagenes_manual = [
        "https://www.lahiguera.net/musicalia/artistas/aitana/disco/14086/tema/32431/aitana_6_de_febrero-portada.jpg",
        "https://cdn-images.dzcdn.net/images/cover/c880caa69be993971d92ad91826fa5bb/0x1900-000000-80-0-0.jpg",
        "https://www.lahiguera.net/musicalia/artistas/aitana/disco/10960/tema/22119/aitana_+_mas-portada.jpg",
        "https://hips.hearstapps.com/hmg-prod/images/aitana-natalia-lacunza-videoclip-1612864284.jpg",
        "https://www.lahiguera.net/musicalia/artistas/aitana/disco/9883/tema/20829/aitana_nada_sale_mal-portada.jpg",
        "https://www.lahiguera.net/musicalia/artistas/aitana/disco/12472/tema/26450/aitana_formentera-portada.jpg",
        "https://upload.wikimedia.org/wikipedia/en/e/e7/CorazonSinVidaCover.jpg",
        "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi93A__7E3G9mAS3riMZpBuHblz69tDI0pcry2Lsmvu_xa-1qgj1DNhAzHoNDvQqAN8XlHzz9JK4Tkg9Jy1isZGUkvOD2iybRaux6yu3iTtzq-kmURZDdGZcbTQcun4R8-yu7Tl87h1OC6koC8tFCKDq828lVQXFAG8xibi1Ddd5KV1iugSzijNZhrR1Ak/s831/aitana1.jpg",
        "https://cdn-images.dzcdn.net/images/cover/57432b0105261abfe8c1e486f4d0de45/500x500.jpg",
        "https://image.europafm.com/clipping/cmsimages02/2023/03/04/BA70DAB2-8C49-4D04-8920-0BB06ED912B8/mas-que-album-todo-que-sabe-alpha-nuevo-disco-aitana-que-saldra-2023_104.jpg?crop=368,368,x144,y0&width=1200&height=1200&optimize=low&format=webply",
    ]

    #Subtítuo con st.subheader para darle una división a la sección
    st.subheader("🎯Top 10 publicaciones con mayor impacto")

    #Recorremos el DataFrame top_instagram para mostrar cada canción del top 10 con su respectiva data
    # .iterrows para iterar fila por fila sobre el dataframe top_instagram
    #Usamos enumerate para llevar el conteo (índice "i") y empezar la numeración en 1.

    for i, (_, row) in enumerate(top_instagram.iterrows()):

        #Usamos una división en dos columnas
        col1, col2 = st.columns([2, 1])
        
        #Definimos contenido de primera columna (datos de publicación)
        with col1:
            #Mostramos el nombre de la canción y su posición en el ranking
            #"i+1" para mostrar su número en el ranking (+1 al índice)
            st.markdown(f"### {i+1}. 🎵 **{row['nombre_canciones']}**")
            
            #Dividimos en 3 columnas para mostrar la data de cada publicación de acuerdo a nuestra base de datos general
            c1, c2, c3 = st.columns([1, 1, 2])
            #Columna 1 para mostrar el número de likes(mostramos su respectivo valor de la columna numlikes_ig de base de datos)
            c1.metric("❤️ Likes (miles)", f"{row['numlikes_ig']:,}")
            #Columna 2 para mostrar el número de comentarios(mostramos su respectivo valor de la columna numcomentarios_ig de base de datos)
            c2.metric("💬 Comentarios", f"{row['numcomentarios_ig']:,}")
            #Columna 3 para mostrar la interacción(mostramos su respectivo valor de la columna interaccion_total, creada previamente)
            c3.metric("✨ Total Interacción", f"{row['interaccion_total']:,}")
            
            #Creamos un texto enlazado con url para redirigir al usuario a la publicación en Instagram
            st.markdown(
                f"[👉🔗 Mira el post en Instagram aquí]({row['post_instagram']})",
                unsafe_allow_html=True
            )
        
        #Definimos contenido de segunda columna (imágenes para acompañar cada resultado del top10)
        #Luego de una previsualización del top10, se le asignó a cada resultado una imagen referencial de la canción- 
        #  que el post de Instagram promociona a partir de la lista "imagenes_manual"
        with col2:
            imagen_url = imagenes_manual[i]
            st.image(imagen_url, use_container_width=True)
        
        st.markdown("---")



##PÁGINA DE "CANCIONES Y LETRAS"
#En caso el usuario seleccione "¿Cantamos?"(o "no seleccione" ninguna de las otras secciones) se ejecutará la siguiente sección :  
else:
    # Mostramos un título al centro de la sección    
    st.markdown("<h1 style='text-align: center;'>¿Listx para un karaoke?🎤</h1>", unsafe_allow_html=True)

    # Para el buscador de canciones, usamos st.text_input para permitir al usuario ingresar búsqueda
    # Se imprime pequeño mensaje con isntrucción al usuario
    busqueda_cancion = st.text_input("¡Canta los mejores hits de Aitana! 🤩 -  🌈Ingresa el nombre de una canción:")


    #Estructura de control para evaluar la búsqueda ingresada
    if busqueda_cancion:

        #Definimos valores de búsqueda posibles (nombres de canciones)
        #usamos str.lower(), str.contains() para homogeneizar el texto y definir mejor los posibles valores
        resultados = basedatos[
            basedatos['nombre_canciones'].str.lower().str.contains(busqueda_cancion.lower())
        ]

        #Constatamos de que se ha ingresado un valor (not y .empty)
        if not resultados.empty:
            #Iteramos sobre los posibles valores
            for _, fila in resultados.iterrows():
                
                #Definimos los contenidos de la base de datos que se mostrarán al usuario
                cancion = fila['nombre_canciones'] #para llamar a la columna con nombres de canciones
                album = fila['album'] #para llamar a la columna con los nombres de álbumes
                letra = fila['letra'] #para llamar a la columba con letras de cada canción
                url_youtube = fila['link_video'] #para llamar a columna con el link de video en youtube
                url_album_img = fila['url_album'] #para llamar a columna con url de imagen html de álbum

                # Título de la canción y álbum con st.markdown
                st.markdown(f"## 🎵 {cancion}")
                st.markdown(f"**💿 Álbum:** {album}")

                # Creamos las dos columnas con st.columns
                col1, col2 = st.columns([1.5,1.5]) 

                #Definimos contenido de columna 1
                with col1:
                    # Para imprimir letra de canciones en texto centrado, st.markdown
                    # Imprimimos un pequeño título "📝🎶 Letra"
                    st.markdown(
                        f"""
                        <div style='text-align: center; font-size: 12px;'>
                            <h4>📝🎶 Letra:</h4>
                            <p>{letra.replace('\n', '<br>')}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                #Definimos contenido de columna 2
                with col2:
                    
                    # Para mostar el video en youtube
                    if url_youtube:

                        # Extraemos el ID de YouTube para incrustar 
                        # (usamos funciones split y recorremos las palabras del url como string para sólo seleccionar el ID)
                        def extraer_id_youtube(url):
                            if "youtu.be" in url:
                                return url.split("/")[-1].split("?")[0]
                            elif "watch?v=" in url:
                                return url.split("watch?v=")[-1].split("&")[0]
                            else:
                                return None
                        
                        # Con ID extraído construimos estructura para incrustar video en la pagina
                        video_id = extraer_id_youtube(url_youtube)

                        #Estructura de control para emplear el id de la canción elegida
                        if video_id:
                            # Generamos iframe construyendo el link de inscrustación
                            youtube_embed_url = f"https://www.youtube.com/embed/{video_id}"
                            
                            # st.markdown para imprimir el url e incrustar el video
                            st.markdown(
                                f"""
                                <iframe width="100%" height="200" src="{youtube_embed_url}" 
                                frameborder="0" allowfullscreen></iframe>
                                """,
                                unsafe_allow_html=True
                            )
                        
                        #En caso haya un problema con el id del video de la canción
                        else:
                            #Imprimimos mensaje alertando el problema con st.info
                           st.info("No se pudo mostrar el video.")
                    
                    # Para imprimir imagen del álbum
                    if url_album_img:
                        #Usamos st.image para emplear el url de imagen de álbum y un caption con la descripción 
                        st.image(
                            url_album_img,
                            caption=f"Portada de {album}🎵",
                            use_container_width=True
                        )
        #En caso la búsqueda del usuario no esté incluida en la base de datos
        else:
            #Se imprime mensaje de error con st.warning
            st.warning("No se encontró ninguna canción con ese nombre.")

    #Se agrega una imagen para mostrar al cierre de la sección
    st.image("https://lamaquinamedio.com/wp-content/uploads/2023/05/Aitana-concierto-en-Chile.jpg")