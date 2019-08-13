this folder is for the info on webscraping

-xpath elements
-scrappy
-building spiders

/!\=>see also more on how to do exceptionHandeling

Possible sites to practice on:
------------------------------
* https://pokemondb.net/pokedex/national

* https://bokunoheroacademia.fandom.com/wiki/My_Hero_Academia_Wiki

* http://www.omdbapi.com =>watchout, need to generate first a key on the website !

* https://httpbin.org

(YES I'm a nerd at hart :p )



Handy elements  seen to remember:
----------------------------------
* xpath = '//*[@id="div3"]/p' =>selects all elements with attribute
    => ~ xpath(By.id('div3'))

* xpath = '//p[@id="p2"]/a/@href'
    ->getting hod of what is set in the attribute value !

* contains(@attri-name,"string-expr") ->can do also a contain on the attributes (not only presented text);
    =># Create an xpath to the href attributes
        xpath = '//a[contains(@class,"course-block")]/@href'


*can chain xpaths
    sel.xpath( '//div' ).xpath( "./span/p[3]" ) = sel.xpath('//div/span/p[3]')


Udemy scrapy tutorials
#########################
after the lessons on scrapy and the spiders in datachamp feeled that there was more to the subject
=>so took on an udemy course on scrappy ("Scrapy: Powerful Web Scraping & Crawling with Python")
->also looked into Requests package =>considering using scrapy can be overkill for some elements

udemy courses taken:
-Scrapy: Powerful Web Scraping & Crawling with Python

youtube courses done=
-Python Requests Tutorial: Request Web Pages, Download Images, POST Data, Read JSON, and More (https://www.youtube.com/watch?v=tb8gHvYlCFs)
-


Avoid Getting Banned!
========================
It is very important to be careful while scraping websites; otherwise, you might be banned. Here are some tips to keep in mind while web scraping:

1- In the file settings.py activate the option DOWNLOAD_DELAY or you can do that manually in your code through sleeping a for a random number of seconds.
        from time import sleep
        import random

        # Your code here
        ...
        sleep(random.randrange(1,3))

2- In the file settings.py activate the option USER_AGENT like the following, or any Chrome or Firefox user agent here. Defining a user agent let you look more like a browser used by a real person, not an automatic robot.
    example: USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"

3- Find external proxies and rotate IP addresses while scraping. You can use the package scrapy-proxies for the purpose. https://github.com/aivarsk/scrapy-proxies

4- For professional work, consider using ScrapingHub.com to host your scrapers - it offers a free limited plan

Recommendations Before Web Scraping:

• it is highly recommended to search for an API for the website you want to get data from.
    Most large websites offer APIs to make data extraction a better experience for both parties.
    So try first to search Google for an API for the website; if you find one, you do not need to scrape it.
    APIs generate JSON objects which are very similar to Python dictionaries, and from which data can be extracted using the Python JSON library.

• it is highly recommended you read the Terms and Conditions of the website.
    Some websites clearly mention prohibiting web scraping without permission,
    or mention some legal or copyright aspects related to the use of its data.

• employ common sense! Some web scraping or other robot activities are obviously illegal if they cause any direct
    or indirect damage to the company owning data or its customers. It is a good idea to discuss the purpose of a
    web scraping project with your client before accepting it.

• prepare your code to be "polite": do not unnecessarily disable robots.txt of the website;
    space out your requests a bit so that you do not hammer the site's server;
    and it is better to run your spiders during off-peak traffic hours of the website.





