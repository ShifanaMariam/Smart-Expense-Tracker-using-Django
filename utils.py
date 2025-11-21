KEYWORD_MAP = {
    'uber': 'Travel', 'ola': 'Travel', 'bus': 'Travel', 'train': 'Travel',
    'pizza': 'Food', 'restaurant': 'Food', 'coffee': 'Food', 'burger': 'Food',
    'electricity': 'Bills', 'internet': 'Bills', 'phone': 'Bills',
    'amazon': 'Shopping', 'flipkart': 'Shopping', 'shirt': 'Shopping',
    'movie': 'Entertainment', 'netflix': 'Entertainment',
    'doctor': 'Health', 'hospital': 'Health', 'pharmacy': 'Health',
}

def predict_category(description):
    desc = (description or "").lower()
    for kw, cat in KEYWORD_MAP.items():
        if kw in desc:
            return cat
    return 'Other'
