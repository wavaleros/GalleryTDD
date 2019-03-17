from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from .models import Image
import json

class GalleryTestCase(TestCase):

    