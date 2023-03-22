import re

text = "Это мой номер телефона: +7 123 456-78-90. А это номер моего друга: 8-800-123-45-67."
phone_regex = r"(?:\+7|8)?[- ](?:(?:\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}))"

matches = re.findall(phone_regex, text)

print(matches)