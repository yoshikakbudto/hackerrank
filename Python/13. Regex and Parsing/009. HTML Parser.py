#! /bin/env python2
# Problem: https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true
# Score: 30


from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : {}".format(tag))
        for attr_name,attr_value in attrs:
            print("-> {} > {}".format(attr_name, attr_value))
    def handle_endtag(self, tag):
        print("End   : {}".format(tag))
    def handle_startendtag(self, tag, attrs):
        print("Empty : {}".format(tag))
        for attr_name,attr_value in attrs:
            print("-> {} > {}".format(attr_name, attr_value))

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()


for _ in range(int(input())):
    parser.feed(raw_input())