def calculate_confidence(source_docs):
    confidence = min(1.0, 0.5 + 0.1 * len(source_docs))
    return round(confidence, 2)
