from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

# plan to use Django user
# plan to use Django permission
class User(models.Model):
    email = models.EmailField(max_length = 100, unique = True)
    name = models.CharField(max_length = 100)
    USER_TYPE = (('STU','Student'), ('STA','Staff'),('FAC','Faculty'))
    user_type = models.CharField(max_length = 3, choices = USER_TYPE, default = 'STU')
    pswd = models.CharField(max_length = 128)

    


class Petition(models.Model):

	userID = models.ForeignKey(User, to_field = 'email', on_delete=models.CASCADE)
	# petitionID
	petitionID = models.IntegerField()

	# category
	ACADEMICS = 'AC'
	ADMINISTRATIVE_ACTION = 'AA'
	DINING_HALLS = 'DH'
	SCHOOL_RECIDENCY = 'SR'
	OTHERS = 'OT'
	PETITION_CATEGORY_CHOICES = (
		(ACADEMICS,'Academics'),
		(ADMINISTRATIVE_ACTION, 'Administrative Action'),
		(DINING_HALLS, 'Dining Halls'),
		(SCHOOL_RECIDENCY, 'School Recidency'),
		(OTHERS,'Others'),
		)
	category = models.CharField(
		max_length = 2
		# choices = PETITION_CATEGORY_CHOICES,
		# default = ACADEMICS,
		)
	# open time
	open_time = models.DateField()
	# close time: no later than open_time
	close_time = models.DateField()
	# threshold: say > 5 for now
	threshold = models.IntegerField()
	# permissions
	# stu_permission = models.ManyToManyField('Permission')
	# staff_permission = models.ManyToManyField('Permission')
	# faculty_permission = models.ManyToManyField('Permission')
	finalized = models.BooleanField()

class Clause(models.Model):
	petitionID = models.ForeignKey(Petition, on_delete=models.CASCADE)
	index = models.IntegerField()
	title = models.CharField(max_length = 64) # change 64 as needed
	content = models.TextField()
	time = models.DateTimeField(auto_now_add=True) #what does the bool do?!

class Change(models.Model):
	userID = models.ForeignKey(User, to_field = 'email', on_delete=models.CASCADE)
	chid = models.IntegerField()
	content = models.TextField()
	decision = models.IntegerField() #limit this to 1, 2, 3

class Comment(models.Model):
	userID = models.ForeignKey(User, to_field = 'email', on_delete=models.CASCADE)
	cid = models.IntegerField()
	content = models.TextField()

class Sign(models.Model):
	userID = models.ForeignKey(User, to_field = 'email', on_delete=models.CASCADE)
	petitionID = models.ForeignKey(Petition) #on-delete???
	time = models.DateTimeField()

class ChangeVote(models.Model):
	userID = models.ForeignKey(User, to_field = 'email', on_delete=models.CASCADE)
	chid = models.ForeignKey(Change, on_delete=models.CASCADE)
	vote = models.BooleanField()

class CommentVote(models.Model):
	userID = models.ForeignKey(User, to_field = 'email', on_delete=models.CASCADE)
	cid = models.ForeignKey(Comment, on_delete=models.CASCADE)
	vote = models.BooleanField()




