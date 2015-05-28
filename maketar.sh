#!/bin/bash

thisdir=`dirname $0`
outfile="pytour.tar.gz"
tar --exclude="pytour*.tar.gz" --exclude=".hg" --exclude=".git" --exclude="*.pyc" --exclude="._*" -czf "/tmp/$outfile" "$thisdir"
mv "/tmp/$outfile" "$thisdir"
