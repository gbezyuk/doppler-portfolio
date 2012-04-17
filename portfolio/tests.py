from django.core.urlresolvers import reverse
from django.template.response import ContentNotRenderedError
from django_any import any_model
from .models import Work
from django_webtest import WebTest

class WorkPublicationTest(WebTest):

    def setUp(self):
        """
        Initialization. Creating model instances for tests
        """
        self.published_work = any_model(Work, is_published=True,)
        self.unpublished_work = any_model(Work, is_published=False)

    def test_list_view(self):
        """
        Test published work present on portfolio index page, and unpublished doesn't
        """
        works_list = self.app.get(reverse('portfolio_work_list'))
        self.assertIn(self.published_work.title, works_list)
        self.assertNotIn(self.unpublished_work.title, works_list)

    def test_published_work_details_view(self):
        """
        Test published work description presence on portfolio work details page
        """
        published_work_page = self.app.get(reverse('portfolio_work_details', kwargs={'work_id': self.published_work.pk}))
        self.assertIn(self.published_work.title, published_work_page)
        self.assertIn(self.published_work.description, published_work_page)

    def test_unpublished_work_details_view(self):
        """
        Test published work description presence on portfolio work details page
        """
        self.assertRaises(ContentNotRenderedError, self.app.get,
            reverse('portfolio_work_details', kwargs={'work_id': self.unpublished_work.pk}))


    def test_unpublished_work_is_filtered_off(self):
        """
        Tests that unpublished works are filtered off by published works filter
        """
        self.assertNotIn(self.unpublished_work, Work.get_published_works())

    def test_published_work_is_filtered_on(self):
        """
        Tests that published works are filtered on by published works filter
        """
        self.assertIn(self.published_work, Work.get_published_works())
