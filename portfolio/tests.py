from django_any import any_model
from portfolio.models import Work
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
        Test published work presence on portfolio index page
        """
        works_list = self.app.get('/portfolio/')
        assert self.published_work.title in works_list

    def test_details_view(self):
        """
        Test published work description presence on portfolio work details page
        """
        work_page = self.app.get('/portfolio/%d/' % self.published_work.pk)
        assert self.published_work.title in work_page
        assert self.published_work.description in work_page

    def test_unpublished_work_is_not_shown(self):
        """
        Tests that unpublished works are filtered off by published works filter
        """
        self.assertNotIn(self.unpublished_work, Work.get_published_works())

    def test_published_work_is_shown(self):
        """
        Tests that published works are filtered on by published works filter
        """
        self.assertIn(self.published_work, Work.get_published_works())