#-*- codng: utf-8 -*-

from lxml import html, etree
import html2text

try:
    from PIL import Image, ImageOps
except ImportError:
    import Image
    import ImageOps

def html_to_text(html_desc):
    h = html2text.HTML2Text()
    h.ignore_links = True
    return h.handle(html_desc)

def get_external_desc(url):
    try:
        parser = etree.HTMLParser(encoding='cp1251')
        page = html.parse(url, parser).getroot()
        hd = etree.tostring(page.xpath('//div[@class="fulltext"]')[0], encoding="utf-8")
        md = html_to_text(hd.decode("utf-8"))
        return md
    except:
        return None

def add_watermark(orig, mark, dest=None, thumbnail=None):
    baseim = Image.open(orig)
    logoim = Image.open(mark)
    baseim.paste(logoim, (baseim.size[0]-logoim.size[0], baseim.size[1]-logoim.size[1]))
    if thumbnail is not None:
        baseim.thumbnail(thumbnail)
    if dest is None :
        dest = orig
    baseim.convert("RGB").save(dest,"JPEG")
