"""Basic unit test for lambdata package"""

import unittest
import pandas as pd
import numpy as np

from example_module import MyDataFrame

class MyDataFrameTests(unittest.TestCase):
  """Tests for usage of MyDataFrame class"""
  def setUp(self):
    self.df1 = MyDataFrame({'State': ['Hawaii', 'California', 'Texas', 'new york']})
    self.df2 = MyDataFrame({'LOCATION': ['NEVADA', 'WYOMING', 'JAPAN', 'FLORIDA']})
    self.df3 = MyDataFrame({'place': ['american samoa', 'guam', 'idaho', 'utah']})
    

    self.df1a = self.df1.state_abb('State')
    self.df1b = self.df2.state_abb('LOCATION')
    self.df1c = self.df3.state_abb('place')
    
  
  def test_abb_column(self):
    """Testing the state_abb method"""
    self.assertEqual(self.df1a['state_abbreviation'].to_list(), ['HI', 'CA', 'TX', 'NY'])
    self.assertEqual(self.df1b['state_abbreviation'].to_list(), ['NV', 'WY', np.nan, 'FL'])
    self.assertEqual(self.df1c['state_abbreviation'].to_list(), ['AS', 'GU', 'ID', 'UT'])
    

if __name__ == "__main__":
  unittest.main()


