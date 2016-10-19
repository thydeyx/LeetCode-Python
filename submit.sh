#!/bin/sh

path=`pwd`
log=$1

git add $path
git commit -m $log
git push
