# Author: Alex J Davies (alexjdavies.net)

import sys
import textwrap

import dataset

import parsing

from config import LINE_WIDTH, TAG_LENGTH
from config import FEEDS_FILE, DATABASE_URL

from output import vprint

ARTICLE_ELEMENTS = ["title", "publish_date", "authors", "url", "summary", "meta_description", "keywords", "meta_keywords", "text"]  
PRINT_ELEMENTS = ["title", "publish_date", "authors", "url", "summary", "meta_description", "keywords", "meta_keywords", "text"]


def process(source, limit):
    """
    Grabs n articles from source, parses and analyses them, where limit specifies maximum n.
    source must be an RSS feed.
    limit must be an integer.

    Returns: list of dictionaries, each containing the tags and parsed information of one article.
    """

    # Getting article links
    feedLinks = parsing.get_links(source, limit)

    # Download articles and gather into list
    articleList = []
    for link in feedLinks:
        article = parsing.get_article(link)
        articleList.append(article)

    # Analyse each article
    analysedList = []
    for article in articleList:
        analysed = parsing.analyse_article(article, ARTICLE_ELEMENTS)
        analysedList.append(analysed)

    vprint(verbose, str(len(articleList)) + " articles processed.")

    return analysedList


def print_article(articleDict, noText=True):
    """
    Wrapper to print the tag, information pairs from a dictionary constructed from an Article object.
    articleDict must be a dictionary.
    noText must be True or False.

    NOTE: you must pass False in the third argument to output full article text.

    Returns: None
    """
    print("*****")
    for tag in PRINT_ELEMENTS:
        target, payload = dump_list(tag, articleDict[tag])
        print_line(target, payload)
    print("*****")


def print_line(paddedTag, infoList):
    """
    Prints the output for a given tag, information pair.
    paddedTag must be a string.
    infoList must be a list.

    Returns: None
    """
    if infoList == []:
        print(paddedTag.ljust(TAG_LENGTH) + "---")
    else:
        print(paddedTag.ljust(TAG_LENGTH) + infoList[0])
        i = 1
        while i < len(infoList):
            print(infoList[i].rjust(len(infoList[i]) + TAG_LENGTH))
            i = i + 1


def dump_list(tag, info):
    """
    Formats tag, information pair for output legibility.
    tag must be a string.
    info type may vary.

    Returns:   string.
    """
    paddedTag = tag + ":"
    info = str(info)
    infoList = textwrap.wrap(info, LINE_WIDTH)
    return paddedTag, infoList


def get_feed_list(feeds):
    """
    Gets RSS feed urls from specified text file.
    feeds must be a string specifying the location to a .txt file.

    Returns: list of RSS feeds.
    """

    # Getting RSS feed URLs
    vprint(verbose, "Getting link list from source file.")
    feedList = []
    feedsFile = open(feeds, "r")
    for link in feedsFile:
        feedList.append(link.strip("\n"))
    feedsFile.close()
    vprint(verbose, str(len(feedList)) + " RSS links acquired.")
    return feedList


def insert_article(article, table, tags):
    """
    Inserts tag, information pairs of article into table of a database.

    Returns:    None.
    """

    record = dict()
    for tag in tags:
        if hasattr(article, tag):
            record.update({tag: article[tag]})
    table.insert(record)


def parse_args(args):
    """
    Checks command line arguments for sanity. 

    Returns:    int, boolean pair.
    """

    if len(args) < 2:
        print("ERROR: Too few arguments. Please provide an integer in the first argument for the number of articles to analyse from each feed.")
        quit()

    if len(args) == 2:
        try:
            if int(args[1]) > 0:
                numArticles = int(args[1])
                verbose = False
                parsing.verbose = False
                print("Verbose mode is OFF.")
        except ValueError:
            print("ERROR: Incorrect argument type. Please provide an integer in the first argument for the number of articles to analyse from each feed.")
            quit()

    if len(args) == 3:
        try:
            if int(args[1]) > 0:
                numArticles = int(args[1])
        except ValueError:
            print("ERROR: Incorrect argument type. Please provide an integer in the first argument for the number of articles to analyse from each feed.")
            quit()

        if args[2] == "-v" or args[2] == "-verbose":
            verbose = True
            parsing.verbose = True
            print("Verbose mode is ON.")
        else:
            verbose = False
            parsing.verbose = False
            print("Verbose mode is OFF.")

    if len(args) > 3:
        print("ERROR: Too many arguments supplied.")
        quit()

    return numArticles, verbose


if __name__ == "__main__":
    print(sys.argv)
    # Parse command line arguments
    numArticles, verbose = parse_args(sys.argv)
    print("---")

    # Get RSS feeds from file
    feeds = get_feed_list(FEEDS_FILE)
    numFeeds = len(feeds)

    # Connect to SQL database and create/specify table
    db = dataset.connect(DATABASE_URL)
    articlesTable = db["article"]

    for index, feed in enumerate(feeds):
        # Construct list of processed articles from feed
        print("Processing " + str(index+1) + " of " + str(numFeeds) + " feeds.")
        news = process(feed, numArticles)

        # Insert each article into the database and print its tag, information pairs
        for article in news:
            insert_article(article, articlesTable, ARTICLE_ELEMENTS)
            print_article(article)
            """
            for elem in ARTICLE_ELEMENTS:
                record.update({elem:article[elem]})
            for i, e in article:
                record.update({i:str(e)})
            """
        print("Feed processed.\n")

    # Write to database
    db.commit()
