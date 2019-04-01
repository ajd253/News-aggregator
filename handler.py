
# TODO: look at google custom searches, this will require work with .json format

import newspaper
import textwrap

import dataset

import parsing

ARTICLE_ELEMENTS = ["title", "publish_date", "authors", "url", "meta_site_name", "summary", "meta_description",
                    "keywords", "meta_keywords", "text"]
LINE_WIDTH = 180
TAG_LENGTH = 18

NUM_ARTICLES = 10

FEEDS_FILE = "feeds.txt"

DATABASE_URL = "sqlite:///article_store.db"


def process(source, limit):
    """
    Grabs n articles from source, parses and analyses them, where limit specifies n.
    source must be an RSS feed (at the moment can be any url though).
    limit must be an integer.

    Returns: list of dictionaries containing tags, information.
    """
    # TODO: reformulate for RSS feeds, create another function for other links

    print("Getting newspaper hot sources...")
    # Get list of links from RSS feed
    # TODO; CHECK THIS
    inputList = newspaper.api.hot(source)
    print("Sources acquired.")
    print("\n")
    
    print("Stripping links from provided list...")
    # Strip urls from list
    # TODO: just get the links straight - it's simpler
    linkList = parsing.get_links(inputList, limit)
    print("Links stripped.")
    print("\n")
    
    print("Commencing articles download...")
    # Download articles and gather into list
    articleList = []
    for link in linkList:
        article = parsing.pull_article(link)
        articleList.append(article)
    print("Articles downloaded.")
    print("\n")

    print("Conducting analysis...")
    # Run analysis on each article
    analysedList = []
    for article in articleList:
        analysed = parsing.analyse_article(article, ARTICLE_ELEMENTS)
        analysedList.append(analysed)
    print("Analysis complete.")

    return analysedList


def print_analysis(analysis, noText=True):
    """
    Prints articles' tag, information pairs.
    analysis must be a list of newspaper.article typed objects.
    noText must be True or False.
    
    NOTE: you must pass False in the third argument to output full article text.

    Returns: None
    """
    print("Outputting analysis...")
    for elem in analysis:
        print("*****")
        for item in ARTICLE_ELEMENTS:
            if item == "text" and noText is True:
                continue
            target, payload = dump_list(item, elem[item])
            print_line(target, payload)
        print("*****")
    print("Your analysis is served.")


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
    #TODO: redundant logic branching
    if type(info) != str:
        info = str(info)
    else:
        info = str(info)
    infoList = textwrap.wrap(info, LINE_WIDTH)
    return paddedTag, infoList


def get_feed_list(feeds):
    """
    Gets RSS feed urls from specified text file.
    feeds must be a string specifying the location to a .txt file.
   
    Returns: list of RSS feeds.
    """
    feedList = []
    feedsFile = open(feeds, "r")
    for link in feedsFile:
        print(link)
        feedList.append(link.strip("\n"))
    feedsFile.close()
    return feedList


if __name__ == "__main__":
    feeds = get_feed_list(FEEDS_FILE)
    db = dataset.connect(DATABASE_URL)
    articlesTable = db["article"]
    for feed in feeds:
        news = process(feed, NUM_ARTICLES)
        for article in news:
            if not articlesTable.find_one(url=article["url"]):
                record = dict()
                record.update({"title":article["title"], "url":article["url"]})
                #for elem in ARTICLE_ELEMENTS:
                #    record.update({elem:article[elem]})
                #for i, e in article:
                #    record.update({i:str(e)})
                articlesTable.insert(record)
    for a in articlesTable:
        print(a)
    db.commit()

