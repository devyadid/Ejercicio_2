# Definimos la clase Libro con sus atributos: título, autor y número de páginas
class Libro:
    def __init__(self, titulo, autor, num_paginas):
        """Constructor de la clase Libro que inicializa los atributos."""
        self.titulo = titulo  # Guarda el título del libro
        self.autor = autor    # Guarda el nombre del autor
        self.num_paginas = num_paginas  # Guarda el número de páginas

    def obtener_num_paginas(self):
        """Método que devuelve el número de páginas del libro."""
        return self.num_paginas

# Creamos un objeto de la clase Libro con valores de ejemplo
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)

# Mostramos el número de páginas del libro usando el método correspondiente
print(f"El libro '{libro1.titulo}' tiene {libro1.obtener_num_paginas()} páginas.")
