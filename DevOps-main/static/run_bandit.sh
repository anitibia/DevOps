#!/bin/bash
bandit -r . --severity-level high --exit-zero > ./bandit_report.txt
if grep -q "HIGH" bandit_report.txt; then
    echo "Bandit обнаружил уязвимости высокой критичности!"
    cat ./bandit_report.txt
    exit 1
fi
