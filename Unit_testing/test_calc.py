import unittest
import calc

# deocumentation: https://www.youtube.com/redirect?q=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funittest.html%23unittest.TestCase.debug&redir_token=QUFFLUhqbGpHTjZrWkt1SjZMY1RZVEVBX2dHcGxIS0RZQXxBQ3Jtc0trdmFXLWE2V2ZsTDh1RDlHTE9lNXAzd1hLUW42RzdIRURDQWRIUXBKNkdzblBYQXFmRS1VLXdpWWo5NGJyVlVZaFROWklWVTJEVVhKb1J4OXlvRF9kVXdMTng1dm9FZEY0aGxVVi1FRjc0ZnZTNndqTQ%3D%3D&v=6tNS--WetLI&event=video_description
# python -m unittest -v test_calc.py
# tests should be isolated and independent of each other
# test-driven development -> write test first and then write code that does what the test does
class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # once before everything
        print('setupClass')

    @classmethod
    def tearDownClass(cls): # once after everything
        print('tearDownClass')

    def setUp(self): # start of every test (function with name starting with "test")
        print('setup')

    def tearDown(self): # end of every test
        print('teardown')

    def test_add(self): # must start with test
        print(1)
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
    def test_subtract(self): # must start with test
        print(2)
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-1, 1),-2)
        self.assertEqual(calc.subtract(-1, -1), 0)
    def test_multiply(self): # must start with test
        print(3)
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
    def test_divide(self): # must start with test
        print(4)
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5) # catch floor division specifically

        with self.assertRaises(ValueError):
            calc.divide(0,0)

if __name__ == '__main__':
    unittest.main() # so that we can run this file in the terminal by just : python test_calc.py





