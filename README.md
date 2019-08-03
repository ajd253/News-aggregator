# News-aggregator
Now:    A tool for aggregating articles from RSS feeds. Currently these are dumped into a SQL database, but this isn't fully functional currently. Information parsed/analysed from articles is printed as tag, information pairs.
Future: Additional functionality to parse and analyse custom Google searches.
...

# Sample output
title:            R3 commits to London despite Brexit uncertainty
publish_date:     2019-08-02 11:00:00
authors:          []
url:              https://www.finextra.com/newsarticle/34202/r3-commits-to-london-despite-brexit-
                  uncertainty?utm_medium=rssfinextra&utm_source=finextrafeed
summary:          R3, the enterprise blockchain software company, has doubled the size of its
                  London hub amidst Brexit precariousness. David E. Rutter, CEO of R3, said:
                  There is enormous opportunity for London post-Brexit. According to the company,
                  the enlargement of their engineering team will ensure that the businesses who
                  build their applications on R3’s Corda blockchain can continue to deploy
                  solutions “simply and successfully”. In 2018, despite ongoing Brexit
                  negotiations, the capital received more Foreign Direct Investment than any other
                  city. Boasting over half of FinTech50’s leading fintech firms, it seems
                  unsurprising that both EY and Deloitte ranked it as the top global fintech hub.
meta_description: R3, the enterprise blockchain software company, has doubled the size of its
                  London hub amidst Brexit precariousness.
keywords:         ['engineering', 'firms', 'team', 'uncertainty', 'hub', 'company', 'r3',
                  'brexit', 'london', 'software', 'commits', 'fintech', 'global', 'despite']
meta_keywords:    ['Finextra', 'news', 'online', 'bank', 'banking', 'technology', 'finance',
                  'financial', 'fin', 'tech', 'fintech', 'IT', 'breaking', 'latest', 'retail',
                  'transaction', 'trade', 'execution', 'headlines', 'blockchain', 'digital',
                  'investment', 'mobile', 'business', 'challenger', 'payments', 'regtech',
                  'insurtech', 'services']
text:             R3, the enterprise blockchain software company, has doubled the size of its
                  London hub amidst Brexit precariousness.  The extra space will cater for a
                  rapidly growing engineering team, supporting the companies vigorous plan to hire
                  40 new members in the capital and to increase its global headcount from 215 to
                  300 by the close of 2019.    David E. Rutter, CEO of R3, said: “There is
                  enormous opportunity for London post-Brexit. While there clearly remain some
                  uncertainties, we believe the city is well placed and established to thrive in
                  the coming years. That’s why we are confident in making this substantial long-
                  term commitment now.”    The firm’s London expansion forms just part of its
                  rapid growth plans, with evaluation already underway to decide the ideal
                  location for an additional engineering center set to open in 2020. According to
                  the company, the enlargement of their engineering team will ensure that the
                  businesses who build their applications on R3’s Corda blockchain can continue to
                  deploy solutions “simply and successfully”.    Rutter states that “as our
                  software gains more use cases and across more sectors, we will be looking to
                  invest further in top talent - London and elsewhere.”    The development
                  exemplifies how London has gained a reputation as a global technology
                  stronghold. In 2018, despite ongoing Brexit negotiations, the capital received
                  more Foreign Direct Investment than any other city. Boasting over half of
                  FinTech50’s leading fintech firms, it seems unsurprising that both EY and
                  Deloitte ranked it as the top global fintech hub.

# How to use
* Specify your feeds file in config.py.
* Run the following command:
    > python handler.py n [-v]
* Options are specified as follows:
    * n             [required] the number of articles to download from each RSS feed. It must be an integer > 0.
    * -v, -verbose  [optional] provides additional output detailing the aggregator's progress.

# Requirements:
* Newspaper module (pypi.org/project/newspaper3k) 
* Dataset module (dataset.readthedocs.io)

# To do:
* Implement full database functionality.
* Refactor code.

Developed by Alex J Davies, alex@alexjdavies.net.
