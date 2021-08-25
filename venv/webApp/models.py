from django.db import models
from django.contrib.auth.models import User
# gender types for selection.
GENDER = (
    ('male', "MALE"),
    ('female', "FEMALE"),
    ('other', "OTHER"),
)
# education type search entry
EDU_LEVEL = (
    ('primary',"PRIMARY"),
    ('o-Level',"O-LEVEL"),
    ('a-level', "A-LEVEL"),
    ('bachelor', "BARCHELOR")
)

# User profile
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="img/faces", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=150, null=True, blank=True)

    @property
    def get_avatar(self):
        return self.avatar.url

# class SearchEntry(models.Model):
#     educationLevel =  models.CharField(max_length=10, choices=EDU_LEVEL, null=True, blank=True)
class UniversityCatalogue(models.Model):
    uni_name = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=10, null=True, blank=True)
    inst_type = models.CharField(max_length=100, null=True, blank=True)
    ownership = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.uni_name

class ProgrammeRequirement(models.Model):
    uni_id = models.ForeignKey(UniversityCatalogue,on_delete=models.CASCADE)
    prog_name = models.CharField(max_length=1000, null=True, blank=True)
    pro_code = models.CharField(max_length=10, null=True, blank=True)
    requirement = models.CharField(max_length=500,null=True,blank=True)
    duration = models.CharField(max_length=100,null=True,blank=True)
    capacity = models.CharField(max_length=10,null=True,blank=True)
    GPA = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.prog_name

class NewsAndUpdates(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    doc = models.ImageField(upload_to="media/", null=True, blank=True)

    def __str__(self):
        return self.title