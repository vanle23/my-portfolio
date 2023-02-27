import sys

def to_slug(string):
    """
    Convert a string to a slug by replacing spaces with hyphens
    and removing all non-alphanumeric characters.
    """
    slug = string.lower().replace(' ', '-')
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    return slug


if __name__ == "__main__":
    print(to_slug(sys.argv[1]))
