from data_processing.validation import validate_isbn

def test_valid_isbn():
    result = validate_isbn('9780306406157')
    # TODO: assert result equals '9780306406157'

def test_invalid_isbn():
    result = validate_isbn('not-an-isbn')
    # TODO: assert result is None

def test_wrong_length():
    result = validate_isbn('123456789')
    # TODO: assert result is None

def test_hyphenated_isbn():
    assert validate_isbn("978-0306406157") == "9780306406157"

def test_empty_string():
    assert validate_isbn("   ") is None


def test_empty_string():
    assert validate_isbn("AGFSAHGOEDAS") is None