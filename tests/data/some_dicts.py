# Test sets for key_diff_something()
set_one = {
    'one': {'alpha': 1, 'delta': 42, 'tango': ['one', 'two'],
            'beta': {'gamma': 99, 'theta one': 123, 500: 500}},
    'two': {'alpha': 1, 'delta': 99, 'tango': ['one', 'two'],
            'beta': {'gamma': 99, 'theta one': 123, 500: 500}},

    'short_results': {
        'missing_keys': [],
        'extra_keys': [],
        'mis_type_keys': [],
        'mis_value_keys': [],
        'mis_order_keys': [],
        'common_keys': ['alpha', 'delta', 'tango', 'beta',
                        'gamma', 'theta one', '500']
    },

    'long_results': {
        'missing_keys': [],
        'extra_keys': [],
        'mis_type_keys': [],
        'mis_value_keys': [],
        'mis_order_keys': [],
        'common_keys': ['alpha', 'delta', 'tango', 'beta',
                        'beta+gamma', 'beta+theta one', 'beta+500']
    }
}

set_two = {
    'one': {'alpha': 1, 'delta': 42, 'tango': ['one', 'two'], 'tigger': 'weird animal',
            'beta': {'gamma': 99, 'theta one': 123, 500: 500}},
    'two': {'alpha': 1, 'epsilon': 99, 'tango': ['one', 'two', 'three'], 'tigger': 86,
            'beta': {'gamma': 99, 'theta one': 123, 500: 500}},

    'short_results': {
        'missing_keys': ['delta'],
        'extra_keys': ['epsilon'],
        'mis_type_keys': ['tigger'],
        'mis_value_keys': [],
        'mis_order_keys': [],
        'common_keys': ['alpha', 'tango', 'tigger', 'beta',
                        'gamma', 'theta one', '500']
    },

    'long_results': {
        'missing_keys': ['delta'],
        'extra_keys': ['epsilon'],
        'mis_type_keys': ['tigger'],
        'mis_value_keys': [],
        'mis_order_keys': [],
        'common_keys': ['alpha', 'tango', 'tigger', 'beta',
                        'beta+gamma', 'beta+theta one', 'beta+500']
    }
}

# Test sets for synchronize_keys()
set_three = {
    'one': {'alpha': 1,
            'beta': {'gamma': 99, 'theta one': 123, 500: 500},
            'tango': ['one', 'two'],
            'tigger': 'weird animal',
            },

    'two': {'alpha': 22,
            'beta': {'gamma': 99, 'theta one': 123, 500: 500},
            'tango': ['one', 'two', 'three'],
            'tigger': 86}
}

set_four = {
    'one': {'alpha': 1,
            'beta': {'gamma': 99, 'theta one': 123, 500: 500},
            'tango': ['one', 'two'],
            'tigger': 'weird animal',
            },

    'two': {'alpha': 22,
            'tango': ['one', 'two', 'three'],
            'tigger': 86,
            'beta': {500: 500, 'gamma': 99, 'theta one': 123}
            }
}

set_five = {
    'one': {'alpha': 1,
            'beta': {'gamma': 99, 'theta one': 123, 500: 500},
            'tango': ['one', 'two'],
            'psi': {'rho': 'row row, your boat', 'theta two': {123: 'key is integer', 'tau': 99}},
            'tigger': 'weird animal',
            },

    'two': {'alpha': 22,
            'delta': 'extra-key here',
            'tigger': 86,
            'beta': {500: 500, 'theta one': 123, 'gamma': 99},
            'tango': ['one', 'two', 'three'],
            'psi': {'beta two': 'extra-key again',
                    'theta two': {'tau': 99, 123: 'key is integer'},
                    'rho': 'to the beat'},
            }
}

set_six = {
    'one': {'alpha': 1,
            'beta': {'gamma': 99, 'theta one': 123, 500: 500},
            'missing-key': 'uh-oh, now what',
            'tango': ['one', 'two'],
            'psi': {'rho': 'row row, your boat', 'theta two': {123: 'key is integer', 'tau': 99}},
            'tigger': 'weird animal',
            },

    'two': {'alpha': 22,
            'delta': 'extra-key here',
            'tigger': 86,
            'beta': {500: 500, 'theta one': 123, 'gamma': 99},
            'tango': ['one', 'two', 'three'],
            'psi': {'beta two': 'extra-key again',
                    'theta two': {'tau': 99, 123: 'key is integer'},
                    'rho': 'to the beat'},
            }
}
