import pytest

@pytest.fixture()
def test01():
    return 1

@pytest.mark.ui('nihao')
def test02():
    print('test02')


def test03():
    print('test03')
@pytest.mark.ui('nihao')
def test04(test01):
    assert  test01==2
    print('test04')

if __name__ == '__main__':
    pytest.main()