Implemente um sistema para gerenciar um estoque de produtos. Cada produto deve ter as seguintes informações:
Nome do produto (String, obrigatório).
Código do produto (String, único, obrigatório).
Descrição (Texto longo, opcional).
Preço (Decimal com 2 casas decimais).
Quantidade em estoque (Número inteiro).
Data de criação (Registrada automaticamente).

Em seguida, registre o modelo na aplicação admin do django com as seguintes configurações:
Exiba na listagem os campos código, nome, preço, quantidade em estoque e data de criação;
Permita a busca do produto via código ou nome;
Permita a filtragem de dados via data de criação;
Ordene os itens por data de criação decrescente.
Os produtos devem ser cadastrados e gerenciados através da aplicação Django Admin. Cadastre pelo menos 5 produtos.
