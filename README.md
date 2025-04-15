# TuPrimeraPagina_GonzalezRojas

Comisión: 84990
Profesor: BARRACO Mariano
Adjunto: DZIUMA Nicolas
Alumno: GONZALEZ ROJAS Fernando

*** VINOTECA ***

superuser: vinoteca_admin
email: fernandodgr@hotmail.com
pass: vinoteca@1234

Barrica de Roble es un sitio web creado para la compra-venta de bebidas alcoholicas de alta gama.

Funcionamiento del sitio web

1- Hacer correr el servidor mediante el comando python manage.py runserver.

2- Acceder al sitio web de Barrica de Roble a traves de cualquiera de estos 3 urls:
    - http://127.0.0.1:8000/vinoteca/vino (muestra todos los vinos que se ofrecen en el sitio);
    - http://127.0.0.1:8000/vinoteca/whisky (muestra todos los whiskys que se ofrecen en el sitio - en construcción -);
    - http://127.0.0.1:8000/vinoteca/champagne (muestra todos los champagnes que se ofrecen en el sitio - en construcción -).

4- El sitio cuenta 5 secciones principales:
    - "VINO";
    - "WHISKY";
    - "CHAMPAGNE";
    - "BUSCAR" (que, a traves de un buscador, permite encontrar los productos disponibles utilizando como atributo de busqueda la etiqueta); y
    - "ADMINISTRACIÓN" (unicamente visible desde el panel de navegacion lateral).

5- "ADMINISTRACIÓN", nos conduce a:
    - "PROVEEDORES" (contiene el link al formulario de alta de proveedores - ingresando aquí y completando los campos, creamos los objetos del modelo "VinotecaProveedor" -);
    - "PRODUCTOS" (tiene el acceso al formulario de alta de prodcutos - ingresando aquí y completando los campos, creamos los objetos del modelo "VinotecaProducto" -);
    - "CLIENTES" (tiene el hipervinculo al formulario de alta de clientes - ingresando aquí y completando los campos, creamos los objetos del modelo "VinotecaCliente" -).

6- Para deneter el servidor presionamos "ctrl + c" en la terminal.
