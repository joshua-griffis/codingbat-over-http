from urllib import response
from django.test import SimpleTestCase

# Create your tests here.


class TestNearHundred(SimpleTestCase):
    def test_near_hundred_93(self):
        response = self.client.get("/near-hundred/93/")
        self.assertContains(response, "True")

    def test_near_hundred_90(self):
        response = self.client.get("/near-hundred/90/")
        self.assertContains(response, "True")

    def test_near_hundred_89(self):
        response = self.client.get("/near-hundred/89/")
        self.assertContains(response, "False")


class TestStringSplosion(SimpleTestCase):
    def test_str_spolsion_code(self):
        response = self.client.get("/string-splosion/Code/")
        self.assertContains(response, "CCoCodCode")

    def test_str_splosion_ab(self):
        response = self.client.get("/string-splosion/ab/")
        self.assertContains(response, "aab")

    def test_str_splosion_Albuquerque(self):
        response = self.client.get("/string-splosion/aab/")
        self.assertContains(response, "aab")


class TestCatDog(SimpleTestCase):
    def test_cat_dog_codecat(self):
        response = self.client.get("/cat-dog/catdog/")
        self.assertContains(response, "True")

    def test_cat_dog_ab(self):
        response = self.client.get("/cat-dog/catcat/")
        self.assertContains(response, "False")

    def test_cat_dog_Albuquerque(self):
        response = self.client.get("/cat-dog/1cat1cadodog/")
        self.assertContains(response, "True")


class TestLoneSum(SimpleTestCase):
    def test_lone_sum_123(self):
        response = self.client.get("/lone-sum/1/2/3/")
        self.assertContains(response, "6")

    def test_lone_sum_323(self):
        response = self.client.get("/lone-sum/3/2/3/")
        self.assertContains(response, "2")

    def test_lone_sum_Albuquerque(self):
        response = self.client.get("/lone-sum/3/3/3/")
        self.assertContains(response, "0")
