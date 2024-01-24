# Gerenciador de Visitantes

###  Desenvolvido seguindo o curso "Django framework na prática" na plataforma Udemy.

O projeto tem como objetivo informatizar o processo de registro e administração de visitantes de um condomínio via 
páginas web, onde é possível registrar visitantes, visualizar suas informações e atualizar o status de sua visita 
(aguardando autorização de entrada, em visita e visita finalizada).

Para fins de testes, o projeto acompanha um banco sqlite preenchido com usuários, porteiros e visitantes. Para logar
nessa versão de teste basta utilizar as credenciais:

 - Login: ian@gmail.com
 - Senha: root

## Principais funcionalidades

### Registro de visitantes

O formulário de registro de visitantes deve abstrair a etapa 01 do processo, onde o visitante informa **nome completo**,
**CPF**, **data de nascimento**, o **número da casa** que deseja visitar e ainda a **placa do veículo**, se estiver 
utilizando durante a visita. Além desta informações, o formulário salva o **horário de chegada** do visitante 
automaticamente.

### Listagem de visitantes

A listagem de visitantes exibe, por meio de uma tabela, os visitantes recentes classificados por horário de chegada, 
do mais recente para o mais antigo.

### Widgets para resumo de informações

O widgets da página inicial da dashboard têm a função de exibir um resumo dos números referentes aos visitantes em cada
status e ainda o número total de visitantes registrados no mês.

### Visualização de informações de visitante

A partir da tabela que lista os visitantes recentes, é possível acessar a página que exibe as informações detalhadas de
cada visitante.

### Autorização de entrada

Quando um visitante está aguardando autorização, o botão para autorizar a entrada fica disponível na tela de informações
deste visitante e, para autorizar a entrada, basta clicar no botão para abrir o formulário que deve ser preenchido com o
nome do morador que autorizou a entrada do visitante e confirmar a ação. O horário da autorização é salvo de forma 
automática.

### Finalização de visita

Assim como conseguimos utilizar a funcionalidade para autorizar a entrada do visitante, podemos finalizar sua visita.
Ao clicar no botão para finalizar uma visita, um alerta é exibido solicitando que o porteiro confirme a ação.

Os botões "autorizar entrada" e "finalizar visita" são exibidos somente quando é possível executar a ação para o
visitante em questão. Caso contrário, como quando o visitante já deixou as dependências do condomínio, nenhum botão
é exibido.

## Tecnologias utilizadas

Informação presente no arquivo "requirements.txt"

