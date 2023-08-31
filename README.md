# Products-API
 Esta API proporciona endpoints para administrar productos, categorías, subcategorías y marcas. La API está basada en Django y Django Rest Framework.
## Base URL
<https://tu-domino.com/api/v1/>

## Autenticación

La API es gratuita y no requiere autenticación.

## Endpoints

### Productos

#### Listar productos y crear uno nuevo

- **URL:** `/products/`
- **Método:** GET (Listar productos), POST (Crear producto)
- **Descripción:** Este endpoint permite listar todos los productos existentes o crear un nuevo producto.
- **Parámetros de consulta:** Ninguno (para GET)
- **Cuerpo de solicitud:** Datos del producto (para POST)
- **Respuesta exitosa:** Lista de productos (GET), Detalles del producto creado (POST)
- **Códigos de respuesta:** 200 OK (GET), 201 Created (POST)
- **Ejemplo:**
~~~
GET /api/v1/products/
POST /api/v1/products/
~~~

#### Obtener, actualizar y eliminar producto

- **URL:** `/product/{id}/`
- **Método:** GET (Obtener producto), PUT (Actualizar producto), DELETE (Eliminar producto)
- **Descripción:** Este endpoint permite obtener, actualizar o eliminar un producto específico por su ID.
- **Parámetros de consulta:** Ninguno (para GET, PUT y DELETE)
- **Cuerpo de solicitud:** Datos actualizados del producto (para PUT)
- **Respuesta exitosa:** Detalles del producto (GET y PUT), Mensaje de éxito (DELETE)
- **Códigos de respuesta:** 200 OK (GET y PUT), 204 No Content (DELETE)
- **Ejemplo:**
~~~
GET /api/v1/product/{id}/
PUT /api/v1/product/{id}/
DELETE /api/v1/product/{id}/
~~~

### Categorías

#### Obtener todas las categorías

- **URL:** `/categories/`
- **Método:** GET
- **Descripción:** Este endpoint permite obtener todas las categorías existentes.
- **Parámetros de consulta:** Ninguno
- **Respuesta exitosa:** Lista de categorías
- **Códigos de respuesta:** 200 OK
- **Ejemplo:**

~~~
GET /api/v1/categories/
~~~

#### Obtener, actualizar y eliminar categoría

- **URL:** `/category/{id}/`
- **Método:** GET (Obtener categoría), PUT (Actualizar categoría), DELETE (Eliminar categoría)
- **Descripción:** Este endpoint permite obtener, actualizar o eliminar una categoría específica por su ID.
- **Parámetros de consulta:** Ninguno (para GET, PUT y DELETE)
- **Cuerpo de solicitud:** Datos actualizados de la categoría (para PUT)
- **Respuesta exitosa:** Detalles de la categoría (GET y PUT), Mensaje de éxito (DELETE)
- **Códigos de respuesta:** 200 OK (GET y PUT), 204 No Content (DELETE)
- **Ejemplo:**
~~~
GET /api/v1/category/{id}/
PUT /api/v1/category/{id}/
DELETE /api/v1/category/{id}/
~~~

### Subcategorías

#### Obtener todas las subcategorías

- **URL:** `/sub-categories/`
- **Método:** GET
- **Descripción:** Este endpoint permite obtener todas las subcategorías existentes.
- **Parámetros de consulta:** Ninguno
- **Respuesta exitosa:** Lista de subcategorías
- **Códigos de respuesta:** 200 OK
- **Ejemplo:**
~~~
GET /api/v1/sub-categories/
~~~

#### Obtener, actualizar y eliminar subcategoría

- **URL:** `/sub-category/{id}/`
- **Método:** GET (Obtener subcategoría), PUT (Actualizar subcategoría), DELETE (Eliminar subcategoría)
- **Descripción:** Este endpoint permite obtener, actualizar o eliminar una subcategoría específica por su ID.
- **Parámetros de consulta:** Ninguno (para GET, PUT y DELETE)
- **Cuerpo de solicitud:** Datos actualizados de la subcategoría (para PUT)
- **Respuesta exitosa:** Detalles de la subcategoría (GET y PUT), Mensaje de éxito (DELETE)
- **Códigos de respuesta:** 200 OK (GET y PUT), 204 No Content (DELETE)
- **Ejemplo:**
~~~
GET /api/v1/sub-category/{id}/
PUT /api/v1/sub-category/{id}/
DELETE /api/v1/sub-category/{id}/
~~~

#### Filtrar subcategorías por categoría

- **URL:** `/sub-categories/filter/category/{id}/`
- **Método:** GET
- **Descripción:** Este endpoint permite filtrar las subcategorías por el ID de una categoría específica.
- **Parámetros de consulta:** Ninguno
- **Respuesta exitosa:** Lista de subcategorías filtradas por categoría
- **Códigos de respuesta:** 200 OK
- **Ejemplo:**
~~~
GET /api/v1/sub-categories/filter/category/{id}/
~~~

### Marcas

#### Obtener todas las marcas

- **URL:** `/brands/`
- **Método:** GET
- **Descripción:** Este endpoint permite obtener todas las marcas existentes.
- **Parámetros de consulta:** Ninguno
- **Respuesta exitosa:** Lista de marcas
- **Códigos de respuesta:** 200 OK
- **Ejemplo:**

~~~
GET /api/v1/brands/
~~~

#### Obtener marca por ID

- **URL:** `/brand/{id}/`
- **Método:** GET
- **Descripción:** Este endpoint permite obtener una marca específica por su ID.
- **Parámetros de consulta:** Ninguno
- **Respuesta exitosa:** Detalles de la marca
- **Códigos de respuesta:** 200 OK
- **Ejemplo:**
~~~
GET /api/v1/brand/{id}/
~~~
