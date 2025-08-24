# LIA---Processo-seletivo
RAG - processo seletivo LIA
Projeto desenvolvido para a segunda fase do processo seletivo do LIA, foi pedido o desenvolvimento de uma RAG que dado um excerto de uma ementa, verifique se exista alguma súmula em consonância com a ementa. 
Para isso foi pensado as seguintes etapas: inicialmente utilizar uma ferramenta para fazer o scrapping do site do STJ (Supremo Tribunal de Justiça) para pegar as 676 súmulas, após isso foi utilizado a técnica de Processamento de Linguagem Natural: embedding para as as súmulas capturadas, por fim, utilizamos um RAG (Retrieval-augmented generation) para avaliar se existia conexão entre o excerto da ementa com alguma súmula.

é necessario a instalação das seguintes bibliotecas python:
pip install playwright
pip install langchain
pip install langchain-nvidia-ai-endpoints
pip install numpy

além de 2 API KEYS:
uma da NVIDIA disponivel em: https://build.nvidia.com/
uma do framework LangChain disponivel em: https://smith.langchain.com/

Vídeo da explicação do código:
falta adicionar
