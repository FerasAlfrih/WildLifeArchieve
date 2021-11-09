from os import name
from django.db import models
from PIL import Image
from io import BytesIO
from django.contrib.auth.models import User
from django.core.files import File
from django.db.models.enums import Choices


class Domain(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_slug(self):
        name = self.name.replace(' ', '_')
        slug = name.lower()
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()

        super().save(*args, **kwargs)


class Kingdom(models.Model):
    domain = models.ForeignKey("Domain", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_slug(self):
        name = self.name.replace(' ', '_')
        slug = name.lower()
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()

        super().save(*args, **kwargs)


class Phylum(models.Model):
    domain = models.ForeignKey("Domain", on_delete=models.CASCADE)
    kingdom = models.ForeignKey("Kingdom", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_slug(self):
        name = self.name.replace(' ', '_')
        slug = name.lower()
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()

        super().save(*args, **kwargs)


class Class(models.Model):
    domain = models.ForeignKey("Domain", on_delete=models.CASCADE)
    kingdom = models.ForeignKey("Kingdom", on_delete=models.CASCADE)
    phylum = models.ForeignKey("Phylum", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_slug(self):
        name = self.name.replace(' ', '_')
        slug = name.lower()
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()

        super().save(*args, **kwargs)


class Order(models.Model):
    domain = models.ForeignKey("Domain", on_delete=models.CASCADE)
    kingdom = models.ForeignKey("Kingdom", on_delete=models.CASCADE)
    phylum = models.ForeignKey("Phylum", on_delete=models.CASCADE)
    _class = models.ForeignKey("Class", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_slug(self):
        name = self.name.replace(' ', '_')
        slug = name.lower()
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()

        super().save(*args, **kwargs)


class Family(models.Model):
    domain = models.ForeignKey("Domain", on_delete=models.CASCADE)
    kingdom = models.ForeignKey("Kingdom", on_delete=models.CASCADE)
    phylum = models.ForeignKey("Phylum", on_delete=models.CASCADE)
    _class = models.ForeignKey("Class", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_slug(self):
        name = self.name.replace(' ', '_')
        slug = name.lower()
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()

        super().save(*args, **kwargs)


class Genus(models.Model):
    domain = models.ForeignKey("Domain", on_delete=models.CASCADE)
    kingdom = models.ForeignKey("Kingdom", on_delete=models.CASCADE)
    phylum = models.ForeignKey("Phylum", on_delete=models.CASCADE)
    _class = models.ForeignKey("Class", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    family = models.ForeignKey("Family", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_slug(self):
        name = self.name.replace(' ', '_')
        slug = name.lower()
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()

        super().save(*args, **kwargs)


class Species(models.Model):
    domain = models.ForeignKey("Domain", on_delete=models.CASCADE)
    kingdom = models.ForeignKey("Kingdom", on_delete=models.CASCADE)
    phylum = models.ForeignKey("Phylum", on_delete=models.CASCADE)
    _class = models.ForeignKey("Class", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    family = models.ForeignKey("Family", on_delete=models.CASCADE)
    genus = models.ForeignKey("Genus", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_slug(self):
        name = self.name.replace(' ', '_')
        slug = name.lower()
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()

        super().save(*args, **kwargs)


class Plant(models.Model):
    domain = models.ForeignKey("Domain", on_delete=models.CASCADE)
    kingdom = models.ForeignKey("Kingdom", on_delete=models.CASCADE)
    phylum = models.ForeignKey("Phylum", on_delete=models.CASCADE)
    _class = models.ForeignKey("Class", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    family = models.ForeignKey("Family", on_delete=models.CASCADE)
    genus = models.ForeignKey("Genus", on_delete=models.CASCADE)
    species = models.ForeignKey("Species", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status_options = [
        ('EX' , 'Extinct'),
        ('EW' , 'Extinct in the wild'),
        ('CR' , 'Critically Endangered'),
        ('EN' , 'Endangered'),
        ('VU' , 'Vulnerable'),
        ('NT' , 'Near Threatened'),
        ('CD' , 'Conservation Dependent'),
        ('LC' , 'Least Concern'),
        ('DD' , 'Data deficient'),
        ('NE' , 'Not evaluated',) 
    ]
    status = models.CharField( max_length=255, choices=status_options, default='LC')
    statusH = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255)
    source_link = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='plantsUpload/', blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='plantsUpload/thumbUploads/', blank=True, null=True)
    thumbnail_url = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    tree = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return f'/{self.slug}'

    def get_tree(self):
        return f'{self.domain}/{self.kingdom}/{self.phylum}/{self._class}/{self.order}/{self.family}/{self.genus}/{self.species}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(250, 250)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'jpeg', quality=100)

        thumbnail = File(thumb_io, name='thumb_' + image.name)
        return thumbnail

    def get_slug(self):
        name = self.name.replace(' ', '_')
        slug = name.lower()
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()
        if not self.thumbnail:
            self.thumbnail = self.make_thumbnail(self.image)
        self.image_url = self.get_image()
        self.thumbnail_url = self.get_thumbnail()
        self.tree = self.get_tree()
        self.statusH = self.get_status_display()
        super().save(*args, **kwargs)


class PlantImages(models.Model):
    plant = models.ForeignKey("Plant", on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=50)

    def get_name(self):
        self.name = self.plant.name + '_' + self.pk
        return self.name

    def __str__(self):
        return self.name
