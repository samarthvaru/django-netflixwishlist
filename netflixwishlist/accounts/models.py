from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=15,null=True)
    email=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(default='logo.png',null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
        GENRE=(
            ('Horror','Horror'),
            ('Comedy','Comedy'),
            ('Thriller','Thriller'),
            ('Documentary','Documentary'),
            ('Romantic','Romantic'),
            ('Short Film','Short Film'),
            ('Action','Action')
        )

        genre=models.CharField(max_length=50,null=True,choices=GENRE)

        def __str__(self):
            return self.genre

class ListItem(models.Model):


    STREAMINGPARTNER=(
                         ('Netflix','Netflix'),
                         ('Prime Video','Prime Video'),
                         ('Hotstar','Hotstar'),
                         ('Voot','Voot'),
                         ('Disney+','Disney+'),
                         ('Zee 5','Zee 5'),
                         ('Other','Other')
    )

    BINGEINTEREST = (
        ('Very Likely', 'Very Likely'),
        ('Likely', 'Likely'),
        ('Maybe', 'Maybe')
    )

    STATUS=(
        ('Not Watched','Not Watched'),
        ('Watched','Watched')
    )



    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=200,null=True)
    tag=models.ManyToManyField(Tag)
    bingeinterest=models.CharField(max_length=50,null=True,choices=BINGEINTEREST)
    note=models.CharField(default='Not watched',max_length=50,null=True,choices=STATUS)
    streamService=models.CharField(max_length=200,null=True,choices=STREAMINGPARTNER)

    def __str__(self):
        return self.name





