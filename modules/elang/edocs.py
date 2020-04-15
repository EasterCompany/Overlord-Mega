from os import path
from sys import argv

'''
CLASS EDOC

    E-DOCS MARKUP LANGUAGE, as in hyper text markup language
    but with an edocs wrapper. this class should be set to a 
    templates/pages directory then built locally as a test 
    or for serving in production.
'''


class EDOC:

    def __init__(self, route):
        self.ROUTE = route
        self.HTML_FILES = []        # HTML FILES INCLUDED IN THIS APP
        self.CSS_FILES = []         # CSS  FILES INCLUDED IN THIS APP
        self.JS_FILES = []          # JS   FILES INCLUDED IN THIS APP
        self.SITE_APPS = []         # OTHER APPS INCLUDED IN THIS APP
        self.LOCAL_BUILD = None     # READY TO DISTRIBUTE LOCAL BUILD
        self.SITE_STYLE = False     # DEFAULT SITE CSS STYLE FILE DIR
        self._TEMP_BUILD = open("templates/pages/" +
                                route + "/" + route + ".html").read()
        # Remove redundent spacing
        while "  " in self._TEMP_BUILD:
            self._TEMP_BUILD = self._TEMP_BUILD.replace("  ", " ")

    def distribute_test_build(self):
        return self._TEMP_BUILD

    def compiler(self):
        OUTPUT = self._TEMP_BUILD.\
            replace("\r", "").\
            replace("\n", "").\
            replace("\t", "").\
            replace("<! ", "<!").\
            replace(" !>", "!>").split("<!")

        if not isinstance(OUTPUT, list):
            return "<! edocs compile error !>"

        for tag in OUTPUT:
            tag = tag.split("!>")[0].replace(" ", "")

            # Ignore HTML Comments or Errors
            if tag == "" or \
                    tag.startswith("-") or \
                    tag.endswith("->"):
                pass

            # Define eTag Inclusions
            elif tag.startswith("include:"):
                if tag.endswith("css"): 
                    include_css = True
                elif tag.endswith("site.style"):
                    include_site_style = True
                elif tag.endswith("site.header"):
                    include_site_header = True
                elif tag.endswith("site.footer"):
                    include_site_footer = True
                elif tag.endswith("js"):
                    include_js = True
                elif tag.endswith("site"):
                    include_site = True

            # Read eTag -> Replace with Content
            else:

                # Check for HTML files that match the tag
                if path.exists("./templates/pages/" + self.ROUTE + "/" + tag + ".html"):
                    self.HTML_FILES.append(
                        (
                            "<!" + tag + "!>",
                            open("./templates/pages/" + self.ROUTE +
                                 "/" + tag + ".html").read()
                        )
                    )

                if path.exists("./templates/site/header.html") and include_site_header:
                    self.HTML_FILES.append(
                        (
                            "<!include:site.header!>",
                            open("./templates/site/header.html").read()
                        )
                    )
                
                if path.exists("./templates/site/footer.html") and include_site_footer:
                    self.HTML_FILES.append(
                        (
                            "<!include:site.footer!>",
                            open("./templates/site/footer.html").read()
                        )
                    )

                # Check for CSS files that match the tag > if included
                if path.exists("./templates/pages/" + self.ROUTE + "/" + tag + ".css") and include_css:
                    self.CSS_FILES.append(
                        open("./templates/pages/" +
                             self.ROUTE + "/" + tag + ".css").read()
                    )

                # Check for JS files that match the tag > if included
                if path.exists("./templates/pages/" + self.ROUTE + "/" + tag + ".js") and include_js:
                    self.JS_FILES.append(
                        open("./templates/pages/" +
                             self.ROUTE + "/" + tag + ".js").read()
                    )

                # Check for SITE files that match the tag > if included
                if path.exists("./templates/site/" + tag) and include_site:
                    self.SITE_APPS.append(
                        (
                            "<!" + tag + "!>",
                            open("./templates/site/" + tag).read()
                        )
                    )

                # Check for SITE.STYLE file that match the tag > if included
                if path.exists("./templates/site/style.css") and include_site_style:
                    self.CSS_FILES.append(
                        open("./templates/site/style.css").read())

        # Connect OUTPUT
        OUTPUT = "<!".join(OUTPUT)
        # Replace HTML, CSS, JS eTAGS
        page_header = ""
        page_body = ["<%>", ""]
        page_footer = ""
        for inclusion in self.HTML_FILES:
            print(inclusion)
            if inclusion[0] == "<!include:site.header!>":
                page_header = inclusion[1]
            elif inclusion[0] == "<!include:site.footer!>":
                page_footer = inclusion[1]
            elif inclusion[0] == "<!body!>":
                page_body = inclusion
            else:
                OUTPUT = OUTPUT.replace(inclusion[0], inclusion[1])

        # ADD CSS OUTPUT
        self.JS_FILES = '\n'.join(self.JS_FILES)
        self.CSS_FILES = '\n'.join(self.CSS_FILES)
        OUTPUT = "<script>" + self.JS_FILES + "</script>"\
            "<style>" + self.CSS_FILES + "</style>" + \
            OUTPUT.replace(page_body[0], page_header +
                           page_body[1] + page_footer)

        # When in developer enviroment
        if "debug" in argv:
            return OUTPUT
        # When in production enviroment
        return OUTPUT.replace("\n", "").replace("\r", "")
