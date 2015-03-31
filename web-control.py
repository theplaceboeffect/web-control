import random
import string
import cherrypy
import telnetlib

class WebControl(object):
    VSX44_HOST="745E1C78ED7B"
    VSX44_PORT=8102

    def generate_link(self,name,code):
        if name is None:
            return '<p/><a href="/">Return</a>'
        else:
            return '<p/><a href="switch_to_device?name='+name+'&code='+code+'">'+name+'</a>'

    @cherrypy.expose
    def index(self):
        return self.generate_link("PS4","48FN") + \
               self.generate_link("XBOXONE","49FN")

    def switch_to(self,code):
        tn = telnetlib.Telnet(self.VSX44_HOST, self.VSX44_PORT)
        tn.write(str(code) + "\r\n")
        tn.close()

    @cherrypy.expose
    def switch_to_device(self,name,code):
        self.switch_to(code)
        return "["+name+","+code+"]" + "Switched to " + name + self.generate_link(None,None)

if __name__ == '__main__':
    cherrypy.quickstart(WebControl())
