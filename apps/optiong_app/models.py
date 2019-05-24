from __future__ import unicode_literals
from django.db import models
from ..lognreg_app.models import LogNReg
import re



class OptionGMessage(models.Manager):
    def quote_validator(self, postData):

        quote_errors = {}

        if len(postData['author']) < 4:
            quote_errors["author"] = "author no less than 3 characters"
        if len(postData['text']) < 11:
            quote_errors["text"] = "quote no less than 10 characters"
            

        
        return quote_errors





class Quote(models.Model):
    users = models.ForeignKey(LogNReg, related_name = "messages")
    likes = models.ManyToManyField(LogNReg, related_name = "Message")
    authors = models.CharField(max_length = 45)
    quotes = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = OptionGMessage()

    def __repr__(self):
        return f"{self.likes} {self.message} {self.users} {self.created_at} {self.updated_at}"