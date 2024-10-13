# Projeto Damas - Visão

Este repositório contém o código referente à parte de visão do projeto Damas, desenvolvido pela equipe 4. O objetivo principal é implementar a detecção de peças no tabuleiro e integrar essa funcionalidade à lógica do jogo.

A classe `CapStructured`, localizada em `visao/cap_structured.py`, é responsável pela detecção das peças no tabuleiro, retornando a classificação e a posição delas. A classe utiliza um modelo pré-treinado, armazenado em `visao/meus_resultados/experimento12/weights/best.pt`, e uma instância da classe `ImageCapture` para capturar e processar as imagens. O modelo foi treinado utilizando YOLOv8n com 10 epochs e uma resolução de 640x640.

Além disso, o projeto inclui scripts para movimentação, remoção e promoção de peças, que podem ser utilizados em um robô real ou em um robô de testes. O menu de controle, localizado em `robot/main.py`, permite a seleção do robô e as ações a serem realizadas, exibindo uma representação do tabuleiro e instruções sobre como enviar coordenadas para manipulação.
