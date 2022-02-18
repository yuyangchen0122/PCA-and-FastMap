"""
Author: {Yuyang Chen, Zihao Mei}
Date: {02/28/2022}
Course: {DSCI-552 Data Science for machine learning}
"""


def read_data(name):
    """
    Reading data
    Parameters
    ----------
    name : file name
    """
    f = open(name, "r")
    lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.strip('\n').split('\t'))
    # close the file
    f.close()
    return data


def read_list(name):
    """
    Reading list data
    Parameters
    ----------
    name : file name
    """
    f = open(name, "r")
    lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.strip('\n'))
    # close the file
    f.close()
    return data


if __name__ == '__main__':
    # read pca data
    pca_data = read_data("pca-data.txt")

    # read fast map data
    fastmap_data = read_data("fastmap-data.txt")

    # read fast map wordlist data
    fastmap_wordlist = read_list("fastmap-wordlist.txt")
