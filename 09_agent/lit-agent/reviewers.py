import argparse
from openai import OpenAI
from pubmed_search import search_pubmed
from pubmed_search import fetch_abstracts

#openai client setup
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
#print('Here are the relevant abstracts: ', abstracts)

#define the prompt loader for the agent
def load_prompt(name):
    with open(f"prompts/{name}.txt", "r") as f:
        return f.read()


def run_agent(prompt, text, max_tokens=500):

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
                             f"Question: {question}\n\nExtracted Information:\n{extracted_info}\n\nSkeptical Review:\n{skeptical_review}\n\nBioinformatics Review:\n{bfx_review}\n\nTranslational Review:\n{translational_review}")

    return final_review

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Review papers from PubMed")
    parser.add_argument("-q", "--question", required=True, 
                        help="Specific search question for PubMed")
    args = parser.parse_args()
    
    question = args.question
    print(f"Searching PubMed for: {question}")
    ids = search_pubmed(question, n=5)
    print('Here are the relevant pubmed IDs: ', ids)
    abstracts = fetch_abstracts(ids)
    
    final_review = review_papers(question, abstracts)
    print("Final Review:\n", final_review)