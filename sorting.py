def sort_queries(queries):
    relevance_scores = []

    # Define relevant keywords or phrases
    relevant_keywords = ['python', 'programming', 'sorting', 'query', 'example']

    # Calculate relevance scores for each query
    for query in queries:
        score = sum(keyword in query.lower() for keyword in relevant_keywords)
        relevance_scores.append((query, score))

    # Sort queries based on relevance scores in descending order
    sorted_queries = sorted(relevance_scores, key=lambda x: x[1], reverse=True)

    return sorted_queries

if __name__ == "__main__":
    # Example usage
    input_queries = [
        'Python sorting algorithm example',
        'Introduction to programming in Python',
        'Query optimization techniques',
        'Relevant query example'
    ]

    sorted_results = sort_queries(input_queries)

    print("Sorted Queries:")
    for query, score in sorted_results:
        print(f"{query}: Relevance Score = {score}")
