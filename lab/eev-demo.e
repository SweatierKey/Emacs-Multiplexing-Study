 (eepitch-shell)
lab-ssh lab-web
cat status.txt; tail -n 3 service.log
export STUDY_KEEP=web-session-alive
 (eepitch-shell2)
lab-ssh lab-db
cat status.txt; tail -n 3 service.log
 (eepitch-shell)
printenv STUDY_KEEP
