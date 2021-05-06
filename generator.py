
#Generator class is the base class for all the code generators used in this project
#Every generator consists of a protected field "content" which is a string which holds
#all the code which later will be transfered to a file

class Generator:

    def __init__(self, name_of_file):
        self._content = ""
        self._name = name_of_file


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



class HTMLGenerator(Generator):


    #The constructor of the HTMLGenerator creates a basic html file in a string
    #which has a css and a js file linked
    #Later use of the methods of the HTMLGenerator will add more structure
    #to the string/file
    def __init__(self, name_of_file, css_file_path, js_file_path):
        super().__init__(name_of_file)
        
        self._add("<html>\n<head>\n")
        self._add('<link rel="stylesheet" type="text/css" href="' + css_file_path + '" />\n')
        self._add('<script type="text/javascript" src="' + js_file_path + '"> </script>\n')
        self._add("<title>\n</title>\n</head>\n<body>\n</body>\n</html>")


    def generate(self):
        f = open(self.name + ".html", "w")
        f.write(self.content)
        f.close()
        


class DummyHTMLGenerator(HTMLGenerator):
    
    def __init__(self, css_file_path = "default.css", js_file_path = "default.js"):
        super().__init__("dummy", css_file_path, js_file_path)
        pos = self.content.find("<body>") + 6
        self._content = self._content[ : pos] + "Dummy HTML file" + self._content[pos : ]
    