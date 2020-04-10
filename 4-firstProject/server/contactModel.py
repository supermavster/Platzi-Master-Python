from google.appengine.ext import ndb

class Contact(ndb.Model):
    name = ndb.StringProperty()
    number = ndb.StringProperty()
    email = ndb.StringProperty()