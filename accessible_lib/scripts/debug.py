"""Debug module formatting prints"""

from .constants import CHILDID_SELF

DEBUG_ENABLED = False

def print_accessible(node):
    """Print the accessible name and role"""
    name = _unicode(node.accName(CHILDID_SELF))
    print '--------------------------'
    print 'Accessible Object'
    print node
    print 'Name: %s' %name
    print 'Role: %s' %node.accRole(CHILDID_SELF)
    print '--------------------------'

def print_simple(node, childid):
    """Print the simple element owner, name and role"""
    name = _unicode(node.accName(childid))
    print '--------------------------'
    print 'Simple Element'
    print 'Owner:%s' %node
    print 'Name: %s' %name
    print 'Role: %s' %node.accRole(childid)
    print '--------------------------'

def _unicode(name):
    if name:
        return name.encode('utf8')
