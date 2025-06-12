# [Are Python Dictionaries Ordered Data Structures?](https://www.thepythoncodingstack.com/p/are-python-dictionaries-ordered-data)

## Introduction

## Some History First

1. un-am-bi-guous
2. de-tour

## Dictionaries in Python 3.6 and 3.7 (and Later)

1. Python dictionaries now maintain the order of insertion of key-value pairs

## Dictionaries Preserve the Order of Insertion

1. The fact that the two dictionaries have the same key-value pairs is sufficient to make these dictionaries equal. The order is not important.
2. The order of the items is a fundamental characteristic of lists. Therefore, these lists are not considered equal.

## How about ````collections.OrderedDict````?

1. In an ````collections.OrderedDict````, the order matters. Recall that the order in a standard dictionary, even though it is preserved, doesn't matter–standard dictionaries with the same items but in a different order are still considered equal.

## Final Words

1. character-is-tics
2. sequences with the same items but in a different order are considered different