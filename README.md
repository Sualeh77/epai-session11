# epai-session10

# Polygon Class

The `Polygon` class is a Python class that represents a regular polygon. It provides various properties and methods to calculate geometric characteristics such as the number of vertices, number of edges, circumradius, interior angle, side length, apothem, area, and perimeter. Additionally, the class is made iterable by implementing an inner iterator class `PolygonIterator`.

## Features

- **Number of Vertices and Edges**: Returns the number of vertices and edges of the polygon.
- **Circumradius**: Returns the circumradius (radius of the circumscribed circle) of the polygon.
- **Interior Angle**: Calculates and returns the interior angle of the polygon.
- **Side Length**: Calculates and returns the length of each side of the polygon.
- **Apothem**: Calculates and returns the apothem (distance from the center to the midpoint of a side) of the polygon.
- **Area**: Calculates and returns the area of the polygon.
- **Perimeter**: Calculates and returns the perimeter of the polygon.
- **Equality and Comparison**: Supports equality (`==`) and greater than (`>`) comparisons based on the number of vertices and circumradius.
- **Iterable**: The `Polygon` class is iterable, allowing for iteration over its instances.

## Usage

Here's how you can use the `Polygon` class:

```python
from polygon import Polygon

# Creating a polygon instance with 5 vertices and a circumradius of 10
polygon = Polygon(n=5, R=10)

# Accessing properties
print(polygon.count_vertices)  # Output: 5
print(polygon.count_edges)     # Output: 5
print(polygon.circumradius)    # Output: 10
print(polygon.interior_angle)  # Output: 108.0
print(polygon.side_length)     # Output: Calculated side length
print(polygon.apothem)         # Output: Calculated apothem
print(polygon.area)            # Output: Calculated area
print(polygon.perimeter)       # Output: Calculated perimeter

# Equality and comparison
polygon2 = Polygon(n=4, R=10)
print(polygon == polygon2)     # Output: False
print(polygon > polygon2)      # Output: True

# Iterating over a polygon
for poly in polygon:
    print(poly)                # Output: Polygon(n=5, R=10)
```

## Methods and Properties

- **count_vertices**: Getter: Returns the number of vertices (n) of the polygon.
- **count_edges**: Getter: Returns the number of edges (n) of the polygon.
- **circumradius**: Getter: Returns the circumradius (R) of the polygon.
- **interior_angle**: Getter: Lazy evaluater, Calculates and returns the interior angle of the polygon.
- **side_length**: Getter: Lazy evaluater, Calculates and returns the length of a side of the polygon.
- **apothem**: Getter: Lazy evaluater, Calculates and returns the apothem of the polygon.
- **area**: Getter: Lazy evaluater, Calculates and returns the area of the polygon.
- **perimeter**: Getter: Lazy evaluater, Calculates and returns the perimeter of the polygon.
- **__eq__(other)**: Checks if two polygons are equal based on the number of edges and circumradius.
- **__gt__(other)**: Compares two polygons based on the number of vertices.
Iterable Support
- **__iter__(self)**: It makes the class iterable, It calls inner Iterator class with the address of the current object of the Polygon class.

## Iterable
The Polygon class is made iterable by implementing an inner iterator class `PolygonIterator`. This allows iteration over a specified number of polygon instances using a for loop. This iterator is an exhaustive iterator, Once looped over it cant be accessed again.

## Error Handling

If the number of vertices (n) is less than 3, a ValueError is raised during initialization with the message "Polygon must have at least 3 vertices."