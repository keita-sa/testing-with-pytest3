"""Demo fixture scope."""

import pytest


@pytest.fixture(scope='function') # テスト関数ごとに1回実行される
def func_scope():
    """A function scope fixture."""


@pytest.fixture(scope='module') # テストファイル全体で1回実行される
def mod_scope():
    """A module scope fixture."""


@pytest.fixture(scope='session') # テスト全体で1回だけ実行される
def sess_scope():
    """A session scope fixture."""


@pytest.fixture(scope='class') # テストクラス全体で1回実行される
def class_scope():
    """A class scope fixture."""


def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module, and function scope fixtures."""


def test_2(sess_scope, mod_scope, func_scope):
    """Demo is more fun with multiple tests."""

@pytest.mark.usefixtures('class_scope')
class TestSomething():
    """Demo class scope fixtures."""

    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Again, multiple tests are more fun."""
