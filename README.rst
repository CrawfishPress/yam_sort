yam_sort
---------

Ever needed to compare two YAML files, when the keys were **out of order**?
Maybe you've tried cutting and pasting to move the keys around, wondering if there's
*a better way*?
Well, now there is - **yam_sort!**

Okay, I may have been watching too much late-night TV. But this library was
born out of frustration working with YAML files.
I was using AWS API-Gateway YAML templates,
which sometimes get exported in *random* order (especially when there are changes to it),
making it hard to
compare with git-checked-in copies. After the *nth* time moving keys around, I
decided to automate it.

- Do basic diff-ing of YAML files, while ignoring the order of keys/sub-keys.
- Re-order a second dictionary/YAML file, to match the first file. Ignore missing keys,
  move extra keys to end of list.

Pip Requirements
----------------

-  PyYAML==5.1.2
-  virtualenv (optional, but highly recommended)

Installation
------------------------

.. code-block::

    # activate a virtual environment
    pip install yam_sort

Usage
------------------------
python -m main -h
usage: main.py [-h] [-s file_one file_two] [-k file_one file_two]

    Usage: TBD

optional arguments:

  -h, --help                                   show this help message and exit

  -s first second, --sync file_one file_two    sync two YAML files

  -k first second, --keys file_one file_two    diff two YAML files by keys only

Warning
------------------------

Since the intent of this library is to compare YAML files that were exported from
AWS API-Gateways, the resulting sorted-file has to be as similar as possible.
This includes formatting of the keys/values in the file. AWS exports keys as unquoted,
and all string-values as quoted. Therefore, this library makes all string-values as quoted.

It's not an ideal solution, and makes the results specific to one formatting-type,
but this way I can 'diff' the two files more easily. Which is the original purpose.

Long-term, I want to find a way to *preserve* the formatting from the source-file,
but for now, this works.
