from zope.interface import Interface

from plone.theme.interfaces import IDefaultPloneLayer

class IRohbergUtilsLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """
    
class IRohbergUtilsProvider(Interface):

    def _is_new(self, modified):
        """ is new since last login
        """