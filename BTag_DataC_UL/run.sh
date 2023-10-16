#!/bin/bash

cluster=$1
process=$2

# CMSSW setup etc
export SCRAM_ARCH="slc7_amd64_gcc820"
export VO_CMS_SW_DIR="/cms/base/cmssoft"
export COIN_FULL_INDIRECT_RENDERING=1
export HOME=/home/akobert/

source $VO_CMS_SW_DIR/cmsset_default.sh

cd /home/akobert/CMSSW_10_6_29_patch1/src/BTag_DataC_UL

eval `scramv1 runtime -sh`

cmsRun nano$2.py >& /home/akobert/CMSSW_10_6_29_patch1/src/CondorFiles/logfiles_BTag_DataC_UL_$1_$2.log
