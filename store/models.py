from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Contact_us(models.Model):
    """
    Contact form model
    """
    NEW_EMAIL = "NEW"
    PENDING_EMAIL = "PENDING"
    DONE_EMAIL = "DONE"
    STATUS = [
        (NEW_EMAIL, 'NEW'),
        (PENDING_EMAIL, 'PENDING'),
        (DONE_EMAIL, 'DONE'),
    ]

    class Meta:
        verbose_name_plural = 'Contact Us Forms'

    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=50)
    contact_details = models.CharField(max_length=5000)
    sent_date = models.DateTimeField(auto_now_add=True)
    email_status = models.CharField(
        max_length=10,
        choices=STATUS,
        default=NEW_EMAIL,
        )

    def __str__(self):
        return str(self.contact_name)


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254)
    session_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.user:
            name = self.user
        else:
            name = self.session_id
        return str(name)


@receiver(post_save, sender=User)
def create_or_update_customer(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Customer.objects.create(user=instance)
    # Existing users: just save the profile
    instance.customer.save()


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=100, null=True, unique=True)
    description = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])


class Product(models.Model):
    STEEL = (
        ('Maru Steel', (
            ('T10 steel', 'T10 steel'),
            ('1095 steel', '1095 steel'),
            ('Manganese steel', 'Manganese steel'),
        )),
        ('Damascus Steel', 'Damascus Steel'),
        ('Kobuse Forge Steel', 'Kobuse Forge Steel'),
        ('San-Mai Forge Steel', 'San-Mai Forge Steel'),
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    blade = models.CharField(choices=STEEL, max_length=200, null=True)
    guard = models.CharField(max_length=200, null=True)
    scabbard = models.CharField(max_length=200, null=True)
    handle = models.CharField(max_length=200, null=True)
    length_with_sleeve = models.FloatField(null=True)
    length_of_the_blade = models.FloatField(null=True)
    length_of_the_handle = models.FloatField(null=True)
    width_of_the_blade = models.FloatField(null=True)
    blade_thickness = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    description = models.TextField(blank=True)
    stock = models.IntegerField(blank=False, null=True)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except ValueError:
            url = ''
        return url
