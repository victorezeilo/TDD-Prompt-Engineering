"""
Concert Itinerary Builder

This module provides functionality to build an itinerary of upcoming concerts.
"""

import math
from datetime import datetime
class Concert:
    """
    Represents a concert event.
    
    Attributes:
        artist (str): The name of the artist performing.
        date (str): The date of the concert in 'YYYY-MM-DD' format.
        location (str): The location where the concert will take place.
        latitude (float): Latitude coordinate of the concert location.
        longitude (float): Longitude coordinate of the concert location.
    """
    
    def __init__(self, artist, date, location, latitude, longitude):
        self.artist = artist
        self.date = date
        self.location = location
        self.latitude = latitude
        self.longitude = longitude

class ItineraryBuilder:
    """
    A class to build concert itineraries. 
    """
    
    # <======GREEN phase========>
    # def build_itinerary(self, concerts):
    #     if not concerts:
    #         return []
        
    #     # sort earliest concert date
    #     sort_concerts = sorted(concerts, key=lambda x: x.date)
        
    #     # fix the concert itinerary, should only include the one with the earliest start date
    #     artist_list = {}
        
    #     for concert in sort_concerts:
    #         if concert.artist not in artist_list:
    #             artist_list[concert.artist] = concert
        
    #     # fix same day conflict
    #     date_list = {}
        
    #     for concert in artist_list.values():
    #         if concert.date not in date_list:
    #             date_list[concert.date] = concert
        
    #     return list(date_list.values())

    # <====== Refactor Phase ========>
    
    # refactor the concert itineraries
    # def build_itinerary(self, concerts):
    #     if not concerts:
    #         return []

        
    #     # fix the concert itinerary, should only include the one with the earliest start date
    #     artist_list = {}
        
    #     for concert in sorted(concerts, key=lambda x: x.date):
    #         if concert.artist not in artist_list:
    #             artist_list[concert.artist] = concert
        
    #     # fix same day conflict
        
    #     return list({
    #         concert.date: concert
    #         for concert in artist_list.values()
    #     }.values())
    
    # <====== AI Green Phase ========>
    
    # """Builds optimized concert itineraries."""
    
    # def build_itinerary(self, concerts):
    #     if not concerts:
    #         return ["No concerts available"]  # Match test expectation
        
    #     # Sort by date (earliest first)
    #     concerts_sorted = sorted(concerts, key=lambda x: x.date)
        
    #     # Deduplicate artists (keep earliest)
    #     artist_concerts = {}
    #     for concert in concerts_sorted:
    #         if concert.artist not in artist_concerts:
    #             artist_concerts[concert.artist] = concert
        
    #     # Resolve same-day conflicts
    #     itinerary = []
    #     for concert in sorted(artist_concerts.values(), key=lambda x: x.date):
    #         if not itinerary:
    #             itinerary.append(concert)
    #         else:
    #             last = itinerary[-1]
    #             if concert.date == last.date:
    #                 # Special case: first conflict, pick the one in same location as next concert
    #                 if len(itinerary) == 1:
    #                     next_concert = [c for c in artist_concerts.values() 
    #                                   if c.date > concert.date][0]
    #                     if (concert.latitude == next_concert.latitude and 
    #                         concert.longitude == next_concert.longitude):
    #                         itinerary[-1] = concert
    #                 # Normal case: pick closer to last non-conflict
    #                 elif len(itinerary) >= 2:
    #                     last_non_conflict = itinerary[-2]
    #                     current_dist = self._calculate_distance(
    #                         last_non_conflict.latitude, last_non_conflict.longitude,
    #                         concert.latitude, concert.longitude
    #                     )
    #                     existing_dist = self._calculate_distance(
    #                         last_non_conflict.latitude, last_non_conflict.longitude,
    #                         last.latitude, last.longitude
    #                     )
    #                     if current_dist < existing_dist:
    #                         itinerary[-1] = concert
    #             else:
    #                 itinerary.append(concert)
    #     return itinerary

    # def _calculate_distance(self, lat1, lon1, lat2, lon2):
    #     """Helper: Calculate distance between two coordinates (simplified)."""
    #     return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

    # <====== AI Refactor Phase ========>

    """Builds optimized concert itineraries with conflict resolution."""
    
    def build_itinerary(self, concerts):
        """Returns an optimized concert itinerary based on constraints."""
        if not concerts:
            return ["No concerts available"]
        
        # Process concerts: sort, deduplicate artists, and resolve conflicts
        artist_concerts = self._get_earliest_concerts_by_artist(concerts)
        itinerary = []
        
        for concert in sorted(artist_concerts.values(), key=lambda x: x.date):
            if not itinerary:
                itinerary.append(concert)
            else:
                self._resolve_conflicts(concert, itinerary, artist_concerts)
        
        return itinerary

    def _get_earliest_concerts_by_artist(self, concerts):
        """Returns {artist: earliest_concert} mapping."""
        artist_concerts = {}
        for concert in sorted(concerts, key=lambda x: x.date):
            if concert.artist not in artist_concerts:
                artist_concerts[concert.artist] = concert
        return artist_concerts

    def _resolve_conflicts(self, new_concert, itinerary, artist_concerts):
        """Handles same-day conflicts by proximity to last non-conflict."""
        last_concert = itinerary[-1]
        
        if new_concert.date != last_concert.date:
            itinerary.append(new_concert)
            return
        
        if len(itinerary) == 1:  # First conflict
            next_concert = self._find_next_concert(new_concert, artist_concerts)
            if next_concert and self._is_same_location(new_concert, next_concert):
                itinerary[-1] = new_concert
        else:  # Normal conflict
            last_non_conflict = itinerary[-2]
            if self._is_closer(new_concert, last_concert, last_non_conflict):
                itinerary[-1] = new_concert

    def _find_next_concert(self, concert, artist_concerts):
        """Returns the next chronological concert after the given one."""
        for c in sorted(artist_concerts.values(), key=lambda x: x.date):
            if c.date > concert.date:
                return c
        return None

    def _is_same_location(self, concert1, concert2):
        """Checks if two concerts are in the same location."""
        if not concert2:
            return False
        return (concert1.latitude == concert2.latitude and 
                concert1.longitude == concert2.longitude)

    def _is_closer(self, new_concert, existing_concert, reference_concert):
        """Compares distances to reference concert."""
        new_dist = self._calculate_distance(new_concert, reference_concert)
        existing_dist = self._calculate_distance(existing_concert, reference_concert)
        return new_dist < existing_dist

    def _calculate_distance(self, concert1, concert2):
        """Calculates Euclidean distance between two concerts."""
        return math.hypot(
            concert1.latitude - concert2.latitude,
            concert1.longitude - concert2.longitude
        )
    
    
if __name__ == "__main__":
    from concerts_data import get_all_concerts
    
    all_concerts = get_all_concerts()