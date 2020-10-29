"""Basic unit test for lambdata package"""

import unittest

from example_module import COLORS, increment



class SocialMediaUserTests(unittest.TestCase):
    """Tests for usage of Social Media Users in our Social Media"""
    def setup(self):
        self.user1 = SocialMediaUser(name="Jimmy", location="France")
        self.user2 = SocialMediaUser(name="Craig", location="Kenya")

    def test_name(self):
        self.assertEqual(self.user1.name, "Jimmy")
        self.assertEqual(self.user2.name, "Craig")

    # def test_location(self):
    #     """Testing Location attribute"""
    #     self.assertEqual(self.user1.location, "France")
    #     self.assertEqual(self.user2.location, "Kenya")

class ExampleTests(unittest.TestCase):
  """Making sure examples work as expected"""
  def test_increment(self):
    """Testing increment adds one to a number"""
    x0 = 0
    y0 = increment(x0) #y0 == 1
    self.assertEqual(y0, 1)

    x1 = 100
    y1 = increment(x1) # y1 == 101
    self.assertEqual(y1, 101)

    x2 = -1
    y2 = increment(x2) # y2 == 0
    self.assertEqual(y2, 0)

    x3 = -1.5
    y3 = increment(x3) # x3 == -0.5
    self.assertEqual(y3, -0.5)

  def test_colors(self):
    """Testing the presence/absence of members in the colors list"""
    self.assertIn("cyan", COLORS)
    self.assertNotIn("brown", COLORS)

  def test_number_colors(self):
    """Testing that we have the expect number of colors"""  
    self.assertEqual(len(COLORS), 3)
    



if __name__ == "__main__":
    unittest.main()


