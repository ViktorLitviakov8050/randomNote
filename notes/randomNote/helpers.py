import re

def camel_snake_case(camel_case_string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()
