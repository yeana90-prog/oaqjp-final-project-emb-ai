import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Unit tests for the emotion_detector function."""

    def test_joy_emotion(self):
        """Test that joy is the dominant emotion for positive text."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        """Test that anger is the dominant emotion for angry text."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        """Test that disgust is the dominant emotion for disgusting text."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        """Test that sadness is the dominant emotion for sad text."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        """Test that fear is the dominant emotion for fearful text."""
        result = emotion_detector("I am really scared and afraid")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_blank_input(self):
        """Test that blank input returns None for all emotions."""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['joy'])


if __name__ == '__main__':
    unittest.main()
