# InterfaceLab!
# CONSTRUCCIÓN DE UNA INTERFAZ GRÁFICA CON UNA RASPBERRY PARA EL CONTROL DE UNA TARJETA FPGA

A continuación, se mostrará el proceso de creación de una interfaz gráfica para el control de una tarjeta FPGA mediante los GPIO de un raspberry, en donde manejaremos los botones y switches de manera remota además de poder visualizar la tarjeta FPGA en tiempo real.

## 1. Diseño de la interfaz gráfica. 
Para la determinación del diseño se reviso las arquitecturas de laboratorios y su desarrollo de software, además se analizo los componentes de hardware utilizados, considerando estos criterios se escogió convenientemente las herramientas a usar en la determinación de requisitos.
### 1.1 Determinación de los requisitos de la interfaz gráfica 
Requisitos del Back End : 
-Python 3 
-Flask Server 
-OpenCV 
Requisitos del Front End: 
-Html 
-Css
### 1.2 Evaluación las características del diseño del BACK END 
Se escogió la versión de Python 3 , puesto que las librerías que usamos son más compatibles con esta versión del lenguaje .
Otro detalle importante para usar este lenguaje como base del proyecto es que es el lenguaje básico del control de GPIOs en el Software Raspbian que posee nuestro Raspberry PI. Por lo tanto instalamos la versión de python 3.6 dentro del software de Raspbian. Dentro de este lenguaje también instalaremos la librería de Flask para Python 3. Su versión es “Flask versión 1.1.2” 
Otra de las librerías a usar en el python será Open CV que permitirá configurar la imagen de video en vivo de la tarjeta FPGA.La versión de esta librería ser opencv-python versión 4.5.1.48. 
La librería Flask que incluímos en nuestro código en python es un framework que se usará como servidor de nuestra aplicación donde el host será la ip estática de nuestro Raspberry PI.

### 1.3 Evaluación las características del diseño del FRONT END 
Para la configuración de Front End utilizaremos los programas básicos de un aplicativo web: El lenguaje de html en donde la plataforma cargará los datos de las funciones que pusimos en nuestro programa python. De esta forma estas funciones pueden ser ejecutadas con comandos básicos de direccionamiento y visualización de parte de la página. Por otra parte el archivo css contará con todos los componentes gráficos que serán añadidos a la plataforma como lo son los botones y los colores de la página. 
### 1.4 Resolución de los programas de uso en el diseño de la interfaz gráfica 
Entonces para el resultado final diseñaremos una plataforma web , que usará el código python como base para las funciones que se especificaron, además de que el servidor Flask permitirá que podamos correr nuestro proyecto en una determinada dirección en la red Lan. Complementando esto los archivos de programación web básico que son: Html , Css contribuirán al desarrollo de esta plataforma de manera substancial, brindando detalle y solidez a las funciones que una interfaz gráfica de laboratorio remoto necesita. El código python albergará las 3 funciones principales de la interfaz, su conexión web al servidor, la configuración de los GPIOs y la integración del video de la cámara. El servidor de conexión es un código corto que incluirá la librería mencionada. El código correspondiente a los GPIOs deberá configurarlos de modo que funcionen de acuerdo a la conexión hecha entre el raspberry pi y la tarjeta FPGA y deberá controlar los estados de encendido y apagado de estos mismos.
En el caso del código correspondiente a la transmisión de imagen de la cámara web, este código de video debe consistir en 3 etapas: 
Generación de imagen: Esta función tendrá como objetivo generar las capturas de imagen consecutivas de la cámara web, para así poder usarlas como objetos en el código.
Obtención de imagen: En esta etapa se leerá el objeto descrito anteriormente para poder entregarlo como imagen de salida para alguna otra función. 
Transmisión de video: Este código mostrará los objetos de salida del paso anterior (imágenes procesadas), en otras palabras, transmitirá constantemente los datos obtenidos de la primera etapa y procesados por la segunda etapa. 


## 2 Implementación de la interfaz gráfica. 
Empezando a desarrollar el código definimos las funciones previamente descritas en el diseño de nuestro código de python: 
```
-Configuración de los GPIOs (botones) 
-Configuración de la cámara web(video) 
-Configuración del servidor(Flask) 
```
### 2.1 Implementación y modificación del entorno según los requerimientos.
En esta parte abordaremos la implementación de dos de los procedimientos mencionados que son : Configuración de la cámara web y configuración del servidor. 
Para la implementación de la cámara web y su visualización en la interfaz nos apoyamos de la librería de Opencv la cual nos brinda todo el setup de una transmisión de video dentro la aplicación y que puede personalizarse según las características requeridas del entorno. Como se puede observar las funcionalidades de esta parte establecen a la variable “camera” como la variable de sensor de la cámara web y utilizamos para guardar , leer y transmitir constantemente , y se genere la video transmisión en la interfaz gráfica. El codigo describe las 3 etapas que mencionamos.

