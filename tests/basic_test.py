from unittest.mock import patch
import sys

import argument


def test_calling_works():
    main_param = 'main_param'
    optional_val = 40
    testargs = ['prog', main_param, '--optional_param', str(optional_val)]

    with patch.object(sys, 'argv', testargs):
        @argument.entrypoint
        def some_main(main_param: str, *, optional_param: int = 42):
            return main_param, optional_param

        main_param, optional_param = some_main()
        assert optional_param == optional_val
