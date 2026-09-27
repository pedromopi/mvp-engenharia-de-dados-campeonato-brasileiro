# Catálogo de dados

Este catálogo descreve as tabelas Delta do projeto no catálogo `workspace` do Databricks. As mesmas descrições são registradas no Unity Catalog pelo notebook `05_catalogo_dados.ipynb`.

## Linhagem

```text
CSV do Kaggle -> Bronze -> Silver -> Gold -> análises
```

- **Bronze:** cópia dos quatro arquivos carregados pelo Catalog Explorer.
- **Silver:** limpeza, tipagem, padronização dos minutos e inclusão de metadados.
- **Gold:** junção das partidas com estatísticas e primeiro gol; `viradas` é um recorte da base analítica.

Os tipos abaixo foram conferidos na saída do notebook de catálogo executado no Databricks.

## `workspace.bronze.campeonato_brasileiro_full`

Dados brutos das partidas, carregados do CSV principal sem transformacoes analiticas.

- **Origem:** campeonato-brasileiro-full.csv
- **Granularidade:** Uma linha por partida.

| Coluna | Tipo | Descrição / domínio esperado |
|---|---|---|
| `ID` | `BIGINT` | Identificador da partida na fonte. |
| `rodata` | `BIGINT` | Numero da rodada, com o nome original da fonte. |
| `data` | `DATE` | Data da partida no formato original. |
| `hora` | `TIME(6)` | Horario informado para a partida. |
| `mandante` | `STRING` | Clube mandante. |
| `visitante` | `STRING` | Clube visitante. |
| `formacao_mandante` | `STRING` | Formacao tatica do mandante. |
| `formacao_visitante` | `STRING` | Formacao tatica do visitante. |
| `tecnico_mandante` | `STRING` | Tecnico do clube mandante. |
| `tecnico_visitante` | `STRING` | Tecnico do clube visitante. |
| `vencedor` | `STRING` | Clube vencedor ou hifen em caso de empate. |
| `arena` | `STRING` | Estadio ou arena da partida. |
| `mandante_Placar` | `BIGINT` | Gols marcados pelo mandante. |
| `visitante_Placar` | `BIGINT` | Gols marcados pelo visitante. |
| `mandante_Estado` | `STRING` | UF do clube mandante. |
| `visitante_Estado` | `STRING` | UF do clube visitante. |
| `arrecadacao` | `DOUBLE` | Arrecadacao informada para a partida. |

## `workspace.bronze.campeonato_brasileiro_gols`

Eventos brutos de gols das partidas.

- **Origem:** campeonato-brasileiro-gols.csv
- **Granularidade:** Uma linha por evento de gol.

| Coluna | Tipo | Descrição / domínio esperado |
|---|---|---|
| `partida_id` | `BIGINT` | Identificador da partida. |
| `rodata` | `BIGINT` | Numero da rodada no arquivo de origem. |
| `clube` | `STRING` | Clube que marcou o gol. |
| `atleta` | `STRING` | Atleta associado ao gol. |
| `minuto` | `STRING` | Minuto do gol como recebido da fonte. |
| `tipo_de_gol` | `STRING` | Classificacao do gol informada pela fonte. |

## `workspace.bronze.campeonato_brasileiro_cartoes`

Eventos brutos de cartoes das partidas.

- **Origem:** campeonato-brasileiro-cartoes.csv
- **Granularidade:** Uma linha por evento de cartao.

| Coluna | Tipo | Descrição / domínio esperado |
|---|---|---|
| `partida_id` | `BIGINT` | Identificador da partida. |
| `rodata` | `BIGINT` | Numero da rodada no arquivo de origem. |
| `clube` | `STRING` | Clube do atleta advertido. |
| `cartao` | `STRING` | Tipo de cartao. |
| `atleta` | `STRING` | Atleta advertido. |
| `num_camisa` | `BIGINT` | Numero da camisa como recebido da fonte. |
| `posicao` | `STRING` | Posicao do atleta. |
| `minuto` | `STRING` | Minuto do cartao como recebido da fonte. |

## `workspace.bronze.campeonato_brasileiro_estatisticas_full`

Estatisticas brutas de cada clube em cada partida.

- **Origem:** campeonato-brasileiro-estatisticas-full.csv
- **Granularidade:** Uma linha por partida e clube.

