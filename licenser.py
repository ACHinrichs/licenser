import argparse
import os

scriptpath = os.path.dirname(os.path.realpath(__file__)) 
licensepath = os.path.join(scriptpath ,"licenses")



def licenseExists(name):
    return(os.path.isfile(os.path.join(licensepath, name.lower())))


# Setup Arg-Parser and parse args
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory",
                    help = "The target directory",
                    type=str,
                    default=".")
parser.add_argument("-l", "--license",
                    help = "The license, which shall be created.\n"+
                    "Will be prompted for if omited. Omit, if a license shall be updated",
                    type=str, default="")
parser.add_argument("--listlicenses",
                    help = "Prints a list of installed licenses",
                    action="store_true")
parser.add_argument("-a", "--author",
                    help = "The author(s) of the piece of sourcecode.\n"+
                    "Will be prompted for if omited. Omit, if a license shall be update",
                    type=str,
                    default="")
parser.add_argument("-u", "--update",
                    help = "If an existing license shall be updated.\n"+
                    "This will replace all year-number which are found with the current year.\n"+
                    "A year is a 4-Digit Number starting with either 19 or 20.",
                    action="store_true")
args = parser.parse_args()


if args.listlicenses:
    print("Listing Licenses\n")
    dirs = os.listdir(licensepath)
    for file in dirs:
        print(file)
    exit()
if args.update:
    print("I will update the LICENSE file in this directory")
else:
    print("I will create a new LICENSE file in this directory")

    license=args.license
    if license == "":
        license = input("Please specify a license: ")
        while not licenseExists(license):
            license = input("Please specify a existing license: ")
    elif not licenseExists(license):
        print("ERROR: License does not exist.")
    author = args.author
    if author == "":
        author = input("Please specify the author: ")
    
