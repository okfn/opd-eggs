from django.contrib import admin
from browser.models import Brand, Gtin, Gs1_gcp, Owner, Packaging, Category, Brand_type, Method, Grade, Size, Color, Fed, Label, Country, Orga, Search

class BrandAdmin(admin.ModelAdmin):
    list_display    = ('BSIN','BRAND_NM','BRAND_COUNTRY_ISO','BRAND_DISPLAY')
    ordering        = ('BRAND_NM',)
    search_fields   = ['BSIN']
    list_filter = (
        ('BRAND_COUNTRY_ISO', admin.RelatedOnlyFieldListFilter),
    )
admin.site.register(Brand, BrandAdmin)
class GtinAdmin(admin.ModelAdmin):
    save_as = True
    list_display    = ('GTIN_ID','GTIN_CD','GCP_CD', 'BSIN','PKG_UNIT','METHOD_CD','SIZE_CD')
    ordering        = ('BSIN','PKG_UNIT',)
    search_fields   = ['GTIN_CD','GTIN_ID']
    list_filter = (
        ('BSIN', admin.RelatedOnlyFieldListFilter),
    )
admin.site.register(Gtin, GtinAdmin)
class Gs1_gcpAdmin(admin.ModelAdmin):
    list_display    = ('GCP_CD','GLN_NM','GLN_COUNTRY_ISO_CD')
    ordering        = ('GCP_CD','GLN_NM',)
admin.site.register(Gs1_gcp, Gs1_gcpAdmin)
class OwnerAdmin(admin.ModelAdmin):
    list_display    = ('OWNER_CD','OWNER_NM')
admin.site.register(Owner, OwnerAdmin)
class OrgaAdmin(admin.ModelAdmin):
    list_display    = ('ORGA_CD','ORGA_NM','ORGA_COUNTRY_ISO')
admin.site.register(Orga, OrgaAdmin)
class PackagingAdmin(admin.ModelAdmin):
    list_display    = ('PACKAGING_CD','PACKAGING_NM')
admin.site.register(Packaging, PackagingAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display    = ('CAT_CD','CAT_NM')
admin.site.register(Category, CategoryAdmin)
class MethodAdmin(admin.ModelAdmin):
    list_display    = ('METHOD_CD','METHOD_ISO','METHOD_NM','METHOD_LEVEL_CD')
admin.site.register(Method, MethodAdmin)
class Brand_typeAdmin(admin.ModelAdmin):
    list_display    = ('BRAND_TYPE_CD','BRAND_TYPE_NM')
admin.site.register(Brand_type, Brand_typeAdmin)
class GradeAdmin(admin.ModelAdmin):
    list_display    = ('GRADE_CD','GRADE_NM')
admin.site.register(Grade, GradeAdmin)
class SizeAdmin(admin.ModelAdmin):
    list_display    = ('SIZE_CD','SIZE_NM')
admin.site.register(Size, SizeAdmin)
class ColorAdmin(admin.ModelAdmin):
    list_display    = ('COLOR_CD','COLOR_NM')
admin.site.register(Color, ColorAdmin)
class FedAdmin(admin.ModelAdmin):
    list_display    = ('FED_CD','FED_NM')
admin.site.register(Fed, FedAdmin)
class LabelAdmin(admin.ModelAdmin):
    list_display    = ('LABEL_NM','LABEL_COUNTRY_ISO','LABEL_CD')
admin.site.register(Label, LabelAdmin)
class CountryAdmin(admin.ModelAdmin):
    list_display    = ('COUNTRY_ISO','COUNTRY_NM_U','COUNTRY_EU')
    search_fields   = ['COUNTRY_ISO']
admin.site.register(Country, CountryAdmin)
class SearchAdmin(admin.ModelAdmin):
    list_display    = ('GTIN_CD','SEARCH_NB')
admin.site.register(Search, SearchAdmin)
