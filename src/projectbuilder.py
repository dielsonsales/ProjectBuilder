from argparse import ArgumentParser
from foldercopier import copy_folder

parser = ArgumentParser(
    description="Create a project stack with all the "
    + "recommended configurations"
)

language_folders_map = {
    "c": "templates/c",
    "python": "templates/python",
}


def setup_parser():
    parser.add_argument(
        "-n", "--name", help="Name of the project", required=True
    )
    parser.add_argument(
        "-l", "--language", help="Language of the project", required=True
    )


def main():
    setup_parser()
    args = parser.parse_args()
    print("Copying files...")
    copy_folder(language_folders_map[args.language], args.name)


if __name__ == "__main__":
    main()
