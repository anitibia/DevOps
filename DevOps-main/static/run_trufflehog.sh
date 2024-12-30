#!/bin/bash
trufflehog filesystem --directory ./ > ./trufflehog_report.txt
if grep -q "Secrets Found" trufflehog_report.txt; then
    echo "TruffleHog обнаружил секреты в коде!"
    cat ./trufflehog_report.txt
    exit 1
fi
echo "No critical issues found."
exit 0
