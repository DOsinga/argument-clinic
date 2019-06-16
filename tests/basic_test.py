from unittest import mock

import argument


def test_calling_works():
    @argument.entrypoint
    def some_main(main_param: str, *, optional_param: int = 42):
        return main_param, optional_param

    # Pytest passes in the name of the test as the first parameter:
    main_param, optional_param = some_main()
    assert optional_param == 42
