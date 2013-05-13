from zope.interface import implements
from Acquisition import aq_base, aq_parent, aq_inner
from zope.component.hooks import getSite
from DateTime.DateTime import DateTime

from rohberg.utils.interfaces import IRohbergUtilsProvider

class RohbergUtilsProvider(object):
    """ Provider for both AT und Dexterity"""

    implements(IRohbergUtilsProvider)

    def __init__(self, context):
        # Each adapter takes the object itself as the construction
        # parameter and possibly provides other parameters for the
        # interface adaption
        self.context = context
        self.portal = getSite()

    def _is_new(self, modified):
        llt = getattr(aq_base(self), '_last_login_time', [])
        if llt == []:
            m = self.portal.portal_membership.getAuthenticatedMember()
            if m.has_role('Anonymous'):
                llt = self._last_login_time = None
            else:
                llt = self._last_login_time = m.getProperty('last_login_time', 0)
        if llt is None: # not logged in
            return False
        elif llt == 0: # never logged in before
            return True
        else:
            return (modified >= DateTime(llt))

