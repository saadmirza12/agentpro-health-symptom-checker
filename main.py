from agentpro.model import OpenAIClient

import getpass
openai_api_key = getpass.getpass("Enter your OpenAI API key: ")


model = OpenAIClient(
    api_key=openai_api_key,
    model_name="gpt-3.5-turbo",
    temperature=0.2
)

from agentpro import ReactAgent

user_agent = ReactAgent(model=model, custom_system_prompt="You are the user agent. Pass the user's symptoms to the Symptom Checker.")
symptom_checker_agent = ReactAgent(
    model=model,
    custom_system_prompt=(
        "You are a medical assistant. Analyze symptoms and provide likely causes. "
        "If the input does not contain any symptoms or is not health-related, immediately reply with "
        "\"Final Answer: Sorry, I can only help with medical symptom analysis.\""
        " Always end with 'Final Answer: ...'"
    )
)
advice_agent = ReactAgent(
    model=model,
    custom_system_prompt="You are a health advisor. Give advice based on the symptom analysis. Always end with 'Final Answer: ...'"
)
user_input = input("Enter your symptoms: ")

# Pass input to Symptom Checker
symptom_checker_response_obj = symptom_checker_agent.run(user_input)
symptom_checker_response = symptom_checker_response_obj.final_answer
print("[Symptom Checker]:", symptom_checker_response)

# Pass to Advice Agent
advice_response_obj = advice_agent.run(symptom_checker_response)
advice_response = advice_response_obj.final_answer
print("[Advice Agent]:", advice_response)
