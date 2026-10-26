"""
Validators and Security Sanitizers for Dynamic Tables and Fields.
Guards against SQL injection and invalid schema identifiers in dynamic DDL.
"""

import re
from django.core.exceptions import ValidationError

# PostgreSQL identifier pattern: starts with a letter or underscore, followed by letters, digits, or underscores.
IDENTIFIER_REGEX = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]{0,62}$')

RESERVED_SQL_KEYWORDS = {
    'select', 'insert', 'update', 'delete', 'drop', 'alter', 'create', 'table',
    'from', 'where', 'join', 'inner', 'outer', 'left', 'right', 'on', 'group',
    'by', 'order', 'having', 'limit', 'offset', 'union', 'all', 'distinct',
    'into', 'values', 'set', 'null', 'default', 'primary', 'key', 'foreign',
    'references', 'check', 'unique', 'index', 'database', 'schema', 'grant', 'revoke'
}


def is_safe_identifier(name: str) -> bool:
    """Checks whether a string is a safe SQL/Python identifier."""
    if not isinstance(name, str):
        return False
    name = name.strip()
    if not IDENTIFIER_REGEX.match(name):
        return False
    if name.lower() in RESERVED_SQL_KEYWORDS:
        return False
    return True


def validate_identifier(name: str, field_type: str = "identifier") -> str:
    """
    Validates that a table or column name is safe to use in SQL and Python models.
    Raises ValidationError if invalid.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValidationError(f"Invalid {field_type}: name cannot be empty.")
    
    clean_name = name.strip()
    if not IDENTIFIER_REGEX.match(clean_name):
        raise ValidationError(
            f"Invalid {field_type} '{clean_name}'. Must start with a Latin letter or underscore, "
            f"contain only alphanumeric characters and underscores, and be at most 63 characters."
        )
        
    if clean_name.lower() in RESERVED_SQL_KEYWORDS:
        raise ValidationError(
            f"Invalid {field_type} '{clean_name}'. Cannot use SQL reserved keyword."
        )
        
    return clean_name


def sanitize_identifier(raw_name: str, fallback_prefix: str = "col") -> str:
    """
    Sanitizes raw user input into a safe SQL/Python identifier.
    Replaces whitespace and special characters with underscores.
    """
    if not raw_name:
        return f"{fallback_prefix}_1"
    
    # Strip leading/trailing whitespace
    name = str(raw_name).strip().lower()
    
    # Replace non-alphanumeric with underscores
    name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    
    # Collapse multiple consecutive underscores
    name = re.sub(r'_+', '_', name).strip('_')
    
    # Ensure starts with a letter or underscore
    if not name or not name[0].isalpha() and name[0] != '_':
        name = f"{fallback_prefix}_{name}"
        
    # Truncate to PostgreSQL limit (63 chars)
    name = name[:63]
    
    # Avoid reserved keywords
    if name.lower() in RESERVED_SQL_KEYWORDS:
        name = f"{name}_field"
        
    return name
