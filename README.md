# IMPORTANTE
# Cambiar a la branch DEVELOP para ver instrucciones

# RCV_UCC
Proyecto de investigacion de Resucitacion Cardio Vascular de la Universidad Catolica de Cordoba.

# IMPORTANTE: NO TRABAJAR SOBRE LA RAMA MAIN. MUEVANSE A DEVELOP Y A PARTIR DE ESTA TRABAJEN.

## Procedimiento para empezar un codigo
1. Abrir una termina en alguna carpeta a eleccion y clonar el repositorio: **git clone https://github.com/LeoSole423/RCV_UCC.git**
2. Dirigirse hacia la branch develop **git checkout develop**
3. Crear una branch a partir de la branch develop: **git branch branch_name**
4. Una vez creada la branch se tienen que ingresar a esa branch **git checkout branch_name**
5. Una vez en este punto pueden empezar a escribir codigo o copiarlo en esta carpeta si ya tienen algo en desarrollo
6. Al terminar de agregar algo tienen que realizar los siguientes comandos:
    ```bash
    git status //Para ver los cambios realizados en el repositorio.
    git add . //Para agregar todos los cambios realizados en el repositorio al commit.
    git commit -m "Texto informativo" //Genera el commit y le agrega un texto descriptivo de este.
    git push --set-upstream origin branch_name //Envia todos los cambios al repositorio de GitHub (Esto solo si es la primera vez que pushean)
    ```
7. La siguiente ves que pusheen solo sera **git push**

## Procedimiento para mejorar codigo (Esto todavia no)
1. Crear un issue con el problema, ajuste o mejora a implementar en el codigo.
2. Crear una branch con el comando: **"git branch f/issue-N-title"** a partir de la branch develop donde **issue-N-title** haga referencia al issue creado en el paso anterior.
3. Una vez realizado los cambios en el codigo, al realizar el commit debemos referencialo al issue de esta manera: **git commit -m "REF #(numero del issue): Texto sobre commit..."**
4. Una vez hecho el commit, realizar un **git push**