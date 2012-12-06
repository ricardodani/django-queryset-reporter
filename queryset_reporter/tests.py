"""
queryset_reporter tests.
"""

from django.test import TestCase


class AjaxViewsTest(TestCase):
    def test_ajax_return_aways_200(self):
        '''
        Test in a range of 0 to 100, if all the ajax calls to model:
        /queryset_reporter/ajax/model-fields/?model=<id> returns a 200 code.
        '''
        for i in range(100):
            url = '/queryset_reporter/ajax/model-fields/?model=%d'
            response = self.client.get(url % i)
            self.assertUnlessEqual(response.status_code, 200)

    def test_ajax_return_with_none_model_id(self):
        '''
        Test if the returns is 200 if the model id is none.
        '''
        response = self.client.get('/queryset_reporter/ajax/model-fields/?model=')
        self.assertUnlessEqual(response.status_code, 200)
