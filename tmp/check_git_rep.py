#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import re

# subproess调用shell命令的安全性
# https://blog.csdn.net/Chasing__Dreams/article/details/124923033

# \033[显示方式; 前景色; 背景色m******\033[0m

rootPath = os.path.dirname(os.path.abspath(__file__)) # 当前文件所在根目录
# rootPath = os.getcwd().replace("\\", "/") # 执行进程所在根目录，取决于在哪个地方执行

count = 0
for dirpath, dirnames, filenames in os.walk(rootPath):
    for dirname in dirnames:
        gitdir = os.path.join(dirpath, dirname, ".git")
        if os.path.isdir(gitdir) and os.path.exists(gitdir):
            repo_path = os.path.dirname(gitdir).replace("\\", "/")
            # out = subprocess.check_output("cd %s && git remote -v" % repo_path, shell=True)
            p = subprocess.Popen('bash', stdin=subprocess.PIPE, shell=True,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.stdin.write("cd %s\n" % repo_path)
            p.stdin.write("git remote -v\n")
            p.stdin.write("git status\n")
            p.stdin.write("exit 0\n")
            p.stdin.close()
            out, err = p.communicate()
    
            ret = re.search("(.*?)\(fetch\)", out)
            if ret:
                print(u"----> {:<35}{:<35}".format(repo_path, ret.group(1)))
            else:
                print(u"----> {:<35}{:<35s}".format(repo_path, u"Local repositories"))

            if re.search("Untracked files:", out):
                print("-> Untracked files")
            if re.search("Changes not staged for commit:", out):
                print("-> Changes not staged for commit")
            if re.search("Changes to be committed:", out):
                print("-> Changes to be committed")

            if ret:
                subprocess.check_output("cd %s && git remote update" % repo_path, shell=True)

                ret = subprocess.check_output("cd %s && git status" % repo_path, shell=True)
                if re.search("Your branch is ahead of ", out):
                    print("-> Your branch is ahead of remote, may be to: git push")
                elif re.search("Your branch is behind ", out):
                    print("-> Your branch is behind of remote:, may be to: git pull")
            print("")