| Coluna | Tipo | Descrição / domínio esperado |
|---|---|---|
| `partida_id` | `BIGINT` | Identificador da partida. |
| `rodata` | `BIGINT` | Numero da rodada no arquivo de origem. |
| `clube` | `STRING` | Clube ao qual as estatisticas pertencem. |
| `chutes` | `BIGINT` | Total de chutes como recebido da fonte. |
| `chutes_no_alvo` | `BIGINT` | Chutes no alvo como recebido da fonte. |
| `posse_de_bola` | `STRING` | Posse de bola com sinal de percentual. |
| `passes` | `BIGINT` | Total de passes como recebido da fonte. |
| `precisao_passes` | `STRING` | Precisao dos passes com sinal de percentual. |
| `faltas` | `BIGINT` | Total de faltas como recebido da fonte. |
| `cartao_amarelo` | `BIGINT` | Total de cartoes amarelos como recebido da fonte. |
| `cartao_vermelho` | `BIGINT` | Total de cartoes vermelhos como recebido da fonte. |
| `impedimentos` | `BIGINT` | Total de impedimentos como recebido da fonte. |
| `escanteios` | `BIGINT` | Total de escanteios como recebido da fonte. |

## `workspace.silver.partidas`

Partidas tipadas, padronizadas e enriquecidas com o resultado.

- **Origem:** Bronze campeonato_brasileiro_full.
- **Granularidade:** Uma linha por partida.

| Coluna | Tipo | Descrição / domínio esperado |
|---|---|---|
| `partida_id` | `BIGINT` | Identificador unico da partida. |
| `rodada` | `INT` | Numero da rodada. |
| `data_partida` | `DATE` | Data da partida. |
| `hora` | `STRING` | Horario informado para a partida. |
| `mandante` | `STRING` | Clube mandante. |
| `visitante` | `STRING` | Clube visitante. |
| `formacao_mandante` | `STRING` | Formacao tatica do mandante. |
| `formacao_visitante` | `STRING` | Formacao tatica do visitante. |
| `tecnico_mandante` | `STRING` | Tecnico do mandante. |
| `tecnico_visitante` | `STRING` | Tecnico do visitante. |
| `vencedor` | `STRING` | Clube vencedor ou hifen em caso de empate. |
| `arena` | `STRING` | Estadio ou arena com espacos padronizados. |
| `placar_mandante` | `INT` | Gols marcados pelo mandante. |
| `placar_visitante` | `INT` | Gols marcados pelo visitante. |
| `estado_mandante` | `STRING` | UF do clube mandante. |
| `estado_visitante` | `STRING` | UF do clube visitante. |
| `arrecadacao` | `DOUBLE` | Arrecadacao convertida para numero; nulo quando invalida ou ausente. |
| `resultado` | `STRING` | Resultado na perspectiva do mando: mandante, visitante ou empate. |
| `versao_fonte` | `INT` | Versao do dataset do Kaggle usada no processamento. |
| `processado_em` | `TIMESTAMP` | Data e hora do processamento. |

## `workspace.silver.gols`

Eventos de gols limpos, com minutos separados e ordenaveis.

- **Origem:** Bronze campeonato_brasileiro_gols.
- **Granularidade:** Uma linha por evento de gol.

| Coluna | Tipo | Descrição / domínio esperado |
|---|---|---|
| `partida_id` | `BIGINT` | Identificador da partida. |
| `rodada` | `INT` | Numero da rodada. |
| `clube` | `STRING` | Clube que marcou o gol. |
| `atleta` | `STRING` | Atleta associado ao gol. |
| `tipo_gol` | `STRING` | Tipo do gol; Normal quando ausente na fonte. |
| `minuto_original` | `STRING` | Minuto exatamente como recebido da fonte. |
| `minuto_base` | `INT` | Parte principal do minuto. |
| `minuto_acrescimo` | `INT` | Acrescimo indicado apos o sinal de mais. |
| `minuto_ordem` | `INT` | Soma do minuto base com o acrescimo, usada para ordenacao. |
| `versao_fonte` | `INT` | Versao do dataset do Kaggle. |
| `processado_em` | `TIMESTAMP` | Data e hora do processamento. |

## `workspace.silver.cartoes`

