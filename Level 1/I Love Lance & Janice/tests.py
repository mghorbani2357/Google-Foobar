from unittest import TestCase
from solution import solution


class TestSolution(TestCase):
    def test_first_example(self):
        self.assertEqual("did you see last night's episode?", solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))

    def test_second_example(self):
        self.assertEqual("Yeah! I can't believe Lance lost his job at the colony!!", solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
