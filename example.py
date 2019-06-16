#!/usr/bin/env python

import argument


@argument.entrypoint
def main(working_dir: str, *, option1:int, option2:int=22):
    """
    Do something clever

    """
    print(working_dir)


if __name__ == '__main__':
    main()
