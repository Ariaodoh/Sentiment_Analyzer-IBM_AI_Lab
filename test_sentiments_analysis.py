#import packages
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

#create test class for test
class TestSentimantAnalyzer(unittest.TestCase):
    def test_sentimet_analyzer(self):
        result_1 = sentiment_analyzer("I love working with Python")
        self.assertEquals(result_1['label'], 'SENT_POSITIVE')
        result_2 = sentiment_analyzer("I hate working with Python")
        self.assertEquals(result_2['label'], 'SENT_NEGATIVE')
        result_3 = sentiment_analyzer("I am neutral on Python")
        self.assertEquals(result_3['label'], 'SENT_NEUTRAL')

#run unit test
unittest.main()

