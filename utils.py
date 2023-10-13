from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import config as cfg


def get_publications_urls(docs, n_urls) -> str:
    title_urls = {docs.metadata["title"]: docs.metadata["url"] for docs in docs}
    title_urls = dict(list(title_urls.items())[0:n_urls])
    urls = "\n".join([f"- [{title}]({url})" for title, url in title_urls.items()])
    urls = f"Here are some of the publications I used to answer your question:\n {urls}"
    return urls


def get_response_from_query(db, query, model=cfg.MODEL, n_dosc=cfg.N_DOSC, n_urls=cfg.N_URLS) -> str:
    docs = db.similarity_search(query, k=n_dosc)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = ChatOpenAI(model=model)

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        You are a scientist who studies the work of Eliezer Yudkowsky and knows all his publications by heart.
        
        Answer the following question: {question}
        By searching the following Eliezer Yudkowsky publications: {docs}
        
        Only use the factual information from the transcript to answer the question.
        You can use your own information about Eliezer Yudkowsky and the topic, but don't make up any new information.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be of medium or short length, but meaningful.
        """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(question=query, docs=docs_page_content)

    if n_urls > 0:
        urls = get_publications_urls(docs, n_urls=n_urls)
        response = response + "\n\n" + urls
    return response
