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
    
    # def test_manual_1(self):
    #     """First manually written test case."""
    #     # TODO: Implement this test
    #     pass
    
    # # test if the lits is sorted chronological order, earliest should come first
    
    # def test_chronological_date(self):
    #     itinerary_builder = self.builder.build_itinerary(self.all_concerts)
        
    #     self.assertGreater(len(itinerary_builder), 0, "Itinerary should not be empty")

    #     get_date = [concert.date for concert in itinerary_builder]
    #     self.assertEqual(get_date, sorted(get_date)) # only check sorting if we have concerts
    
    # # test if only earliest concert per artist is included
    # def test_only_earliest_concert(self):

    #     itinerary_builder = self.builder.build_itinerary(self.all_concerts)
        
    #     # check no artist appears twice
    #     artists = [concert.artist for concert in itinerary_builder]
    #     self.assertEqual(len(artists), len(set(artists)))
        
    #     # if  an artist with multiple concerts, assert that earliest is chosen, example: "Taylor Swift"
    #     multi_concerts = [c for c in self.all_concerts if c.artist == "Taylor Swift"]
    #     earliest = min(multi_concerts, key=lambda x: x.date)
    #     self.assertIn(earliest, itinerary_builder)
    
    # # test No two concerts may take place on the same day
    # def test_same_day_conflict(self):
    #     # create a test case with the same concerts
    #     test_concerts = [
    #         Concert("Artist1", "2025-06-05", "Stockholm", 59.3293, 18.0686),
    #         Concert("Artist2", "2025-06-05", "Copenhagen", 55.6761, 12.5683),
    #         Concert("Artist3", "2025-06-06", "Oslo", 59.9139, 10.7522),
    #     ]
        
    #     itinerary_builder = self.builder.build_itinerary(test_concerts)
        
    #     # only one concert should be included for 2025-06-05
    #     same_day_concerts = [c for c in itinerary_builder if c.date == "2025-06-05"]
    #     self.assertEqual(len(same_day_concerts), 1)
        
    # ----- AI-Assisted Test Cases -----
    # Participants will implement their AI-assisted test cases here.
    # Please name your test in a way which indicates that these are AI-assisted test cases.


    # AI Prompt Used:
    # "Generate 3 Python unit tests for a Concert Itinerary Builder with these constraints:

    #     No two concerts on the same day; if conflict, pick closest to last concert.

    #     Single-concert artists prioritized over multi-concert artists.

    #     Handle artists with no concerts.
    #     Use unittest and assume Concert class has artist, date, location, latitude, longitude attributes."
    
    def test_same_day_closest_to_last(self):
        """AI-Test: Same-day conflicts resolve by proximity to last concert."""
        # Last concert location: Oslo (59.9139, 10.7522)
        test_concerts = [
            Concert("ArtistA", "2025-06-10", "Stockholm", 59.3293, 18.0686),  # Farther
            Concert("ArtistB", "2025-06-10", "Oslo", 59.9139, 10.7522),       # Closer
            Concert("ArtistC", "2025-06-15", "Oslo", 59.9139, 10.7522),       # Last concert
        ]
        itinerary = self.builder.build_itinerary(test_concerts)
        same_day_concerts = [c for c in itinerary if c.date == "2025-06-10"]
        self.assertEqual(len(same_day_concerts), 1)
        self.assertEqual(same_day_concerts[0].artist, "ArtistB")  # Closer to Oslo

    def test_prioritize_single_concert_artists(self):
        """AI-Test: Single-concert artists prioritized over multi-concert artists."""
        test_concerts = [
            Concert("Artist1", "2025-06-01", "Stockholm", 59.3293, 18.0686),  # Single
            Concert("Artist2", "2025-06-05", "Oslo", 59.9139, 10.7522),       # Single
            Concert("Artist3", "2025-06-10", "Copenhagen", 55.6761, 12.5683), # Multi (earlier)
            Concert("Artist3", "2025-06-15", "Gothenburg", 57.7089, 11.9746), # Multi (later)
        ]
        itinerary = self.builder.build_itinerary(test_concerts)
        self.assertIn("Artist1", [c.artist for c in itinerary])  # Single-concert included
        self.assertIn("Artist2", [c.artist for c in itinerary])  # Single-concert included

    def test_artist_with_no_concerts(self):
        """AI-Test: Artist with no concerts is indicated in itinerary."""
        test_concerts = [
            Concert("ArtistA", "2025-06-10", "Stockholm", 59.3293, 18.0686),
        ]
        itinerary = self.builder.build_itinerary(test_concerts)
        self.assertNotIn("NonExistentArtist", [c.artist for c in itinerary])  # Not in list

if __name__ == "__main__":
    unittest.main()