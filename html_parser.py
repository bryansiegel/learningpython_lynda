from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("encountered data",data)
        pos = self.getpos()
        print("at ine ", pos[0], "postition ", pos[1])

parser = MyHTMLParser()

f = open("samplehtml.html")
if f.mode == 'r':
    contents = f.read()
    parser.feed(contents)
