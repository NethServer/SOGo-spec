#!/bin/bash
set -e 
echo ""
echo "### Build Libwbmxl"
mockcfg=nethserver-7-x86_64 make-rpms libwbxml.spec
echo ""
echo "### Build Sope"
mockcfg=nethserver-7-x86_64 make-rpms sope.spec
echo ""
echo "### Build Ytnef"
dist=ns7 mockcfg=nethserver-7-x86_64 make-rpms ytnef.spec
echo ""
echo "### Create local repository"
createrepo . --compatibility=rhel7
echo ""
echo "### Build SOGo"
mockcfg=nethserver-7-x86_64 make-rpms sogo.spec
rm -rf libwbxml*.rpm *devel*.rpm
