# CIMAS_Constructions_Patologies_1
# Sistema de Detecção de Ausência de Vegetação em Barragens

Este projeto visa automatizar a detecção de áreas críticas de ausência de vegetação em barragens, um indicador importante de risco estrutural. Utilizando visão computacional e o modelo YOLO (You Only Look Once), o sistema permite analisar imagens de barragens, identificando automaticamente as áreas que necessitam de intervenção.

Objetivo
Desenvolver uma solução automatizada, rápida e confiável para a detecção da ausência de vegetação, reduzindo a dependência de inspeções manuais demoradas e suscetíveis a erros, garantindo maior segurança em barragens.

Tecnologias Utilizadas
Python: Linguagem principal do projeto.
YOLO (Ultralytics): Modelo de detecção de objetos utilizado para identificar as áreas críticas de ausência de vegetação.
Flask: Framework para o desenvolvimento do back-end e da interface do usuário.
MakeSense: Ferramenta para a rotulagem das imagens durante o treinamento do modelo.
GitHub: Controle de versão e colaboração entre as equipes.
Funcionalidades
Envio de Imagens: O sistema permite o envio de imagens de barragens para análise.
Identificação Automática: As áreas sem vegetação são destacadas automaticamente, indicando pontos críticos.
Interface Intuitiva: Desenvolvemos um front-end simples e acessível, permitindo que o sistema seja utilizado por não especialistas.
Desafios Enfrentados
Durante o desenvolvimento do projeto, enfrentamos diversos desafios, incluindo:

Classificação de Imagens em Diagonal: Ajustes no treinamento foram necessários para melhorar a precisão do modelo.
Hardware Limitado: O treinamento do modelo foi mais demorado devido à falta de equipamentos de alto desempenho, mas conseguimos otimizar os recursos disponíveis.
Mudanças de Requisitos: O cliente solicitou mudanças ao longo do desenvolvimento, o que exigiu adaptação e flexibilidade da equipe.
Metodologia
Scrum: Utilizamos a metodologia ágil para organizar as tarefas e priorizar as entregas.
Trabalho em Equipe: A colaboração entre dois grupos com o mesmo projeto foi essencial para a rotulagem de centenas de imagens e para lidar com as mudanças de requisitos do cliente.
Resultados Esperados
Precisão: A detecção de áreas sem vegetação com alta acurácia, utilizando aprendizado profundo com o YOLO.
Eficiência: Redução no tempo e custo das análises manuais.
Acessibilidade: Interface simples e intuitiva para facilitar o uso por não especialistas.
Conclusão
O sistema desenvolvido oferece uma solução eficaz e prática para um problema crítico de segurança em barragens, integrando tecnologias de visão computacional com uma aplicação prática em infraestrutura. Além disso, o projeto proporcionou aprendizado técnico em machine learning, engenharia de software e metodologias ágeis, além de fortalecer habilidades interpessoais como comunicação, trabalho em equipe e adaptação a mudanças.

Perspectivas Futuras
O sistema pode ser expandido para detectar outros tipos de falhas em barragens ou outras estruturas, ampliando seu impacto na segurança e otimização de recursos.
