import re


def camel_to_snake(s):
    s1 = re.sub(r'^[a-z0-9]+', '', s)
    s2 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s1)
    s3 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s2)
    s4 = re.sub(r'(64|32|16)$', '', s3)
    return s4.lower()

def camel_to_capital(s):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.upper()


if __name__ == '__main__':
    print(camel_to_snake("dwLevel"))