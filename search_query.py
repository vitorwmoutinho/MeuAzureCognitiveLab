from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# Substitua pelos seus valores do serviço Azure
endpoint = "https://SEU_SERVICO.search.windows.net"
api_key = "SUA_API_KEY"
index_name = "products-index"

# Inicializando o cliente de busca
search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCredential(api_key))

def search_products(query):
    results = search_client.search(search_text=query)
    for result in results:
        print(f"Produto: {result['name']}, Descrição: {result['description']}, Preço: {result['price']}")

# Pesquisa de exemplo: buscando "laptop"
search_products("laptop")
