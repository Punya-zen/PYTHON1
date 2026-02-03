import os

def run():
    # GitHub Actions pass inputs as environment variables prefixed with INPUT_
    name_to_greet = os.environ.get("INPUT_WHO_TO_GREET", "World")
    print(f"Hello, {name_to_greet}!")
    
    # Setting an output for other steps to use
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f"time=noon", file=fh)

if _name_ == "_main_":
    run()
