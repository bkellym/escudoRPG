# ⚔️ Escudo RPG

Aplicação Web desenvolvida com Django e Materialize, utilizando o servidor Heroku.

Acesse aqui: [EscudoRPG](https://escudorpg.herokuapp.com/ "EscudoRPG")

### 📝 Resumo

Essa aplicação tem como objetivo funcionar como um "Escudo de Mestre", ou seja, reunindo regras importantes e informações rápidas de acordo com o livro base do sistema de RPG, a principio é focado apenas em dois sistemas:
- Vampiro a Máscara
- O Chamado de Cthulhu

#####Tendo o ponto de vista de dois tipos de usuários

* **Narrador:** Terá acesso à uma visão da mesa, e de como estão os personagens dos jogadores, seus pontos de vida, sangue/sanidade. Poderá criar fichas resumidas para os NPCs, criar cenas para cada personagem, entre outras funcionalidades.

* **Jogadores:** Poderá participar de mesas, criar seu personagem, a própria aplicação lhe dará resumos sobre o que cada atributo/habilidade representa no jogo, durante o jogo terá acesso com fácil visualização de sua ficha e com resumos das disciplinas, além de em campanhas ter auxílio para distribuição dos pontos Bônus e de XP.

### 🖥️ Desenvolvimento

O desenvolvimento desta aplicação está sendo feita por dois estudantes de Sistemas e Mídias Digitais, com o intuito de auxiliar a narração de RPG de mesa online, focado principalmente no storytelling, e pensado dentro do cenário da quarentena onde os encontros pessoalmente eram impossibilitados, mas se estende para outros como a possibilidade de pessoas de estados diferentes jogarem com uma melhor dinâmica.

---
### Primeiros Passos:

É necessário antes de tudo, realizar a instalação dos pré-requisitos, e após isso temos também as ferramentas recomendadas que auxiliarão na visualização e deploy da aplicação.

> Obs.: Os frameworks são apenas para documentação, não é necessário realizar o download deles.

#### 📌 Pré-requisitos:

* [Git](https://git-scm.com/downloads "Git")
* [Python 3.8](https://www.python.org/downloads/ "Python 3.8")
* [Django](https://www.djangoproject.com/start/ "Django")

#### 🔨 Ferramentas:

* [Pycharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows "Pycharm")
* [Sublime Merge](https://www.sublimemerge.com/ "Sublime Merge")

##### 📕 Frameworks:

* [Materialize](https://materializecss.com/getting-started.html "Materialize")
* [pytest](https://docs.pytest.org/en/latest/getting-started.html "pytest")

---

##### 🧬 Clonando Repositório:

Escolha um diretório de sua preferência, abra o git bash e execute o seguinte comando:

	git clone https://github.com/bkellym/escudoRPG

Caso queira clonar apenas uma branch específica:

	git clone -b develop  https://github.com/bkellym/escudoRPG


##### 🗄️ Criando seu próprio banco:

Caso não queira utilizar o banco de testes SQLite que vem no projeto, basta excluir o arquivo "db.sqlite3", e o conteúdo da pasta migrations dentro de core.

Depois execute estes comandos no terminal:

	python manage.py makemigrations
	python manage.py migrate

##### 🎬 Rodando a aplicação localmente:

Por fim, você pode agora rodar a aplicação na sua máquina e realizar as alterações que desejar, e ver o resultado delas em tempo real, para isso execute no terminal:

	python manage.py runserver
