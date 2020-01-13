import os

PATH = 'data/'


def traversal(path):
    ls = os.listdir(path)
    res = []
    extra_ls = []
    for l in ls:
        if os.path.isdir(os.sep.join([path, l])):
            extra_ls = traversal(os.sep.join([path, l]))
        else:
            res += l
    res += extra_ls
    return res

traversal(PATH)
