from bs4 import BeautifulSoup
import re

orig_prettify = BeautifulSoup.prettify
r = re.compile(r'^(\s*)', re.MULTILINE)
def prettify(self, encoding=None, formatter="minimal", indent_width=4):
    return r.sub(r'\1' * indent_width, orig_prettify(self, encoding, formatter))
BeautifulSoup.prettify = prettify


if __name__ == "__main__":
    linestring = open("E:/Claudio/git/sites/GoodrichTamassiaGoldwasser/file.html", 'r').read()
    soup = BeautifulSoup(linestring)
    text = soup.prettify("utf-8", indent_width=3)
    #text = text.replace('<div class="nav nav-stacked" id="sidebar">', '<br><br><div class="nav nav-stacked" id="sidebar">')
    text_file = open("E:/Claudio/git/sites/GoodrichTamassiaGoldwasser/index.html", "wb")
    text_file.write(text)
    text_file.close()