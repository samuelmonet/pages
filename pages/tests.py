from django.test import SimpleTestCase # (Simple Test when no Data Base)
from django.urls import reverse
# Create your tests here.

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self): # verifie que la page renvoi bien un status code 200
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)

    def test_url_available_by_name(self): # verifie le nom de "home" renvoit bien aussi 200
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)

    def test_template_name_correct(self): # verifie que le nom de "home" renvoit bien sur home.html
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response,"home.html")

    def test_template_content(self): # verifie une parti du contenu de la page
        response = self.client.get(reverse("home"))
        self.assertContains(response,"<h1> Home page </h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code,200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):  # verifie une parti du contenu de la page
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1> About page </h1>")

