import unittest
from polygon import Polygon
from polygon import Polygons

import math
"""
    LESSONS LEARNED:
        - float comparision uses math.isclose instead equals
        - 

"""

class PolygonTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_polygon(self):
        rel_tol = 0.001
        abs_tol = 0.001

        n = 3
        R = 1
        p = Polygon(n, R)

        self.assertEqual(p.count_vertices, n, (f'actual: {p.count_vertices}', f'expected: {n}'))
        self.assertEqual(p.circumradius, R, (f'actual: {p.circumradius}', f'expected: {R}'))
        self.assertEqual(p.interior_angle, 60)
        self.assertTrue(math.isclose(p.side_length, 1.732, rel_tol=rel_tol, abs_tol=abs_tol), 
            (f'actual: {p.apothem}', 'expected: 1.732'))
        self.assertTrue(math.isclose(p.apothem, 0.5, rel_tol=rel_tol, abs_tol=abs_tol), 
            (f'actual: {p.apothem}', 'expected: 0.5')
        )
        self.assertTrue(math.isclose(p.area, 1.299, rel_tol=rel_tol, abs_tol=abs_tol), 
            (f'actual: {p.apothem}', 'expected: 1.299')
        )
        self.assertTrue(math.isclose(p.perimeter, 5.196, rel_tol=rel_tol, abs_tol=abs_tol), 
            (f'actual: {p.apothem}', 'expected: 5.196')
        )
        self.assertEqual(str(p), 'Polygon(n=3, R=1)', f'actual: {str(p)}')

    def test_equals(self):
        p1 = Polygon(3, 1)
        p2 = Polygon(3, 1)
        self.assertEqual(p1, p2)

    def test_not_equals(self):
        p1 = Polygon(3, 1)
        p2 = Polygon(4, 2)
        self.assertNotEqual(p1, p2)

    def test_greater_than(self):
        p1 = Polygon(4, 1)
        p2 = Polygon(3, 2)
        self.assertGreater(p1, p2)

    def test_mininmal_vertices(self):
        with self.assertRaises(Exception, msg="The minimum vertices to form a polygon is 3"):
            p = Polygon(2, 1)

    def test_mininmal_circumradius(self):
        with self.assertRaises(Exception, msg="The circumradius must be a positive number"):
            p = Polygon(3, 0)

        with self.assertRaises(Exception, msg="The circumradius must be a positive number"):
            p = Polygon(3, -1)


class PolygonsTestCase(unittest.TestCase):
    def test_polygons(self):
        max_n = 10
        polygons = Polygons(max_n, 1)

        self.assertEqual(len(polygons), max_n-2)
        self.assertEqual(str(polygons), f'Polygons(max_n={max_n}, R=1)')

        for i in range(max_n-2):
            self.assertEqual(polygons[i], Polygon(i+3, 1))

        self.assertEqual(polygons[2:5], [Polygon(i, 1) for i in range(5, 8)])
        self.assertEqual(polygons.max_efficiency_polygon, Polygon(10, 1)), 

    def test_max_efficincy_polygon(self):
        polygons = Polygons(500, 1)
        self.assertEqual(polygons.max_efficiency_polygon, Polygon(500, 1))
        self.assertTrue(math.isclose(polygons.max_efficiency_polygon.area, math.pi, rel_tol=0.001, abs_tol=0.001, ))
if __name__ == '__main__':
    unittest.main()