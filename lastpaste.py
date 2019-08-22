import requests
from lxml import html

pb_home_url = 'https://pastebin.com'
pb_archive_url = pb_home_url + '/archive'


def get_document(url):
    # http call to get source page for given url and return it's document.
    response = requests.get(url)
    # check response.status_code ?
    document = html.document_fromstring(response.content)
    return document


def parse_pastes_hrefs(archive_document):
    # parse pastes hrefs from 'Pastes Archive'
    # filtering pastes older than 2 minutes
    # filtering 'syntax' hrefs
    post_time_filter = "[tr/td/text() = '1 min ago' or tr/td/text() = '2 min ago' or contains(tr/td/text(), 'sec ago')]"
    pastes_table = archive_document.xpath("//table[@class='maintable']" + post_time_filter)[0]
    pastes = pastes_table.xpath("tr/td/a[not(contains(@href, 'archive'))]/@href")
    print(len(pastes))
    return pastes


def parse_paste(paste_document):
    pass


def write_to_file(paste_model):
    time = None
    filename = "{}_pastes.txt".format(time)
    file = open(filename, "w")
    file.write(paste_model)


doc = get_document(pb_archive_url)
pastes_hrefs = parse_pastes_hrefs(doc)

for href in pastes_hrefs:
    paste_url = pb_home_url + href
    print(paste_url)
    paste_doc = get_document(paste_url)
    # async?
    parse_paste(doc)





