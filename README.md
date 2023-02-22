:pushpin: INTRODUCCIÓN
-------------

"Snake" o de forma criolla "La víborita", es un clásico juego en el que una víbora gana tamaño conforme va comiendo más y más comida repartida en toda la pantalla, cada vez que esto pasa paralelamente se van acumulando puntos. ¿Sencillo no?, a raíz de estas simples reglas ha habido infinidad de nuevos lanzamientos de este clásico, con nuevas características, nuevas reglas, nuevos diseños y todo lo que distintos desarrolladores quisiesen plasmar en su juego.
Así es como, por su simple premisa y por busca de una distracción a la rutina, me propuse el hacer como proyecto de verano el juego de la víborita.

En principio no fue de gran dificultad lograr todo esto, ya que, en anteriores años tuve que hacer un juego de mesa llamado "Scrabble" a través de tkinter en el lenguaje Python junto a 2 compañeros de facultad.

Por esa razón elegí el lenguaje anterior mencionado para la realización de este juego, porque, además de saber otros lenguajes como Java y un poco de C, sabía por experiencia que Python no era un lenguaje que sea muy complicado de manejar, eso se traduciría en un perfecto equilibrio entre disfrutar los días de verano y ponerme a trabajar en este proyecto.

Entonces así fue, comenzado el día 23 de enero y finalizado en la semana del 13 de febrero del presente año, este es el primer proyecto de muchos por venir.

:snake: SOBRE EL JUEGO
-------------

![GameplayGIF](https://user-images.githubusercontent.com/62036353/220705396-1837feb5-553f-4f20-b79f-ba5609f5565e.gif)

Pequeño resumen sobre qué trata este juego y cómo jugarlo.

La premisa es simple, hacer comer a la víbora hasta que no quepa en la pantalla, ¿facil verdad?, pues no lo es, esta víbora en particular (además de sufrir trastorno de personalidades cada vez que come) ¡¡le encantan las frutas!!, por lo tanto va a moverse a una velocidad mayor que lo normal con tal de comer lo antes posible. Dicho esto todo lo demás está presentado a continuación:

![InstruccionesGIF](https://user-images.githubusercontent.com/62036353/220705466-86439423-1a97-4b50-add9-95c4cf5d614f.gif)

Controles: 
- Flechas: Mueves a la víbora.
- Esc: Pones el juego en pausa.

La partida se pierde si:
- La víbora choca contra alguna de las esquinas de la pantalla.
- La víbora choca contra sí misma.

Sobre el objetivo:
- La víbora debe comer tantas frutas como sea posible, entre más frutas comas, más puntos sumaras a tu contador.

:nut_and_bolt: SOBRE LAS HERRAMIENTAS USADAS
-------------

- Pygame: Para poder llevar a cabo el desarrollo del videojuego.
- Pygame.mixer: Para poder darle sonido a la víbora cuando come. 
- PyInstaller: Para poder compilar todo mi programa en un ejecutable .exe
- Paint: Para todo lo relacionado a imágenes, hechas por mí, desde la víbora, pasando por la hierba y el arbusto del terreno, hasta las imágenes del tutorial.

:beers: CREDITOS
-------------

Fuentes de letra:
- Comfortaa de **Johan Aakerlund**.
- Sunny Spells de **Niskala Huruf**.
- Pixel Sans Serif de **Muhd Rusyaidi**.

Todas las fuentes fueron extraídas de: www.dafont.com

Imágenes:
- Snake de www.flaticon.com
- Flechas y tecla Esc de ?.
- Frutas por mi amiga **Jazmin Garcia**.

Sonidos:
- Sonido de comer hecho por **todos mis panas**.

:arrow_double_down: DESCARGA
-------------

Si quieres probarlo te dejo un link a un .rar para que lo puedas descargar sin problemas.

[//LINK MEGA](https://mega.nz/file/TJliQKZY#qlVQLqzJXhNwCQa1Q99BtUSQcDmBCez7xtbjLSiY0FE)

¡Importante leer!:
1. Por ahora solo está disponible para windows.
2. Puede que al descargarlo windows te lo detecte como posible amenaza, pero no te preocupes, su ejecucion es segura. Esto se debe a que el ejecutable (.exe) no tiene firma ni esta certificado, por lo tanto es normal este comportamiento del sistema operativo.
