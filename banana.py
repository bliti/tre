#banana.py
#reddit robot using praw

#!/usr/bin/env python
import praw
import json


#TRE = The Robot Enchilada.
#Base class for all other robots.
class TRE(object):
        
        
        def __init__(self, robot_name):
            with open('settings.json', 'r') as f:
                settings = json.loads(f.read())
            self.settings = settings[robot_name] 
            

