from django.db import models
import datetime

class Poll(models.Model):
    question = models.CharField('Question', max_length=200)
    pub_date = models.DateTimeField('Date de publication')
    def __unicode__(self):
        return self.question
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField('Choix', max_length=200)
    votes = models.IntegerField('Votes')
    def __unicode__(self):
        return self.choice