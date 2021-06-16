# Libraries
Miniaplicación enfocada en la búsqueda y creación de libros de una biblioteca.  El sistema, no encontrando resultados para la búsqueda del usuario, conecta con el API de Google para llevar a cabo la búsqueda.

_Endpoints:_
```
GET http://ec2-3-14-4-72.us-east-2.compute.amazonaws.com/api/v1/book?query=libros
```
Esta petición GET permite filtrar los libros existentes, o recibir la lista de libros de las APIs públicas
a las que el sistema se encuentra suscrito.

El parámetro _query_ permite enviar el término de búsqueda.

```
POST http://ec2-3-14-4-72.us-east-2.compute.amazonaws.com/api/v1/book

BODY JSON:

{
    "book_authors": [
        "Varios"
    ],
    "book_categories": [
        {
            "category_id": 223,
            "name": "Javascript / AJAX",
            "nicename": "programacion_javascript_ajax"
        },
        {
            "category_id": 220,
            "name": "Programación",
            "nicename": "libros_programacion"
        },
        {
            "category_id": 501,
            "name": "Textos Académicos",
            "nicename": "textos-academicos"
        }
    ],
    "book_description": "Increased focus on JavaScript performance has resulted in vast performance improvements for many benchmarks. However, for actual code used in websites, the attained improvements often lag far behind those for popular benchmarks.\r\n\r\nThis paper shows that the main reason behind this shortfall is how the compiler understands types. JavaScript has no concept of types, but the compiler assigns types to objects anyway for ease of code generation. We examine the way that the Chrome V8 compiler defines types, and identify two design decisions that are the main reasons for the lack of improvement: the inherited prototype object is part of the current object&rsquo;s type definition, and method bindings are also part of the type definition. These requirements make types very unpredictable, which hinders type specialization by the compiler. Hence, we modify V8 to remove these requirements, and use it to compile the JavaScript code assembled by JSBench from real websites. On average, we reduce the execution time of JSBench by 36%, and the dynamic instruction count by 49%.",
    "book_editor": "University of Illinois",
    "book_id": "c4fe18ae-8478-4094-85b3-e18193bdb38e",
    "book_image": "http://collection.openlibra.com.s3.amazonaws.com/covers/2014/07/Improving-Javascript-Performance-by-Deconstructing-theType-System-OpenLibra-110x153.gif",
    "book_name": "Improving JavaScript Performance by Deconstructing the Type System",
    "book_publication_date": "2014",
    "book_source": "Etnassoft"
}
```

Este endpoint nos permite registrar un libro nuevo siempre y cuando no exista en la base de datos del sistema.

## TODO:
- Se espera implementar GraphQL en los endpoints.
- Se espera implementar autenticación mediante JWT

## Oportunidades de mejora
- Se puede implementar el patrón observable para facilitar la escalabilidad en la inclusión de más APIs públicas para buscar libros.
- Es posible optimizar la ejecución del Dockerfile
- Es necesario utilizar algún servidor de aplicaciones para prescindir de _flask run_, pues no es recomendable para ambientes de producción.
- Se puede buscar una mejora en la resiliencia del aplicativo implementando una arquitectura de producción con K8s
- Es conveniente desacoplar el archivo de variables de entorno en un sistema de almacenamiento de _secretos_, de manera que los datos de conexión al dynamodb entre, otras cosas, puedan quedar securizados.