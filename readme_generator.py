#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Generate a README.md

initially forked from https://github.com/yoshikakbudto/hackerrank

"""

import os
import functools


def getFoldersNames(path):
    folders = []
    for item in os.listdir(path):
        if not os.path.isfile(item) and item not in ('.git', '.code'):
            folders.append(item)
    return folders


def getFilesNames(path):
    files = os.listdir(path)
    return files


def getProblemURLandScore(path):
    inFile = open(path, 'r', encoding='utf-8')
    url = inFile.readline().split()[-1]
    score = inFile.readline().split()[-1]
    inFile.close()
    return url, score


def getTotalNumberOfProblems():
    totalNumber = 0
    folders = getFoldersNames(os.getcwd())
    for folder in folders:
        subfolders = getFoldersNames(os.path.join(os.getcwd(), folder))
        for subfolder in subfolders:
            totalNumber += len(getFilesNames(os.path.join(os.getcwd(), folder, subfolder)))
    return totalNumber


readmeFile = open('README.md', 'w', encoding='utf-8')

print(file=readmeFile)
print('# Solutions to Hackerrank practice problems', file=readmeFile)
print('This repository contains ' + str(getTotalNumberOfProblems()) + ' solutions to Hackerrank practice problems with Python 3.', file=readmeFile)
print(file=readmeFile)

print(file=readmeFile)
print('[![commit activity](https://img.shields.io/github/commit-activity/y/yoshikakbudto/hackerrank.svg)](https://github.com/yoshikakbudto/hackerrank)', file=readmeFile)
print('[![repo size in bytes](https://img.shields.io/github/repo-size/yoshikakbudto/hackerrank.svg)](https://github.com/yoshikakbudto/hackerrank) ', file=readmeFile)
print('[![last commit](https://img.shields.io/github/last-commit/yoshikakbudto/hackerrank.svg)](https://github.com/yoshikakbudto/hackerrank) ', file=readmeFile)

print(file=readmeFile)

folders = getFoldersNames(os.getcwd())
for folder in sorted(folders):
    print('- ' + folder, file=readmeFile)
    subfolders = getFoldersNames(os.path.join(os.getcwd(), folder))
    for subfolder in sorted(subfolders):
        print('    ' + subfolder, file=readmeFile)
        files = getFilesNames(os.path.join(os.getcwd(), folder, subfolder))
        for file in sorted(files):
            if file.endswith(('.cpp', '.py', '.sql')):
                print("parsing", file)
                url, score = getProblemURLandScore(os.path.join(os.getcwd(), folder, subfolder, file))
                print('        - ' + "".join(file.split(".")[1:-1])[1:]
                      + ' | [Problem](' + url
                      + ')'
                      + ' | [Solution]'
                      + '(https://github.com/yoshikakbudto/hackerrank/blob/master/'
                      + folder.replace(' ', '%20') + '/' + subfolder.replace(' ', '%20') + '/'
                      + file.replace(' ', '%20') + ')'
                      + ' | Score: ' + str(score), file=readmeFile)

readmeFile.close()
