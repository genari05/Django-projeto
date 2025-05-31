# Projeto Django - Formulário e Gerenciamento de Produtos

Este projeto é uma aplicação web desenvolvida em Django para gerenciar produtos e um formulário de contato. O sistema possui funcionalidades para cadastro de produtos, upload de imagens, e um formulário de contato funcional.

## Funcionalidades

- Cadastro, edição e visualização de produtos.
- Upload de imagens para os produtos (utilizando Pillow).
- Formulário de contato com validação.
- Integração com banco de dados MySQL.
- Interface básica usando Bootstrap para responsividade.

## Requisitos

- Python 3.12+
- Django 5.2.1
- MySQL (com database `django2` criado e configurado)
- Biblioteca Pillow para manipulação de imagens
- mysqlclient para conexão com MySQL
- Bootstrap (via CDN ou instalação local)

## Configuração do Ambiente

1. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
