"""Simple CLI entrypoint."""

import argparse
from .utils import sum_list, greet

def run():
    parser = argparse.ArgumentParser(description="Example app")
    parser.add_argument("--name", type=str, default="World", help="Name to greet")
    parser.add_argument("--nums", nargs="*", default=["1","2","3"], help="Numbers to sum")
    args = parser.parse_args()

    print(greet(args.name))
    print("Sum:", sum_list(args.nums))

if __name__ == "__main__":
    run()


























































#V2VsbCwgd2VsbOKApiBJIGhvcGUgeW914oCZdmUgYWxyZWFkeSBmaWd1cmVkIG91dCB0aGUgeWVhciBhbmQgbW9udGguIEkgZ3Vlc3MgeW914oCZcmUgY3VyaW91cyBhYm91dCB0aGUgZGF5PyBFYXN5IHBlYXN5IOKAlCBpdOKAmXMgdGhlIDEwdGg=
