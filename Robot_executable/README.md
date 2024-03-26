# Crear ambiente virtual con Python 3.12.x e instalar librerias
```
- robotframework-seleniumlibrary==7.0
- webdriver-manager==4.0.1
- pandas
- beautifulsoup4==4.12.3
- lxml==5.1.0
- robot==20071211 (me parece que sí se necesita)
```
Igual se agrega file requirements.txt

## Como crear el .exe:

Para crear mi file main.exe, requiero instalar pyinstaller (6.3.0), con python 3.12.2

```
pip install pyinstaller
```
```
pyinstaller --hidden-import=robot.libraries.BuiltIn --hidden-import=robot.libraries.Easter --hidden-import=SeleniumLibrary --hidden-import=webdriver_manager --onefile --add-data "main.robot;." --add-data "Results;Results" --add-data "C:/Users/20023350/Documents/Robotframework/Robot_executable/venv/Lib/site-packages/robot/htmldata;robot/htmldata" main.py
```
or pass -w:
```
pyinstaller --hidden-import=robot.libraries.BuiltIn --hidden-import=robot.libraries.Easter --hidden-import=SeleniumLibrary --hidden-import=webdriver_manager --onefile --add-data "main.robot;." --add-data "Results;Results" --add-data "C:/Users/20023350/Documents/Robotframework/Robot_executable/venv/Lib/site-packages/robot/htmldata;robot/htmldata" -w main.py
```


En donde esta el archivo main.exe copiar el archivo main.robot

Ejecutar el main.exe.

# Docs:
https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#examples-2

https://robot-framework.readthedocs.io/en/master/autodoc/robot.running.html#robot.running.model.TestSuite.from_json

https://github.com/robotframework/QuickStartGuide/blob/master/QuickStart.rst

https://github.com/robotframework/WebDemo/tree/master


## Omitir esto, pues es de primeros pasos previos:

Para crear mi file main.exe, requiero instalar pyinstaller (6.5.0), con python 3.12.2, o tal vez 6.3.0

```
pip install pyinstaller
```
```
pyinstaller --onefile --add-data "main.robot;." --add-data "Results;Results" main.py
```
or use:
```
pyinstaller --onefile --add-data "main.robot;." --add-data "Results;Results" -w main.py
```


En donde esta el archivo main.exe copiar el archivo main.robot
Instalar globalmente en la computadora python 3.12, y ejecutar:

```pip install robotframework-seleniumlibrary```