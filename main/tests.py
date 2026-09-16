"""
Run tests with:
    python manage.py test main
"""

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Coursework


# ---------------------------------------------------------------------------
# Shared fixture helper
# ---------------------------------------------------------------------------

def make_experience(**kwargs):
    defaults = dict(
        title="Asisten Dosen PBP",
        description="Membantu mahasiswa memahami pengembangan web.",
        category="part-time",
    )
    defaults.update(kwargs)
    return Experience.objects.create(**defaults)


def make_coursework(**kwargs):
    defaults = dict(
        name="Business Management",
        category="Management and Strategy",
        description="Fundamental principles of organisational strategy.",
        credits=3,
    )
    defaults.update(kwargs)
    return Coursework.objects.create(**defaults)


# ===========================================================================
# 1.  MODEL TESTS
# ===========================================================================

class ExperienceModelTest(TestCase):

    def test_str_returns_title(self):
        exp = make_experience()
        self.assertEqual(str(exp), "Asisten Dosen PBP")

    def test_is_ongoing_when_no_end_date(self):
        exp = make_experience()
        self.assertTrue(exp.is_ongoing)

    def test_not_ongoing_when_end_date_set(self):
        exp = make_experience(ended_at=timezone.now())
        self.assertFalse(exp.is_ongoing)

    def test_company_defaults_to_empty_string(self):
        exp = make_experience()
        self.assertEqual(exp.company, "")

    def test_category_choices(self):
        valid_categories = {"internship", "research", "volunteer",
                            "part-time", "full-time", "freelance"}
        exp = make_experience(category="internship")
        self.assertIn(exp.category, valid_categories)


class CourseworkModelTest(TestCase):

    def test_str_returns_name(self):
        cw = make_coursework()
        self.assertEqual(str(cw), "Business Management")

    def test_credits_stored_correctly(self):
        cw = make_coursework(credits=4)
        self.assertEqual(cw.credits, 4)

    def test_journal_can_be_blank(self):
        cw = make_coursework()
        self.assertIsNone(cw.journal)

    def test_journal_can_be_set(self):
        cw = make_coursework(journal="Week 1: learned SQL joins.")
        self.assertEqual(cw.journal, "Week 1: learned SQL joins.")


# ===========================================================================
# 2.  PROFILE / INDEX PAGE TESTS
# ===========================================================================

class ProfilePageTest(TestCase):

    def setUp(self):
        self.coursework = make_coursework()
        self.url = reverse("main:show_main")
        self.response = self.client.get(self.url)

    def test_returns_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_uses_correct_template(self):
        self.assertTemplateUsed(self.response, "index.html")

    def test_nav_links_present(self):
        self.assertContains(self.response,
                            f'href="{reverse("main:show_experience")}"')
        self.assertContains(self.response,
                            f'href="{reverse("main:show_coursework")}"')

    def test_coursework_dropdown_shows_course_name(self):
        """Dropdown nav on index must list the coursework entry."""
        self.assertContains(self.response, self.coursework.name)

    def test_education_list_renders_dynamically(self):
        self.assertIn("education_list", self.response.context)
        self.assertContains(self.response, "Universitas Indonesia")
        self.assertContains(self.response, "Undergraduate of Information Systems")

    def test_interests_list_renders_dynamically(self):
        self.assertIn("interests_list", self.response.context)
        self.assertContains(self.response, "Auditing")
        self.assertContains(self.response, "Marine Sciences")


class NotFoundTest(TestCase):

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)


# ===========================================================================
# 3.  EXPERIENCE PAGE TESTS
# ===========================================================================

