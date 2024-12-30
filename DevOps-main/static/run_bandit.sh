#!/bin/bash
bandit -r ./project_directory -ll -f txt -o bandit_report.txt

if grep -q 'CRITICAL' bandit_report.txt; then
    echo "Critical issues found in the code!"
    exit 1
fi
echo "No critical issues found."
exit 0



