# import libs
import argparse
from os.path import exists

# build a parser
parser = argparse.ArgumentParser(description='Patch ACF models from txt files')

parser.add_argument('-a', metavar='--acf', type=str, required=True,
    help='filename of your acf model, ex: carboncub.acf')

parser.add_argument('-p', metavar='--patch', type=str, required=True,
    help='patch file ending in .acf.txt')

args = parser.parse_args()

# check if files exists
acf_exists = exists(args.a)
patch_exists = exists(args.p)

# acf model check
if (acf_exists):
    print("Using model: " + args.a)

else:
    raise Exception(args.a + " file does not exist")

# patch text check
if (patch_exists):
    print("Using model: " + args.p)

else:
    raise Exception(args.p + " file does not exist")

# open acf file
with open(args.a, 'r') as file:
    acf = file.read().split('\n')

# open patch file
with open(args.p, 'r') as file:
    patch = file.read().split('\n')

# acf list
acfList = []
for line in acf:
    vars = line.split(' ')
    acfList.append(vars)

# patch list
patchList = []
for line in patch:
    if line.rstrip():
        vars = line.split(' ')
        patchList.append(vars)

# open patched file
patched_file = open(args.a + ".patched", "w")

# write acf patched file
for line in acf:

    output = line + "\n"
    vars = line.split(' ')

    if len(vars) == 3:
        for p_vars in patchList:
            if (vars[1] == p_vars[1]):
                output = vars[0] + " " + vars[1] + " " + p_vars[2] + "\n"

    patched_file.write(output)

# close patched file
patched_file.close()
