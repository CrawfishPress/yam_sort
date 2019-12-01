## Purpose

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

This is a very narrowly-focussed library - it sorts one YAML file to match the
key-order in another YAML file. But I don't know of any other automated way of
doing this, and got tired of doing it manually.

## Pip Requirements

- PyYAML==5.1.2
- virtualenv (optional, but highly recommended)

## Installation

    # activate a virtual environment
    pip install yam_sort

## Usage

    yam_sort -h  
    yam_sort -s file_one file_two  # synchronizes second file with first, 
                                     writes to stdout
    yam_sort -s file_one file_two -o  # synchronizes second file with first, 
                                        overwrites second file
    yam_sort -k file_one file_two  # lists key-differences between files

```
optional arguments:
  -h, --help                                   show this help message and exit
  -s first second, --sync file_one file_two    sync two YAML files
  -o, --overwrite                              saves output to second file
  -k first second, --keys file_one file_two    diff two YAML files by keys only
```

#### Note

Since the intent of this library is to compare YAML files that were exported from
AWS API-Gateways, the resulting sorted-file has to be as similar as possible.
This includes formatting of the keys/values in the file. AWS exports keys as unquoted,
and all string-values as quoted. Therefore, this library copies the formatting
from the original file, in the output-file. If a string was double-quoted, it
will (should) be double-quoted in the output, and the same for single-quoting, etc.

#### Known Bugs

Some values can be multi-line, particularly in the section:
 - x-amazon-apigateway-gateway-responses:

These do not get properly copied over to the output-dict.
