# Author: Alex J Davies (alexjdavies.net)

import feedparser

from newspaper import Article

from output import vprint

verbose = False


def get_links(RSSFeed, numLinks):
    """
    Scrape n article URLs from an RSS feed, where n=numLinks.
    RSSFeed must be a string holding an RSS feed URL.
    numLinks must be an integer.

    Returns: list of article urls.
    """

    vprint(verbose, str("Getting " + str(numLinks) + " article links from the feed at " + RSSFeed + "..."))
    parsedFeed = feedparser.parse(RSSFeed)
    articleLinks = []
    i = 0
    while i < numLinks and i < len(parsedFeed.entries):
        articleLinks.append(parsedFeed.entries[i].link)
        i = i + 1
    vprint(verbose, "Article links acquired.\n")
    return articleLinks


def get_article(url):
    """
    Downloads an article from url.
    url must be a string.

    Returns: instance of newspaper.article.
    """

    vprint(verbose, "Downloading article from " + url + " ...")
    article = Article(url, language="en")
    article.download()
    vprint(verbose, "Article downloaded.\n")

    return article


def analyse_article(article, elems):
    """
    Parses article for information that matches tags specified in elems, then performs NLP on that information.
    article must be an object of type newspaper.article.
    elems must be a list of tags to scrape from article.

    Returns: dictionary of tags and matching data.
    """

    vprint(verbose, "Parsing and analysing article...")
    # Parse article and conduct NLP analysis using newspaper supplied methods
    article.parse()
    article.nlp()

    breakdown = {}
    for elem in elems:
        payload = getattr(article, elem)
        breakdown.update({elem: payload})

    vprint(verbose, "Parsing and analysis complete.")

    return breakdown


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode()    # uses 'utf-8' for encoding
    else:
        value = bytes_or_str
    return value                # Instance of bytes


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode()  # uses 'utf-8' for encoding
    else:
        value = bytes_or_str
    return value  # Instance of str
