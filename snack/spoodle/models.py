from django.db import models

# Create your models here.


class Class(models.Model):
    """
    Model representing a Class.
    """
    name = models.CharField(max_length=200)
    monday = models.NullBooleanField()
    tuesday = models.NullBooleanField()
    wednesday = models.NullBooleanField()
    thursday = models.NullBooleanField()
    friday = models.NullBooleanField()
    start = models.TimeField(blank = True, null = True)
    end = models.TimeField(blank = True, null = True)
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
		
class Student(models.Model):
    """
    Model representing a student.
    """
    name = models.CharField(max_length=200)
    classes = models.ManyToManyField(Class)
    id = models.CharField('ID',max_length=8, help_text='8 digit Student ID number',primary_key=True)
    email = models.EmailField(primary_key=True)
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
		
class Todo(models.Model):
    """
    Model representing a todo item (e.g. mow the lawn).
    """
    student = models.ForeignKey('Student')
    activity = models.CharField(max_length=200, help_text="Enter a task you have to do.")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.activity
		
class Professor(models.Model):
    """
    Model representing a professor.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10, help_text='Ten digit phone number, no dashes')
    office = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    classes= models.ForeignKey(Class)
    
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
		
class Homework(models.Model):
    """
    Model representing a homework assignment.
    """
    title = models.CharField(max_length=200)
    duedate = models.DateField()
    classes = models.ForeignKey(Class)
    
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
		
class Note(models.Model):
    """"
	Model representing a class note
	"""
    title = models.CharField(max_length=100)
    note = models.TextField()
    classes = models.ForeignKey(Class)
	
    def __str__(self):
        return self.title

