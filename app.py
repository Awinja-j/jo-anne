from hypothesis import given
import hypothesis.strategies as st

@given(st.datetimes())
def test_is_datetime(s):
    print(s)
    assert s == s

@given(st.booleans())
def test_is_boolean(s):
    print(s)
    assert s == s

@given(st.dates())
def test_is_dates(s):
    print(s)
    assert s == s

@given(st.integers(min_value=0, max_value=10))
def test_is_integers(s):
    print(s)
    assert s == s

@given(st.lists(st.integers()))
def test_is_list(s):
    print(s)
    assert s == s


if __name__ == '__main__':
    test_is_datetime()
    test_is_list()
    test_is_integers()
    test_is_dates()
    test_is_boolean()