<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=409AD5&height=150&text=KoAlly&fontColor=ff8300&animation=fadeIn&section=header"/>

# 🐨 KoAlly Mission Scheduler - Sistema de Gerenciamento de Tarefas Espaciais

## 👥 Integrantes

<div align="center">
  <table border="0" style="border-collapse: collapse; border: none;">
    <tr style="border: none; background: none;">
      <td align="left" style="border: none; padding-right: 40px; vertical-align: middle; line-height: 1.8;">
        🧑‍🚀 <strong>Enzo Carvalho Brincalepe Campo</strong>  <code style="color: #0366d6;">RM 562296</code> <br><br>
        🧑‍🚀 <strong>João Vitor Parizotto Rocha</strong> <code style="color: #0366d6;">RM 562719</code> <br><br>
        🧑‍🚀 <strong>Luccas Figueira Gonçalves Costa</strong> <code style="color: #0366d6;">RM 564240</code> <br><br>
        🧑‍🚀 <strong>Paulo Henrique Souza Vieira</strong> <code style="color: #0366d6;">RM 566240</code> <br><br>
        🧑‍🚀 <strong>Pedro Albuquerque Drumond</strong>  <code style="color: #0366d6;">RM 566255</code>
      </td>
      <td align="center" style="border: none; vertical-align: middle;">
        <img width="280" height="280" alt="Mission Logo" src="https://github.com/user-attachments/assets/5e2f5b84-895d-4936-a120-7efc8375c540" style="border-radius: 20px; box-shadow: 0px 4px 10px rgba(0,0,0,0.3);" />
      </td>
    </tr>
  </table>
</div>

---

## 🐨 O que é o koally e Definição do Problema
O KoAlly é um copiloto de inteligência artificial desenvolvido para acompanhar astronautas
durante missões espaciais de longa duração. O sistema opera completamente a bordo da nave,
sem depender de comunicação com a Terra, e atua em três frentes simultâneas: monitoramento
contínuo da saúde mental de cada tripulante, suporte técnico operacional da nave, e
gerenciamento adaptativo da rotina de missão com base na capacidade humana real de cada
astronauta em cada momento.
Na camada de saúde mental, o agente registra sessões de acompanhamento, analisa dados
biométricos e gera um relatório psicológico baseado em frameworks clínicos validados.
Quando o estado do astronauta atinge um nível crítico, um psicólogo humano é acionado de
forma assíncrona, recebendo apenas os dados necessários e enviando protocolos de intervenção
que o agente entrega no momento adequado. Na camada operacional, o sistema monitora os
sistemas da nave e guia o tripulante na resolução de falhas em tempo real. No scheduler
adaptativo, o agente cruza a demanda do cronograma oficial de missão com o estado físico e
mental do astronauta, recomendando redistribuição de tarefas quando necessário para prevenir
sobrecarga acumulada.
O nome KoAlly é uma referência ao coala, animal conhecido por sua natureza calma e
acolhedora, qualidades centrais para um sistema voltado ao bem-estar humano em um dos
contextos mais extrem

Em missões espaciais tripuladas, a gestão do tempo e das atividades dos astronautas é crítica para a sobrevivência e o sucesso da expedição. O desafio consiste em coordenar uma rotina complexa que envolve dois tipos distintos de atividades:

* **Tarefas Universais (Gerais):** Atividades diárias obrigatórias que todos os membros da tripulação precisam realizar (ex: exercícios, alimentação, sono).
* **Tarefas de Missão:** Atividades técnicas e operacionais específicas da nave que precisam ser distribuídas de forma justa e equilibrada entre a equipe (ex: manutenção de hardware, experimentos científicos).

Além disso, as tarefas possuem diferentes níveis de urgência. Se uma falha crítica no suporte à vida acontecer, o sistema precisa garantir que essa tarefa passe à frente de tarefas rotineiras, organizando a execução por ordem de prioridade.

---

## 🛠️ Solução Proposta e Estruturas de Dados

Para resolver esse problema, o sistema simula o dia a dia da tripulação utilizando conceitos fundamentais de Estruturas de Dados:

* **Fila (Queue) com Ordenação de Prioridade:** Cada astronauta possui uma fila de tarefas. Embora as tarefas universais e de missão entrem na fila, o método `ordenar()` garante que as tarefas com maior nível de prioridade (escala de 1 a 10) sejam executadas primeiro. Tarefas com prioridade máxima (10) utilizam uma inserção direta no início da fila (`enfileirarPrioridade`).
* **Pilha (Stack):** Funciona como o Histórico de Execução. À medida que o astronauta conclui uma tarefa (retirada do início da fila), ela é empilhada no histórico. Ao exibir o histórico, os eventos aparecem em ordem cronológica inversa (da mais recente para a mais antiga), respeitando a propriedade LIFO (*Last In, First Out*).

---

## 🏗️ Arquitetura do Código

O sistema é dividido em 5 classes principais:

### 1. Tarefa
Modela a atividade a ser realizada.
* `nome`: Descrição da tarefa.
* `prioridade`: Um inteiro (geralmente de 1 a 10).
* `geral`: Booleano que indica se a tarefa é universal.

### 2. Fila
Gerencia a lista de tarefas pendentes de um astronauta.
* `enfileirar()`: Adiciona ao final.
* `enfileirarPrioridade()`: Insere no topo (índice 0).
* `ordenar()`: Reorganiza a fila decrescentemente com base na prioridade.
* `remover()`: Retira e retorna a tarefa do topo da fila para execução.

### 3. Pilha
Armazena o histórico de tarefas concluídas.
* `push()`: Adiciona a tarefa concluída no topo da pilha.
* `mostrar()`: Exibe os itens do topo para a base (da última executada para a primeira).

### 4. Astronauta
Representa um membro da tripulação. Possui seu próprio nome, função, uma `Fila` de tarefas a fazer e uma `Pilha` de histórico.

### 5. MissionScheduler
O motor do sistema. Ele recebe a lista de astronautas e a lista de tarefas e realiza o seguinte fluxo:
1. Separa tarefas universais de tarefas de missão.
2. Atribui as universais para absolutamente todos os astronautas.
3. Distribui as de missão de forma rotativa (usando o operador mod `%`), garantindo um balanceamento de carga de trabalho equilibrado.
4. Ordena a fila de cada astronauta antes da execução começar.

---

## 🏃‍♂️ Como Executar o Projeto

1. Certifique-se de ter o Python 3.14 instalado em sua máquina.
2. Clone este repositório ou copie o código para um arquivo chamado `main.py`.
3. Execute o arquivo no terminal:

```bash
python main.py
```
<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=409AD5&height=120&section=footer"/>