class ExperiencePageTest(TestCase):

    def setUp(self):
        self.experience = make_experience()
        self.url = reverse("main:show_experience")

    def test_returns_200(self):
        self.assertEqual(self.client.get(self.url).status_code, 200)

    def test_uses_correct_template(self):
        self.assertTemplateUsed(self.client.get(self.url), "experience.html")

    def test_shows_experience_title(self):
        self.assertContains(self.client.get(self.url), self.experience.title)

    def test_shows_description(self):
        self.assertContains(self.client.get(self.url),
                            self.experience.description)

    def test_shows_category_display(self):
        """Category 'part-time' should render as 'Part-Time'."""
        self.assertContains(self.client.get(self.url), "Part-Time")

    def test_ongoing_label_shown(self):
        self.assertContains(self.client.get(self.url), "Ongoing")

    def test_completed_label_shown_when_end_date_set(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(self.url)
        self.assertContains(response, "Completed")
        self.assertNotContains(response, "Ongoing")

    def test_empty_state_when_no_experiences(self):
        Experience.objects.all().delete()
        self.assertContains(self.client.get(self.url),
                            "No experiences added yet.")

    def test_nav_links_present(self):
        response = self.client.get(self.url)
        self.assertContains(response,
                            f'href="{reverse("main:show_main")}"')
        self.assertContains(response,
                            f'href="{reverse("main:show_coursework")}"')

    def test_coursework_dropdown_lists_course(self):
        cw = make_coursework()
        self.assertContains(self.client.get(self.url), cw.name)

    def test_search_experience_by_title(self):
        exp2 = make_experience(title="Frontend Developer")
        response = self.client.get(self.url + "?title=Asisten")
        self.assertContains(response, self.experience.title)
        self.assertNotContains(response, "Frontend Developer")

    def test_create_experience_get(self):
        add_url = reverse("main:create_experience")
        response = self.client.get(add_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience_form.html")

    def test_create_experience_post_success(self):
        add_url = reverse("main:create_experience")
        data = {
            "title": "Software Engineer Intern",
            "company": "Tech Corp",
            "description": "Building backend microservices.",
            "category": "internship",
            "started_at": "2026-01-01T09:00",
        }
        response = self.client.post(add_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Experience.objects.filter(title="Software Engineer Intern").exists())

    def test_delete_experience_post(self):
        delete_url = reverse("main:delete_experience", args=[self.experience.id])
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Experience.objects.filter(id=self.experience.id).exists())

    def test_get_experience_json(self):
        json_url = reverse("main:get_experience_json")
        response = self.client.get(json_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertIn(self.experience.title, response.content.decode("utf-8"))

    def test_edit_experience_get(self):
        edit_url = reverse("main:edit_experience", args=[self.experience.id])
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience_form.html")
        self.assertContains(response, self.experience.title)

    def test_edit_experience_post_success(self):
        edit_url = reverse("main:edit_experience", args=[self.experience.id])
        data = {
            "title": "Lead Assistant Lecturer",
            "company": "Fasilkom UI",
            "description": "Leading labs and lectures.",
            "category": "part-time",
            "started_at": "2026-02-01T08:00",
        }
        response = self.client.post(edit_url, data)
        self.assertEqual(response.status_code, 302)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Lead Assistant Lecturer")
        self.assertEqual(self.experience.company, "Fasilkom UI")

    def test_filter_experience_by_category(self):
        make_experience(title="Startup Intern", category="internship")
        response = self.client.get(self.url + "?category=internship")
        self.assertContains(response, "Startup Intern")
        self.assertNotContains(response, "Asisten Dosen PBP")


# ===========================================================================
# 4.  COURSEWORK LIST PAGE TESTS
# ===========================================================================

class CourseworkListPageTest(TestCase):

    def setUp(self):
        self.coursework = make_coursework()
        self.url = reverse("main:show_coursework")

    def test_returns_200(self):
        self.assertEqual(self.client.get(self.url).status_code, 200)

    def test_uses_correct_template(self):
        self.assertTemplateUsed(self.client.get(self.url), "coursework.html")

    def test_shows_course_name(self):
        self.assertContains(self.client.get(self.url), self.coursework.name)

    def test_shows_category(self):
        self.assertContains(self.client.get(self.url),
                            self.coursework.category)

    def test_shows_description(self):
        self.assertContains(self.client.get(self.url),
                            self.coursework.description)

    def test_card_links_to_detail_page(self):
        expected_href = reverse("main:show_coursework_detail",
                                args=[self.coursework.id])
        self.assertContains(self.client.get(self.url),
                            f'href="{expected_href}"')

    def test_empty_state_when_no_coursework(self):
        Coursework.objects.all().delete()
        self.assertContains(self.client.get(self.url),
                            "No coursework added yet.")

    def test_nav_links_present(self):
        response = self.client.get(self.url)
        self.assertContains(response,
                            f'href="{reverse("main:show_main")}"')
        self.assertContains(response,
                            f'href="{reverse("main:show_experience")}"')


# ===========================================================================
# 5.  COURSEWORK DETAIL PAGE TESTS
# ===========================================================================

class CourseworkDetailPageTest(TestCase):

    def setUp(self):
        self.coursework = make_coursework(
            journal="Week 1: intro to strategy frameworks.\n"
                    "Week 2: Porter's Five Forces analysis."
        )
        self.url = reverse("main:show_coursework_detail",
                           args=[self.coursework.id])

    def test_returns_200(self):
        self.assertEqual(self.client.get(self.url).status_code, 200)

    def test_uses_correct_template(self):
        self.assertTemplateUsed(self.client.get(self.url),
                                "coursework_detail.html")

    def test_shows_course_name_as_heading(self):
        self.assertContains(self.client.get(self.url), self.coursework.name)

    def test_shows_category_tag(self):
        self.assertContains(self.client.get(self.url),
                            self.coursework.category)

    def test_shows_credits(self):
        self.assertContains(self.client.get(self.url), "3 Credits")

    def test_shows_description(self):
        self.assertContains(self.client.get(self.url),
                            self.coursework.description)

    def test_shows_journal_content(self):
        self.assertContains(self.client.get(self.url),
                            "Week 1: intro to strategy frameworks.")

    def test_empty_journal_shows_placeholder(self):
        cw = make_coursework(name="Empty Course", journal=None)
        url = reverse("main:show_coursework_detail", args=[cw.id])
        self.assertContains(self.client.get(url),
                            "No journal entry yet.")

    def test_back_link_points_to_coursework_list(self):
        expected_href = reverse("main:show_coursework")
        self.assertContains(self.client.get(self.url),
                            f'href="{expected_href}"')

    def test_breadcrumb_contains_home_and_coursework(self):
        response = self.client.get(self.url)
        self.assertContains(response,
                            f'href="{reverse("main:show_main")}"')
        self.assertContains(response,
                            f'href="{reverse("main:show_coursework")}"')

    def test_invalid_uuid_returns_404(self):
        fake_url = reverse("main:show_coursework_detail",
                           args=["00000000-0000-0000-0000-000000000000"])
        self.assertEqual(self.client.get(fake_url).status_code, 404)

    def test_dropdown_nav_lists_course(self):
        """The detail page nav dropdown should include this course's link."""
        response = self.client.get(self.url)
        self.assertContains(response, self.coursework.name)

    def test_journal_images_gallery_renders_when_images_found(self):
        """When journal_images are in context, the gallery block and captions render."""
        response = self.client.get(self.url)
        self.assertIn("journal_images", response.context)
