"""
Unit tests for the Concert Itinerary Builder.

This file contains unit tests for the ItineraryBuilder class in main.py.
Participants will implement tests based on the system specifications.
"""

import unittest
from main import Concert, ItineraryBuilder
from concerts_data import get_all_concerts

class ItineraryBuilderTest(unittest.TestCase):
    """Test cases for the ItineraryBuilder class."""
    
    def setUp(self):
        """Set up for the tests."""
        self.builder = ItineraryBuilder()
        
        self.all_concerts = get_all_concerts()
    
    # ----- Manual Test Cases -----
    # Participants will implement their manual test cases here. 
    
    def test_manual_1(self):
        """First manually written test case."""
        # TODO: Implement this test
        pass
    
    # ----- AI-Assisted Test Cases -----
    # Participants will implement their AI-assisted test cases here.
    # Please name your test in a way which indicates that these are AI-assisted test cases.


if __name__ == "__main__":
    unittest.main()