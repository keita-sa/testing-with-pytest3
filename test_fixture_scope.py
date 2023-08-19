import pytest

@pytest.fixture(scope='function')
def fixture_function():
    """
    テスト関数ごとに、一回実行
    """
    print('前処理： function')
    yield
    print('後処理： function')

@pytest.fixture(scope='class')
def fixture_class():
    """
    テストクラスごとに、一回実行
    """
    print('前処理： class')
    yield
    print('後処理： class')

@pytest.fixture(scope='module')
def fixture_module():
    """
    モジュール(ファイル)ごとに、一回実行
    """
    print('前処理： module')
    yield
    print('後処理： module')

@pytest.fixture(scope='session')
def fixture_session():
    """
    セッション(pytestコマンドでテストを実施)ごとに、一回実行
    """
    print('前処理： session')
    yield
    print('後処理： session')


class TestFixtureScope_2():

    def test_1(
            self,
            fixture_function,
            fixture_class,
            fixture_module,
            fixture_session):
        pass

    def test_2(
            self,
            fixture_function,
            fixture_class,
            fixture_module,
            fixture_session):
        pass


class TestFixtureScope_1():

    def test_1(
            self,
            fixture_function,
            fixture_class,
            fixture_module,
            fixture_session):
        pass

    def test_2(
            self,
            fixture_function,
            fixture_class,
            fixture_module,
            fixture_session):
        pass