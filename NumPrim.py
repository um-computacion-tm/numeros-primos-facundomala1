import unittest


def is_prime(value):
    
        if value == 1:
    
            return True
    
        if value == 2:
    
            return True
    
        if value == 3:
    
            return True
    
        if value % 2 == 0:
    
            return False
    
        if value % 3 == 0:
            return False
        i = 5
    
        w = 2
        while i * i <= value:
            if value % i == 0:
                return False
            i += w
            w = 6 - w
        return True

class TestPrimos(unittest.TestCase):

    def test_with_1(self):

        result = is_prime(1)

        self.assertTrue(result)

    

    def test_with_2(self):

        result = is_prime(2)

        self.assertTrue(result)

    

    def test_with_3(self):

        result = is_prime(3)

        self.assertTrue(result)

    

    def test_with_4(self):

        result = is_prime(4)

        self.assertFalse(result)

    

    def test_with_5(self):

        result = is_prime(5)

        self.assertTrue(result)



unittest.main()