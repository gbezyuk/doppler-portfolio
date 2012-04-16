from django.test import TestCase
from django_any import any_model
from portfolio.models import Work

class WorkPublicationTest(TestCase):

    def test_unpublished_work_is_not_shown(self):
        """Tests that unpublished works are filtered off by published works filter"""
        work = any_model(Work, is_published=False)
        self.assertNotIn(work, Work.get_published_works())

    def test_published_work_is_shown(self):
        """Tests that published works are filtered on by published works filter"""
        work = any_model(Work, is_published=True)
        self.assertIn(work, Work.get_published_works())
