# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, as long as
# any reuse or further development of the software attributes the
# National Geospatial-Intelligence Agency (NGA) authorship as follows:
# 'This software (django-gamification)
# is provided to the public as a courtesy of the National
# Geospatial-Intelligence Agency.
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

class State(object):
    
    def __init__(self, user_id, project_id, event_data):
        self._user_id = user_id
        self._project_id = project_id
        self._event_data = event_data # A dictionary (with event type as key) of dictionaries
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def project_id(self):
        return self._project_id
    
    @property
    def event_data(self):
        return self._event_data
        
    def award_badge(self, user_id, project_id, badge_id):
        #TODO: Update database with badge info instead
        print ('\n{0} awarded {1} badge for {2}'.format(user_id, badge_id, project_id))