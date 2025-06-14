import streamlit as st
from utils.agent import Cardiologist,Psychologist,Pulmonologist,MultidisciplinaryTeam
from concurrent.futures import ThreadPoolExecutor,as_completed

st.title('Analyse your report :- ')
st.header('Upload your report.....')


medical_report = st.file_uploader("upload file here",type=['.txt','.pdf'])

agents={
    'Cardiologist':Cardiologist(medical_report),
    'Psychologist':Psychologist(medical_report),
    'Pulmonologist':Pulmonologist(medical_report)

}

def get_response(agent_name,agent):
    response = agent.run()
    return agent_name,response

responses={}

with ThreadPoolExecutor() as executor:
    futures = {executor.submit(get_response,name,agent): name for name,agent in agents.items()}

    for future in as_completed(futures):
        agent_name,response = future.result()
        responses[agent_name]=response


team_agents = MultidisciplinaryTeam(
    cardiologist_report=responses['Cardiologist'],
    psychologist_report=responses["Psychologist"],
    pulmonologist_report=responses['Pulmonologist']
)


if medical_report:

    final_diagnosis = team_agents.run()

    st.markdown(final_diagnosis)
