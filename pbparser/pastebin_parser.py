import sys
from paste import Paste
from lxml import html
import logging


def parse_archive(archive_text):
    # parse pastes hrefs from 'Pastes Archive'
    # filtering pastes older than 2 minutes
    # filtering 'syntax' hrefs
    try:
        archive_doc = html.document_fromstring(archive_text)
        post_time_filter = "[(td/text() = '1 min ago' or td/text() = '2 min ago' or contains(td/text(), 'sec ago'))]"
        filtered_tr_list = archive_doc.xpath(".//table[@class='maintable']/tr{}".format(post_time_filter))
    except Exception as e:
        logging.error("'Failed to parse 'Archive'.\n {}\nExiting ...'".format(e))
        sys.exit(1)
    hrefs = []
    logging.info('parsing {} optional pastes'.format(len(hrefs)))
    for e in filtered_tr_list:
        try:
            href = e.xpath("td[1]/a/@href")[0]
            hrefs.append(href)
        except Exception as e:
            logging.error("'Failed to parse 'href'.\n {}\nSkipping ...'".format(e))
    return hrefs


def parse_paste(paste_text):
    # parse paste meta_data & content
    if not paste_text:
        return None
    try:
        paste_doc = html.document_fromstring(paste_text)
        title = paste_doc.xpath(".//div[@class='paste_box_line1']/@title")[0].strip()
        box_line2_element = paste_doc.xpath(".//div[@class='paste_box_line2']")[0]
        author = box_line2_element.xpath("img")[0].tail.strip()
        date = box_line2_element.xpath("span/@title")[0]
        content = paste_doc.xpath("//textarea[@id='paste_code']/text()")[0].strip()
    except Exception as e:
        logging.error("'Failed to parse 'paste'.\n {}\nSkipping ...'".format(e))
        return None
    paste = Paste(title, author, date, content)
    return paste
