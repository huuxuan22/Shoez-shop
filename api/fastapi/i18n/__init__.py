"""
I18n package for internationalization support.

This package provides:
- MessageKey enum for type-safe message keys
- Translation functions with context support
- Multi-language message definitions
"""

# Import only what's needed, avoid circular imports
try:
    from .translator import translate, set_language, get_available_languages, _, t
    __all__ = [
        'translate',
        'set_language',
        'get_available_languages',
        '_',
        't'
    ]
except ImportError:
    # Fallback if translator module is not available
    __all__ = []
