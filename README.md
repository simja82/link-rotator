# Bienvenidos a Link Rotator

Este pequeño proyecto está hecho para que los Portfolios de YoProgramo no se "duerman" y, siempre, siempre estén disponibles de cara a un potencial Cliente, Empleador o para quienes los tienen que corregir...

La consigna es: No dejes que se caiga tu enlace!!!

IMPORTANTE: 
<br>
Este programa funciona, por el momento, únicamente en Windows y con Google Chrome. 

Está permitido hacer forks y modificaciones para otros S.O., navegadores y, se agradece mucho, avisar para sumarlos a este Readme.md de manera que todos los que quieran puedan colaborar para que los Portfolios se mantengan activos.

## Instalación

1- De https://www.python.org/downloads/ descargar Python y luego instalarlo.
<br>
2- En cmd correr pip install selenium y pip install webdriver-manager.
<br>
3- Descargar el archivo pages.py que está en este repositorio (también puede bajarse todo como .zip o clonarse pero solo se necesita el archivo pages.py).

## Uso

1- En cmd, navegar, con cd, hasta el directorio donde esté el archivo pages.py.
<br>
2- Una vez dentro del directorio correr python pages.py.

NOTA: 
<br>
Se va abrir de forma automática una página del navegador Chrome con una leyenda que avisa que un software automatizado controla la página y va a recorrer en bucle el listado de Portfolios/Páginas que contiene el archivo pages.py.

VISUALIZACIÓN:
<br>
Tanto cmd como la página del navegador que recorre los Portfolios pueden quedar minimizadas y van a seguir trabajando en todo momento. Se puede ver el recorrido en el listado que se muestra en cmd.

IMPORTANTE: 
<br>
Todos los días hay que hacer correr los dos puntos del apartado Uso de este archivo Readme.md de lo contrario no funciona el mantenimiento de las visitas para que se mantengan vivos los enlaces.

RECOMENDACIÓN: 
<br>
Periódicamente descargar el archivo pages.py y reemplazar el archivo que se tenga por el nuevo.

Si se hiciera la actualización del archivo pages.py mientras está corriendo el programa en cmd debe cerrarse cmd y abrirse nuevamente para hacer correr python pages.py después de reemplazar el archivo que se tenía en primera instancia por el nuevo para que los cambios tengan efecto y el bucle se actualice.
