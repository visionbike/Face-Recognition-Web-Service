import os
import base64
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import BASE_DIR


class TestApi(TestCase):
    def test_add_new_employee(self):
        pass

    def test_update_employee(self):
        pass

    def test_delete_employee(self):
        pass

    def test_get_employee(self):
        pass

    def test_get_staff(self):
        pass

    def test_update_image_by_image_id(self):
        pass

    def test_delete_image_by_image_id(self):
        pass

    def test_get_images_by_staff_id(self):
        pass

    def delete_images_by_staff_id(self):
        pass

    def test_add_new_image_by_staff_id(self):
        pass

    def test_get_all_images(self):
        pass

    def delete_all_images(self):
        pass
