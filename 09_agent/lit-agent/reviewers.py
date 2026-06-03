import argparse
import json
from openai import OpenAI
from pubmed_search import search_pubmed
from pubmed_search import fetch_abstracts
from itertools import product

#openai client setup
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

#plan search parameters for pubmed 

def plan_search_strategy(topic: str):

    system_prompt = """
    You are an expert scientific librarian.

    Expand the user's research topic into:

    - core concepts
    - synonyms
    - related concepts
    - methods
    - organisms
    - technologies

    Return ONLY valid JSON.

    Example:

    {
      "core_concepts": [],
      "synonyms": [],
      "related_concepts": [],
      "methods": [],
      "organisms": [],
      "technologies": []
    }
    """

    response = client.chat.completions.create(
        model="qwen3:8b",
        max_tokens=1000,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": topic
            }
        ]
    )

    #print('Raw response from the model: ', response.choices[0].message.content)

    return json.loads(response.choices[0].message.content)

    #return json.loads(response.choices[0].message.content)

#mix and re-mix the search parameters to generate a variety of queries for pubmed
def generate_pubmed_queries(strategy, main_terms=None):

    queries = []

    core = strategy["core_concepts"]
    synonyms = strategy["synonyms"]
    concepts = strategy["related_concepts"]
    methods = strategy["methods"]
    organisms = strategy["organisms"]
    technologies = strategy["technologies"]

    all_main_terms = core + synonyms
    if main_terms:
        all_main_terms = main_terms 

    for a, b in product(all_main_terms, concepts):
        queries.append(f'"{a}" AND "{b}"')

    for a, b in product(all_main_terms, methods):
        queries.append(f'"{a}" AND "{b}"')

    for a, b in product(all_main_terms, organisms):
        queries.append(f'"{a}" AND "{b}"')

    for a, b in product(all_main_terms, technologies):
        queries.append(f'"{a}" AND "{b}"')

    return list(set(queries))



#define the prompt loader for the agent
def load_prompt(name):
    with open(f"prompts/{name}.txt", "r") as f:
        return f.read()


def run_agent(prompt, text, max_tokens=10000):

    response = client.chat.completions.create(
        model="qwen3:8b",
        max_tokens=max_tokens,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content


def review_papers( question, abstracts):

    #extract relevant info
    extracted_info = run_agent(load_prompt("extractor"), 
                               f"Abstracts:\n{abstracts}")

    #skeptical review of the extracted info
    skeptical_review = run_agent(load_prompt("skeptic"), 
                                 f"Extracted Information:\n{extracted_info}")

    #bioinformatics review of the extracted info
    bfx_review = run_agent(load_prompt("bioinformatics"), 
                           f"Extracted Information:\n{extracted_info}")

    #translational review of the extracted info
    translational_review = run_agent(load_prompt("translational"), 
                                     f"Extracted Information:\n{extracted_info}")

    #final synthesis of the reviews
    final_review = run_agent(load_prompt("synthesizer"), 
                             f"Question: {question}\n\nExtracted Information:\n{extracted_info}\n\nSkeptical Review:\n{skeptical_review}\n\nBioinformatics Review:\n{bfx_review}\n\nTranslational Review:\n{translational_review}",
                             max_tokens=25000)

    return final_review



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Review papers from PubMed")
    parser.add_argument("-q", "--question", required=True,
                        help="Specific search question for PubMed")
    parser.add_argument("-o", "--output", default="final_review.txt",
                        help="Path to the output file for the review")
    parser.add_argument("-m", "--mainterms",
                        help="The main term to focus the search on, len of 1")
    args = parser.parse_args()
    
    question = args.question
    filename = args.output
    terms = args.mainterms.split(",") if args.mainterms else None
    
    #plan the search strategy
    strategy = plan_search_strategy(question)
    #print('Planned Search Strategy: ', strategy)

    #generate a variety of queries for pubmed
    queries = generate_pubmed_queries(strategy, main_terms=terms)
    #print('Generated PubMed Queries: ', queries)


    #print(f"Searching PubMed for: {question}")
    ids = []
    for query in queries:
        print(f"Searching PubMed for: {query}")
        ids.extend(search_pubmed(query, n=5))


    ids = set(ids)  # Remove duplicates
    print('Here are the relevant pubmed IDs: ', ids)
    abstracts = fetch_abstracts(ids)
    
    final_review = review_papers(question, abstracts)
    #print("Final Review:\n", final_review)
    with open(f'{filename}.md', "w") as f:
        f.write(f"output/{final_review}")
