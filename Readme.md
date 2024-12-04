# Azure Cognitive Search: Indexação e Consulta de Dados com AI Search

## Descrição do Projeto  
Este projeto demonstra como usar o Azure Cognitive Search para indexar e consultar dados utilizando inteligência artificial. Criamos um conjunto de dados fictício em JSON e mostramos como indexá-lo e realizar buscas inteligentes.

## Tecnologias Utilizadas  
- **Azure Cognitive Search**  
- **Python 3.x**  
- **Azure SDK for Python**  

## Configuração do Azure Cognitive Search  

### 1. Criar Serviço de Pesquisa  
1. Acesse o [Portal do Azure](https://portal.azure.com/).
2. Crie um novo recurso de **Azure Cognitive Search**.
3. Forneça um nome para o serviço e escolha a região.
4. Selecione uma camada de preços adequada para suas necessidades.

### 2. Criar um Índice  
1. No portal, vá até **Index Management** e clique em **Create Index**.
2. Configure o índice com as seguintes propriedades:

```json
{
  "name": "products-index",
  "fields": [
    { "name": "id", "type": "Edm.String", "key": true },
    { "name": "name", "type": "Edm.String", "searchable": true },
    { "name": "description", "type": "Edm.String", "searchable": true },
    { "name": "category", "type": "Edm.String", "facetable": true },
    { "name": "price", "type": "Edm.Double", "sortable": true }
  ]
}
