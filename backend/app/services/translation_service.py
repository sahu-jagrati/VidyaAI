from deep_translator import GoogleTranslator


def translate_hi(text: str) -> str | None:
    if not text or not text.strip():
        return None
    try:
        result = GoogleTranslator(source='en', target='hi').translate(text)
        return result or None
    except Exception as e:
        print(f"[translate_hi] FAILED: {type(e).__name__}: {e} | text={text[:50]!r}")
        return None
