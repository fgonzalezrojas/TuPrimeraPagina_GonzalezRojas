# ENTREGA FINAL

Comisión: 84990
Profesor: BARRACO Mariano
Adjunto: DZIUMA Nicolas
Alumno: GONZALEZ ROJAS Fernando

Link acceso al video: https://drive.google.com/drive/folders/1QWMZljNCrh7Pe1YFsrbK_ap-MXXQ_TCC?usp=sharing



*** BARRICA DE ROBLE ***

Barrica de Roble es un sitio web creado, en esta etapa, para brindar informacion acerca de bebidas alcoholicas de alta gama. En un futuro, luego de aplicadas las funcionalidades y modificaiones necesarias, será un sitio de compra-venta.

Funcionamiento del sitio web

1- Hacer correr el servidor mediante el comando python manage.py runserver.

2- Acceder al sitio web de Barrica de Roble a traves de cualquiera de estos 5 urls:
    - http://127.0.0.1:8000 (pagina de incio/ bienvenida);
    - http://127.0.0.1:8000/vinoteca/home (pagina de incio/ bienvenida);
    - http://127.0.0.1:8000/vinoteca/vino (muestra todos los vinos almacenados en la base de datos del sitio);
    - http://127.0.0.1:8000/vinoteca/whisky (muestra todos los whiskys almacenados en la base de datos del sitio);
    - http://127.0.0.1:8000/vinoteca/champagne (muestra todos los champagnes almacenados en la base de datos del sitio).

4- El sitio cuenta 6 secciones principales:
    - "INICIO";
    - "VINO";
    - "WHISKY";
    - "CHAMPAGNE";
    - "BUSCAR" (que, a traves de un buscador, permite encontrar los productos disponibles utilizando como atributo de busqueda la etiqueta); y
    - "ADMINISTRACIÓN" (unicamente visible para usuarios que hayan iniciado sesion, disponible en el panel de navegacion lateral).

5- "ADMINISTRACIÓN", nos conduce a:
    - "PROVEEDORES" (contiene el link a los formulario de alta de proveedores - ingresando aquí y completando los campos, creamos los objetos del modelo "VinotecaProveedor" - y al listado de proveedores creados - desde donde podemos ver los datos en detalle, editarlos o borrar el registro -);
    - "PRODUCTOS" (tiene el acceso a los formulario de alta de prodcutos - ingresando aquí y completando los campos, creamos los objetos del modelo "VinotecaProducto" - y al listado de productos dados de alta - desde donde podemos ver los datos en detalle, editarlos o borrar el registro -);
    - "CLIENTES" (tiene el hipervinculo al formulario de alta de clientes - ingresando aquí y completando los campos, creamos los objetos del modelo "VinotecaCliente" - y al listado de clientes  - desde donde podemos ver los datos en detalle, editarlos o borrar el registro -).

6- PANEL DE NAVEGACIÓN LATERAL. Si el ususario ingresa mediante su cuenta y clave, visualizará las seciones "PROVEEDORES", "PRODUCTOS" y "CLIENTES", con sus respectivos links a los formularios de alta y a los listados. 

7- "INICIO". Si el ususario ingresa mediante su cuenta y clave, podrá ingresar al panel de edicion de peril donde tendrá la posibilidad de actualizar su nombre, apellido, direccion de correo electronico y su avatar.

8- Para deneter el servidor presionamos "ctrl + c" en la terminal.
