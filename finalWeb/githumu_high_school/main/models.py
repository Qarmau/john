from django.db import models


offices=[('CHIEF PRINCIPAL','CHIEF PRINCIPAL'),
        ('DEPUTY PRINCIPAL(ADMIN)','DEPUTY PRINCIPAL(ADMIN)'),
        ('DEPUTY PRINCIPAL(ACAD)','DEPUTY PRINCIPAL(ACAD)'),
        ('DEAN','DEAN'),
        ('HOD MATHEMATICS','HOD MATHEMATICS'),
        ('HOD SCIENCE','HOD SCIENCE'),
        ('HOD ENGLISH','HOD ENGLISH'),
        ('HOD KISWAHILI','HOD KISWAHILI'), 
        ('HOD HUMANITIES','HOD HUMANITIES'),
        ('HOD TECHNICALS','HOD TECHNICALS'),
        ('HOD G&C','HOD G&C'),
        ('HOD CAREERS','HOD CAREERS'),
        ('HOD SPORTS','HOD SPORTS'),
        ('HOS','HOS')]

gender=[('Mr', 'Mr'), 
        ('Mrs', 'Mrs'), 
        ('Ms', 'Ms')]

subjects=[
    ('BIO & CHEM','BIO & CHEM'),
    ('PHYS & CHEM','PHY & CHEM'),
    ('MATH & PHY','MATH & PHY'),
    ('MATH & CHEM','MATH & CHEM'),
    ('HIS & CRE','HIS & CRE'),
    ('GEO & HIS','GEO & HIS'),
    ('HIS & KIS','HIS & KIS'),
    ('KIS & CRE','KIS & CRE'),
    ('ENG/LIT','ENG/LIT'),
    ('MATH/COMP','MATH/COMP'),
    ('MATH/BUS','MATH/BUS'),
    ('HSC/BIO','HSC/BIO'),
    ('MATH/GEO','MATH/GEO')
]
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
 
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    mynews = models.FileField(upload_to='news_info/')
    
    class Meta: 
        verbose_name = ("News")
        verbose_name_plural = ("News")

class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

class About(models.Model):
    history = models.TextField(help_text="Enter each point on a new line")
    population = models.IntegerField()
    school_motto = models.CharField(max_length=200)
    vision = models.TextField()
    mission = models.TextField()
    subjects_offered = models.TextField(help_text="Enter each subject on a new line")
    clubs_and_societies = models.TextField(help_text="Enter each club/society on a new line")
    contact_information = models.TextField()
    email = models.EmailField()
    class Meta:
        verbose_name = ("about")
        verbose_name_plural = ("about")

class Administrator(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=10,choices=gender)
    photo = models.ImageField(upload_to='admin_photos/')
    order = models.IntegerField(default=0)
    role = models.CharField(max_length=100, blank=True, choices=offices)
    subjects = models.CharField(max_length=200, blank=True ,choices=subjects)
   
  

class TeachingStaff(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=10, choices=gender)
    role = models.CharField(max_length=100, blank=True, choices=offices)
    subjects = models.CharField(max_length=200,choices=subjects)
    photo = models.ImageField(upload_to='staff_photos/')
    order = models.IntegerField(default=0)

    

class Achievement(models.Model):
    year = models.IntegerField()
    university_admission_rate = models.FloatField()

class CoCurricularAward(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='award_photos/')

class HolidayAssignment(models.Model):
    title = models.CharField(max_length=200)
    grade = models.CharField(max_length=50)
    file = models.FileField(upload_to='assignments/')
    date_uploaded = models.DateTimeField(auto_now_add=True)

class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='background_images/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Background Image {self.order}"
