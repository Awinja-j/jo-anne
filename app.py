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
g=st.lists(st.one_of(st.integers(),st.just('joan'), st.none()))
h=st.dates()
n={"a":g}
m={"p":h}
l=st.fixed_dictionaries(n, optional=m).map(lambda x: anything(x['a'], x['p'] if 'p' in x else 90) )
@given(l)
def test_is_integers(s):
    print(s)
    assert s == s

@given(st.lists(st.integers()))
def test_is_list(s):
    print(s)
    assert s == s

class anything:
    def __init__(self, d, b):
        self.d=d
        self.b=b





if __name__ == '__main__':
    # test_is_datetime()
    # test_is_list()
    test_is_integers()
    # test_is_dates()
    # test_is_boolean()