import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        actual_res1 = emotion_detector("I am glad this happened")
        self.assertEqual(actual_res1["dominant_emotion"], "joy")

        actual_res2 = emotion_detector("I am really mad about this")
        self.assertEqual(actual_res2["dominant_emotion"], "anger")

        actual_res3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(actual_res3["dominant_emotion"], "disgust")

        actual_res4 = emotion_detector("I am so sad about this")
        self.assertEqual(actual_res4["dominant_emotion"], "sadness")

        actual_res5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(actual_res5["dominant_emotion"], "fear")

unittest.main()
