from reviewers import plan_search_strategy
from reviewers import generate_pubmed_queries
strategy = plan_search_strategy("antimicrobial resistance in E. coli")

queries = generate_pubmed_queries(strategy)
print(len(queries))