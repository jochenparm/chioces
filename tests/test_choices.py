from collections import OrderedDict

from enum_choices import (
    __version__,
    Choices,
    BoolIntTypeChoice,
)


def test_version():
    assert __version__ == '0.0.1'


def test_choices_bool():
    assert BoolIntTypeChoice.YES == 1
    assert BoolIntTypeChoice.NO == 0


def test_choices_bool_choice():
    assert BoolIntTypeChoice.choices == [(0, 'no'), (1, 'yes')]


def test_choices_bool_choices_map():
    item = [(0, 'no'), (1, 'yes')]
    assert BoolIntTypeChoice.choices_map == OrderedDict(item)


def test_choices_bool_choices_map():
    item = [(0, 'no'), (1, 'yes')]
    assert BoolIntTypeChoice.choices_map == OrderedDict(item)


def test_choices_bool_fmt():
    target = "0:no,1:yes"
    assert ",".join(BoolIntTypeChoice.iter) == target