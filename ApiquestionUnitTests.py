import unittest
import apiquestion

class TestApiquestion(unittest.TestCase):
    def test_generate_temp_from_place(self):
        result = apiquestion.generate_temp_from_place("Amsterda")
        self.assertEqual(result, "Please enter a valid city name!")
        result2 = apiquestion.generate_temp_from_place("Berli")
        self.assertEqual(result2, "Please enter a valid city name!")
        result3 = apiquestion.generate_temp_from_place("   ")
        self.assertEqual(result3, "Please enter a valid city name!")
        result4 = apiquestion.generate_temp_from_place("aaaaa")
        self.assertEqual(result4, "Please enter a valid city name!")
    def test_process_input(self):
        test = apiquestion.process_input("New York")
        self.assertEqual(test, "New%20york")
        test2 = apiquestion.process_input("newyork")
        self.assertEqual(test2, "Newyork")
        test3 = apiquestion.process_input("lONdOn")
        self.assertEqual(test3,"London")

if __name__ == "__main__":
    unittest.main()


