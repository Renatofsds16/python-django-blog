# Blog - Plataforma Web com Django

Este projeto é uma aplicação web de blog desenvolvida com Django, com o objetivo de permitir a criação, edição e publicação de conteúdos de forma simples e organizada. A aplicação foi construída seguindo boas práticas de desenvolvimento backend e estruturação de projetos web.

O sistema possibilita a gestão de postagens, autenticação de usuários e exibição dinâmica de conteúdo, sendo ideal para aprendizado e evolução em desenvolvimento web com Django.

## Visão Geral

O Blog oferece uma interface intuitiva para leitura de conteúdos e uma área administrativa para gerenciamento das postagens.

## Funcionalidades

- Criação, edição e exclusão de posts
- Listagem de artigos em ordem cronológica
- Página de detalhes de cada postagem
- Sistema de autenticação (login e logout)
- Área administrativa para gerenciamento de conteúdo
- Organização de posts por categorias (se implementado)
- Suporte a imagens nas postagens (se implementado)

## Tecnologias Utilizadas

- Python
- Django
- SQLite 
- HTML5
- CSS3
- JavaScript

## Estrutura do Projeto


## Como Executar o Projeto

### Pré-requisitos

- Python 3.8+
- pip
- virtualenv (recomendado)

### 1. Clone o repositório

```bash
git clone https://github.com/Renatofsds16/blog.git

cd blog
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
