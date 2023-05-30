## __Instalación__:
`Podemos elegir entre 2 ambientes para llevar a cabo las actividades propuestas con PySpark.`
#### __Usando Google Colab__:  
__Ventaja__: Instalación rápida, usarás recursos de Google por lo tanto no se usarán los recursos de tu computadora, compilaciones más veloces ya que Google Colab nos da aproximadamente 10GB de RAM y GB de Disco.  

__Desventaja__:  Tendrás que instalar el pyspark cada vez que tu sesión termine en Google Colab.  

1.Nos dirigimos a [Google Colab](https://colab.research.google.com).  

2.Crear un nuevo cuaderno haciendo click en `Nuevo Cuaderno`.
![Creando nuevo cuaderno](Imagenes/1.png)  
3.Se abrirá una hoja de trabajo al estipo de Jupiter Notebook.  ´

4.Ejecutamos el comando usando `pip` (**P**ackage **I**nstaller for **P**ython):  
```shell 
pip install pyspark
```  
![Ejecutando pip install](Imagenes/2.png)  
5.Cuando se haya instalado ya podemos usar comandos de PySpark:  
```shell 
from pyspark import SparkContext
```
![Ejecutando comando pyspark](Imagenes/3.png)  
#### __Usando Anaconda__:  
__Ventaja__: No tendrás que volver a instalar pyspark ya que estará en tu sistema local, no dependerás de servicios de terceros.  

__Desventaja__:  Proceso de instalación un poco más tardado, se usarán recursos de tu máquina así que puede que algunas consultas demoren ya que dependerá de la capacidad de tu equipo.  

1.Nos dirigimos a [la página oficial de descarga de Anaconda](https://www.anaconda.com/download).  
 
2.Descargamos e instalamos Anaconda, una vez instalada nos dirigimos a la sección `Environments` y luego a `Create`.
![Descarga e instalación anaconda](Imagenes/4.png)  

3.Creamos un nuevo ambiente de desarrollo al cual llamaremos  `BigData`.  
![Entorno de desarrollo](Imagenes/5.png)  
4.Una vez que Anaconda termine de crear el ambiente de desarrollo nos dirigimos a `Home` e instamos `Jupyter Notebook` y `PowerShell Prompt`  
![Instalando Jupyter y PowerSell](Imagenes/6.png)  
5.Una vez instaladas ambas herramientas Abrimos primero el `PowerShell Prompt` haciendo click en `LAUNCH`.  

6.Una vez en la terminal ejecutamos el comando:
```shell
conda install -c conda-forge pyspark
```  
![Instalando pyspark](Imagenes/7.png) 
Y luego confirmamos con "Y"  

7.Una vez instalado ejecutamos el comando:
```shell
pyspark
```
![PySpark Instalado](Imagenes/8.png) 

8.Abrimos `Jupyter Notebook` dándole a `LAUNCH`, una vez abierto el Jupyter crearemos un archivo similar al cuaderno del google Colab. Para eso primero nos ubicamos en alguna carpeta donde querramos crear nuestros archivos de pruebas. Luego en la parte superior derecha click a `New` y `Python 3 ipykernel`.  
![Entorno Jupyter Notebook](Imagenes/9.png)   
9.Una vez creado el archivo kernel, ya podemos ejecutar dentro el comando:
```shell
from pyspark import SparkContext
```
No debería mostrar ningún error.
![Probando en el archivo ipy](Imagenes/10.png)  

## __TODO LISTO, ¡YA PODEMOS EMPEZAR A CODIFICAR!__
