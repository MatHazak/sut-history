import pandas as pd

def load_processed():
    from pathlib import Path
    notebook_dir = Path.cwd()
    data_path = notebook_dir.parent / "data" / "processed" / "courses_clean.csv"
    return pd.read_csv(data_path, dtype={"capacity": "Int32", "enrolled": "Int32"})
	
def normalize_persian_text(text: str) -> str:
    import re
    
    if pd.isna(text):
        return None
    text = str(text).strip()
    
    text = text.replace("ي", "ی").replace("ك", "ک")
    
    text = re.sub(r"^[-–—]+\s*", "", text)
    
    text = re.sub(r"\s+", " ", text)
    return text if text else None

def persian_text(txt):
    import arabic_reshaper, bidi.algorithm
    return bidi.algorithm.get_display(arabic_reshaper.reshape(txt))