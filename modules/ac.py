#!/usr/bin/env python2 
try:
    from activecollab.library import ACRequest
except ImportError:
    print "You need to install pyacollab to use this"

import re
import sys

def ac(phenny, input): 
    """
        Makes a request to an Active Collab install. Needs pyacollab to
        work. 
    """
    ac_filter = input.group(2).split(' ')
    filter_name = ac_filter[0]
    if str.isdigit(str(filter_name)):
        # Assume that we're referencing a project id
        item_id = ac_filter[0]
    else:
        item_id = None

    def _param(num):
        try:
            return ac_filter[num]
        except IndexError:
            return None
        
    subcommand, sub_id = [_param(x) for x in range(1, 3)]
    req = ACRequest('projects', item_id=item_id, subcommand=subcommand, sub_id=sub_id)
    ac_response = req.execute()

    for item in ac_response:
        # If we have an id then print out all the returned data
        if str.isdigit(str(filter_name)):
            phenny.say(item)
        else:
            # Otherwise we're filtering on the project names
            if filter_name in item.lower():
                phenny.say(item)

def setup(self):
    """ 
        I was using this as a quick n easy debug 
        
    class phenny_mock(object):
        def say(self, inp):
            print inp
    dummycmd = re.match("(a):(.*)", "a:31 tickets 5")
    ac(phenny_mock(), dummycmd)
    sys.exit()
    
    """
    pass
                
ac.commands = ['ac',]
ac.priority = 'high'