Eventos de cartoes limpos, tipados e com minutos ordenaveis.

- **Origem:** Bronze campeonato_brasileiro_cartoes.
- **Granularidade:** Uma linha por evento de cartao.

| Coluna | Tipo | Descrição / domínio esperado |
|---|---|---|
| `partida_id` | `BIGINT` | Identificador da partida. |
| `rodada` | `INT` | Numero da rodada. |
| `clube` | `STRING` | Clube do atleta advertido. |
| `cartao` | `STRING` | Tipo de cartao. |
| `atleta` | `STRING` | Atleta advertido. |
| `numero_camisa` | `INT` | Numero da camisa; nulo quando invalido ou ausente. |
| `posicao` | `STRING` | Posicao do atleta. |
| `minuto_original` | `STRING` | Minuto exatamente como recebido da fonte. |
| `minuto_base` | `INT` | Parte principal do minuto. |
| `minuto_acrescimo` | `INT` | Acrescimo indicado apos o sinal de mais. |
| `minuto_ordem` | `INT` | Soma do minuto base com o acrescimo. |
| `versao_fonte` | `INT` | Versao do dataset do Kaggle. |
| `processado_em` | `TIMESTAMP` | Data e hora do processamento. |

## `workspace.silver.estatisticas`

Estatisticas por partida e clube, tipadas e padronizadas.

- **Origem:** Bronze campeonato_brasileiro_estatisticas_full.
- **Granularidade:** Uma linha por partida e clube.

| Coluna | Tipo | Descrição / domínio esperado |
|---|---|---|
| `partida_id` | `BIGINT` | Identificador da partida. |
| `rodada` | `INT` | Numero da rodada. |
| `clube` | `STRING` | Clube ao qual as estatisticas pertencem. |
| `chutes` | `INT` | Total de chutes. |
| `chutes_no_alvo` | `INT` | Total de chutes no alvo. |
| `posse_bola_pct` | `DOUBLE` | Percentual de posse, esperado entre 0 e 100. |
| `passes` | `INT` | Total de passes. |
| `precisao_passes_pct` | `DOUBLE` | Percentual de precisao dos passes, esperado entre 0 e 100. |
| `faltas` | `INT` | Total de faltas. |
| `cartoes_amarelos` | `INT` | Total de cartoes amarelos. |
| `cartoes_vermelhos` | `INT` | Total de cartoes vermelhos. |
| `impedimentos` | `INT` | Total de impedimentos. |
| `escanteios` | `INT` | Total de escanteios. |
| `estatisticas_disponiveis` | `BOOLEAN` | Indica disponibilidade da posse de bola. |
| `versao_fonte` | `INT` | Versao do dataset do Kaggle. |
| `processado_em` | `TIMESTAMP` | Data e hora do processamento. |

## `workspace.gold.partidas_analiticas`

Base analitica por partida, reunindo resultado, estatisticas e primeiro gol.

- **Origem:** Join de Silver partidas, estatisticas e gols.
- **Granularidade:** Uma linha por partida.

