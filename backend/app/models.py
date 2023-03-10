from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name_company = models.CharField(max_length=1000)
    info = models.TextField(max_length=10000)#информация о компании
    
    def __str__(self):
        return f"Название компании {self.name_company}\n Информация \n{self.info[:20]}..."
    
    def __repr__(self) -> str:
        return f"pk {self.pk}| name company {self.name_company}\n Информация \n{self.info[:20]}..."
    
    class Meta:
        db_table = "company"
        # ordering = ["id"]


class HardSkill(models.Model):
    skill = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return f" skill {self.skill}"
    
    class Meta:
        db_name = "hard_skill"


class SoftSkill(models.Model):
    skill = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return f" skill {self.skill}"
    
    class Meta:
        db_name = "soft_skill"






class CustomUser(AbstractUser):#Собсвенный BaseUser вместо дефолтного User Django
    password = models.CharField(max_length=100)
    # role = models.ManyToManyField(Group)
    contact = models.CharField(max_length=200)
    
    def __str__(self):
        return f"email {self.email} role {self.role}"
    
    
    def __repr__(self) -> str:
         return f" pk {self.pk}|email {self.email}|role {self.role}"
    
    class Meta:
        db_table = "custom_user"
        abstract = True
        exclude = ('username')
        # default_related_name = "user"


class Employer(CustomUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    
    class Meta:
        db_table = "employer"
        abstract = False
        
        
class Worker(CustomUser):
    age = models.CharField(max_length=200)
    moving = models.BooleanField()
    
    class Meta:
        db_table = "worker"
        abstract = False
    



class Resume(models.Model):
    hard_skill = models.ManyToManyField(HardSkill)#потестиить мб как JsonField
    soft_skill = models.ManyToManyField(SoftSkill)
    Worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "resume"
        