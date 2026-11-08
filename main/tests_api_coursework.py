import uuid
from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from main.models import Coursework


class CourseworkAPITest(APITestCase):
    def setUp(self):
        # 1. Superuser / Owner
        self.owner = User.objects.create_superuser(
            username="cw_owner",
            password="test-password",
            email="cw_owner@example.com",
        )
        # 2. Regular visitor
        self.visitor = User.objects.create_user(username="cw_visitor", password="test-password")

        # 3. Editor
        self.editor = User.objects.create_user(username="cw_editor", password="test-password")
        self.editor_group, _ = Group.objects.get_or_create(name="Editor")
        self.editor.groups.add(self.editor_group)

        # Initial Coursework
        self.coursework = Coursework.objects.create(
            name="Pemrograman Berbasis Platform",
            category="Software Development",
            description="Web engineering and frameworks.",
            credits=3,
            journal="Learning Django and REST API.",
        )

        self.list_url = reverse("api:coursework-list")
        self.detail_url = reverse("api:coursework-detail", args=[self.coursework.id])
        self.star_url = reverse("api:coursework-star", args=[self.coursework.id])

        self.payload = {
            "name": "Database Systems",
            "category": "Data Management",
            "description": "SQL and relational database management.",
            "credits": 4,
            "journal": "Studied ERD and query optimization.",
        }

    # --- Pengujian Akses Publik ---
    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], str(self.coursework.id))
        self.assertFalse(response.data[0]["is_starred"])
        self.assertNotIn("fields", response.data[0])

        detail_res = self.client.get(self.detail_url)
        self.assertEqual(detail_res.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_res.data["name"], self.coursework.name)

    def test_search_and_category_filtering(self):
        response = self.client.get(self.list_url, {"search": "Platform"})
        self.assertEqual(len(response.data), 1)

        empty_res = self.client.get(self.list_url, {"search": "non-existent-course"})
        self.assertEqual(empty_res.data, [])

        cat_res = self.client.get(self.list_url, {"category": "Software"})
        self.assertEqual(len(cat_res.data), 1)

    def test_missing_coursework_returns_404(self):
        random_url = reverse("api:coursework-detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(random_url).status_code, status.HTTP_404_NOT_FOUND)

    # --- Pengujian Role: Guest & Regular User (Tolak Tulis, Cek DB) ---
    def test_guest_and_regular_user_cannot_modify(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            # Create ditolak -> 403
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
            # Update ditolak -> 403
            self.assertEqual(self.client.patch(self.detail_url, {"name": "Hacked Name"}, format="json").status_code, 403)
            # Delete ditolak -> 403
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)

        # Verifikasi isi database tidak berubah
        self.assertEqual(Coursework.objects.count(), 1)
        self.coursework.refresh_from_db()
        self.assertEqual(self.coursework.name, "Pemrograman Berbasis Platform")

    # --- Pengujian Role: Editor (Boleh PUT/PATCH, Tolak POST/DELETE) ---
    def test_editor_can_update_but_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)

        # 1. Editor tidak boleh membuat coursework baru -> 403
        post_res = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(post_res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Coursework.objects.count(), 1)

        # 2. Editor boleh melakukan PATCH -> 200
        patch_res = self.client.patch(self.detail_url, {"name": "PBP (Updated by Editor)"}, format="json")
        self.assertEqual(patch_res.status_code, status.HTTP_200_OK)
        self.coursework.refresh_from_db()
        self.assertEqual(self.coursework.name, "PBP (Updated by Editor)")

        # 3. Editor boleh melakukan PUT -> 200
        updated_payload = {
            "name": "PBP Full Update",
            "category": "Software",
            "description": "Comprehensive web frameworks.",
            "credits": 4,
            "journal": "Updated by editor.",
        }
        put_res = self.client.put(self.detail_url, updated_payload, format="json")
        self.assertEqual(put_res.status_code, status.HTTP_200_OK)
        self.coursework.refresh_from_db()
        self.assertEqual(self.coursework.name, "PBP Full Update")
        self.assertEqual(self.coursework.credits, 4)

        # 4. Editor tidak boleh menghapus -> 403
        del_res = self.client.delete(self.detail_url)
        self.assertEqual(del_res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Coursework.objects.filter(pk=self.coursework.id).exists())

    # --- Pengujian Role: Superuser / Owner (Bisa Create, Update, Delete) ---
    def test_owner_can_create_and_delete(self):
        self.client.force_authenticate(user=self.owner)

        # 1. Create -> 201
        res = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        new_id = res.data["id"]
        self.assertTrue(Coursework.objects.filter(pk=new_id).exists())
        self.assertEqual(Coursework.objects.count(), 2)

        # 2. Delete -> 204
        del_res = self.client.delete(reverse("api:coursework-detail", args=[new_id]))
        self.assertEqual(del_res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(del_res.content, b"")
        self.assertFalse(Coursework.objects.filter(pk=new_id).exists())
        self.assertEqual(Coursework.objects.count(), 1)

    # --- Pengujian Validasi Input & Sanitasi XSS ---
    def test_validation_and_sanitization(self):
        self.client.force_authenticate(user=self.owner)
        for changes, expected_field in [
            ({"name": " "}, "name"),
            ({"name": '<img src="x" onerror="alert(1)">'}, "name"),
            ({"category": " "}, "category"),
            ({"category": '<img src="x">'}, "category"),
            ({"description": " "}, "description"),
            ({"description": '<p></p>'}, "description"),
            ({"credits": 0}, "credits"),
            ({"credits": -5}, "credits"),
        ]:
            response = self.client.post(self.list_url, {**self.payload, **changes}, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn(expected_field, response.data)

        # Verifikasi tidak ada data baru yang tersimpan
        self.assertEqual(Coursework.objects.count(), 1)

    # --- Pengujian Fitur Star ---
    def test_star_requires_authentication_and_toggles(self):
        # 1. Anonim ditolak -> 403
        anon_res = self.client.post(self.star_url)
        self.assertEqual(anon_res.status_code, status.HTTP_403_FORBIDDEN)

        # 2. User biasa login -> star berhasil (1 star)
        self.client.force_authenticate(user=self.visitor)
        res1 = self.client.post(self.star_url)
        self.assertEqual(res1.status_code, status.HTTP_200_OK)
        self.assertTrue(res1.data["is_starred"])
        self.assertEqual(res1.data["star_count"], 1)
        self.coursework.refresh_from_db()
        self.assertIn(self.visitor, self.coursework.starred_by.all())

        # 3. Klik lagi -> unstar (0 star)
        res2 = self.client.post(self.star_url)
        self.assertEqual(res2.status_code, status.HTTP_200_OK)
        self.assertFalse(res2.data["is_starred"])
        self.assertEqual(res2.data["star_count"], 0)
        self.coursework.refresh_from_db()
        self.assertNotIn(self.visitor, self.coursework.starred_by.all())

    def test_computed_fields_are_strictly_read_only(self):
        self.client.force_authenticate(user=self.owner)
        forged_payload = {
            **self.payload,
            "star_count": 999,
            "is_starred": True,
            "starred_by_names": "fake_user",
        }
        res = self.client.post(self.list_url, forged_payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["star_count"], 0)
        self.assertFalse(res.data["is_starred"])

    # --- Pengujian CSRF Enforcement ---
    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="cw_owner", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Coursework.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)
        client.login(username="cw_owner", password="test-password")

        # Ambil token CSRF dari Browsable API HTML
        page = client.get(self.list_url, HTTP_ACCEPT="text/html")
        self.assertEqual(page.status_code, status.HTTP_200_OK)
        token = client.cookies["csrftoken"].value

        response = client.post(
            self.list_url,
            self.payload,
            format="json",
            HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Coursework.objects.filter(name="Database Systems").exists())
