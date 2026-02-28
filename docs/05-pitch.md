# 🎓 Sophia - Educadora Financeira Inteligente

## 📝 Descrição do Projeto
A **Sophia** é uma assistente de educação financeira desenvolvida para transformar dados bancários complexos em ensinamentos simples e práticos. O projeto utiliza IA generativa de última geração para analisar o perfil do investidor, transações e histórico, oferecendo uma mentoria personalizada e segura.

---

## 🚀 Conclusões Técnicas

### **O que funcionou bem:**
* **Integração Cloud (Gemini API):** A migração para a API do Gemini 1.5 Flash eliminou gargalos de hardware e latência, garantindo respostas em milissegundos.
* **Arquitetura de Dados Dinâmica:** Uso das bibliotecas `os` e `pandas` para leitura de arquivos `.json` e `.csv` com caminhos dinâmicos, garantindo a portabilidade do sistema.
* **Engenharia de Prompt e Segurança:** Implementação de travas de tokens e instruções rígidas para garantir que a assistente seja objetiva, didática e não realize recomendações diretas de compra.
* **Interface Streamlit:** Desenvolvimento de uma interface de chat intuitiva e leve, focada na experiência do usuário final.

### **O que pode melhorar:**
* **Implementação de RAG (Retrieval-Augmented Generation):** Para otimizar a consulta a bases de produtos financeiros extensas sem sobrecarregar o contexto.
* **Monitoramento de Observabilidade:** Integração com ferramentas como LangFuse para rastrear custos, latência e taxa de erros em produção.

---

## 📊 Avaliação e Métricas de Qualidade

| Métrica | O que avalia | Resultado do Teste |
|---------|--------------|------------------|
| **Assertividade** | Resposta direta sobre saldo e gastos. | ✅ 100% (Consulta correta aos arquivos de dados) |
| **Segurança** | Evitar assuntos fora do escopo financeiro. | ✅ Aprovado (Recusa temas irrelevantes conforme System Prompt) |
| **Coerência** | Conselhos alinhados ao perfil do investidor. | ✅ 5/5 (Exemplos baseados no patrimônio real do cliente) |

---

## 🎤 Pitch de Apresentação (3 Minutos)

### 1. O Problema (30 seg)
A complexidade do mercado financeiro e o excesso de termos técnicos afastam o cidadão comum de uma gestão saudável de seu patrimônio. Dados isolados em extratos bancários não educam; muitas vezes, apenas confundem o usuário.

### 2. A Solução (1 min)
A Sophia resolve essa dor integrando o poder do **Gemini 1.5 Flash** com os dados reais do usuário. Ela atua como uma mentora disponível 24/7, que interpreta gastos e objetivos para ensinar finanças de forma personalizada, sem exigir hardware potente do usuário.

### 3. Demonstração (1 min)
* **Cenário:** O usuário pergunta "O que é CDI e como ele afeta meu saldo?".
* **Ação:** A Sophia consulta o saldo real no `perfil_investidor.json` e explica o conceito usando o patrimônio do cliente como exemplo prático de rendimento.

### 4. Diferencial e Impacto (30 seg)
O diferencial é a **latência ultra-baixa** aliada à **personalização extrema**. O impacto social é a democratização da educação financeira, transformando a relação das pessoas com o dinheiro através da tecnologia e acessibilidade.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.10+**
* **Streamlit** (Interface Web)
* **Google Generative AI SDK** (Gemini 1.5 Flash)
* **Pandas** (Tratamento de Dados CSV)
* **JSON** (Persistência de Perfil e Produtos)

---

## 🔗 Link do Vídeo
[Insira aqui o link para o seu vídeo no YouTube/Loom]
