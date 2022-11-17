from pyexpat import model
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
# Create your models here.
class Questions(models.Model):
    title = models.CharField(max_length = 250)
    description = models.CharField(max_length = 1000)
    image = models.ImageField(upload_to ="image", null = True)
    created_date = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE )
    def __str__(self):
        return self.title
    #question ans orumichu varan
    @property
    def question_answers(self):
        qs = self.answers_set.all().annotate(u_count = Count("up_vote")).order_by('-u_count')
        return qs
        #-u_count -dec order
        
        # return self.answers_set.all()
#for listing answers in decreasing order of upvote
    
class Answers(models.Model):
    question = models.ForeignKey(Questions,on_delete = models.CASCADE)
    answer =  models.CharField(max_length = 5000)
    user = models.ForeignKey(User,on_delete = models.CASCADE )
    created_date = models.DateField(auto_now_add = True)
    up_vote = models.ManyToManyField(User,related_name = "upvote")
    def __str__(self):
        return self.answer
    @property
    def votecount(self):
        return self.up_vote.all().count()
#for upvote count

#python manage.py createsuperuser
#python manage.py shell
#from api.models import Questions,Answers
    
