from django_webtest import WebTest

class IndexPageTest(WebTest):

    def test_index_view(self):
        """
        Test index page opens
        """
        index_page = self.app.get('/')
        self.assertIn('breadcrumb', index_page)