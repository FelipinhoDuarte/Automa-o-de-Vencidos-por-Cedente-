# 📊 Sistema de Relatório de Títulos Vencidos

Sistema automatizado para consulta, geração de relatórios e envio de e-mails sobre títulos vencidos via API OData.

## 📋 Descrição

Este sistema consulta uma API OData do Ártico Capital para obter informações sobre títulos vencidos, gera relatórios em HTML e envia e-mails automatizados para os cedentes cadastrados.

## 🚀 Funcionalidades

- **Consulta em API OData** para obter títulos vencidos
- **Processamento paralelo** para melhor performance
- **Geração de relatórios HTML** formatados
- **Envio automático de e-mails** via Microsoft Graph API
- **Cache inteligente** para evitar requisições repetidas
- **Suporte a múltiplos cedentes** e e-mails

## 🛠️ Pré-requisitos

- Python 3.7+
- Conta Microsoft Azure com Graph API configurada
- Acesso à API OData do Banco Ártico
- Token de autenticação válido

## 📦 Dependências

```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

### 1. Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
TOKEN=seu_token_api_odata
TENANT_ID=seu_tenant_id_azure
CLIENT_ID=seu_client_id_azure
CLIENT_SECRET=seu_client_secret_azure
```

### 2. Configuração dos Cedentes

Edite a lista `cedentes_email` no código para incluir seus cedentes:

```python
cedentes_email = [
    {
        "nome": "Nome da Empresa",
        "codigo_pessoa": 12345,
        "email": "email@empresa.com"
    },
    # ... mais cedentes
]
```

## 🎯 Como Usar

### Execução Completa

```python
# Executa para todos os cedentes cadastrados
mandar_email_cada_cedente()
```

### Execução para Cedente Específico

```python
# Consulta dados de um cedente específico
dados = carregar_dados_odata(17122)

# Gera HTML do relatório
html = gerar_html_tabela(dados)

# Salva localmente
salvar_html_local(html)
```

### Envio de E-mail Individual

```python
registrar_e_enviar_email(dados, "Nome Cedente", "email@cedente.com")
```

## 📊 Estrutura do Relatório

O relatório HTML inclui:

- **Cabeçalho** com data e informações gerais
- **Tabela detalhada** com todos os títulos vencidos
- **Totais** por tipo de operação (Desconto, Intercompany, etc.)
- **Valores formatados** em Real brasileiro
- **Design responsivo** e profissional

## 🔧 Funções Principais

### `carregar_dados_odata(codigo_cedente)`
Consulta a API OData para obter títulos vencidos do cedente especificado.

### `gerar_html_tabela(dados_titulos)`
Gera o HTML formatado do relatório com os dados dos títulos.

### `registrar_e_enviar_email(dados, nome_cedente, email_cedente)`
Autentica e envia e-mail via Microsoft Graph API.

### `mandar_email_cada_cedente()`
Processa todos os cedentes cadastrados e envia e-mails.

## 🎨 Personalização

### Modificar Template HTML
Edite a função `gerar_html_tabela()` para alterar o layout do relatório.

### Adicionar Novos Cedentes
Inclua novos objetos na lista `cedentes_email` com a estrutura:
```python
{
    "nome": "Nome Empresa",
    "codigo_pessoa": 12345,  # ou lista [123, 456]
    "email": "email@empresa.com"  # ou lista de e-mails
}
```

### Modificar Filtros
Ajuste os filtros na função `carregar_dados_odata()` para diferentes critérios de consulta.

## ⚠️ Tratamento de Erros

- **Timeouts** são tratados com retry
- **Erros de autenticação** são logados
- **Dados ausentes** são substituídos por valores padrão
- **Falhas de e-mail** são reportadas no console

## 🔒 Segurança

- Tokens armazenados em variáveis de ambiente
- Autenticação via OAuth 2.0 Client Credentials
- Cache local para reduzir requisições
- Timeouts configurados para evitar travamentos

## 📈 Performance

- **Processamento paralelo** com ThreadPoolExecutor
- **Cache de CNPJ** e encargos para consultas repetidas
- **Limite de workers** para não sobrecarregar a API
- **Timeouts configuráveis** nas requisições

## 🐛 Solução de Problemas

### Erro de Autenticação
- Verifique as variáveis de ambiente
- Confirme as permissões no Azure AD
- Valide o token da API OData

### Timeouts na API
- Ajuste o parâmetro `timeout` nas requisições
- Verifique a conectividade de rede
- Considere aumentar o `max_workers`

### E-mails Não Enviados
- Confirme as permissões do Graph API
- Verifique os logs de erro do Azure
- Valide os endereços de e-mail

## 📄 Licença

Este projeto é para uso interno da Ártico Capital.

## 👥 Suporte

Para suporte técnico, contate a equipe de desenvolvimento.
