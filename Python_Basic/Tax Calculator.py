# 👇🏻 Write your code here 👇🏻:
def get_yearly_revenue(monthly_revenue: int) -> int:
    """
    연간 매출 계산 수식
    월간매출 * 12개월
    Args:
        monthly_revenue (int): 월간매출
    Returns:
        int: yearly_revenue, : 연간매출
    """
    return monthly_revenue * 12


def get_yearly_expenses(monthly_expenses: int) -> int:
    """
    연간 비용 계산 수식
    월간비용 * 12개월
    Args:
        monthly_expenses (int): 월간비용
    Returns:
        int: yearly_expenses : 연간비용
    """
    return monthly_expenses * 12


def get_tax_amount(profit: int) -> float:
    """
    세금 계산 수식
    $100,000 초과시 세율 25%, 이하 15%
    Args:
        profit (int): 이익

    Returns:
        float: 세금 계산
    """
    if profit > 100000:
        return profit * 0.25
    else:
        return profit * 0.15


def apply_tax_credits(tax_amount: float, tax_credits: float) -> float:
    """
    세금 공제액 수식
    세금 * 세금 공제율
    Args:
        tax_amount (float): 세금
        tax_credits (float): 세금 공제율

    Returns:
        float: 세금 공재액
    """
    return tax_amount * tax_credits


# ❌ Don't touch anthing below this line ❌

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

profit = yearly_revenue - yearly_expenses

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")
