added project by using the following:

#sets up the project
- cd pythonexecutables/datacampelements/scrappyspiders/spiderprojects/
- scrapy startproject quotes_spider

#sets up the spider
-cd quotes_spider/
-scrapy genspider quotes quotes.toscrape.com

=>build all the needed elements for doing a scarping project (yea!!!)

can check with "scrapy list" ->lists the spiders in the project


to run the spider:
    -> scrapy crawl quotes
        =>inside the directory where the cfg file is located (start of the project)


robots.txt site of the page:
    """
    Webmasters use this file to give instructions to robots about which pages of the website they should not visit.
    It is also called The Robots Exclusion Protocol.
    While web scraping, it is recommended to respect it.
    """
    =>seeing if there are 'scraping rules' for the site
    ->to set this behaviour off need to do the following:
        -go to the settings.py file that was made and set following to false
            # Obey robots.txt rules
            ROBOTSTXT_OBEY = False



