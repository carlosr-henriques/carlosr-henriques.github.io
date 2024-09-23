import streamlit as st

st.set_page_config(page_title="Carlos Roberto - Portifólio", page_icon="📊")

st.markdown("<h1 style='text-align: center; color: white;'>Carlos Roberto Henriques Machado Ozorio</h1>", unsafe_allow_html=True)
container = st.container(border=True)
container.page_link("main.py", label="Home", icon="🏠", use_container_width=False)
container.page_link("pages/presentation.py", label="Apresentação", icon="🎤", use_container_width=False)
container.page_link("pages/about-me.py", label="Sobre mim", icon="😊", use_container_width=False)
container.page_link("pages/projects.py", label="Projetos", icon="🛠️", use_container_width=False)
container.page_link("pages/contact.py", label="Contato", icon="✉️", use_container_width=False)

st.markdown("<p style='text-align: center; color: white;'>Analista de dados</p>", unsafe_allow_html=True)


'''
    [![Repo](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/carlos-roberto1/)
    [![Repo](https://img.shields.io/badge/Github-0A66C2?style=flat&logo=github&logoColor=white&color=black)](https://github.com/AvratanuBiswas/PubLit)
    [![Repo](https://img.shields.io/badge/Medium-0A66C2?style=flat&logo=medium&logoColor=white&color=black)](https://medium.com/@carl0sr_)
    [![Repo](https://img.shields.io/badge/Curriculo-4285F4?style=for-the-badge&logo=word&logoColor=white)](https://docs.google.com/document/d/14nifkIZ-PZ5uUEIVZ1qwJuKKdSsX9FLkxVA7N8imA1k/edit?usp=sharing)

'''

st.markdown("<p style='text-align: center; color: white;'>Python | SQL | NoSQL | GCP | Looker Studio | Estatística | Excel | Jamovi | Metabase | Power BI</p>", unsafe_allow_html=True)

