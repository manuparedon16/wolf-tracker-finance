# Wolf Tracker -  Notas/Setup

Lo primero que hice fue conectar el proyecto con **GitHub** para llevar un control de versiones y que la gente interesada pueda consultar mi código para ver el trabajo realizado.

1. ### Notas de GitHub
Ya instalado git checamos la versión con git --version (Comando git y los dos guiones hacen referencia a una opción, igual podemos hacer que la opción aparezca de manera abreviada como -v en vez de --version). Además iniciamos sesión con nuestro usuario y el comando git config --global user.name "user" y con git config --global user.email "email".

Es necesario también hacer un .gitignore para decirle a GitHub que cosas debe ignorar y no subir al repo, como estas notas jeje. Igual con el venv, no es necesario subir todo eso ya que es como "mandar toda tu casa" para que la vean.

- Hacemos el git init para inicializar un repo
- Luego git add . si quieremos agregar todo
- Después un git commit -m "nombre del commit" para hacer el primer commit que es como un bloque que guarda cambios en el proyecto
- Un git status para ver las ramas y donde están todos los cambios.
-  git remote add origin https://github.com/manuparedon16/wolf-tracker-finance.git
- git branch -M main (seleccionar la rama que queremos)
- git push -u origin main (push hacia la rama elegida)

Esto sirvió como primer configuración pero para seguir avanzando únicamente puedo utilizar estas 3 líneas:
- git add .
- git commit -m "qué hice"
- git push

2. ### Configuración de entorno virtual
El entorno lo usamos como caja que engloba todo lo que necesita cada proyecto sin ensuciar lo global. Primero checamos que estemos en la ruta del proyecto correcta y corremos el comando en la terminal: python -m venv venv para que se cree el entorno. Justo después de hacer eso, colocamos el comando .\venv\Scripts\Activate para activarlo.

Pasó un error que descargué con pip las librerías que tenía que utilizar pero en el momento de llamar yfinance no aparecía como si hubiera sido descargada y era porque no tenía seleccionado el intérprete del venv de python, para ello tuve que hacer:
- Ctrl + Shift + P
- Opción - Python: Select Interpreter
- Colocar en la terminal pip -V para ver la ruta del venv en donde se había creado
- Como no me daba la ruta del venv que había creado tuve que colocar la ruta: wolf-tracker\venv\Scripts\python.exe en la opción de "Enter interpreter path"

También, cuando trabajo con notebook y necesito seleccionar el kernel del venv de python:
- pip install ipykernel (si no está instalado y no aparece como kernel de python)
- Registraremos el bash directamente python -m ipykernel install --user --name=wolf-tracker
- Ctrl + Shift + P → Developer: Reload Window para cargar de nuevo todo y que aparezca, esperar un poco

3. ### Definir el objetivo del proyecto
Lo primero es que quise hacer este proyecto porque con el dinero que gano quiero ver en que mercados globales y nacionales es mejor invertir mi dinero, por ello haré un dashboard y análisis de ciertos datos que me ayudarán a darme cuenta día con día como es que va cambiando el mercado y de que manera puedo decidir en qué meter mi dinero real.