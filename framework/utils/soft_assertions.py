def multiple(assertion_method, *methods):
    collected_fails = []
    for assertion in (assertion_method, *methods):
        passed, err = assertion()
        if not passed:
            collected_fails.append(err)

    formatted_messages = format_error_messages(collected_fails)
    message = 'One or more errors occurred:\n' + '\n'.join(formatted_messages)
    assert not collected_fails, message


def collect_multiple(assertion_condition_and_message, *assertion_conditions_and_messages):
    errors = [error
              for passed, error in (assertion_condition_and_message, *assertion_conditions_and_messages)
              if not passed]
    formatted_messages = format_error_messages(errors)
    message = 'One or more errors occurred:\n' + '\n'.join(formatted_messages)
    assert not errors, message


def format_error_messages(error_messages):
    return [f'{idx + 1}) {fail}' for idx, fail in enumerate(error_messages)]
