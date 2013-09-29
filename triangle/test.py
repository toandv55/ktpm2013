from triangle import detect_triangle
import unittest
class TestTriangle(unittest.TestCase):
    # tests for checking input type 
    def test_input_1(self):
        self.assertEquals(detect_triangle("string", 2, 2), "Invalid input type", "input type 1 failed")
    def test_input_type_2(self):
        self.assertEquals(detect_triangle(2, "string", 2), "Invalid input type", "input type 2 failed")
    def test_input_type_3(self):
        self.assertEquals(detect_triangle(2, 2, "string"), "Invalid input type", "input type 3 failed")
    def test_input_type_4(self):
        self.assertEquals(detect_triangle("string", "string", "string"), "Invalid input type", "input type 4 failed")
    def test_input_type_5(self):
        self.assertEquals(detect_triangle("string", "string", 2), "Invalid input type", "input type 5 failed")
    def test_input_type_6(self):
        self.assertEquals(detect_triangle("string", 2, "string"), "Invalid input type", "input type 6 failed")
    def test_input_type_7(self):
        self.assertEquals(detect_triangle(2, "string", "string"), "Invalid input type", "input type 7 failed")
    # check input value range
    def test_input_value_1(self):
        self.assertEquals(detect_triangle(-1, 2, 2), "Invalid value range", "input value 1 failed")
    def test_input_value_2(self):
        self.assertEquals(detect_triangle(2, -1, 2), "Invalid value range", "input value 2 failed") 
    def test_input_value_3(self):
        self.assertEquals(detect_triangle(2, 2, -1), "Invalid value range", "input value 3 failed")
    def test_input_value_4(self):
        self.assertEquals(detect_triangle(-1, -1, -1), "Invalid value range", "input value 4 failed")
    def test_input_value_5(self):
        self.assertEquals(detect_triangle(-1, -1, 1), "Invalid value range", "input value 5 failed")
    def test_input_value_6(self):
        self.assertEquals(detect_triangle(-1, 1, -1), "Invalid value range", "input value 6 failed")    
    def test_input_value_7(self):
        self.assertEquals(detect_triangle(1, -1, -1), "Invalid value range", "input value 7 failed")
    # check if this is a triangle
    def test_is_triangular_1(self):
        self.assertEquals(detect_triangle(1, 2, 3), "Not a triangle", "is triangular 1 failed")
    def test_is_triangular_2(self):
        self.assertEquals(detect_triangle('1', '2', '3'), "Not a triangle", "is triangular 2 failed")
    def test_is_triangular_3(self):
        self.assertEquals(detect_triangle("1", "2", "3"), "Not a triangle", "is triangular 3 failed")
    def test_is_triangular_4(self):
        self.assertEquals(detect_triangle(3, 2, 1), "Not a triangle", "is triangular 4 failed")
    def test_is_triangular_5(self):
        self.assertEquals(detect_triangle('3', '2', '1'), "Not a triangle", "is triangular 5 failed")
    def test_is_triangular_6(self):
        self.assertEquals(detect_triangle("3", "2", "1"), "Not a triangle", "is triangular 5 failed")
    def test_is_triangular_7(self):
        self.assertEquals(detect_triangle(2, 1, 3), "Not a triangle", "is triangular 7 failed")
    def test_is_triangular_8(self):
        self.assertEquals(detect_triangle(2, 3, 1), "Not a triangle", "is triangular 8 failed")
    def test_is_triangular_9(self):
        self.assertEquals(detect_triangle(1, 3, 2), "Not a triangle", "is triangular 9 failed")
    def test_is_triangular_10(self):
        self.assertEquals(detect_triangle(2, 3, 1), "Not a triangle", "is triangular 10 failed")
       
    # tests for checking type - Normal triangle
    def test_triangle_type_1(self):
        self.assertEquals(detect_triangle(2, 3, 4), "Normal triangle", "triangle type 1 failed")
    def test_triangle_type_2(self):
        self.assertEquals(detect_triangle(2, 4, 3), "Normal triangle", "triangle type 2 failed")
    def test_triangle_type_3(self):
        self.assertEquals(detect_triangle(3, 2, 4), "Normal triangle", "triangle type 3 failed")
    def test_triangle_type_4(self):
        self.assertEquals(detect_triangle(2, 4, 3), "Normal triangle", "triangle type 4 failed")
    def test_triangle_type_5(self):
        self.assertEquals(detect_triangle(4, 3, 2), "Normal triangle", "triangle type 5 failed")
    def test_triangle_type_6(self):
        self.assertEquals(detect_triangle(4, 2, 3), "Normal triangle", "triangle type 6 failed")
    # Tests for Isosceles triangle
    def test_triangle_type_7(self):
        self.assertEquals(detect_triangle(2, 2, 3.5), "Isosceles triangle", "triangle type 7 failed")
    def test_triangle_type_8(self):
        self.assertEquals(detect_triangle(2, 3, 3), "Isosceles triangle", "triangle type 8 failed")
    def test_triangle_type_9(self):
        self.assertEquals(detect_triangle('2', '2', '3'), "Isosceles triangle", "triangle type 9 failed")
    def test_triangle_type_10(self):
        self.assertEquals(detect_triangle('2', '2', "3"), "Isosceles triangle", "triangle type 10 failed")
    # Tests for Isosceles and right triangle
    def test_triangle_type_11(self):
        self.assertEquals(detect_triangle(2, 2, 8**0.5), "Isosceles and Right triangle", "triangle type 11 failed")
    def test_triangle_type_12(self):
        self.assertEquals(detect_triangle(2, 8**0.5, 2), "Isosceles and Right triangle", "triangle type 12 failed")
    def test_triangle_type_13(self):
        self.assertEquals(detect_triangle(8**0.5, 2, 2), "Isosceles and Right triangle", "triangle type 13 failed")
    # Tests for right triangle
    def test_triangle_type_14(self):
        self.assertEquals(detect_triangle(2, 3, 13**0.5), "Right triangle", "triangle type 14 failed")
    def test_triangle_type_15(self):
        self.assertEquals(detect_triangle(2, 13**0.5, 3), "Right triangle", "triangle type 15 failed")
    def test_triangle_type_16(self):
        self.assertEquals(detect_triangle(13**0.5, 2, 3), "Right triangle", "triangle type 16 failed")
    # tests for Equilateral triangle
    def test_triangle_type_17(self):
        self.assertEquals(detect_triangle(3, 3, 3), "Equilateral triangle", "triangle type 17 failed")
    def test_triangle_type_18(self):
        self.assertEquals(detect_triangle("3", "3", "3"), "Equilateral triangle", "triangle type 18 failed")
    def test_triangle_type_19(self):
        self.assertEquals(detect_triangle('3', '3', '3'), "Equilateral triangle", "triangle type 19 failed")
    # Test boundaries
    def test_boundary_1(self):
        self.assertEquals(detect_triangle(0, 0, 0), "Invalid value range", "boundary 1 failed")
    def test_boundary_2(self):
        self.assertEquals(detect_triangle(0, 1, 1), "Invalid value range", "boundary 2 failed")
    def test_boundary_3(self):
        self.assertEquals(detect_triangle(0, 1, 0), "Invalid value range", "boundary 3 failed")
    def test_boundary_4(self):
        self.assertEquals(detect_triangle(1, 0, 0), "Invalid value range", "boundary 4 failed")
    def test_boundary_5(self):
        self.assertEquals(detect_triangle(1, 1, 0), "Invalid value range", "boundary 5 failed")
    def test_boundary_6(self):
        self.assertEquals(detect_triangle(1, 0, 1), "Invalid value range", "boundary 6 failed")
    def test_boundary_7(self):
        self.assertEquals(detect_triangle(-2**32 + 1, -2**32 + 1, -2**32 + 1), "Invalid value range", "boundary 7 failed")
    def test_boundary_8(self):
        self.assertEquals(detect_triangle(2**32 - 1, 2**32 - 1, 2**32 - 1), "Equilateral triangle", "boundary 8 failed")
    
if __name__ == '__main__':
    unittest.main()
    
    
    