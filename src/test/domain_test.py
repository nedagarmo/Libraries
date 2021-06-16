from ..domain.models import Book


def test_create_new_book_instance():
    data = {
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
        "book_description": "Increased focus on JavaScript performance has resulted in vast performance improvements "
                            "for many benchmarks. However, for actual code used in websites, the attained improvements "
                            "often lag far behind those for popular benchmarks.\r\n\r\nThis paper shows that the main "
                            "reason behind this shortfall is how the compiler understands types. JavaScript has no "
                            "concept of types, but the compiler assigns types to objects anyway for ease of code "
                            "generation. We examine the way that the Chrome V8 compiler defines types, and identify "
                            "two design decisions that are the main reasons for the lack of improvement: the inherited"
                            " prototype object is part of the current object&rsquo;s type definition, and method "
                            "bindings are also part of the type definition. These requirements make types very "
                            "unpredictable, which hinders type specialization by the compiler. Hence, we modify V8 "
                            "to remove these requirements, and use it to compile the JavaScript code assembled by "
                            "JSBench from real websites. On average, we reduce the execution time of JSBench by 36%, "
                            "and the dynamic instruction count by 49%.",
        "book_editor": "University of Illinois",
        "book_external_id": None,
        "book_id": None,
        "book_image": "http://collection.openlibra.com.s3.amazonaws.com/covers/2014/07/Improving-Javascript-"
                      "Performance-by-Deconstructing-theType-System-OpenLibra-110x153.gif",
        "book_name": "Improving JavaScript Performance by Deconstructing the Type System",
        "book_publication_date": "2014",
        "book_source": "Etnassoft",
        "book_subtitle": "Subtítulo elegido"
    }
    book = Book(**data, book_action='C')
    assert book.id is not None and book.id != data['book_id']