Figura 1
Descripción de las etapas del código de video con Opencv. 
![image](https://user-images.githubusercontent.com/85809354/156904945-3fdcb41f-76a2-4740-979f-2e30c257d2b2.png)

Configuración del servidor: 
Como se detalló usamos la librería de Flask, que nos dará una URL de activación para la plataforma. 
Esta dirección es la dirección ip host de nuestro Raspberry pi al cual se le adiciona “80” porque ese será el puerto que usaremos para el servidor.Como se ve en la imagen:

Figura 2 
Código correspondiente a la configuración del servidor Flask. 
![image](https://user-images.githubusercontent.com/85809354/156904952-f343e06b-2b9a-46da-a930-ed59273c9da9.png)

### 2.2 Configuración de los GPIOs del RPI a través del setup en Python. Para la primera parte de la configuración de los GPIOs usaremos el orden descrito anteriormente, sumado a esto la librería de python específica para control de los GPIOs. Asi pues se tiene la siguiente codificación

Figura 3 
Código correspondiente a la configuración del servidor Flask. 
![image](https://user-images.githubusercontent.com/85809354/156904959-55173214-ca6f-46a9-a828-dcef72054871.png)

### 2.3 Actualización y reparación de los errores que podrían surgir en el entorno. 
Algunos de los errores surgidos derivan de la función de video en el código de python, puesto que al definir la variable “camera” ,que es la que recoge las imágenes de la cámara como resultado, se generaba un error con respecto al bus de uso del dispositivo. Esto es un error de la librería opencv en complemento con el raspberry. Se revisó este error en un foro de ayuda de programación en python/raspberry.Concluyendo así la solución implementada donde cada uno de las funciones que corresponden al uso del código para el video, definieron a la variable “camera” en su primera línea de código. 

### 2.4 Evaluación del protocolo de comunicación que requiera el servidor. 
Evaluamos la comunicación de la interfaz gráfica con las funciones actuadores de los gpio , las cuales se propagaron en la red local a través del servidor de flask.Esta comunicación de las salidas y acciones hechas desde el arranque de la interfaz , son cambios de estados que responden a los buses GPIO del raspberry, que al activarse, se comunican con la tarjeta FPGA. Para lograr esta comunicación se generó el cambio de estados en el código el cual reacciona a la modificación de nuestro archivo principal de html donde cada cambio corresponde a un direccionamiento del url que corre en el servidor de Flask. Esto se ilustra en la parte siguiente del código:

Figura 4 
Código para la acción de los estados de los GPIOs
![image](https://user-images.githubusercontent.com/85809354/156904974-70fd278b-fbce-4a73-8c80-2e53d298175b.png)

### 2.5 Puesta en marcha de la comunicación del hardware con la interfaz gráfica. 
En este parte podemos observar cómo al modificar los estados correspondientes a los GPIOs del raspberry en la interfaz gráfica habilitada en el servidor , este responde con un cambio físico en el circuito , manifestando la comunicación generada por la instancia de código correspondiente a los actuadores de GPIO y su consecuente cambio de voltaje que habilitará los led del ejemplo de la siguiente imagen:

Figura 5 
Cambio de estado del led por activación de un gpio del Raspberry 
![image](https://user-images.githubusercontent.com/85809354/156904976-1d3931d0-6112-49eb-b72a-caefd7336899.png)

### 2.6 Ejecución de las aplicaciones desde el sistema embebido. 
Ejecutamos la aplicación completa en el raspberry dentro de una red Lan hogar simple y probamos su funcionamiento. Comprobamos la ejecución del servidor mediante el comando de arranque de la interfaz en Raspbian. 

Figura 6 
Ejecutando el proyecto con nombre app.py en el command window de Raspbian
![image](https://user-images.githubusercontent.com/85809354/156904982-bd9dda0f-4774-4b39-bb01-020209b85463.png)

Al arrancar podemos visualizar la dirección en la cual nuestro proyecto está ejecutándose dentro de la LAN , esto viene derivado de la configuración del servidor en python. Una vez ejecutado el archivo python , procedemos a copiar esta dirección en el navegador que tengamos disponible y tendremos acceso a la interfaz gráfica. 

Figura 7 
Acceso a la interfaz gráfica mediante la dirección web. 
![image](https://user-images.githubusercontent.com/85809354/156904989-1c524f9d-146e-40d3-952b-f98a07bbcf83.png)

Ahora observamos la interfaz y como primer componente observable tenemos el video en vivo de la tarjeta FPGA , el cual se llega a monitorear los cambios hechos en los botones y switches en la tarjeta .


Figura 8 
Interfaz Gráfica de laboratorio remoto 
![image](https://user-images.githubusercontent.com/85809354/156905032-3abedba8-7d1b-4441-848c-07016f0a8969.png)

Abajo de esta tenemos los botones que corresponden a los botones que se usarán en la tarjeta FPGA , y se visualiza el estado de cada uno de estos. 
Para verificar su funcionamiento probamos el cambio de estado de uno de estos, de encendido a apagado y viceversa.


