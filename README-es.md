:earth_americas:
*[English](README-en.md) ∙ [Español](README-es.md)*

<h1 align="center">Edición de video automatizada basada en audio</h1>

<div align="center">
 :ear::loud_sound::film_strip::scissors:
</div>

<br />

## Descripción

*Nota: Proyecto aún no terminado*

El propósito de este trabajo es proporcionar una solución de edición de video automatizada con el fin de ahorrar trabajo humano para editar videos muy grandes y con ciertos estándares de edición. Para hacer esto, usamos la energía del audio del video para identificar los puntos clave de edición, y cortamos el video original en todos estos puntos clave / de interés y los editamos todos juntos en un solo archivo.

## Sugerencia sobre cómo importar el entorno virtual

Se recomienda encarecidamente cuando se trabaja con proyectos de Python, utilizar desde [entornos virtuales](https://csguide.cs.princeton.edu/software/virtualenv), los entornos virtuales de Python ayudan a desacoplar y aislar las versiones de Python y los paquetes pip asociados. Esto permite a los usuarios finales instalar y administrar su propio conjunto de paquetes que son independientes de los proporcionados por el sistema. Los entornos virtuales le permiten tener un entorno estable, reproducible y portátil. Usted controla qué versiones de paquetes se instalan y cuándo se actualizan.
Hay varias formas de configurar un entorno virtual en Python, aquí enumeraré algunos buenos enlaces que pueden ayudar con esta configuración: [:link:](https://docs.python.org/3/library/venv.html), [:link:](https://realpython.com/lessons/creating-virtual-environment/), [:link:](https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b), [:link:](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

Una vez que se elige el método para crear el entorno virtual, simplemente marque una forma de crear el entorno de acuerdo con el archivo  `requirements.txt`. También enumeraré algunas buenas formas de hacer esto aquí: [:link:](https://developer.akamai.com/blog/2017/06/21/how-building-virtual-python-environment), [:link:](https://gist.github.com/luiscape/19d2d73a8c7b59411a2fb73a697f5ed4), [:link:](https://www.jetbrains.com/help/pycharm/managing-dependencies.html), [:link:](https://www.codegrepper.com/code-examples/python/conda+create+requirements.txt).

Mi recomendación es utilizar el [Anaconda](https://conda.io/projects/conda/en/latest/index.html) realizar la gestión de dependencias y entornos virtualizados, de forma más sencilla. Y sigue estos pasos:

- [Descargar Anaconda](https://www.anaconda.com/products/individual)
- Para crear el medio ambiente [abrir el indicador de anaconda](https://stackoverflow.com/questions/47914980/how-to-access-anaconda-command-prompt-in-windows-10-64-bit/55545141#:~:text=Go%20with%20the%20mouse%20to,%22Anaconda%20Prompt%22%20will%20open.), escribe en la terminal `pip install -r requirements.txt` o si prefiere usar la sintaxis conda `conda create --name <env_name> --file requirements.txt`
- It's interesting to check the [anaconda navigator](https://docs.anaconda.com/anaconda/navigator/getting-started/) si el ambiente fue creado correctamente
- Una vez creado el entorno, debe comprobar cómo trabajar con este entorno dentro del IDE utilizado, aquí hay algunos enlaces que ejemplifican esto: [:link:](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html), [:link:](https://stackoverflow.com/questions/43351596/activating-anaconda-environment-in-vscode), [:link:](https://docs.anaconda.com/anaconda/user-guide/tasks/integration/sublime/)
- Después de seguir este paso a paso, ahora es posible ejecutar el proyecto en un entorno adecuado en el IDE que se prefiera.

## Referencias para manipulación de audio

Las técnicas utilizadas para el tratamiento de audio se basaron en los siguientes materiales:
- [Manejo básico de audio en Python](https://medium.com/behavioral-signals-ai/basic-audio-handling-d4cc9c70d64d)
- [Guía para el procesamiento de señales digitales](https://www.dspguide.com/)




