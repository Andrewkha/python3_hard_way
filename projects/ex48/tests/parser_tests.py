from nose.tools import *
import lexicon


def test_sentence():
    assert_equals(lexicon.parse_sentence([('verb', 'run'), ('direction', 'north')]).subject, 'player')
    assert_equals(lexicon.parse_sentence([('verb', 'run'), ('direction', 'north')]).verb, 'run')
    assert_equals(lexicon.parse_sentence([('verb', 'run'), ('direction', 'north')]).object, 'north')


def test_exception():
    assert_raises(lexicon.ParserError, lexicon.parse_sentence, [('direction', 'north'), ('verb', 'run')])

