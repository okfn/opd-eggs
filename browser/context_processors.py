from django.conf import settings

def debug(context):
  return {'DEBUG': settings.DEBUG,'SHOW_GTIN': settings.SHOW_GTIN }
