import argparse
parser = argparse.ArgumentParser()
parser.add_argument("greeting", help="greeting")
parser.add_argument("-n", "--name", help="name of the person you are greeting")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()

if (args.name):
    print(args.greeting + " " + args.name)
else:
    print(args.greeting)
