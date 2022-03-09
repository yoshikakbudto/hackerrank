# Problem: https://www.hackerrank.com/challenges/html-parser-part-2/problem?isFullScreen=false
# Score: 30

from html.parser import HTMLParser
class CustomHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

parser = CustomHTMLParser()

html_string = ''
for _ in range(int(input())):
    html_string += input().rstrip()+'\n'
parser.feed(html_string)
parser.close()
