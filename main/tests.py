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
                            "Belum ada coursework yang ditambahkan.")

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
