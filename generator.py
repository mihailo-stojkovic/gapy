
#Generator class is the base class for all the code generators used in this project
#Every generator consists of a protected field "content" which is a string which holds
#all the code which later will be transfered to a file

class Generator:

    def __init__(self, name_of_file):
        self._content = ""
        self._name = name_of_file

    #Protected method which adds elements at the end of the self._content
    #The method is protected because later every single generator
    #will only have a certain number of elements
    def _add(self, element):
        self._content += element

    @property
    def name(self):
        return self._name

    @property
    def content(self):
        return self._content



    #protected method which adds content to the self._content
    #before the tag (if option == 'b') or after the tag (if option =='a') 
    def _add_content(self, tag, content, option = 'a'):
        
        #used for determening if the content should be before
        #or after the tag
        offset = 0
        
        if option == 'a':
            offset = len(tag)

        pos = self._content.find(tag) + offset
        
        self._content = self._content[ : pos] + content + self._content[pos : ]


class HTMLGenerator(Generator):


    #The constructor of the HTMLGenerator creates a basic html file in a string
    #which has a css and a js file linked
    #Later use of the methods of the HTMLGenerator will add more structure
    #to the string/file
    def __init__(self, name_of_file, css_file_path, js_file_path):
        super().__init__(name_of_file)
        
        self._add("<html><head>")
        self._add('<link rel="stylesheet" type="text/css" href="' + css_file_path + '" />')
        self._add('<script type="text/javascript" src="' + js_file_path + '"> </script>')
        self._add("<title></title></head><body></body></html>")

    #Generates the html file
    #BeautifulSoup4 module is used so that the output html file is
    #easily readable (it will probably be excluded once the project is complete...
    # for now, its good for debugging)
    def generate(self):
        f = open(self.name + ".html", "w")
        from bs4 import BeautifulSoup as bs
        soup = bs(self.content, features="lxml")
        f.write(soup.prettify())
        f.close()
        

#A dummy HTML class which has all of the elements which the base class has
# plus additional text in the body tag (Only used for debugging)
class DummyHTMLGenerator(HTMLGenerator):
    
    def __init__(self, css_file_path = "default.css", js_file_path = "default.js"):
        super().__init__("dummy", css_file_path, js_file_path)
        pos = self.content.find("<body>") + 6
        self._content = self._content[ : pos] + "Dummy HTML file" + self._content[pos : ]

#Prototype of the Javascript Generator class    
class JSGenerator(Generator):
    pass


#Prototype of the CSS Generator class
class CSSGenerator(Generator):
    pass

#Used for debugging
"""
test = DummyHTMLGenerator()
test.generate()
"""