#banana.py
#reddit robot using praw

#!/usr/bin/env python
import praw
from robot import RobotBase


class Bananapy(RobotBase):
    pass
    
    
    

banana = Bananapy('bananapy')

r = praw.Reddit('bananapy - member The Robot Enchiladas'
                'v 0.1'
                'Url: https://github.com/bliti/tre')


r.login(username=banana.username, password=banana.password)

post_title='Gone Bananas!'
post_body='Yeah, I know...'

r.submit(banana.subreddit, post_title, text=post_body)    