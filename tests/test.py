import unittest
from format_name import get_formatted_name

class NameTestCase:
    
    def test_formatted_name(self):
        formatted_name = get_formatted_name('eugene', 'masaka')
        self.assertEqual(formatted_name, 'Eugene Masaka')
        
    if __name__ == '__main__':
        unittest.main()
        
