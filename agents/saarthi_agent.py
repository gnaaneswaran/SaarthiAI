def handle_query(query):
    # Simple rules-based response before LLM integration
    if "scheme" in query.lower():
        return "You may be eligible for PM-KISAN or state-specific subsidy schemes."
    elif "hospital" in query.lower():
        return "The nearest government hospital is 5 km away."
    else:
        return "I'm still learning. Please ask something else!"
