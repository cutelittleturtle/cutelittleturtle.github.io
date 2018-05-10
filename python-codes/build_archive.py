#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs
import sys, getopt
import os
import shutil

from get_stream import update_stream_archive
from get_gongyan import update_gongyan_archive

# This script read a text+url text file to produce a jekyll friendly post file for publihsing html

def _isurl(line):

    _urldef = ('http','https','www','ftp')
    if any(x in line for x in _urldef):
        return True
    else:
        return False

def build_teamX(sourcefolder, outputfile):
    header_string = ""
    with codecs.open(sourcefolder + "sources" + os.path.sep + "teamX-show.head", 'r', encoding='utf-8') as f:
        for line in f:
            header_string = header_string + line

    body_string = ""
    with codecs.open(sourcefolder + "补档.txt", 'r', encoding="utf-8") as f:
        # print('Opening file: ' + inputfile)
        linecount = 0
        firstsection = True

        for line in f:
            outline2 = ""

             # remove UTF-BOM made by Windows notepad
            if codecs.BOM_UTF8.decode('utf-8') in line:
                line = line.replace(codecs.BOM_UTF8.decode('utf-8'),"")

            if "asset_img" in line:
                if not firstsection:
                    outline2 = "</div>" + "\n"+ "\n\n\n"
                outline2 = outline2 + "<div id = \"asset-img\">" + "\n" + line.strip() + "\n"
            elif line.strip(): # start with non-empty lines
                try:
                    neline = next(f)
                except StopIteration:
                    print("End of file")
                    break

                if not neline.strip(): # if empty next line -> section header
                    if not firstsection:
                        outline2 = "</div>" + "\n"

                    if line[0] == "#":
                        outline2 = outline2 + "\n\n\n## " + line[1:].strip()
                    else:
                        outline2 = outline2 + "\n\n\n# " + line.strip()

                    _id = 1
                    outline2 = outline2 + "\n" + "<div id = \"bqdark\" markdown=\"1\">\n"
                    firstsection = False

                elif _isurl(neline): # if valid url next line -> source
                    outline2 = str(_id) + ". [" + line.rstrip() + "]" + "(" + neline.rstrip() + ")"
                    placeholder = " " * len(str(_id))

                    try:
                        neneline=next(f)
                    except StopIteration:
                        _id = _id + 1
                        body_string = body_string + outline2 + "\n"
                        print("End of file")
                        break

                    while neneline.strip(): # all consecutive lines under a source are treated as urls
                        if not _isurl(neneline):
                            print(neneline + " not an url: skipped")
                            try:
                                neneline=next(f)
                                continue
                            except StopIteration:
                                print("End of file")
                                break


                        sourcename = ""
                        if "youku" in neneline:
                            sourcename = "优酷"
                        elif "iqiyi" in neneline:
                            sourcename = "爱奇艺"
                        elif "tudou" in neneline:
                            sourcename = "土豆"
                        elif "v.qq.com" in neneline:
                            sourcename = "腾讯"
                        elif "youtube" in neneline:
                            sourcename = "油管"
                        else:
                            sourcename = "其它"
                            #emsg = "Unknown video source: \n" + neneline
                            #raise ValueError(emsg)

                        outline2 = outline2 + "," + placeholder + "   [" + sourcename + "]" + "(" + neneline.rstrip() + ")"
                        try:
                            neneline=next(f)
                        except StopIteration:
                            print("End of file")
                            break

                    outline2 = outline2 + "\n"
                    _id = _id + 1

                else: # if next line is not empty nor a source with a valid url
                    print("Error at line: " + line)
                    print(neline)
                    raise ValueError("Only one line is allowed for each section header")

            linecount = linecount + 1
            body_string = body_string + outline2

    body_string = body_string + "</div>\n"

    wiki_string = ""
    with codecs.open(sourcefolder + "sources" + os.path.sep + "teamX-show.wiki", 'r', encoding="utf-8") as f:
        for line in f:
            wiki_string = wiki_string + line

    with codecs.open(outputfile,"w", encoding="utf-8") as fo:
        fo.write(header_string + "\n")
        fo.write(body_string + "\n")
        fo.write(wiki_string)

def concatenate_files(sourcefolder):

    sourcefolder2 = sourcefolder + "补档模块" + os.path.sep
    filenames = [sourcefolder2 + "公演.txt", sourcefolder2 + "最新活动.txt", sourcefolder2 + "综艺.txt", sourcefolder2 + "MV.txt",
                 sourcefolder2 + "mini-live.txt", sourcefolder2 + "直播.txt"]

    with codecs.open(sourcefolder + "补档.txt", 'w', encoding='utf-8') as fo:
        for fname in filenames:
            with codecs.open(fname, 'r', encoding='utf-8') as fi:
                for line in fi:
                    # remove UTF-BOM made by Windows notepad
                    if codecs.BOM_UTF8.decode('utf-8') in line:
                        line = line.replace(codecs.BOM_UTF8.decode('utf-8'),"")
                    fo.write(line)
            fo.write("\n\n")

    print("archive parts concatenated for 补档.txt!")

if __name__ == '__main__':

    sourcefolder = os.path.abspath(os.path.join(os.getcwd(), "..")) + os.path.sep + "文章" + os.path.sep

    # 创立 公演补档
    update_stream_archive()
    update_gongyan_archive()

    concatenate_files(sourcefolder)

    build_teamX(sourcefolder, os.getcwd() + os.path.sep + "teamX-archive.md")
    destination = os.path.abspath(os.path.join(os.getcwd(), "..")) + os.path.sep + "source" + os.path.sep + "_posts" + os.path.sep
    shutil.copy2("teamX-archive.md", destination + "teamX-show.md")

    # 复制 CP补档
    shutil.copy2(sourcefolder + "teamX-cp.md", destination + "teamX-cp.md")

