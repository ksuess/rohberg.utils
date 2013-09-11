from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.ATContentTypes.interfaces import IATContentType
from rohberg.utils.interfaces import IRohbergUtilsProvider

from rohberg.utils import RUMessageFactory as _

class TabularViewPlus(BrowserView):
    """new since last login"""
    
    template = ViewPageTemplateFile("tabularviewplus.pt")
    
    def new_icon(self, item):
        """ If item is new to logged in user, then return image tag for icon """
        obj = item.getObject()
        plus_provider = IRohbergUtilsProvider(obj)
        if plus_provider._is_new(obj.modified()):
            return '<img src="new.gif">' 
                
    def __call__(self):
        return self.template()