# Construção de um diretório

## Motivação

Adotar uma estrutura de diretórios padronizada para cada projeto pode trazer muitos benefícios, especialmente em ambientes onde várias pessoas estão trabalhando em projetos simultaneamente ou em projetos que serão mantidos e atualizados ao longo do tempo. Aqui estão alguns dos principais benefícios:

1. **Consistência:** Quando todos os projetos seguem a mesma estrutura de diretórios, novos membros da equipe podem rapidamente entender onde encontrar os arquivos necessários e como os dados e scripts estão organizados. Isso reduz a curva de aprendizado e facilita a integração de novos colaboradores.
2. **Colaboração eficiente:** Uma estrutura padronizada evita confusões e erros que podem surgir quando diferentes pessoas organizam arquivos de maneiras distintas. Isso torna mais fácil para todos na equipe colaborar, compartilhar arquivos e manter o trabalho alinhado.
3. **Manutenção e atualizações:** Projetos com uma estrutura organizada e bem documentada são mais fáceis de serem mantidos e atualizados. Isso é especialmente importante em projetos de longo prazo ou que são passados entre diferentes equipes ou gerações de analistas.
Escalabilidade: Conforme o projeto cresce, uma estrutura bem definida facilita a adição de novos dados, scripts e funcionalidades sem perturbar a organização existente. Isso pode ajudar a evitar problemas de desempenho ou complexidade que poderiam dificultar a escalabilidade do projeto.
4. **Automatização:** Uma estrutura padronizada facilita a implementação de scripts de automação para tarefas comuns, como backups, testes e deploy de modelos. A automação pode ser configurada uma vez e reutilizada em vários projetos com estruturas similares.
5. **Compliance e segurança:** Manter uma estrutura organizada e consistente ajuda a garantir que todos os aspectos de segurança e compliance (como a gestão de dados sensíveis) sejam tratados de forma uniforme em todos os projetos.

## Padronização

Será adotado um esquema de nomenclatura padronizado para os diretórios dos projetos, onde eles iniciarão com o ano com 4 dígitos, o mês numérico com dois dígitos, o caractere ´_´ e seguido de um nome com todas as letras em minúsculo, que não ultrapassem 24 caracteres e não contenha nenhum caractere especial, com exeção de ´_´ ou ´-´.

## Estrutura das pastas:

1. /01_dados;
    - /bruto: Dados brutos, exatamente como foram obtidos.
    - /proces: Dados que foram limpos e transformados para análises.
    - /externo: Dados de fontes externas.
    - /saida: Dados finais ou resultados de modelos que serão usados para visualização ou relatórios
2. /02_notebook: Notebooks para exploração de dados, análises preliminares e prototipagem.
3. /03_fonte;
    - /dados: Códigos para processamento de dados.
    - /atributo: Códigos para geração de features.
    - /modelo: Scripts para treinamento e validação de modelos.
    - /visu: Scripts para criação de visualizações e gráficos.
    - /util: Códigos auxiliares e funções de uso geral.
4. /04_relatorio: Relatórios analíticos ou de pesquisa, geralmente em formatos como PDF ou Markdown.
5. /00_README.md: Uma descrição do projeto, como configurá-lo, como executar os scripts e qualquer outra informação relevante que ajudaria um novo colaborador a entender rapidamente o projeto.


