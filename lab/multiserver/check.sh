#!/bin/sh
printf 'CHECK role=%s\n' "$STUDY_ROLE"
cat status.txt
tail -n 2 service.log
