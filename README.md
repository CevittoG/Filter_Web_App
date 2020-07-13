# Descripción Proyecto

Aplicación web que, utilizando la información de sandwiches publicada en blog chileno, logra hacer distintos tipos de búsquedas para encontrar sándwiches que se ajusten a los criterios que el usuario desee ingresar. Luego de ingresar sus criterios de búsqueda, el usuario recibirá como output el local donde sirven el sandwich, la ciudad, los ingredientes que este contiene y la calificación que se le otorgó en el blog. Entre las formas de búsqueda que tiene la aplicación están:

* “Crealo en casa”, donde se espera que el usuario ingrese todos los ingredientes que posee en el hogar para bucar todos los sanguches que tengan coincidencias, pero no ingredeintes fuera de los especificados.

* Buscar un sandwich por el número que este tiene asignado en el blog. 

* Búsqueda por alguna de las características del sándwich, ya sea el nombre de este, el local donde es servido, su puntuación, ingredientes o ciudad.
 
* Ingresar una variedad de ingredientes con lo que el buscador entregará los sandwiches con mejor puntuación que contengan uno o más de estos ingredientes.
 
* Ingresar una comuna o ciudad para recibir los sandwiches con mejor puntuación dentro de estas.

# Documentación

* webtest.py : Programa central que procesa todos los datos, manipulando las conexiones entre rutas y acceso a Google Drive
* templates : Carpeta que almacena archivos HTML en las que se muestran los datos resultantes de la busqueda
* Flask : Librería de python la cual permite generar conexión entre lenguajes, permitiendo definir rutas de las páginas web, direcciones y traspaso de datos (variables) entre ambos
* Google Drive API : Conexión de documento online con programa en Python
* Google Sheet API : Permite editar de cualquier manera los datos dentro de hoja de calculo online
* PythonAnywhere : Servidor gratuito, funcional por 3 meses 

# Implementación
Pasos a seguir para lograr implementar de manera completa la aplicacion web. Junto a algunas de las siguientes instrucciones se podra encontrar un enlace que servira de ayuda al momento de recrear la implementacion. Estos son guias, listas de videos en YouTube y blogs creados por terceros.

  1. En orden de lograr generar un acceso por parte del código desarrollado a los archivos que se encuentran en la nube, es necesario crear un proyecto en Google Console Cloud, el cual se relaciona directamente con el proyecto. Para lograr hacer esto solo se requiere una cuenta de Google. 
    * Google. (s. f.). Google Cloud Platform. Google Cloud Platform. Recuperado 10 de junio de 2020, de https://console.cloud.google.com/

  2. Una vez creado el proyecto, es necesario activar API de Google Sheet dentro del mismo. Esto se puede llevar a cabo utilizando la barra de búsqueda al ingresar “Google Sheet API”. Luego se debe presionar resultado y activar la API.
    * Google. (2020a, abril 21). Python Quickstart | Sheets API | . Google Developers. https://developers.google.com/sheets/api/quickstart/python

  3. De la misma manera, será necesario activar API de Google Drive dentro del proyecto, siguiendo las mismas instrucciones del paso anterior. 
    * Google. (2020, 20 junio). Browser Quickstart | Google Drive API | . Google Developers. https://developers.google.com/drive/api/v3/quickstart/js

  4. Una vez activada la API de Google Drive, se podrá generar una credencial especificando que ésta será utilizada como aplicación web y definiendo un nombre de cliente con categoría de editor. La credencial se descarga bajo el nombre de “creds.json” para ser reconocida por el programa ya desarrollado y debe ser almacenada en el mismo directorio que éste.
    * Tech With Tim. (2019, 12 marzo). Python Google Sheets API Tutorial - 2019 [Vídeo]. YouTube. https://www.youtube.com/watch?v=cnPlKLEGR7E

  5. En el archivo “creds.json” se puede encontrar una serie de datos pertenecientes a la credencial generada. Dentro de estos datos, en la sección de "client_email" se encontrará la dirección de email del cliente creado, el cual será la conexión con el archivo online almacenado en Google Drive. Para enlazar ambas partes, es importante compartir el archivo con dicha dirección email bajo la categoría de editor. Para esto, una vez que se está dentro del archivo Google Sheet, se debe hacer click en el botón verde ubicado en el extremo superior derecho de la pantalla; seguidamente se ingresa la dirección extraída de la credencial.

  6. Una vez completados los pasos anteriores, el programa se encontrará conectado a Google Drive, por lo que se puede subir los archivos enviados por email al servidor de la página web de 365Sanguchez.

  7. Para lograr que el programa sea completamente funcional, se instalará las librerías de Python (flask, gspread, oauth2client.service_account, numpy, pandas) ocupadas en el programa, dentro del servidor. De esta manera el servidor podrá leer el código de Python sin problemas.

# Enlaces relacionados de utilidad

* Tutoriales Flask. (2020, 24 abril). [Vídeo]. YouTube. https://www.youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
* Python Anywhere. (2013, 5 diciembre). PythonAnywhere in one minute [Vídeo]. YouTube. https://www.youtube.com/watch?v=NH2PhXYvrWs
* Baugues, G. (2018, 28 agosto). Google Spreadsheets and Python. Twilio Blog. https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html


