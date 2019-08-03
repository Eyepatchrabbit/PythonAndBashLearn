from scrapy import Selector
import requests

###how get a html from webpage:
# exmple usinf requests:


def extractionDataStats(name):
    print("\nGetting viatals "+name.capitalize()+":")
    rhydonPokedexPage = "https://pokemondb.net/pokedex/"+name

    htmlPoke = requests.get(rhydonPokedexPage).content

    pageselection = Selector(text=htmlPoke)

    #battlestats:
    vitalsExtract=pageselection.xpath("//h2[text()='Base stats']/..//table[@class='vitals-table']/tbody/tr")

    vitalsNames = vitalsExtract.xpath("./th//text()").extract()
    vitalStats=vitalsExtract.xpath(".//td[@class='cell-num'][1]/text()").extract()

    vitals=zip(vitalsNames,vitalStats)

    for name, stat in vitals:
        print(name,stat)


extractionDataStats('rhyhorn')
extractionDataStats('rhydon')
extractionDataStats('abra')