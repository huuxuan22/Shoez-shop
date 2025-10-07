from typing import Optional, Union
from i18n.messages import en, vi
from config.context import get_current_lang
from config.enum import MessageKey, LanguageCode

LOCALES = {
    LanguageCode.ENGLISH: en.MESSAGES,
    LanguageCode.VIETNAMESE: vi.MESSAGES,
}

def translate(key: Union[MessageKey, str], lang: Optional[str] = None) -> str:
    """
    Translate a message key to the current or specified language.
    
    Args:
        key: MessageKey enum or string key to translate
        lang: Optional language code. If not provided, uses current context language
        
    Returns:
        Translated message string
    """
    # Get language from parameter or context
    if lang is None:
        lang = get_current_lang()
    
    # Convert string to LanguageCode if needed
    if isinstance(lang, str):
        try:
            lang_code = LanguageCode(lang)
        except ValueError:
            lang_code = LanguageCode.ENGLISH  # Default fallback
    else:
        lang_code = lang
    
    # Get the message key value
    if isinstance(key, MessageKey):
        key_value = key.value
    else:
        key_value = key
    
    # Get messages for the language with fallback to English
    messages = LOCALES.get(lang_code, LOCALES[LanguageCode.ENGLISH])
    
    # Return translated message or key as fallback
    return messages.get(key_value, key_value)

def set_language(lang: Union[str, LanguageCode]) -> None:
    """
    Set the current language in context.
    
    Args:
        lang: Language code to set
    """
    from config.context import lang_var
    
    if isinstance(lang, LanguageCode):
        lang_var.set(lang.value)
    else:
        lang_var.set(lang)

def get_available_languages() -> list[str]:
    """
    Get list of available language codes.
    
    Returns:
        List of available language codes
    """
    return [lang.value for lang in LanguageCode]

# Convenience function shortcuts
def _(key: Union[MessageKey, str], lang: Optional[str] = None) -> str:
    """Shorthand for translate function."""
    return translate(key, lang)

def t(key: Union[MessageKey, str], lang: Optional[str] = None) -> str:
    """Another shorthand for translate function."""
    return translate(key, lang)