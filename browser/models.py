from django.db import models
from django.core.validators import RegexValidator
import uuid
from django_extensions.db.fields import UUIDField

def get_brand_default():
    return 'ZZZZZZ'

def get_color_default():
    return 1

# Gtin contains products with a GTIN-13
class Gtin(models.Model):
    GTIN_ID = UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    GTIN_CD = models.CharField(max_length=13, validators=[RegexValidator(regex='^.{13}$', message='Length has to be 13', code='nomatch')], null=True, blank=True)
    GCP_CD = models.ForeignKey('Gs1_gcp', null=True, blank=True)
    BSIN = models.ForeignKey('Brand', default=get_brand_default)
    CAT_CD = models.ForeignKey('Category', null=True, blank=True, default=1)
    PKG_UNIT = models.IntegerField(default=0, null=True, blank=True)
    PACKAGING_CD = models.ForeignKey('Packaging', null=True, blank=True)
    METHOD_CD = models.ForeignKey('Method', null=True, blank=True)
    SIZE_CD = models.ForeignKey('Size', null=True, blank=True)
    GRADE_CD = models.ForeignKey('Grade', null=True, blank=True)
    COLOR_CD = models.ForeignKey('Color', null=True, blank=True, default=get_color_default)
    FED_CD = models.ForeignKey('Fed', null=True, blank=True)
    LABEL_CD = models.ManyToManyField('Label', blank=True)
    def __str__(self):
        return self.GTIN_CD
    class Meta:
        ordering = ('METHOD_CD','SIZE_CD','GTIN_CD', )
# Using multi table inheritance - automaticly creates one to one field
#class GtinPackagingDetail(Gtin):
#    PACKAGING_2_CD = models.ForeignKey('Packaging', null=True, blank=True)

class Label(models.Model):
    LABEL_CD = models.AutoField(primary_key=True)
    LABEL_NM = models.CharField(max_length=255)
    LABEL_COUNTRY_ISO = models.ForeignKey('Country', null=True, blank=True)
    LABEL_DESC = models.TextField(null=True, blank=True)
    LABEL_LINK = models.CharField(max_length=255, null=True, blank=True)
    LABEL_WIKI_EN = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return u'%s - %s' % (self.LABEL_COUNTRY_ISO, self.LABEL_NM )
    class Meta:
        ordering = ('LABEL_COUNTRY_ISO', 'LABEL_NM',)

class Color(models.Model):
    COLOR_CD = models.AutoField(primary_key=True)
    COLOR_NM = models.CharField(max_length=255)
    COLOR_DESC = models.TextField(null=True, blank=True)
    def __str__(self):
        return u'%s' % (self.COLOR_NM )

class Fed(models.Model):
    FED_CD = models.AutoField(primary_key=True)
    FED_NM = models.CharField(max_length=255)
    FED_DESC = models.TextField(null=True, blank=True)
    def __str__(self):
        return u'%s' % (self.FED_NM )


class Size(models.Model):
    SIZE_CD = models.AutoField(primary_key=True)
    SIZE_NM = models.CharField(max_length=255)
    SIZE_SIZE_NM = models.CharField(max_length=255,null=True, blank=True)
    SIZE_DESC = models.TextField(null=True, blank=True)
    def __str__(self):
        return u'%s' % (self.SIZE_NM )
    class Meta:
        ordering = ('SIZE_NM', )

class Grade(models.Model):
    GRADE_CD =  models.AutoField(primary_key=True)
    GRADE_NM = models.CharField(max_length=255)
    GRADE_SHORT_NM = models.CharField(max_length=255,null=True, blank=True)
    GRADE_DESC = models.TextField(null=True, blank=True)
    def __str__(self):
        return u'%s' % (self.GRADE_NM)

class Method(models.Model):
    METHOD_CD = models.AutoField(primary_key=True)
    METHOD_NM = models.CharField(max_length=255)
    METHOD_ISO = models.ForeignKey('Country', null=True, blank=True)
    METHOD_DESC = models.TextField(null=True, blank=True)
    METHOD_LEVEL_CD = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return u'%s - %s' % (self.METHOD_ISO, self.METHOD_NM)
    class Meta:
        ordering = ('METHOD_ISO', 'METHOD_NM',)

class Packaging(models.Model):
    PACKAGING_CD = models.AutoField(primary_key=True)
    PACKAGING_NM = models.CharField(max_length=255)
    PACKAGING_LINK = models.CharField(max_length=255,null=True, blank=True)
    def __str__(self):
        return u'%s - %s' % (self.PACKAGING_CD, self.PACKAGING_NM)

class Category(models.Model):
    CAT_CD = models.AutoField(primary_key=True)
    CAT_NM = models.CharField(max_length=255)
    CAT_LINK = models.CharField(max_length=255,null=True, blank=True)
    def __str__(self):
        return u'%s - %s' % (self.CAT_CD, self.CAT_NM)

