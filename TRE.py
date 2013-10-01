#!/usr/bin/env python
import json


#TRE = The Robot Enchilada.
#Base class for all other robots.
class TRE(object):
        
        
        def __init__(self, robot_name):
            with open('settings.json', 'r') as f:
                settings = json.loads(f.read())
            self.settings = settings[robot_name]
            self.username = settings[robot_name]['username']
            self.password = settings[robot_name]['password']
            self.subreddit = settings['subreddit']        
        