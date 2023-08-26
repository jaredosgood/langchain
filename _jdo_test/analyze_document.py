from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.chains import AnalyzeDocumentChain


llm = OpenAI(temperature=0)
summary_chain = load_summarize_chain(llm, chain_type="map_reduce")

with open(
    r"C:\Users\JaredOsgood\OneDrive - QuantumData\GitHub\langchain\_jdo_test\on_war_excerpt.txt",
    encoding='utf-8') as f:
    on_war_ex = f.read()

summarize_document_chain = AnalyzeDocumentChain(combine_docs_chain=summary_chain)

summary = summarize_document_chain.run(on_war_ex)

print(summary)

# OUTPUT:
# This chapter examines the concept of military genius, exploring the qualities and
# characteristics that make a great military leader, such as strategy, tactics, and
# the ability to inspire and motivate troops. It also discusses the two kinds of courage
# needed for war, physical strength, common sense, and the role of luck and
# chance in military success.
