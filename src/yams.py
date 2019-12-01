"""
Loads and processes YAML files

# Issue One
Sigh... And now I'm doing something completely kludgy.
The original YAML files I'm getting from AWS, and so they have
double-quoted strings. So I need the output from PyYaml
to use double-quotes strings - but only the value-strings, not the keys.
This is easier said than done... I looked at another library, ruamel.yaml,
which Stackoverflow seemed to indicate would work. But all it does,
besides diss-ing PyYaml, is preserve the formatting from an original
load of a file, when it's dumped back out. I'm creating a new dict
from scratch and converting it to YAML, so this doesn't help.

So I'm using the formatting from the *original* file, in the final result.
This is not ideal, but gets the file close enough to the repo-checked-in
version, that it's easy to diff, which was my original goal.

Long-term, it might be possible to modify PyYaml's Representers, so
they can distinguish between keys and values (all it knows is data-types,
like strings), but that's a much more involved project, and I'm trying
to finish this weekend - or at least have something that works
well enough. :)

# Issue two
Some values can be multi-line! That sounds like a project for version 2.0...

"""

import os

from yaml import load, dump, Loader, Dumper

from .differ import key_diff_something, synchronize_keys


def sync_two_files(some_list, overwrite=False):
    """ Re-orders second file to match key-order of first file. Writes to stdout, or
        existing file.
    :param some_list: list - of strings
    :param overwrite: boolean
    :return: stdout (or writes file)
    """

    files_valid = validate_yaml_file_pair(some_list, needs_write=overwrite)
    if not files_valid:
        return

    first_file, second_file = some_list[0], some_list[1]
    with open(first_file, 'r') as ffp:
        first_data = load(ffp, Loader=Loader)

    with open(second_file, 'r') as sfp:
        second_data = load(sfp, Loader=Loader)

    result_data = synchronize_keys(first_data, second_data)

    quoted_output = dump(result_data, Dumper=Dumper, sort_keys=False,
                         default_flow_style=False)

    final_output = kludge_re_format_strings(second_file, quoted_output)

    if overwrite:
        with open(second_file, 'w') as sfp:
            sfp.write(final_output)
    else:
        print(f"{final_output}")


def perform_key_diff(some_list):
    """ Determine key diff-set and print results
    :param some_list: list - of strings
    :return: list, list
    """

    files_valid = validate_yaml_file_pair(some_list)
    if not files_valid:
        return

    first, second = some_list[0], some_list[1]
    with open(first, 'r') as ffp:
        first_data = load(ffp, Loader=Loader)
    with open(second, 'r') as sfp:
        second_data = load(sfp, Loader=Loader)

    diff_set = key_diff_something(first_data, second_data)

    for diff_key, diff_val in diff_set.items():
        if diff_key != 'common_keys':
            print(f"{diff_key}: {diff_val}")
        else:
            print(f"\ncommon_keys:\n")
            for one_key in diff_val:
                print(f"{one_key}")


def validate_yaml_file_pair(some_list, needs_write=False):
    """
    :param some_list:   list - of strings
    :param needs_write: boolean
    :return: boolean
    """

    if len(some_list) != 2:
        print(f"wrong number of files given: [{len(some_list)}]")
        return False

    first, second = some_list[0], some_list[1]
    error_list = []

    check_file_perms(error_list, first)
    check_file_perms(error_list, second, needs_write)

    if error_list:
        for one_err in error_list:
            print(one_err)
        return False

    return True


def check_file_perms(error_list, one_file, needs_write=False):
    """
    :param error_list:  list
    :param one_file:    str
    :param needs_write: bool
    :return: - adds to error_list
    """

    if not one_file.endswith('.yaml'):
        err_msg = f"file [{one_file}] must be of type '.yaml'"
        error_list.append(err_msg)

    if needs_write:
        if not os.access(one_file, os.W_OK):
            err_msg = f"file [{one_file}] does not have WRITE permission"
            error_list.append(err_msg)
        else:
            if not os.access(one_file, os.R_OK):
                err_msg = f"file [{one_file}] does not have READ permission"
                error_list.append(err_msg)


def kludge_re_format_strings(second_file_name, quoted_output):
    """ Actually converts strings to a dict, where the key is the "normalized" (unquoted)
        version of the string, and the value is the original string. Then finds the output-string
        (which have been quoted by the representer(), and using the dict, gets the original
        string with its original formatting.
    :param second_file_name: str
    :param quoted_output:    list of str
    :return: str
    """

    def normalize_string(one_string):
        return one_string.rstrip().replace('"', '').replace('\\n', '').replace("'", "").replace('\\', '')

    with open(second_file_name, 'r') as sfp:
        second_data_lines = sfp.readlines()

    second_dict = {normalize_string(x): x.rstrip() for x in second_data_lines}

    unquoted_lines = [normalize_string(x) for x in quoted_output.split('\n')]

    final_lines = [second_dict[x] for x in unquoted_lines if x in second_dict and len(x) > 0]

    final_string = "\n".join(final_lines)

    return final_string
