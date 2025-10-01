import pandas as pd

def normalize_persian_text(text: str) -> str:
    import re
    
    if pd.isna(text):
        return None
    text = str(text).strip()
    
    text = text.replace("ي", "ی").replace("ك", "ک")
    
    text = re.sub(r"^[-–—]+\s*", "", text)
    
    text = re.sub(r"\s+", " ", text)
    return text if text else None