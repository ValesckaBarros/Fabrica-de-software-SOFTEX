# Sistema de Casa Inteligente

## Visão Geral do Projeto
Este projeto implementa um sistema de casa inteligente que permite controlar vários dispositivos, como luzes, termostatos e sistemas de segurança, através de uma interface de linha de comando (CLI). O projeto integra conceitos de programação orientada a objetos, padrões de projeto, máquinas de estados e programação funcional.

## Estrutura do Projeto

O projeto está dividido em vários módulos:

1. **casainteligente.py**: Implementa a classe `CasaInteligente`, que gerencia os dispositivos na casa.
2. **dispositivo.py**: Define a classe base abstrata `Dispositivo`.
3. **fabricadispositivos.py**: Implementa a fábrica `DispositivoFactory` para criar instâncias de dispositivos.
4. **interface.py**: Contém a implementação da CLI.
5. **luz.py**: Define a classe `Luz`.
6. **observer.py**: Implementa o padrão Observer (a ser implementado conforme necessidade).
7. **seguranca.py**: Define a classe `SistemaSeguranca`.
8. **termostato.py**: Define a classe `Termostato`.

## Instruções para Configurar e Executar o Projeto

### Pré-requisitos

1. Certifique-se de ter o Python 3 instalado. Para garantir que o Python 3 está instalado no seu sistema, siga os passos abaixo:
   - Use o CMD (Prompt de Comando) no Windows ou o terminal no macOS ou Linux.
   - Digite o seguinte comando no CMD ou terminal e pressione `Enter`: 
```bash
python --version
```

2. Você também precisará instalar a biblioteca `transitions`:

```bash
pip install transitions
```
### Como Abrir o Arquivo no CMD

Para abrir e executar o arquivo `interface.py` no Prompt de Comando (CMD) do Windows, siga os passos abaixo:

1. **Abrir o CMD:**
   - Pressione a tecla `Windows` no seu teclado ou clique no ícone do Windows na barra de tarefas.
   - Digite `cmd` ou `Prompt de Comando` na caixa de pesquisa.
   - Selecione `Prompt de Comando` nos resultados da pesquisa e clique para abrir.

2. **Navegar até o Diretório do Projeto:**
   - Use o comando `cd` (Change Directory) para mudar para o diretório onde o arquivo `interface.py` está localizado. Por exemplo:
     ```bash
     cd "C:\Caminho\Para\Seu\Projeto"
     ```
   - Substitua `"C:\Caminho\Para\Seu\Projeto"` pelo caminho real do diretório que contém o arquivo `interface.py`.

3. **Executar o Arquivo:**
   - Após navegar para o diretório correto, execute o arquivo `interface.py` usando o comando Python. Por exemplo:
     ```bash
     python interface.py
     ```
   
4. **Usar a CLI:**
   - Após executar o arquivo, você verá o prompt para digitar comandos. Você pode usar os comandos disponíveis para interagir com o sistema de casa inteligente, como listar dispositivos, adicionar novos dispositivos, e muito mais.

Se precisar de mais assistência, consulte a documentação ou peça ajuda na comunidade Python.


### Comandos da CLI

#### Adicionar Dispositivos

| Comando                                         | Descrição                                        | Exemplo de Saída                          |
|-------------------------------------------------|--------------------------------------------------|-------------------------------------------|
| `python interface.py --adicionar luz`           | Adicionar uma Luz                                | Luz adicionada.                           |
| `python interface.py --adicionar termostato`    | Adicionar um Termostato                         | Termostato adicionado.                    |
| `python interface.py --adicionar seguranca`     | Adicionar um Sistema de Segurança                | Sistema de segurança adicionado.          |

#### Listar Dispositivos

| Comando                                         | Descrição                                        | Exemplo de Saída                          |
|-------------------------------------------------|--------------------------------------------------|-------------------------------------------|
| `python interface.py --listar`                  | Listar todos os dispositivos                    | 0: Luz está desligada                     |

#### Ligar/Desligar Dispositivos

| Comando                                         | Descrição                                        | Exemplo de Saída                                              |
|-------------------------------------------------|--------------------------------------------------|---------------------------------------------------------------|
| `python interface.py --ligar <índice>`          | Ligar um dispositivo pelo índice                | Dispositivo no índice <índice> ligado.                       |
| `python interface.py --desligar <índice>`       | Desligar um dispositivo pelo índice             | Dispositivo no índice <índice> desligado.                    |

#### Remover Dispositivos

| Comando                                         | Descrição                                        | Exemplo de Saída                        |
|-------------------------------------------------|--------------------------------------------------|-----------------------------------------|
| `python interface.py --remover <índice>`        | Remover um dispositivo pelo índice              | Dispositivo no índice <índice> removido. |

#### Ligar Todos os Dispositivos

| Comando                                         | Descrição                                        | Exemplo de Saída                          |
|-------------------------------------------------|--------------------------------------------------|-------------------------------------------|
| `python interface.py --ligar_todos`             | Ligar todos os dispositivos                     | Todos os dispositivos ligados.            |

#### Desligar Todos os Dispositivos

| Comando                                         | Descrição                                        | Exemplo de Saída                          |
|-------------------------------------------------|--------------------------------------------------|-------------------------------------------|
| `python interface.py --desligar_todos`          | Desligar todos os dispositivos                  | Todos os dispositivos desligados.         |

#### Aquecer/Esfriar Termostato

| Comando                                         | Descrição                                        | Exemplo de Saída                                  |
|-------------------------------------------------|--------------------------------------------------|---------------------------------------------------|
| `python interface.py --aquecer <índice>`        | Aquecer um termostato pelo índice               | Termostato no índice <índice> aquecendo.         |
| `python interface.py --esfriar <índice>`        | Esfriar um termostato pelo índice               | Termostato no índice <índice> esfriando.         |

#### Armar Sistema de Segurança

| Comando                                             | Descrição                                        | Exemplo de Saída                                                        |
|-----------------------------------------------------|--------------------------------------------------|-------------------------------------------------------------------------|
| `python interface.py --armar_com_gente_em_casa <índice>` | Armar o sistema de segurança com gente em casa | Sistema de segurança no índice <índice> armado com gente em casa.       |
| `python interface.py --armar_sem_gente_em_casa <índice>`  | Armar o sistema de segurança sem gente em casa | Sistema de segurança no índice <índice> armado sem ninguém em casa.      |

#### Exibir Ajuda

| Comando                                         | Descrição                    | Exemplo de Saída                          |
|-------------------------------------------------|------------------------------|-------------------------------------------|
| `python interface.py --help`                    | Exibir lista de comandos     | Exibe a lista de comandos disponíveis.    |
