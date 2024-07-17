from django.db import models
from django.db.models import Model
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)


class Category(BaseModel):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE, related_name='products')
    shipping_price = models.FloatField()
    quantity = models.IntegerField()
    discount = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def discount_price(self):
        return self.price - (self.discount * self.price / 100)




class Specification(Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    product = models.ForeignKey('apps.Product', on_delete=models.CASCADE, related_name='specifications')

    def __str__(self):
        return self.key


class ProductImage(Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('apps.Product', on_delete=models.CASCADE,
                                related_name='images')


# models.py
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
