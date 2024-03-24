#!/bin/bash

echo ""
echo "### Build Libwbmxl"
mockcfg=epel-7-x86_64 make-rpms libwbxml.spec
echo ""
echo "### Build Sope"
mockcfg=epel-7-x86_64 make-rpms sope.spec
echo ""
echo "### Build Ytnef"
dist=ns7 mockcfg=epel-7-x86_64 make-rpms ytnef.spec
echo ""
echo "### Create local repository"
createrepo .
echo ""
echo "### Build SOGo"
mockcfg=epel-7-x86_64 make-rpms sogo.spec
rm -rf libwbxml*.rpm *devel*.rpm
