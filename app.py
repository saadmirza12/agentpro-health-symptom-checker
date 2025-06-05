import gradio as gr
from agentpro.model import OpenAIClient
from agentpro import ReactAgent

def analyze_symptoms(symptoms, api_key):
    try:
        model = OpenAIClient(api_key=api_key, model_name="gpt-3.5-turbo", temperature=0.2)
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

        symptom_checker_response = symptom_checker_agent.run(symptoms).final_answer
        advice_response = advice_agent.run(symptom_checker_response).final_answer

        return f"[Symptom Checker]: {symptom_checker_response}\n\n[Advice Agent]: {advice_response}"
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("# 🩺 AgentPro Health Symptom Checker\nPaste your OpenAI API key below. (It is NOT stored or shared.)")
    with gr.Row():
        symptoms = gr.Textbox(label="Enter your symptoms", placeholder="e.g. fever and headache")
        api_key = gr.Textbox(label="OpenAI API Key", type="password", placeholder="sk-...")
    output = gr.Textbox(label="Analysis and Advice", lines=8)
    submit = gr.Button("Analyze Symptoms")
    submit.click(analyze_symptoms, inputs=[symptoms, api_key], outputs=output)

demo.launch()
