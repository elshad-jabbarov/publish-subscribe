import os


def contents(root):
    list_of_contents = []
    for item in os.listdir(root):
        if os.path.isdir or os.path.isfile(os.path.join(root, item)):
            k = (root + "\ has " + item)
            list_of_contents.append(k)
    return list_of_contents
