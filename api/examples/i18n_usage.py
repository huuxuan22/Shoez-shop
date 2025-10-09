"""
Example usage of the i18n system.

This file demonstrates how to use the internationalization features.
"""

from i18n import translate, set_language, MessageKey, LanguageCode, _, t

def demo_i18n_usage():
    """Demonstrate various ways to use the i18n system."""
    
    print("=== I18N Demo ===")
    
    # Using MessageKey enum (recommended for type safety)
    print("\n1. Using MessageKey enum:")
    print(f"English: {translate(MessageKey.WELCOME)}")
    
    # Switch to Vietnamese
    set_language(LanguageCode.VIETNAMESE)
    print(f"Vietnamese: {translate(MessageKey.WELCOME)}")
    
    # Using string keys
    print("\n2. Using string keys:")
    print(f"English: {translate('user_created', 'en')}")
    print(f"Vietnamese: {translate('user_created', 'vi')}")
    
    # Using shorthand functions
    print("\n3. Using shorthand functions:")
    print(f"_ function: {_(MessageKey.SUCCESS)}")
    print(f"t function: {t(MessageKey.PRODUCT_CREATED)}")
    
    # Product management messages
    print("\n4. Product management messages:")
    set_language('en')
    print(f"EN - Product created: {_(MessageKey.PRODUCT_CREATED)}")
    print(f"EN - Product not found: {_(MessageKey.PRODUCT_NOT_FOUND)}")
    
    set_language('vi')
    print(f"VI - Product created: {_(MessageKey.PRODUCT_CREATED)}")
    print(f"VI - Product not found: {_(MessageKey.PRODUCT_NOT_FOUND)}")
    
    # Error handling
    print("\n5. Error handling:")
    print(f"Non-existent key: {_('non_existent_key')}")  # Returns the key itself
    print(f"Invalid language: {translate(MessageKey.ERROR, 'invalid_lang')}")  # Falls back to English

if __name__ == "__main__":
    demo_i18n_usage()
