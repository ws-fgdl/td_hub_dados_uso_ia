# Análise do uso de IA na companhia

Este projeto reúne dados de colaboradores e registros de uso de ferramentas de inteligência artificial para apoiar a análise de adoção da IA na companhia. O objetivo é transformar essas fontes em métricas que permitam comparar o uso entre cargos, áreas, segmentos e níveis de senioridade, respeitando a privacidade dos colaboradores.

## Objetivos da análise

- Medir o volume e a distribuição de acessos às ferramentas de IA.
- Comparar indicadores entre cargos, departamentos, segmentos e hierarquias.
- Identificar padrões de adoção e diferenças entre grupos organizacionais.
- Preparar uma base consolidada para análises e visualizações posteriores.

## Arquivos de dados

Os arquivos abaixo são insumos locais e podem conter informações corporativas ou pessoais. Não devem ser publicados nem compartilhados fora dos canais autorizados.

| Arquivo | Finalidade |
| --- | --- |
| `BASE_USUARIOS_WS.csv` | Base de colaboradores em CSV, com campos como e-mail, login, nome, cargo e segmento. |
| `usuarios_ws.xlsx` | Base de colaboradores em Excel, usada atualmente pelo script para obter atributos organizacionais. |
| `acesso_ia.csv` | Registros de acesso, incluindo usuário, serviço, quantidade de acessos, uso ativo e hosts. |
| `base_gemini.xlsx` | Relatório de uso do Gemini; o script lê a aba `Gemini Report 1026`. |
| `analise_tratamento_base.py` | Script de preparação e consolidação dos dados. |

## Fluxo atual

O script `analise_tratamento_base.py`:

1. Carrega a base de colaboradores e remove registros sem cargo.
2. Cria agrupamentos de cargo e hierarquia (JR, PL, SR ou sem hierarquia) e normaliza alguns nomes de departamento.
3. Filtra os registros de acesso para usuários presentes na base de colaboradores.
4. Relaciona os registros de acesso e do relatório Gemini com os atributos dos colaboradores, usando login ou e-mail.
5. Soma as quantidades de uso por colaborador, cargo, departamento, segmento e hierarquia e combina os resultados em uma base chamada `final`.

Atualmente, a base consolidada existe apenas em memória durante a execução: o script ainda não exporta um arquivo de resultados nem gera relatórios ou gráficos.

## Como executar

Requisitos: Python e as bibliotecas `pandas`, `numpy` e `openpyxl`.

Instale as dependências, se necessário:

```bash
python -m pip install pandas numpy openpyxl
```

Com os arquivos de dados na mesma pasta do script, execute:

```bash
python analise_tratamento_base.py
```

## Métricas que podem ser desenvolvidas

Com a consolidação atual, é possível avançar para indicadores como:

- total e média de acessos por cargo, área, segmento e hierarquia;
- quantidade e proporção de colaboradores com registros de uso;
- distribuição do uso por serviço e por grupo organizacional;
- percentis de acessos para entender a variação dentro de cada grupo;
- evolução temporal, caso as fontes passem a incluir datas comparáveis.

As métricas devem explicitar o período analisado e a definição de “uso”. Quantidade de acessos não equivale necessariamente a número de pessoas usuárias, intensidade de uso, produtividade ou impacto no trabalho. Para comparar grupos, é importante considerar também o tamanho de cada grupo e a cobertura das fontes.

## Privacidade e interpretação

As bases podem conter identificadores e dados organizacionais de colaboradores. Restrinja o acesso aos arquivos, evite incluir dados individuais em materiais de divulgação e prefira resultados agregados. Antes de compartilhar análises, verifique se grupos pequenos ou combinações de atributos podem permitir a identificação de pessoas e siga as políticas internas de privacidade e governança de dados.
