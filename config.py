"""
Central configuration file for the aggregator.
"""
# Global constants
LINE_WIDTH = 80                # Line width for printing articles
TAG_LENGTH = 18                 # Used to pad tags when printing articles and ensure ouptput alignment
FEEDS_FILE = "feeds.txt"        # File holding RSS feed URLs 
DATABASE_URL = "sqlite:///article_store.db"     # Database in which to store analysed articles
