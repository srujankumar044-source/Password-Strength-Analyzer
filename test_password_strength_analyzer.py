import unittest

from src.password_strength_analyzer import check_password, generate_password


class TestPasswordStrengthAnalyzer(unittest.TestCase):

    def test_weak_password(self):
        score, strength, suggestions = check_password("123456")
        self.assertEqual(strength, "Weak")
        self.assertTrue(suggestions)

    def test_strong_password(self):
        score, strength, suggestions = check_password("Strong@Pass123")
        self.assertIn(strength, {"Strong", "Very Strong"})
        self.assertGreaterEqual(score, 5)

    def test_common_password(self):
        score, strength, suggestions = check_password("password")
        self.assertEqual(score, 0)
        self.assertIn("Avoid common passwords.", suggestions)

    def test_generated_password_length(self):
        password = generate_password(16)
        self.assertEqual(len(password), 16)


if __name__ == "__main__":
    unittest.main()
