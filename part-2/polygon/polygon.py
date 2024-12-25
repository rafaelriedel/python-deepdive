"""
    Background info
        - n edges (=n vertices)
        - R circumradius
        interior angle = (n-2)*180/n
        edge length: s = 2*R*sin(pi/n) -> math.sin
        apothem: a = R * cos(pi/n)
        area = 1/2 * n * s * a
        perimeter = n*s

    GOAL 1:
        Create a polygon class
        initializer
            - number of edges/vertices
            - circumradius

        properties
            - # edges
            - # vertices
            - interior angle
            - apothem
            - area
            - perimeter

        functionality
            - a proper representation __repr__
            - implements equality == base on # vertices circumradius __eq__
            - implements > bases on number of vertices only __gt__

    GOAL 2:
        Implement a Polygons sequence type
        - initializer
            - number of vertices for the largets polygons in the sequence
            - commomn circumradius for all polygons

        properties
            - max efficiency polygon: returns the polugon with the highest area:periment ratio

        functionality
            - functions as a sequence type __getitem__
            - suports the len() function __len__
"""

"""
LESSONS LEARNED
    - uses property instead attribute:
            @property    
            def count_vertices(self):
                return self._n
    - perform calculation on the property instead of __init__
        @property
        def side_length(self):
            return 2 * self._R * math.sin(math.pi / self._n)
"""

import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise Exception("The minimum n to form a polygon is 3")

        if R <= 0:
            raise Exception("The R must be a positive number")

        self._n = n
        self._R = R

    @property    
    def count_vertices(self):
        return self._n

    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)

    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)

    @property
    def area(self):
        return self._n /2 * self.side_length * self.apothem

    @property
    def perimeter(self):
        return self._n * self.side_length

    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_vertices == other.count_vertices 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self._n > other.count_vertices
        else:
            return NotImplemented



class Polygons:
    def __init__(self, max_n, R):
        if max_n < 3:
            raise ValueError("max_n must be greater than 3")

        self._max_n = max_n
        self._R = R

        self._polygons = [Polygon(i, R) for i in range(3, self._max_n+1)]

    def __len__(self):
        return self._max_n - 2

    def __repr__(self):
        return f'Polygons(max_n={self._max_n}, R={self._R})'

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, key=lambda p: p.area / p.perimeter, reverse=True)
        return sorted_polygons[0]


if __name__ == '__main__':
    p = Polygons(10, 1)
    print(len(p))
    print(p[0])
    print(p[7])
    print(p[2:5])