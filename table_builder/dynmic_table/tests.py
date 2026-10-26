"""
Unit and Security Tests for dynmic_table
"""

from unittest import TestCase
from django.core.exceptions import ValidationError
from dynmic_table.validators import (
    is_safe_identifier,
    validate_identifier,
    sanitize_identifier,
)


class IdentifierSecurityTestCase(TestCase):
    """Verifies that dynamic identifier validation prevents SQL injection & malformed DDL."""

    def test_valid_identifiers(self):
        valid_cases = ["customer", "order_items", "_internal_id", "column_123", "EmployeeRecord"]
        for case in valid_cases:
            self.assertTrue(is_safe_identifier(case), f"Expected '{case}' to be valid.")
            self.assertEqual(validate_identifier(case), case)

    def test_sql_injection_rejection(self):
        malicious_inputs = [
            "table_name; DROP TABLE users;--",
            "col' OR 1=1--",
            "table\"name",
            "field; SELECT * FROM pg_user;",
            "users (id INT)",
            "col--comment",
            "col/*comment*/",
        ]
        for bad in malicious_inputs:
            self.assertFalse(is_safe_identifier(bad), f"Expected injection '{bad}' to be blocked.")
            with self.assertRaises(ValidationError, msg=f"Should raise ValidationError for '{bad}'"):
                validate_identifier(bad)

    def test_reserved_keywords_rejection(self):
        keywords = ["select", "SELECT", "drop", "table", "from", "where", "insert", "delete"]
        for kw in keywords:
            self.assertFalse(is_safe_identifier(kw), f"Keyword '{kw}' must be rejected.")
            with self.assertRaises(ValidationError):
                validate_identifier(kw)

    def test_invalid_formats(self):
        invalid_cases = [
            "",  # Empty
            " ",  # Whitespace
            "123start_with_number",  # Starts with number
            "contains-hyphen",  # Hyphen not allowed in SQL identifiers
            "has space",  # Spaces not allowed
            "a" * 64,  # Exceeds max length (63)
        ]
        for inv in invalid_cases:
            self.assertFalse(is_safe_identifier(inv), f"Expected '{inv}' to be rejected.")
            with self.assertRaises(ValidationError):
                validate_identifier(inv)

    def test_identifier_sanitization(self):
        test_inputs = {
            "First Name": "first_name",
            "123_number": "col_123_number",
            "user-email@domain": "user_email_domain",
            "SELECT": "select_field",
            "multiple   spaces   here": "multiple_spaces_here",
            "": "col_1",
        }
        for raw, expected in test_inputs.items():
            sanitized = sanitize_identifier(raw)
            self.assertEqual(sanitized, expected, f"Failed sanitizing '{raw}'")
            self.assertTrue(is_safe_identifier(sanitized), f"Sanitized result '{sanitized}' must be safe.")
