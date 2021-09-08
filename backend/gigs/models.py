from django.db import models

# Create your models here.

class Gig(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    start_datetime = models.DateTimeField('gig starts')
    end_datetime = models.DateTimeField('gig ends')
    
    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text