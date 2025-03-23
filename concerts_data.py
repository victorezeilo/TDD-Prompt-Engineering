"""
Concert Data

This file contains the dataset of concerts that will be used
for the experiment.
"""

from main import Concert

CONCERTS_DATA = [
    Concert("Taylor Swift", "2025-06-10", "Stockholm", 59.3293, 18.0686),
    Concert("Taylor Swift", "2025-07-15", "Copenhagen", 55.6761, 12.5683),
    Concert("Taylor Swift", "2025-05-20", "Oslo", 59.9139, 10.7522),
    Concert("Ed Sheeran", "2025-06-05", "Gothenburg", 57.7089, 11.9746),
    Concert("Coldplay", "2025-06-05", "Stockholm", 59.3293, 18.0686),
    Concert("Adele", "2025-06-15", "Oslo", 59.9139, 10.7522),
    Concert("Beyoncé", "2025-06-20", "Copenhagen", 55.6761, 12.5683),
    Concert("The Weeknd", "2025-06-25", "Stockholm", 59.3293, 18.0686),
    Concert("Justin Bieber", "2025-07-01", "Malmö", 55.6050, 13.0038),
    Concert("BTS", "2025-07-01", "Copenhagen", 55.6761, 12.5683),
    Concert("Dua Lipa", "2025-07-01", "Oslo", 59.9139, 10.7522),
    Concert("Billie Eilish", "2025-07-10", "Stockholm", 59.3293, 18.0686),
    Concert("Billie Eilish", "2025-08-05", "Oslo", 59.9139, 10.7522),
    Concert("Imagine Dragons", "2025-08-15", "Stockholm", 59.3293, 18.0686),
    Concert("Bruno Mars", "2025-08-20", "Copenhagen", 55.6761, 12.5683),
    Concert("Post Malone", "2025-08-25", "Gothenburg", 57.7089, 11.9746),
    Concert("Ariana Grande", "2025-09-01", "Oslo", 59.9139, 10.7522),
    Concert("Drake", "2025-09-10", "Stockholm", 59.3293, 18.0686),
    Concert("Lady Gaga", "2025-09-15", "Copenhagen", 55.6761, 12.5683),
    Concert("Lady Gaga", "2025-09-05", "Gothenburg", 57.7089, 11.9746),
    Concert("Rihanna", "2025-09-20", "Stockholm", 59.3293, 18.0686),
    Concert("Rihanna", "2025-10-05", "Oslo", 59.9139, 10.7522),
    Concert("Kendrick Lamar", "2025-07-25", "London", 51.5074, -0.1278),
    Concert("Metallica", "2025-08-01", "Berlin", 52.5200, 13.4050),
    Concert("The Rolling Stones", "2025-08-10", "Paris", 48.8566, 2.3522),
    Concert("Foo Fighters", "2025-09-25", "Amsterdam", 52.3676, 4.9041),
]

def get_all_concerts():
    """
    Returns the list of all concerts.
    
    Returns:
        list: A list of Concert objects
    """
    return CONCERTS_DATA.copy()