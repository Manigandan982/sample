#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands


def get_paths(dirname):
  """Given a dirname, returns a list of all its special files."""
  output = []
  current_path = os.listdir(dirname) 
  for fname in current_path:
    match = re.search(r'__(\w+)__', fname)
    if match:
      output.append(os.path.abspath(os.path.join(dirname, fname)))
  return output


def copy_to(current_path, to_dir):
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in current_path:
    fname = os.path.basename(path)
    shutil.copy(path, os.path.join(to_dir, fname))
    # could error out if already exists os.path.exists():


def zip_to(current_path, zipfile):
  """Zip up all of the given files into a new zip file with the given name."""
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(current_path)
  print "Command I'm going to do:" + cmd
  (status, output) = commands.getstatusoutput(cmd)
  # If command had a problem (status is non-zero),
  # print its output to stderr and exit.
  if status:
    sys.stderr.write(output)
    sys.exit(1)

# LAB(end solution)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  # LAB(begin solution)

  # Gather all the special files
  current_paths = []
  for dirname in args:
    current_paths.extend(get_paths(dirname))

  if todir:
    copy_to(current_paths, todir)
  elif tozip:
    zip_to(current_paths, tozip)
  else:
    print '\n'.join(current_paths)
  # LAB(end solution)

if __name__ == "__main__":
  main()
