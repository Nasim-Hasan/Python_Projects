"""
Build a dictionary of countries mapped to their capitals.

Steps:
1) Define a list of countries.
2) Define a list of corresponding capitals (same order as countries).
3) Create a dictionary mapping using a helper function.
4) Optionally, print the results in a readable way.
"""

from typing import List, Dict


def build_country_capital_dict(countries: List[str], capitals: List[str]) -> Dict[str, str]:
    """
    Build a mapping of country -> capital.

    Args:
        countries: A list of country names.
        capitals: A list of capital names (must align by index with `countries`).

    Returns:
        A dictionary where keys are country names and values are capital names.

    Raises:
        ValueError: If the input lists have different lengths.
    """
    # ✅ Step 3a: Validate that the lists align by length
    if len(countries) != len(capitals):
        raise ValueError(
            f"List length mismatch: countries={len(countries)} vs capitals={len(capitals)}"
        )

    # ✅ Step 3b: Build the dictionary (country -> capital) using zip
    country_to_capital: Dict[str, str] = {country: capital for country, capital in zip(countries, capitals)}
    return country_to_capital


def print_country_capital_pairs(country_to_capital: Dict[str, str]) -> None:
    """
    Pretty-print the country-capital pairs in alphabetical order of countries.
    """
    # ✅ Optional: present the result nicely for human reading
    for country in sorted(country_to_capital.keys()):
        print(f"{country}: {country_to_capital[country]}")


def main() -> None:
    # ✅ Step 1: Generate a list of countries
    countries: List[str] = [
        "Bangladesh", "India", "Pakistan", "Nepal", "Bhutan",
        "Maldives", "China", "Japan", "South Korea", "Indonesia",
        "Malaysia", "Singapore", "Thailand", "Vietnam", "Philippines",
        "Sri Lanka", "United States", "United Kingdom", "France", "Germany",
        "Italy", "Spain", "Canada", "Australia", "New Zealand"
    ]

    # ✅ Step 2: Generate their corresponding capitals (same order as `countries`)
    capitals: List[str] = [
        "Dhaka", "New Delhi", "Islamabad", "Kathmandu", "Thimphu",
        "Malé", "Beijing", "Tokyo", "Seoul", "Jakarta",
        "Kuala Lumpur", "Singapore", "Bangkok", "Hanoi", "Manila",
        "Sri Jayawardenepura Kotte", "Washington, D.C.", "London", "Paris", "Berlin",
        "Rome", "Madrid", "Ottawa", "Canberra", "Wellington"
    ]

    # ✅ Step 3: Arrange countries with their capitals in a dictionary
    country_to_capital: Dict[str, str] = build_country_capital_dict(countries, capitals)

    # ✅ Step 4 (Optional): Print the mapping
    print_country_capital_pairs(country_to_capital)


if __name__ == "__main__":
    # ✅ Program entry point
    main()