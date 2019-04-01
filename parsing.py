import newspaper
from newspaper import Article

def get_links(itemList, numLinks):
    """
    Extracts urls from an n-dimensional list.
    itemList must be a list of lists, and links must be indexed to itemList[n][1]
    numLinks must be an integer.
    
    Returns: list of urls

    """
    print("     Getting " + str(numLinks) + " links.")
    links = []
    i = 0
    while i < numLinks:
        item = itemList[i][1]
        links.append(item)
        i = i + 1
    return links

def pull_article(url):
    """
    url must be a string.
    Returns: instance of newspaper.article.
    """
    
    print("     Pulling article...")
    article = Article(url)
    article.download()
    print("     Article pulled.")
    return article

def analyse_article(article, elems):
    """
    Scrapes information from article that matches tags specified in elems.
    article must be an object of type newspaper.article.
    elems must be a list of tags to scrape from article.
    
    Returns: dictionary of tags and matching data.
    """
    
    print("     Parsing article...")
    # Parse article and conduct NLP analysis using newspaper supplied methods
    article.parse()
    article.nlp()

    # Create dictionary container
    breakdown = {}
    # Add information matching elements to breakdown
    for elem in elems:
        payload = getattr(article, elem)
        breakdown.update({elem:payload})
    print("     Article parsed.")

    return breakdown


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode()    # uses 'utf-8' for encoding
    else:
        value = bytes_or_str
    return value                # Instance of bytes


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode() # uses 'utf-8' for encoding
    else:
        value = bytes_or_str
    return value # Instance of str





