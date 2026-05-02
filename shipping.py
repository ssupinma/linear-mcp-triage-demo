def estimate_shipping_days(method: str) -> str:
    """Return the estimated shipping time for a checkout order."""
    normalized_method = method.strip().lower()

    if normalized_method == "standard":
        return "3-5 business days"

    if normalized_method == "express":
        return "1-2 business days"

    return "shipping estimate unavailable"


if __name__ == "__main__":
    print("Standard:", estimate_shipping_days("standard"))
    print("Express:", estimate_shipping_days("express"))