| Coluna | Tipo | Descrição / domínio esperado |
|---|---|---|
| `partida_id` | `BIGINT` | Identificador unico da partida. |
| `ano` | `INT` | Ano civil da data da partida. |
| `data_partida` | `DATE` | Data da partida. |
| `rodada` | `INT` | Numero da rodada. |
| `mandante` | `STRING` | Clube mandante. |
| `visitante` | `STRING` | Clube visitante. |
| `estado_mandante` | `STRING` | UF do clube mandante. |
| `estado_visitante` | `STRING` | UF do clube visitante. |
| `placar_mandante` | `INT` | Gols marcados pelo mandante. |
| `placar_visitante` | `INT` | Gols marcados pelo visitante. |
| `vencedor` | `STRING` | Clube vencedor ou hifen em caso de empate. |
| `resultado` | `STRING` | Resultado na perspectiva do mando: mandante, visitante ou empate. |
| `posse_mandante` | `DOUBLE` | Percentual de posse do mandante. |
| `posse_visitante` | `DOUBLE` | Percentual de posse do visitante. |
| `escanteios_mandante` | `INT` | Escanteios do mandante. |
| `escanteios_visitante` | `INT` | Escanteios do visitante. |
| `chutes_mandante` | `INT` | Chutes do mandante. |
| `chutes_visitante` | `INT` | Chutes do visitante. |
| `chutes_alvo_mandante` | `INT` | Chutes no alvo do mandante. |
| `chutes_alvo_visitante` | `INT` | Chutes no alvo do visitante. |
| `estatisticas_mandante_disponiveis` | `BOOLEAN` | Indica disponibilidade das estatisticas do mandante. |
| `estatisticas_visitante_disponiveis` | `BOOLEAN` | Indica disponibilidade das estatisticas do visitante. |
| `primeiro_clube` | `STRING` | Clube que marcou o primeiro gol identificado. |
| `primeiro_minuto` | `INT` | Minuto ordenavel do primeiro gol. |
| `primeiro_gol_ambiguo` | `BOOLEAN` | Indica mais de um clube associado ao primeiro minuto. |
| `primeiro_gol_venceu` | `BOOLEAN` | Indica se o clube que marcou primeiro venceu. |
| `houve_virada` | `BOOLEAN` | Indica vitoria do clube que sofreu o primeiro gol. |
| `estado_vencedor` | `STRING` | UF do clube vencedor; nulo em empates. |
| `estatisticas_disponiveis` | `BOOLEAN` | Indica estatisticas disponiveis para os dois clubes. |
| `processado_em` | `TIMESTAMP` | Data e hora do processamento da Gold. |

## `workspace.gold.viradas`

Recorte das partidas vencidas pelo clube que sofreu o primeiro gol.

- **Origem:** Filtro houve_virada da Gold partidas_analiticas.
- **Granularidade:** Uma linha por partida com virada.

| Coluna | Tipo | Descrição / domínio esperado |
|---|---|---|
| `partida_id` | `BIGINT` | Identificador unico da partida. |
| `ano` | `INT` | Ano civil da data da partida. |
| `data_partida` | `DATE` | Data da partida. |
| `rodada` | `INT` | Numero da rodada. |
| `mandante` | `STRING` | Clube mandante. |
| `visitante` | `STRING` | Clube visitante. |
| `estado_mandante` | `STRING` | UF do clube mandante. |
| `estado_visitante` | `STRING` | UF do clube visitante. |
| `placar_mandante` | `INT` | Gols marcados pelo mandante. |
| `placar_visitante` | `INT` | Gols marcados pelo visitante. |
| `vencedor` | `STRING` | Clube vencedor ou hifen em caso de empate. |
| `resultado` | `STRING` | Resultado na perspectiva do mando: mandante, visitante ou empate. |
| `posse_mandante` | `DOUBLE` | Percentual de posse do mandante. |
| `posse_visitante` | `DOUBLE` | Percentual de posse do visitante. |
| `escanteios_mandante` | `INT` | Escanteios do mandante. |
| `escanteios_visitante` | `INT` | Escanteios do visitante. |
| `chutes_mandante` | `INT` | Chutes do mandante. |
| `chutes_visitante` | `INT` | Chutes do visitante. |
| `chutes_alvo_mandante` | `INT` | Chutes no alvo do mandante. |
| `chutes_alvo_visitante` | `INT` | Chutes no alvo do visitante. |
| `estatisticas_mandante_disponiveis` | `BOOLEAN` | Indica disponibilidade das estatisticas do mandante. |
| `estatisticas_visitante_disponiveis` | `BOOLEAN` | Indica disponibilidade das estatisticas do visitante. |
| `primeiro_clube` | `STRING` | Clube que marcou o primeiro gol identificado. |
| `primeiro_minuto` | `INT` | Minuto ordenavel do primeiro gol. |
| `primeiro_gol_ambiguo` | `BOOLEAN` | Indica mais de um clube associado ao primeiro minuto. |
| `primeiro_gol_venceu` | `BOOLEAN` | Indica se o clube que marcou primeiro venceu. |
| `houve_virada` | `BOOLEAN` | Indica vitoria do clube que sofreu o primeiro gol. |
| `estado_vencedor` | `STRING` | UF do clube vencedor; nulo em empates. |
| `estatisticas_disponiveis` | `BOOLEAN` | Indica estatisticas disponiveis para os dois clubes. |
| `processado_em` | `TIMESTAMP` | Data e hora do processamento da Gold. |
