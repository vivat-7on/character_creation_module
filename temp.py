TEST_DATA = tuple[
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

for rep, result, effect in TEST_DATA:
    print(rep, result, effect)
