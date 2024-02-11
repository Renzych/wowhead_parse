import scrapy
from scrapy.crawler import CrawlerProcess
import logging
from bs4 import BeautifulSoup

logging.getLogger('scrapy').propagate = False


class MySpider(scrapy.Spider):
    name = 'myspider'

    def start_requests(self):
        with open('spell_id.txt', 'r') as f:  # file with spellid, one line - one id
            ids = f.read().splitlines()
        for spell_id in ids:
            url = f'https://wowhead.com/classic/ru/spell={spell_id}'  # you need to change link to your locale
            yield scrapy.Request(url, self.parse, meta={'spell_id': spell_id})

    def parse(self, response):
        spell_id = response.meta['spell_id']
        skillName_xpath = '//*[@id="main-contents"]/div[3]/h1/text()'
        skillCost_xpath = '(//tr[@class="first"]/td)[2]/text()'
        skillCast_xpath = '//*[@id="spelldetails"]/tr[4]/td/text()'
        skillRange_xpath = '//*[@id="spelldetails"]/tr[3]/td/text()'
        skillDescription_xpath = '//div[@class="q"]'
        skillCost = response.xpath(skillCost_xpath).get()
        skillName = response.xpath(skillName_xpath).extract_first()
        skillCast = response.xpath(skillCast_xpath).get()
        skillRange = response.xpath(skillRange_xpath).get()
        skill_Description = response.xpath(skillDescription_xpath).extract_first()
        skillName = str(skillName)
        skillName = skillName.replace('"', '\\"')
        if skill_Description is not None:  # some fixes for skill description text, \n \"
            skill_Description = skill_Description.replace('<br>', '\\n')
            soup = BeautifulSoup(skill_Description, 'html.parser')
            skill_Description = soup.get_text()  # delete all html tags from skill description
            skill_Description = str(skill_Description)
            skill_Description = skill_Description.replace('"', '\\"')
        if skill_Description is None:
            skill_Description = str('')
        if not response.xpath(
                '//div[@class="database-detail-page-not-found-message"]').get():  # trying to find skill not found, its just for trying parse something like 400000-500000 id, when you dont know spell ID
            with open('output.txt', 'a', encoding='utf-8') as f:
                f.write(f'"' + str(skillName) + '£' + str(skillCost) + '£' + str(skillCast) + '£' + str(
                    skillRange) + '£Å' + str(skill_Description) + '", --' + str(spell_id) + '\n')
                print('all OK, last spellId =' + str(spell_id))


process = CrawlerProcess()
process.crawl(MySpider)
process.start()  # wowhead skill parse start


# After we get all spells we need to sort it, cause scrapy a-sync ^^^^^

def sort_file():
    with open('spell_collection.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Сортируем строки по числу в конце строки
    lines.sort(key=lambda line: int(line.split('--')[-1]))

    # Открываем файл для записи и записываем отсортированные строки
    with open('sorted_spell_collection.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)


#sort_file()           #launch sorting