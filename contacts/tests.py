from django.test import TestCase, Client
from django.urls import reverse
from .models import Contact


class ContactHtmxTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.contact = Contact.objects.create(name="Budi Utomo", email="budi@example.com")

    def test_contact_list_view(self):
        response = self.client.get(reverse("contacts:contact_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Budi Utomo")
        self.assertContains(response, "budi@example.com")

    def test_contact_add_view(self):
        response = self.client.post(
            reverse("contacts:contact_add"),
            {"name": "Siti Nurhaliza", "email": "siti@example.com"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Contact.objects.filter(name="Siti Nurhaliza").exists())
        self.assertContains(response, "Siti Nurhaliza")

    def test_contact_search_view(self):
        Contact.objects.create(name="Andi Wijaya", email="andi@example.com")
        response = self.client.get(reverse("contacts:contact_search") + "?q=Andi")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Andi Wijaya")
        self.assertNotContains(response, "Budi Utomo")

    def test_contact_edit_row_view(self):
        response = self.client.get(reverse("contacts:contact_edit", args=[self.contact.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'value="Budi Utomo"')
        self.assertContains(response, 'Simpan')

    def test_contact_update_view(self):
        response = self.client.put(
            reverse("contacts:contact_update", args=[self.contact.id]),
            data="name=Budi+Santoso&email=budisantoso@example.com",
            content_type="application/x-www-form-urlencoded"
        )
        self.assertEqual(response.status_code, 200)
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.name, "Budi Santoso")
        self.assertEqual(self.contact.email, "budisantoso@example.com")
        self.assertContains(response, "Budi Santoso")

    def test_contact_row_view(self):
        response = self.client.get(reverse("contacts:contact_row", args=[self.contact.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Budi Utomo")

    def test_contact_delete_view(self):
        response = self.client.delete(reverse("contacts:contact_delete", args=[self.contact.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "")
        self.assertFalse(Contact.objects.filter(id=self.contact.id).exists())
