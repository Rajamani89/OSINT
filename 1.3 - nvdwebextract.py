import scrapy
cvelist = ['CVE-2019-3654','CVE-2019-4214','CVE-2019-4215','CVE-2019-4216','CVE-2019-4243','CVE-2019-4569']
urllist = []


# cve urls are formed here
def formurlist():
	for cve in cvelist:
		cveurl = 'https://nvd.nist.gov/vuln/detail/' + cve
		urllist.append(cveurl)

# testing url list
formurlist()

class nvdSpider(scrapy.Spider):
    #name of the spider
    name = 'nvdextraction'

    #list of allowed domains
    allowed_domains = ['https://nvd.nist.gov/vuln/detail/']

    #starting url for scraping
    #start_urls = ['https://nvd.nist.gov/vuln/detail/CVE-2019-4569']
    start_urls = urllist

    #setting the location of the output csv file
    custom_settings = {
        'FEED_URI' : 'tmp/nvd.csv'
    }

    def parse(self, response):
        #Remove XML namespaces
        response.selector.remove_namespaces()


        #Extract article information
        Descriptions = response.xpath('/html/body/form/div[3]/div[1]/div/table//tr/td/div/div[1]/p[1]/text()').extract()
        cvemetrics = response.xpath('/html/body/form/div[3]/div[1]/div/table//tr/td/div/div[1]/div[2]/div[2]/div[2]/div[3]/span/span/text()').extract()
        scores = response.xpath('/html/body/form/div[3]/div[1]/div/table//tr/td/div/div[1]/div[2]/div[2]/div[2]/div[2]/span/span/a/text()').extract()
        #links = response.xpath('//item/link/text()').extract()

        for item in zip(Descriptions,cvemetrics,scores):
            scraped_info = {
                'Description' : item[0],
                'cvemetric' : item[1],
               	'score' : item[2],
                #'link' : item[3]
            }

            yield scraped_info
