import pytest


class TestFountains:

    @pytest.mark.parametrize("test_input,expected",[
        ([1, 1, 1, 1], 2),
        ([1, 3, 1, 1, 1, 1, 2, 1, 1], 2),
        ([1, 1, 1, 2, 1, 1, 1, 3, 1, 1], 3)
    ])
    def test_fountain_activation(self, test_input, expected):
        pytest.fail()

    def test_covers_until_previous_running_fountain(self):
        pytest.fail()
