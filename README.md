# Argument Clinic

>  Ah. I'd like to have an argument, please.

The standard way of writing a command line tool in Python is rather
repetitive. You construct an `ArgumentParser` object with a doc
string add documented parameters with their type, call parse on
it and then call your `main(...)` with exactly the same parameters
and if you are a good citizen, you document the call stuff again.

```python

def main(input_file : str, *, scale : float = 125, fps : int = 30):
    """Create a movie based that has droste aspects."""
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Create a movie based that has droste aspects.')
    parser.add_argument('input_file', type=str)
    parser.add_argument('--scale', type=float, default=125)
    parser.add_argument('--fps', type=float, default=30)

    args = parser.parse_args()

    main(args.input, scale=args.scale, fps=args.fps)

``` 

With argument-clinic you can do the same with just:

```python

@argument.entrypoint
def main(input_file : str, *, scale : float = 125, fps : int = 30):
    """Create a movie based that has droste aspects."""
    pass

if __name__ == '__main__':
    main()

``` 

## Installation

`pip install argument-clinic`

## More details

As shown above, the basic usage is to use the `@argument.entrypoint`
for your main and have all command line arguments to your script be 
arguments of your `main(..)` entry point. When you call `main` the values
for each argument will be supplied automatically.

Separate positional arguments and keyword arguments in your
main with a `*` (which is good practice anyway). Anything after
the star becomes a flag that requires a value.

The doc string of your `main` will automatically become the help
for your script. If you document the parameters to your `main` in your
doc string, these comments will be added to the right parameters (any type
specification will be ignored though)

The best thing: it doesn't cost you 5 pounds for 5 more minutes.