class Brand(models.Model):
    BSIN = models.CharField(max_length=6, primary_key=True)
    BRAND_NM = models.CharField(max_length=255)
    BRAND_TYPE_CD = models.ForeignKey('Brand_type', null=True, blank=True)
    BRAND_LINK = models.CharField(max_length=255, null=True, blank=True)
    BRAND_COUNTRY_ISO = models.ForeignKey('Country')
    OWNER_CD = models.ForeignKey('Owner', null=True, blank=True)
    BRAND_OPEN = models.NullBooleanField(default=False, null=True, blank=True)
    BRAND_DISPLAY = models.NullBooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return u'%s - %s' % (self.BRAND_NM, self.BSIN)

    class Meta:
        ordering = ('BRAND_NM', )

class Brand_type(models.Model):
    BRAND_TYPE_CD = models.AutoField(primary_key=True)
    BRAND_TYPE_NM = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.BRAND_TYPE_NM

class Owner(models.Model):
    OWNER_CD = models.AutoField(primary_key=True)
    OWNER_NM = models.CharField(max_length=255, null=True, blank=True)
    OWNER_LINK = models.CharField(max_length=255, null=True, blank=True)
    OWNER_COUNTRY_ISO = models.ForeignKey('Country')
    OWNER_WIKI_EN = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return u'%s - %s' % (self.OWNER_CD, self.OWNER_NM)
    class Meta:
        ordering = ('OWNER_NM', )

class Orga(models.Model):
    ORGA_CD = models.AutoField(primary_key=True)
    ORGA_NM = models.CharField(max_length=255, null=True, blank=True)
    ORGA_LINK = models.CharField(max_length=255, null=True, blank=True)
    ORGA_COUNTRY_ISO = models.ForeignKey('Country')
    ORGA_WIKI_EN = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return u'%s - %s' % (self.ORGA_CD, self.ORGA_NM)
    class Meta:
        ordering = ('ORGA_NM', )


class Gs1_gcp(models.Model):
    GCP_CD = models.CharField(max_length=13, primary_key=True)
    GLN_CD = models.CharField(max_length=13,null=True, blank=True)
    GLN_NM = models.CharField(max_length=255,null=True, blank=True)
    GLN_ADDR_02 = models.CharField(max_length=38,null=True, blank=True)
    GLN_ADDR_03 = models.CharField(max_length=38,null=True, blank=True)
    GLN_ADDR_04 = models.CharField(max_length=38,null=True, blank=True)
    GLN_ADDR_POSTALCODE = models.CharField(max_length=38,null=True, blank=True)
    GLN_ADDR_CITY = models.CharField(max_length=38)
    GLN_COUNTRY_ISO_CD = models.CharField(max_length=38)
    CONTACT_NAME = models.CharField(max_length=38,null=True, blank=True)
    CONTACT_TEL = models.CharField(max_length=255,null=True, blank=True)
    CONTACT_HOTLINE = models.CharField(max_length=255, null=True, blank=True)
    CONTACT_FAX = models.CharField(max_length=255,null=True, blank=True)
    CONTACT_MAIL = models.CharField(max_length=255,null=True, blank=True)
    CONTACT_WEB = models.CharField(max_length=255,null=True, blank=True)
    GLN_LAST_CHANGE = models.CharField(max_length=10,null=True, blank=True)
    GLN_PROVIDER = models.CharField(max_length=13,null=True, blank=True)
    SEARCH_GTIN_CD = models.CharField(max_length=13,null=True, blank=True)
    GEPIR_GCP_CD = models.CharField(max_length=13,null=True, blank=True)
    ADD_PARTY_ID = models.CharField(max_length=13,null=True, blank=True)
    RETURN_CODE = models.ForeignKey('Gs1_gcp_rc', null=True, blank=True)
    SOURCE = models.CharField(max_length=100)
    SYNC_DT = models.DateField(null=True, blank=True)
    def __str__(self):
        return u'%s - %s' % (self.GCP_CD, self.GLN_NM)
    class Meta:
        ordering = ('GCP_CD', )

class Gs1_gcp_rc(models.Model):
    RETURN_CODE = models.CharField(max_length=3, primary_key=True)
    RETURN_NAME = models.CharField(max_length=255)
    ORIGIN = models.CharField(max_length=255)
    def __str__(self):
        return u'%s - %s' % (self.RETURN_CODE, self.RETURN_NAME)

class Country(models.Model):
    COUNTRY_ISO = models.CharField(max_length=2, primary_key=True)
    COUNTRY_NM_U = models.CharField(max_length=80)
    COUNTRY_NM_L = models.CharField(max_length=80)
    COUNTRY_EU = models.NullBooleanField(default=False, null=True, blank=True)
    def __str__(self):
        return u'%s - %s' % (self.COUNTRY_ISO, self.COUNTRY_NM_U)
    class Meta:
        ordering = ('COUNTRY_ISO', )

# Search is used to store gtin that people are searching and the number of times it has been searched
class Search(models.Model):
    GTIN_CD = models.CharField(max_length=13, primary_key=True)
    SEARCH_NB =  models.IntegerField(default=1)

# same but for the API
class Search_api(models.Model):
    GTIN_CD = models.CharField(max_length=13, primary_key=True)
    SEARCH_NB =  models.IntegerField(default=1)
