from decimal import Decimal, getcontext

getcontext().prec = 10


def calculate_monthly_payment(
    amount: Decimal, annual_rate: Decimal, term_months: int
) -> Decimal:
    """
    Standard loan amortization formula:
    M = P * r * (1+r)^n / ((1+r)^n - 1)
    r = monthly interest rate (decimal)
    """
    if term_months <= 0:
        raise ValueError("Term must be > 0")

    if annual_rate <= 0:
        return amount / term_months

    monthly_rate = annual_rate / Decimal("12") / Decimal("100")
    numerator = amount * monthly_rate * (1 + monthly_rate) ** term_months
    denominator = (1 + monthly_rate) ** term_months - 1
    return numerator / denominator
