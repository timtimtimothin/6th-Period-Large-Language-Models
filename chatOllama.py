from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

Model = ChatOllama(model="Interpreter")
Interpreter_Prompt = ChatPromptTemplate.from_template("You are an Artificial Intelligence solely used for interpretation. Read the provided {feasible} and decide if the prompt is feasible or not. If it is, say 'feasible'; if not satIn 'not feasible'.")
Neanderthal_Prompt = ChatPromptTemplate.from_template("You are an Artificial Intelligence that is acting like a neanderthal. When responding to prompts, maintain a certain form outlined in your system message.")
Parser = StrOutputParser()

Interpreter_Chain = Interpreter_Prompt | Model | Parser
Neanderthal_Chain = Neanderthal_Prompt | Model | Parser
user_Text = input("What would you like to ask the neanderthal?")

feasibility = Interpreter_Chain.invoke({"feasible":f"Decide if {user_Text} is feasible."})
if "not feasible" in feasibility:
    print("The data is not feasible!")
    print("Your data was identified not feasible because:")
    print(feasibility)
elif "feasible" in feasibility:
    response = Neanderthal_Chain.invoke({})
    print(response)
else:
    print("An error has occurred.")