from .pricing import MODEL_PRICING

def calculate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    if model not in MODEL_PRICING: raise ValueError(f"Unknown model: '{model}'")
    pricing = MODEL_PRICING[model]
    return round((input_tokens * pricing["input"]) + (output_tokens * pricing["output"]), 8)