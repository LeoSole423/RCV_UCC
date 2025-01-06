# RCV_UCC
Proyecto de investigación de Resucitación Cardio Vascular de la Universidad Católica de Córdoba.

## IMPORTANTE
1. Cambiar a la branch DEVELOP para ver instrucciones.
2. NO TRABAJAR SOBRE LA RAMA MAIN. MUEVANSE A DEVELOP Y A PARTIR DE ESTA TRABAJEN.

---

## Procedimiento para empezar un código
1. Abrir una terminal en alguna carpeta a elección y clonar el repositorio:
   ```bash
   git clone https://github.com/LeoSole423/RCV_UCC.git
   ```
2. Dirigirse hacia la branch develop:
   ```bash
   git checkout develop
   ```
3. Crear una branch a partir de la branch develop:
   ```bash
   git branch branch_name
   ```
4. Ingresar a la branch recién creada:
   ```bash
   git checkout branch_name
   ```
5. Una vez en este punto pueden empezar a escribir código o copiarlo en esta carpeta si ya tienen algo en desarrollo.
6. Al terminar de agregar algo tienen que realizar los siguientes comandos:
   ```bash
   git commit -m "Texto informativo"
   git push --set-upstream origin branch_name
   ```
   (Esto solo si es la primera vez que pushean.)

---

## Procedimiento para mejorar código
1. Crear un issue con el problema, ajuste o mejora a implementar en el código.
2. Crear una branch con el comando a partir de la branch develop:
   ```bash
   git branch f/issue-N-title
   ```
   Donde `issue-N-title` haga referencia al issue creado en el paso anterior.
3. Una vez realizados los cambios en el código, al realizar el commit debemos referenciarlo al issue de esta manera:
   ```bash
   git commit -m "REF #(número del issue): Texto sobre commit..."
   ```
4. Una vez hecho el commit, realizar un push:
   ```bash
   git push
   ```

---

## Procedimiento para instalar dependencias y correr el código por primera vez
1. Clonar el repositorio en una carpeta local:
   ```bash
   git clone https://github.com/LeoSole423/RCV_UCC.git
   ```
2. Cambiar a la branch develop:
   ```bash
   git checkout develop
   ```
3. Crear un entorno virtual para aislar las dependencias del proyecto:
   ```bash
   python -m venv venv
   ```
4. Activar el entorno virtual:
   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Instalar las dependencias listadas en el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
6. Verificar que las dependencias se hayan instalado correctamente ejecutando el siguiente comando:
   ```bash
   pip list
   ```
7. Ejecutar el código principal del proyecto:
   ```bash
   python main.py
   ```
