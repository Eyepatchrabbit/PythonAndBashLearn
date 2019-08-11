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


