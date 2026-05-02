def estimate_shipping_days(method: str) -> str:
    """Return the estimated shipping time for a checkout order."""
    return "0 days"


if __name__ == "__main__":
    print("Standard:", estimate_shipping_days("standard"))
    print("Express:", estimate_shipping_days("express"))
