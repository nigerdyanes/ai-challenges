# Gestión de Libros en una Biblioteca

Este proyecto implementa una clase `Book` en Python para gestionar libros en una biblioteca. La clase `Book` permite realizar operaciones como prestar libros, devolver libros, verificar la disponibilidad de libros, entre otras.

## Características

- **Constructor:** La clase tiene un constructor que acepta varios parámetros para inicializar un libro, como título, autor, ISBN, cantidad disponible y cantidad prestada.
- **Propiedad de clase:** La clase tiene una propiedad de clase para llevar el conteo del número total de libros creados.
- **Método de clase:** La clase tiene un método de clase para obtener el número total de libros prestados en la biblioteca.
- **Método estático:** La clase tiene un método estático para validar el formato del ISBN.
- **Métodos mágicos:** La clase implementa varios métodos mágicos, como `__str__`, `__del__` y `__eq__`.
- **Gestión de contenedores:** La clase permite prestar y devolver libros, manteniendo un registro adecuado de la cantidad disponible y prestada.

## Uso

```python
# Crear una instancia de Book
book1 = Book("Python for Beginners", "John Smith", "978-1-23456-789-0", 10, 2)

# Prestar un libro
book1.lend_book(1)

# Devolver un libro
book1.return_book(1)

# Verificar disponibilidad
print(book1.available)

```

## Contribuciones

Las contribuciones son bienvenidas. Siéntase libre de enviar sugerencias, mejoras o informes de errores.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo LICENSE para obtener más detalles.

---

Creado por Niger Yanes
