from scrapy import Selector
import requests


###how get a html from webpage:
# exmple usinf requests:
def extractionDataStats(name):
    print("\nGetting viatals " + name.capitalize() + ":")
    pokedexPage = "https://pokemondb.net/pokedex/" + name

    # use request to get the webpage
    htmlPoke = requests.get(pokedexPage).content

    # use selector to extract data from the HTML source
    pageselection = Selector(text=htmlPoke)

    # get main location of the vitals:
    vitalsExtract = pageselection.xpath("//h2[text()='Base stats']/..//table[@class='vitals-table']/tbody/tr")

    vitalsNames = vitalsExtract.xpath("./th//text()").extract()
    vitalStats = vitalsExtract.xpath(".//td[@class='cell-num'][1]/text()").extract()

    vitals = zip(vitalsNames, vitalStats)

    for name, stat in vitals:
        print(name, stat)


extractionDataStats('rhyhorn')
extractionDataStats('rhydon')
extractionDataStats('abra')
