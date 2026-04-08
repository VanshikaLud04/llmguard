from llmguard.cost import calculate_cost
from llmguard.burn import calculate_burn_rate

def test_basic_cost():
    cost = calculate_cost("gpt-4o-mini", 1000, 500)
    assert cost == round(1000 * 0.00000015 + 500 * 0.0000006, 8)
    print(f"✅ test_basic_cost: ${cost}")

def test_unknown_model():
    try:
        calculate_cost("gpt-99-ultra", 100, 100)
        assert False
    except ValueError as e:
        print(f"✅ test_unknown_model: raised ValueError")

def test_burn_rate():
    rate = calculate_burn_rate([(0.003, 1000), (0.002, 1001), (0.004, 1002)])
    assert rate == 0.009
    print(f"✅ test_burn_rate: ${rate}")

if __name__ == "__main__":
    test_basic_cost()
    test_unknown_model()
    test_burn_rate()
    print("✅ All tests passed.")