def validate_isbn(isbn):
    """Clean and validate an ISBN-13 value.

    Args:
        isbn: Raw ISBN value (may be a hyphenated string, a number, or None)

    Returns:
        The cleaned ISBN-13 string if valid, or None if invalid.
    """

    if isbn is None:
        return None

    # Convert to string and remove hyphens
    isbn = str(isbn).replace("-", "").strip()

    # Must be exactly 13 digits
    if len(isbn) != 13:
        return None

    if not isbn.isdigit():
        return None

    # Calculate check digit from first 12 digits
    total = 0

    for i, digit in enumerate(isbn[:12]):
        digit = int(digit)

        if i % 2 == 0:
            total += digit
        else:
            total += digit * 3

    expected_check_digit = (10 - (total % 10)) % 10
    actual_check_digit = int(isbn[12])

    if expected_check_digit != actual_check_digit:
        return None

    return isbn