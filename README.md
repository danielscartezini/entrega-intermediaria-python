# 🚀 Entrega Intermediária - Python CLI com Integração de API

Este projeto demonstra uma aplicação de linha de comando (CLI) em Python que se integra com uma API externa (JSONPlaceholder) para buscar e exibir dados. O objetivo principal é seguir um Procedimento Operacional Padrão (SOP) rigoroso para desenvolvimento, versionamento e integração contínua, simulando uma etapa intermediária na evolução de um software.

## ✨ Funcionalidades

- **Integração com API Externa:** Consome dados da API JSONPlaceholder.
- **Exibição de Dados:** Apresenta os títulos e corpos das primeiras 5 postagens de forma organizada no console.
- **Tratamento de Erros:** Inclui tratamento básico para falhas na conexão ou na requisição da API.
- **Testes de Integração:** Validação da funcionalidade de busca da API e tratamento de erros usando `pytest`.
- **Integração Contínua (CI):** Configuração de GitHub Actions para automatizar a execução de testes em cada push e Pull Request.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11:** Linguagem de programação principal.
- **`requests`:** Biblioteca HTTP para Python, utilizada para fazer requisições à API.
- **`pytest`:** Framework de testes para Python.
- **`unittest.mock`:** Módulo para simulação (mocking) em testes.
- **GitHub Actions:** Para automação de CI.
- **JSONPlaceholder:** API REST gratuita para testes e prototipagem.

## ⚙️ Configuração e Execução

Siga os passos abaixo para configurar e executar o projeto localmente.

### Pré-requisitos

Certifique-se de ter o Python 3.11 (ou superior) e `pip` instalados em sua máquina.

### 1. Clonar o Repositório

```bash
git clone https://github.com/danielscartezini/entrega-intermediaria-python.git
cd entrega-intermediaria-python
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Executar a Aplicação

Para buscar e exibir as postagens da API:

```bash
python main.py
```

### 4. Executar os Testes

Para rodar os testes de integração e garantir que a aplicação está funcionando corretamente:

```bash
pytest
```

## 🌐 API Integrada

Este projeto utiliza a [JSONPlaceholder](https://jsonplaceholder.typicode.com/), uma API REST online gratuita que fornece dados falsos para testes e prototipagem. Especificamente, o endpoint `/posts` é consumido para obter uma lista de postagens.

- **Endpoint:** `https://jsonplaceholder.typicode.com/posts`
- **Método:** `GET`
- **Dados Consumidos:** `title` e `body` de cada postagem.

Como esta é uma aplicação CLI, não há uma interface web interativa para deploy direto em plataformas como GitHub Pages. O link acima direciona para o repositório onde todo o código e a documentação estão disponíveis.

## 🤝 Contribuição

Contribuições são bem-vindas! Para propor melhorias ou correções, por favor, siga o fluxo de trabalho de Pull Request:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/sua-feature`).
3. Faça suas alterações e adicione testes, se aplicável.
4. Commit suas mudanças (`git commit -m 'feat: adicione nova funcionalidade'`).
5. Faça push para a branch (`git push origin feature/sua-feature`).
6. Abra um Pull Request para a branch `main`.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. (Nota: O arquivo LICENSE não foi criado neste SOP, mas é uma boa prática incluí-lo.)
