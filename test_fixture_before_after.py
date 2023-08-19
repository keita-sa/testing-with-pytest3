import pytest


class TestFixtures():

    @pytest.fixture()
    def sample(self):
        print("前処理")
        yield
        print("後処理")

    def test_hoge(self, sample):
        print(sample)
        print("本処理")
        assert 1 == 1