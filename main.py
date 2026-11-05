
import csv

# CREDIT RISK ANALYZER
# Proyecto educativo con datos ficticios.

applicants = [
    {
        "id": "C001",
        "income": 3000,
        "debt": 500,
        "late_payments": 0
    },
    {
        "id": "C002",
        "income": 1800,
        "debt": 1100,
        "late_payments": 4
    },
    {
        "id": "C003",
        "income": 4500,
        "debt": 700,
        "late_payments": 1
    },
    {
        "id": "C004",
        "income": 2200,
        "debt": 1300,
        "late_payments": 3
    },
    {
        "id": "C005",
        "income": 6000,
        "debt": 800,
        "late_payments": 0
    }
]


def analyze_applicant(person):

    income = person["income"]
    debt = person["debt"]
    late = person["late_payments"]

    debt_ratio = debt / income if income > 0 else 1

    score = 0

    if debt_ratio > 0.40:
        score += 2
    elif debt_ratio > 0.25:
        score += 1

    if late >= 3:
        score += 2
    elif late >= 1:
        score += 1

    if score >= 4:
        risk = "HIGH"
    elif score >= 2:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return debt_ratio, score, risk


def main():

    print("=" * 45)
    print("       CREDIT RISK ANALYZER")
    print("=" * 45)

    for person in applicants:

        ratio, score, risk = analyze_applicant(person)

        print(f"\nApplicant: {person['id']}")
        print(f"Debt ratio: {ratio:.2%}")
        print(f"Risk score: {score}")
        print(f"Risk level: {risk}")

    print("\nAnalysis completed.")


if __name__ == "__main__":
    main()
