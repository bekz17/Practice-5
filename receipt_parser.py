import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# --- 1. Extract all prices ---
prices = re.findall(r"\d[\d\s]*,\d{2}", text)

# --- 2. Extract product names ---
product_pattern = r"\d+\.\n(.+)"
products = re.findall(product_pattern, text)

# --- 3. Extract total ---
total_match = re.search(r"ИТОГО:\n([\d\s]+,\d{2})", text)
total = total_match.group(1) if total_match else None

# --- 4. Extract date and time ---
datetime_match = re.search(r"Время:\s([\d\.]+\s[\d:]+)", text)
datetime = datetime_match.group(1) if datetime_match else None

# --- 5. Extract payment method ---
payment_match = re.search(r"(Банковская карта|Наличные):", text)
payment_method = payment_match.group(1) if payment_match else None

# --- 6. Structured output ---
data = {
    "products": products,
    "prices": prices,
    "total": total,
    "datetime": datetime,
    "payment_method": payment_method
}

print(json.dumps(data, indent=4, ensure_ascii=False))