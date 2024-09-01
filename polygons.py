import math

class Polygon:
    def __init__(self, n, R, length:'how many ploygons'=1):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self.length = length

        # Instance variables that needs computation
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None
        self._interior_angle = None
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def n(self):
        # getter for n
        return self._n

    @n.setter
    def n(self, n):
        """
            Setter for n.
            Additionally it also sets the other attributes listed below to None. To make them lazy evaluator.
            Those will onyly be computed when someone tries to access it.
            - _side_length
        """
        self._n = n
        print("setting other properties that requires computation, to None, to make them lazy evaluator")
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def R(self):
        # getter for R
        return self._R

    @R.setter
    def R(self, r):
        """
            Setter for R.
            Additionally it also sets the other attributes listed below to None. To make them lazy evaluator.
            Those will onyly be computed when someone tries to access it.
            - _side_length
        """
        self._R = r
        print("setting other properties that requires computation, to None, to make them lazy evaluator")
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None
    
    @property
    def count_vertices(self):
        # getter for number of vertices, need not be a lazy evaluator
        return self._n
    
    @property
    def count_edges(self):
        # getter for number of edges, need not be a lazy evaluator
        return self._n
    
    @property
    def circumradius(self):
        # getter for circum radius, need not be a lazy evaluator
        return self._R
    
    @property
    def interior_angle(self):
        """
             getter for interior_angle.
             It's a lazy evaluator, it only gets computed when n or r are resetted or when the instance is created.
             It only gets computed once, when instance is created or this property is accessed.
        """
        if self._interior_angle == None:
            print("Computing interior_angle")
        self._interior_angle = (self._n - 2) * 180 / self._n
        return self._interior_angle

    @property
    def side_length(self):
        """
             getter for side_length.
             It's a lazy evaluator, it only gets computed when n or r are resetted or when the instance is created.
             It only gets computed once, when instance is created or this property is accessed.
        """
        if self._side_length == None:
            print("Computing side_legnth")
            self._side_length = 2 * self._R * math.sin(math.pi / self._n)
        return self._side_length
    
    @property
    def apothem(self):
        """
             getter for apothem.
             It's a lazy evaluator, it only gets computed when n or r are resetted or when the instance is created.
             It only gets computed once, when instance is created or this property is accessed.
        """
        if self._apothem == None:
            print("Computing apothem")
            self._apothem = self._R * math.cos(math.pi / self._n)
        return self._apothem
    
    @property
    def area(self):
        """
             getter for area.
             It's a lazy evaluator, it only gets computed when n or r are resetted or when the instance is created.
             It only gets computed once, when instance is created or this property is accessed.
        """
        if self._area == None:
            print("Computing area")
            self._area = self._n / 2 * self.side_length * self.apothem
        return self._area
    
    @property
    def perimeter(self):
        """
             getter for perimeter.
             It's a lazy evaluator, it only gets computed when n or r are resetted or when the instance is created.
             It only gets computed once, when instance is created or this property is accessed.
        """
        if self._perimeter == None:
            print("Computing perimeter")
            self._perimeter = self._n * self.side_length
        return self._perimeter
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented
    
    # Making Class an iterable
    def __iter__(self):
        return self.PolygonIterator(self, self.length)
        
    class PolygonIterator:
        """
            Inner class that makes the Polygon class an iterable
            Parameter: It expects a Polygon object as a parameter
            Iterator is set to be only consumed once, Once it is iterated it will be exhausted.
        """
        def __init__(self, polygon_obj, sentinel) -> None:
            self.polygon_obj = polygon_obj
            self._index = 0
            self.sentinel = sentinel
            self.is_consumed = False

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.is_consumed:
                raise StopIteration
            else:
                if self._index >= self.sentinel:
                    self.is_consumed = True
                    raise StopIteration
                else:
                    result = self.polygon_obj
                    self._index += 1
                    return result