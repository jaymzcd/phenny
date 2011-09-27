#!/usr/bin/env python2 

from activecollab.library import ACRequest

def ac(phenny, input): 
    filter_name = input.group(2)
    item_id, subcommand, sub_id = None, None, None
    req = ACRequest('projects', item_id=item_id, subcommand=subcommand, sub_id=sub_id)
    for item in req.execute():
        if filter_name in item:
            phenny.say(item)

ac.commands = ['ac']
ac.priority = 'high'

