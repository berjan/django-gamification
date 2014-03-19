# -*- coding: utf-8 -*-

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

import json
from django.contrib.auth.models import User
from gamification.core.models import Project
from django.db import models


class Event(models.Model):
    """
    An Event is an action reported by an external system
    """

    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    event_dtg = models.DateTimeField('event date')
    details = models.TextField(editable=False)

    def __init__(self, *args, **kw):
        # dictionary for the details of the event
        self.details_map = {}
        super(Event, self).__init__(*args,**kw)
        if self.details:
            self.details_map = json.loads(self.details)

    def save(self, *args, **kw):
        self.details = json.dumps(self.details_map)
        super(Event, self).save(*args,**kw)



