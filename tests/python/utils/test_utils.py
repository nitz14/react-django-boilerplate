from utils import validate_email


def test_validate_email():
    assert validate_email('fail') is False
    assert validate_email('') is False
