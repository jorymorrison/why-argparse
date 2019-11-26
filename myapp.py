import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--greeting")
parser.add_argument("-n", "--name")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
print(args.greeting + " " + args.name)
