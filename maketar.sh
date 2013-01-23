#!/bin/bash

thisdir=`dirname $0`
thisversion=`sed -e 's/^VERSION: //p' -e 'd' "$thisdir/CHANGES"`
outfile="pytour-$thisversion.tar.gz"
tar --exclude=".hg" --exclude="*.pyc" --exclude="._*" -czf "/tmp/$outfile" "$thisdir"
mv "/tmp/$outfile" "$thisdir"
