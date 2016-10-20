#!/bin/sh

path=`pwd`
log=$1

git add --ignore-removal $path
git commit -m $log
git push
