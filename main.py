def remove_prefix_suffix_common(template, test):
    prefix_len = 0
    suffix_len = 0

    # Calculate prefix of template and test
    for template_letter, test_letter in zip(template, test):
        if template_letter != test_letter:
            break
        else:
            prefix_len += 1

    # Remove prefix
    template = template[prefix_len: len(template)]
    test = test[prefix_len: len(test)]

    # Calculate suffix of template and test
    for template_letter, test_letter in zip(reversed(template), reversed(test)):
        if template_letter != test_letter:
            break
        else:
            suffix_len += 1

    # Remove prefix
    template = template[0: len(template) - suffix_len]
    test = test[0: len(test) - suffix_len]

    return template, test


def is_typo(template, test):
    template, test = remove_prefix_suffix_common(template, test)

    if len(template) > 1 or len(test) > 1:
        return False
    else:
        return True


template_input, test_input = input().replace(" ", "").split(",")

print(is_typo(template_input, test_input))
