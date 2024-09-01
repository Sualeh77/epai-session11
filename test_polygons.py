from polygons import Polygon
import math

def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001
    
    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass
                       
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.count_vertices == n, (f'actual: {p.count_vertices},'
                                   f' expected: {n}')
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')
    
    assert math.isclose(p.side_length, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.side_length},'
                                          f' expected: {math.sqrt(2)}')
    
    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
    
    assert math.isclose(p.apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          ' expected: 0.707')
    p = Polygon(6, 2)
    assert math.isclose(p.side_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p = Polygon(12, 3)
    assert math.isclose(p.side_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)
    
    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
def test_polygon_is_iterable():
    polygon = Polygon(3,3,3)
    assert is_iterable(polygon), "object of class Polygon is not iterable"

def test_polygon_iterator_is_exhasustive():
    polygons = Polygon(3,3,3)
    poly_iter = iter(polygons)
    for poly in poly_iter:
        pass
    try:
        next(poly_iter)
    except StopIteration:
        msg = "Iterator is exhausted"
    assert msg == "Iterator is exhausted", "Polygon iterator is not exhaustive"

# Test Case to Verify lazy evaluation and computation only once
def test_polygon_lazy_evaluation():
    p = Polygon(n=5, R=10)
    
    # Accessing the side_length for the first time, should compute and cache the value
    first_computation = p.side_length
    
    # Accessing the side_length again, should return cached value, not recompute
    second_computation = p.side_length
    
    assert first_computation == second_computation, "side_length should be computed only once and cached."

# Test Case to Verify that changing `n` resets computed properties
def test_polygon_property_reset_on_n_change():
    p = Polygon(n=5, R=10)
    
    # Access properties to compute them
    side_length = p.side_length
    area = p.area
    
    # Change n value
    p.n = 6
    
    # Access properties again; should be recomputed
    new_side_length = p.side_length
    new_area = p.area
    
    assert new_side_length is not None and new_side_length != side_length, "side_length should be recomputed after `n` changes."
    assert new_area is not None and new_area!= area, "area should be recomputed after `n` changes."

# Test Case to Verify that changing R resets computed properties
def test_polygon_property_reset_on_R_change():
    p = Polygon(n=5, R=10)
    
    # Access properties to compute them
    side_length = p.side_length
    area = p.area
    
    # Change n value
    p.R = 6
    
    # Access properties again; should be recomputed
    new_side_length = p.side_length
    new_area = p.area
    
    assert new_side_length is not None and new_side_length != side_length, "side_length should be recomputed after `n` changes."
    assert new_area is not None and new_area!= area, "area should be recomputed after `n` changes."