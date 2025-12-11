from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

Model = ChatOllama(model="Interpreter")
Interpreter_Prompt = ChatPromptTemplate.from_template("You are an Artificial Intelligence solely used for interpretation. Read the provided {feasible} and decide if the prompt is feasible or not. If it is, say 'feasible'; if not satIn 'not feasible'.")
Neanderthal_Prompt = ChatPromptTemplate.from_template("You are an Artificial Intelligence that is acting like a neanderthal. When responding to {user_Text}, maintain a certain form outlined in your system message.")
Parser = StrOutputParser()

Interpreter_Chain = Interpreter_Prompt | Model | Parser
Neanderthal_Chain = Neanderthal_Prompt | Model | Parser
simulation_running = True
while simulation_running == True:
    user_Text = input("What would you like to ask the neanderthal?")
    feasibility = Interpreter_Chain.invoke({"feasible":f"Decide if {user_Text} is feasible."})
    print(feasibility)
    if "not feasible" in feasibility:
        print("The data is not feasible!")
        print("Your data was identified not feasible because:")
        print(feasibility)
        Attempt = input("Would you like to enter a different prompt?")
        if Attempt.lower().strip() == "no" or Attempt.lower().strip() == "no thank you" or Attempt.lower().strip() == "nope" or Attempt.lower().strip() == "i'm good" or Attempt.lower().strip() == "im good":
            print(":(")
            simulation_running = False
        else:
            print(":D")
    if "feasible" in feasibility:
        response = Neanderthal_Chain.invoke({"user_Text":f"Generate a response to {user_Text}."})
        print(response)
    else:
        print("An error has occurred.")