"""
Sorts one dictionary to match key-order of second dictionary.
Diffs two dictionaries, ignoring the order of sub-keys.

Keys are considered "in the same order" if they have the same position
in a list of keys (so extra keys in the list, would make matching keys
"out of order").

Assumes Python 3.6, which has OrderedDict as the base dictionary.

https://yaml.org/spec/1.2/spec.html
Note that special-characters are not recommended, but *are* allowed, in YAML key-names.
I'm currently using a plus-sign, that may change, or become configurable.
(And now I really should make the unit-tests work with any character. Sigh...)

"""

from copy import deepcopy
import os

KEY_SEP = '+'


def synchronize_keys(first_data, second_data):
    """ Re-orders second dictionary to match key-order of first dictionary
    :param first_data:  dict
    :param second_data: dict
    :return: dict
    """

    new_dict = {}
    copy_keys(first_data, second_data, new_dict)

    # print(f"new_dict = {new_dict}")

    return new_dict


def copy_keys(one_d, two_d, new_dict):
    """
    :param one_d:    dict
    :param two_d:    dict
    :param new_dict: dict - built up each iteration
    :return:
    """

    one_keys = list(one_d.keys())
    two_keys = list(two_d.keys())
    common_keys = [a_key for a_key in one_keys if a_key in two_keys]
    extra_keys = [a_key for a_key in two_keys if a_key not in one_keys]

    for a_key in common_keys:
        new_dict[a_key] = two_d[a_key]

    for a_key in extra_keys:
        new_dict[a_key] = two_d[a_key]

    for a_key in common_keys:
        if isinstance(one_d[a_key], dict) and isinstance(two_d[a_key], dict):
            new_dict[a_key] = {}  # getting rid of existing sub-dict, may be in wrong order
            copy_keys(one_d[a_key], two_d[a_key], new_dict[a_key])


def key_diff_something(first_data, second_data, format='long', key_sep=KEY_SEP):
    """ Determine key diff-set
    :param first_data:  dict
    :param second_data: dict
    :param format:      str ('short', 'long')
    :param key_sep:     str
    :return: dict
    """

    diffs = {'missing_keys': [],
             'extra_keys': [],
             'mis_type_keys': [],
             'mis_value_keys': [],
             'mis_order_keys': [],
             'common_keys': [],
             }

    cur_key_path = ''

    meander_down_dict(first_data, second_data, cur_key_path, diffs, format, key_sep)

    return diffs


def meander_down_dict(one_d, two_d, cur_key_path, results, format, key_sep):
    """ Recurses down two dictionaries, more-or-less in parallel. Builds list of each
        type of key.
    :param one_d:        dict
    :param two_d:        dict
    :param cur_key_path: str
    :param results:      dict - added to, each iteration
    :param format:       str
    :param key_sep:      str
    :return:
    """

    if format == 'long' and cur_key_path:
        key_pre = f"{cur_key_path}{key_sep}"
    else:
        key_pre = ""

    one_keys = list(one_d.keys())
    two_keys = list(two_d.keys())

    missing = [f"{key_pre}{str(a_key)}" for a_key in one_keys if a_key not in two_keys]
    extra = [f"{key_pre}{str(a_key)}" for a_key in two_keys if a_key not in one_keys]

    common_keys = [a_key for a_key in one_keys if a_key in two_keys]
    common = [f"{key_pre}{str(a_key)}" for a_key in common_keys]

    mis_types = [f"{key_pre}{str(a_key)}" for a_key in common_keys
                 if not isinstance(one_d[a_key], type(two_d[a_key]))]

    mis_order = [f"{key_pre}{str(a_key)}" for a_key in common_keys
                 if one_keys.index(a_key) != two_keys.index(a_key)]

    results['missing_keys'].extend(missing)
    results['extra_keys'].extend(extra)
    results['mis_type_keys'].extend(mis_types)
    results['mis_order_keys'].extend(mis_order)
    results['common_keys'].extend(common)

    for a_key in common_keys:
        if format == 'long' and cur_key_path:
            sub_key_pre = f"{cur_key_path}{key_sep}{str(a_key)}"
        else:
            sub_key_pre = f"{str(a_key)}"

        if isinstance(one_d[a_key], dict) and isinstance(two_d[a_key], dict):
            meander_down_dict(one_d[a_key], two_d[a_key], sub_key_pre, results, format, key_sep)
