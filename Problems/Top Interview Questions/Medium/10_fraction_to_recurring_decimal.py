# https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        def get_gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        # Simple cases
        if numerator == 0:
            return '0'
        if numerator % denominator == 0:
            return str(numerator // denominator)
        # Determine sign of the result
        neg_result = numerator < 0 < denominator or numerator > 0 > denominator
        # Work with positive numbers
        numerator, denominator = abs(numerator), abs(denominator)
        # Simplify fraction
        gcd = get_gcd(numerator, denominator)
        numerator, denominator = numerator // gcd, denominator // gcd
        # Calculate whole part and fractional part
        whole, mod = divmod(numerator, denominator)
        fraction_digits = list()
        recurring_start = -1
        mod *= 10
        prior_mod_to_digit_nr = {mod: 0}
        i = 1
        while mod != 0:
            div, mod = divmod(mod, denominator)
            fraction_digits.append(str(div))
            mod *= 10
            if mod in prior_mod_to_digit_nr:
                recurring_start = prior_mod_to_digit_nr[mod]
                break
            else:
                prior_mod_to_digit_nr[mod] = i
                i += 1
        # Construct answer
        sign = '-' if neg_result else ''
        if recurring_start >= 0:
            fraction_start = ''.join(fraction_digits[:recurring_start])
            fraction_end = f"({''.join(fraction_digits[recurring_start:])})"
            fraction = f'{fraction_start}{fraction_end}'
        else:
            fraction = ''.join(fraction_digits)
        return f'{sign}{whole}.{fraction}'
