# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase
from api.models import SubjectEmotionsCount


class SubjectEmotionsCountTestCase(APITestCase):
    def test_subject_emotions_count_str(self):

        subject_name = 'Computacao basica'
        good_count = 3
        bad_count = 1

        emotions_count = SubjectEmotionsCount(subject_name=subject_name,
                                              good_count=good_count,
                                              bad_count=bad_count)

        emotions_count_str = emotions_count.__str__()
        expected_str = '(Computacao basica, {\'good\': 3, \'bad\': 1})'
        self.assertEquals(emotions_count_str, expected_str)
