from scrapy import Selector

###on how to do the basic setup
html = "<html><body><div>Div 1: <p>paragraph 1</p></div><div>Div 2: <p>paragraph 2</p> <p>paragraph 3</p> </div><div>Div 3: <p>paragraph 4</p> <p>paragraph 5</p> <p>paragraph 6</p></div><div>Div 4: <p>paragraph 7</p></div><div>Div 5: <p>paragraph 8</p></div></body></html>"

sel = Selector(text=html)

divs = sel.xpath("//div")

for div in divs:
    print(div)

print("\n",divs[2])
