"""Unit tests for emotion_detector function."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_joy_for_happy_text(self):
        """Test that joy is the dominant emotion for happy text."""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_for_angry_text(self):
        """Test that anger is the dominant emotion for angry text."""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_for_disgusting_text(self):
        """Test that disgust is the dominant emotion for disgusting text."""
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_fear_for_fearful_text(self):
        """Test that fear is the dominant emotion for fearful text."""
        result = emotion_detector('I am scared to death by this')
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_sadness_for_sad_text(self):
        """Test that sadness is the dominant emotion for sad text."""
        result = emotion_detector('I feel so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')


if __name__ == '__main__':
    unittest.main()
