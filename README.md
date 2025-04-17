# __PyTrivia__


### __Descripcion:__

    El juego consiste en responder un conjunto de preguntas, a las cuales el jugador o jugadora deberá responder correctamente para acumular puntos.

    La partida concluye cuando el jugador responde todas las preguntas de la ronda, momento en el cual se le informará al usuario su puntaje final y su posicion en el ranking de puntajes historicos.


### __Grupo 15:__

* __Santiago Michel__: 23991/7

* __Gonzalo Dario Battistella__: 17064/7

* __Lara Devincenti__: 18898/8

* __Mirko Emiliano Gonzalez__ :18531/8


### __Instalación:__

    Instalación en modo desarrollo
    -------------------------------

    Para instalar este proyecto:

        Usar una version de Python 3.11.X o superior y ejecutar en la terminal los siguientes comandos:

        """
        * Para crear un Entorno Virtual:
        python3.11 -m venv venv 
        
        * Para Sistema operativo Windows:
            Para activar el Entorno Virtual: source  venv/Scripts/activate
        * Para Sistema Operativo Linux/Mac:
            Para activar el Entorno Virtual: source venv/bin/activate

        *Para instalar las librerias necesarias:
            Ejecutar este comando: pip install -r requirements.txt

        Recordar desactivar el Entorno Virtual, luego de utilizar el programa.

        * Para desactivar el Entrono Virtual:
            Ejecutar el comando: deactivate
        """


### __Testeo del Programa:__

    * Para testear la parte de Procesamiento: Dentro de la carpeta llamada, 'procesamiento' se encuentran los archivos jupyter notebooks (archivos con extension .ipynb).
    Abrir estos archivos y ejecutar cada una de las celdas o ejecutar la opción 'run all'.
    Dicho procesamiento, lo que hace, es generar los datasets (archivos.  csv) modificados.

    * Para testear la parte de Consultas: Dentro de la carpeta 'Consultas' se encuentran los archivos jupyter notebooks (archivos con extension .ipynb).
    Abrir estos archivos y ejecutar cada una de las celdas o ejecutar la opcion 'run all'.
    En caso, que se solicite, ingresar los datos necesarios por teclado.
    La parte de consultas, lo que hace, es trabajar con los datasets modificados, e informar datos especificos de dichos datasets.

    * Para jugar al juego PyTrivia: A traves de una terminal, posicionarse dentro de la carpeta Streamlit y ejecutar el siguiente comando: Streamlit run inicio.py.

        * Comandos utiles para posicionarse dentro de dicha carpeta: 
            - ls = muestra las carpetas y archivos que se encuentran en el directorio actual.
            - cd nombre_carpeta = Para movernos dentro de ese directorio o carpeta.
            - cd .. = Para volver al directorio  padre, es decir, a la carpeta anterior. 

    * Inicio (inicio.py)
    Descripción:
    La página de inicio proporciona una breve descripción del juego, instrucciones básicas y una explicación del parámetro de dificultad.
    Funcionalidades:
    Descripción del Juego: Presenta una breve descripción del juego y su objetivo.
    Instrucciones Básicas: Detalla los pasos necesarios para comenzar a jugar.
    Explicación del Parámetro de Dificultad: Describe cómo funciona el parámetro de dificultad en el juego.
    Menú de Navegación: Proporciona enlaces a las secciones principales del juego.

    *Conociendo nuestros datos (conociendo_nuestros_datos.py)
    *Descripción: Esta sección permite a los usuarios explorar los datasets disponibles en el juego, brindando información adicional que puede ser útil para contestar las preguntas.
    Funcionalidades:
    Exploración de Datos: Permite a los usuarios explorar los datos de los diferentes datasets utilizados en el juego.

    *Juegos (juegos.py)
    Descripción: Este archivo contiene la lógica del juego, permitiendo a los usuarios seleccionar su nombre, dataset y dificultad, y luego responder a las preguntas.

    Funcionalidades:
    Selección de Usuario, Dataset y Dificultad: Permite a los usuarios elegir su nombre, el dataset y la dificultad del juego.
    Juego de Preguntas: Presenta una serie de preguntas para contestar, dependiente lo que el usuario responda obtendra puntos dependiendo la dificultad elegida. 
    Cálculo del Puntaje: Calcula el puntaje final basado en las respuestas correctas dependiendo que dificultad haya elegido el usuario.El puntaje se calcula según la dificultad elegida:
    -Facil:1
    -Media:1,5
    -Dificil:2 

    *Formulario de registro (formulario_de_registro.py)
    Descripción: Permite a los usuarios registrarse creando una nueva cuenta, almacenando los datos en la base de datos.
    Funcionalidades:
    Registro de Usuarios: Recoge datos como nombre completo, mail, fecha de nacimiento, genero y los almacena en la base de datos.
    
    *Ranking (ranking.py)
    Descripción: Muestra el ranking de los mejores 15 usuarios con mayor puntaje.

    *Estadísticas (estadisticas.py)
    Descripción: Muestra estadísticas detalladas sobre el rendimiento de los usuarios, incluyendo análisis de la partida jugada por los usuarios.