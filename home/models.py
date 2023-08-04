from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class AboutMe(models.Model):

    title = models.CharField(max_length=234)
    mini_desk = models.CharField(max_length=233)

    description = models.TextField()

    # Person haqqinda
    name = models.CharField(max_length=232)
    birthday = models.CharField(max_length=232)
    mail = models.CharField(max_length=232)
    phone = models.IntegerField(default="998995099251")
    address = models.CharField(max_length=232)
    millati = models.CharField(max_length=232)

    image = models.ImageField(upload_to="about/img/")


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = "Men Xaqimda"
        verbose_name_plural = "Men Xaqimda"
    

class Education(models.Model):

    title = models.CharField(max_length=234)
    mini_title = models.CharField(max_length=234)

    description = models.TextField()

    yillar = models.TextField()



class Experience(models.Model):

    title = models.CharField(max_length=234)
    mini_title = models.CharField(max_length=234)

    description = models.TextField()

    yillar = models.TextField()


    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = "Soha haqida"
        verbose_name_plural = "Sohalar haqida"



class PortfolioCategory(MPTTModel):

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)


    class MPTTMeta:
        order_insertion_by = ['name']
 

    def get_full_path(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])


    def __str__(self):
        return self.get_full_path()



class Portfolio(models.Model):

    imagename = models.CharField(max_length=255)
    image = models.ImageField(upload_to="portfolio/img/", blank=True, null=True)
    video = models.FileField(upload_to="portfolio/video/", blank=True, null=True)
    category = models.ForeignKey(PortfolioCategory, blank=True, null=True, on_delete=models.CASCADE)

    title_video = models.CharField(max_length=223)

    def __str__(self) -> str:
        return self.imagename



class Service(MPTTModel):

    """ Never compromise with quality """
    icon = models.ImageField(upload_to="service/icon/")
    title = models.CharField(max_length=234)
    desc = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    


class Testimonials(MPTTModel):

    """ What people say about me """

    text = models.TextField()
    author = models.CharField(max_length=234)
    yonalishi = models.CharField(max_length=234)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    

    def __str__(self) -> str:
        return self.author



class Blog(MPTTModel):

    """ Latest tips, tricks & Updates """

    title = models.CharField(max_length=234)
    category = models.CharField(max_length=234)
    desc = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)


    def __str__(self) -> str:
        return self.title

    

class Contact(models.Model):

    """Contact me to get your work done"""

    title = models.CharField(max_length=234)
    info = models.CharField(max_length=234)

    icon = models.ImageField(upload_to="contact/img/")

    def __str__(self) -> str:
        return self.title


#                                  Inline Models                                 

class Konikmalar(models.Model):
    # experience = models.ForeignKey(to=Experience, null=True, blank=True, on_delete=models.CASCADE)

    title = models.CharField(max_length=233, null=True, blank=True)
    foiz = models.IntegerField(default=90)

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = "Konikma"
        verbose_name_plural = "Konikmalar"

