import requests
from datetime import datetime
import json
import concurrent.futures
from threading import Lock
from pathlib import Path
from dotenv import load_dotenv
import os   
load_dotenv()


base_url = "https://bancoartico-odata-standard.qprof.com.br"
auth = {'Authorization': f'Bearer {os.getenv('TOKEN')}'}
def dataForHtml():
    return f'{int(datetime.now().day - 1)}/{datetime.now().month}/{datetime.now().year}'
data_atual = datetime.now().strftime("%Y-%m-%dT%H:%M:%S-03:00")
def data_d_menos_1():
    from datetime import datetime
    data_atual = datetime.now().strftime("%Y-%m-%dT%H:%M:%S-03:00") # data de hj
    numero_dia = (data_atual.split(':')[0].split('-')[2][:2]) # pego o dia da data de hj
    dia_anterior = (int(numero_dia) - 1) if int(numero_dia) > 10 else f'0{int(numero_dia) - 1}' # pego o dia de hj e subtraio menos 1, que é o que ja venceu
    data_vencidos = f"{(data_atual.split(':')[0][:8])}{dia_anterior}{data_atual[10:]}" # data completa com o que ta vencido
    return data_vencidos



cedentes_email = [
    {
    "nome": "Multiplus",
    "codigo_pessoa":412,
    "email" :"pedro.rogel@articocapital.com.br" 
    },
    {
    "nome": "Tx platico",
    "codigo_pessoa":15039,
    "email" :"pedro.rogel@articocapital.com.br" #"guilherme@ambientalloma.com.br"
    },
    {
    "nome": "Casa do Café",
    "codigo_pessoa": 20515,
    "email" :"pedro.rogel@articocapital.com.br" 
    },
    {
    "nome": "Soma",
    "codigo_pessoa":781,
    "email" :"pedro.rogel@articocapital.com.br" #"guilherme@ambientalloma.com.br"
    },
    {
    "nome": "Raposo",
    "codigo_pessoa":10984,
    "email" :"pedro.rogel@articocapital.com.br" #"andre@raposoplasticos.com.br"
    },
    {
    "nome": "New Power",
    "codigo_pessoa":5705,
    "email" :"pedro.rogel@articocapital.com.br" #["daniela.vac@fulguris.com.br", "gabriela.oliveira@fulguris.com.br"]
    },
    {
    "nome": "MCM",
    "codigo_pessoa":1542,
    "email" :"pedro.rogel@articocapital.com.br" #["eder.leonel@mcm.ind.br", "l.bussola@bxgroup.com.br", "fernando.ribeiro@mcm.ind.br", "jussara.garcia@mcm.ind.br", "tamiris.quirino@mcm.ind.br"]
    },
    {
    "nome": "Laticínios Latco",
    "codigo_pessoa":1931,
    "email" :"pedro.rogel@articocapital.com.br" #"supervisorfinanceiro@latco.com.br"
    },
    {
    "nome": "KF Embalagens",
    "codigo_pessoa":6313,
    "email" :"pedro.rogel@articocapital.com.br" #"luiz@kfembalagens.com.br"
    },
    {
    "nome": "Green Packing",
    "codigo_pessoa":17122,
    "email" :"pedro.rogel@articocapital.com.br" #["victorhugocugi@yahoo.com.br", "margutti1960@gmail.com"]
    },
    {
    "nome": "Rainha da Paz",
    "codigo_pessoa":5705,
    "email" :"pedro.rogel@articocapital.com.br" #["pamela.carvalho@rpfgroup.com.br", "joao.almeida@rpfgroup.com.br", "luana.pinheiro@rpfgroup.com.br", "heloisa.belanson@rpfgroup.com.br", "pedro.takahashi@rpfgroup.com.br"]
    },
    {
    "nome": "Detallia Fitas",
    "codigo_pessoa":18431,
    "email" :"pedro.rogel@articocapital.com.br" #"alex.lacerda@fitasprogresso.com.br"
    },
    {
    "nome": "Condex",
    "codigo_pessoa":460,
    "email" :"pedro.rogel@articocapital.com.br" #["cobranca@condexcabos.com.br", "vendas@condexcabos.com.br"]
    },
    {
    "nome": "Combrasil",
    "codigo_pessoa":796,
    "email" :"pedro.rogel@articocapital.com.br" #"cobranca@combrasil.com"
    },
    {
    "nome": "Bronzearte",
    "codigo_pessoa":27,
    "email" :"pedro.rogel@articocapital.com.br" #"tesouraria@bronzearte.com.br"
    },
    {
    "nome": "Brasil Sul",
    "codigo_pessoa":185,
    "email" :"pedro.rogel@articocapital.com.br" #["contasareceber@brasilsulpescados.com.br", "financeiro@brasilsulpescados.com.br", "l.rocha@bxgroup.com.br", "v.azevedo@bxgroup.com.br"]
    },
    {
    "nome": "Bluecom",
    "codigo_pessoa":1175,
    "email" :"pedro.rogel@articocapital.com.br" #"diego.cartizani@fostercapital.com.br"
    },
    {
    "nome": "Amazonas",
    "codigo_pessoa":396,
    "email" :"pedro.rogel@articocapital.com.br" #"brunareis@amazonas.com.br"
    },
    {
    "nome": "Agroman",
    "codigo_pessoa":20515,
    "email" :"pedro.rogel@articocapital.com.br" #"adrien.mateus@agroman.ind.br"
    },
    {
    "nome": "Pontual Farmacêutica",
    "codigo_pessoa":19710,
    "email" :"pedro.rogel@articocapital.com.br" #"elionaldo.freitas@farmapontual.com"
    },
    {
    "nome": "Pricemet",
    "codigo_pessoa":7810,
    "email" :"pedro.rogel@articocapital.com.br" #["financeiro@pricemet.com.br", "jorge.ortiz@pricemet.com.br", "luana.ortiz@pricemet.com.br"]
    },
    {
    "nome": "Propel",
    "codigo_pessoa":16274,
    "email" :"pedro.rogel@articocapital.com.br" #"yeda.santos@propel.com.br"
    },
    {
    "nome": "Nutriplant",
    "codigo_pessoa":3798,
    "email" :"pedro.rogel@articocapital.com.br" #["agatha.noriller@nutriplant.com.br"," contasareceber@nutriplant.com.br", "leticia.zanele@nutriplant.com.br", "contasapagar@nutriplant.com.br"]
    },
    ]

# Cache para evitar requisições repetidas
cnpj_cache = {}
encargos_cache = {}
cache_lock = Lock()


def data_format(data):
    """Versão mais eficiente da formatação de data"""
    try:
        return f"{data[8:10]}/{data[5:7]}/{data[0:4]}"
    except:
        return data

def valor_encargos(codigo_pessoa):
    """Com cache para evitar requisições repetidas"""
    with cache_lock:
        if codigo_pessoa in encargos_cache:
            return encargos_cache[codigo_pessoa]
    
    url = f'{base_url}/ContaCorrenteCedente?$select=VALOR_ENCARGOS&$filter=CODIGO_PESSOA eq {codigo_pessoa} and VALOR_ENCARGOS ne null'
    
    
    try:
        request = requests.get(url, headers=auth, timeout=10)
        if request.status_code == 200:
            data = request.json()
            with cache_lock:
                encargos_cache[codigo_pessoa] = data
            return data
    except requests.exceptions.Timeout:
        print(f"Timeout ao buscar encargos para pessoa {codigo_pessoa}")
    return None

def pessoaJuridica(codigo_pessoa):
    """Com cache e tratamento de erro"""
    with cache_lock:
        if codigo_pessoa in cnpj_cache:
            return cnpj_cache[codigo_pessoa]
    
    url = f'{base_url}/PessoaJuridica?$select=CODIGO_PESSOA,NUMERO_EST_CNPJ,NUMERO_FILIAL_CNPJ,DIGITO_CNPJ&$top=1&$filter=CODIGO_PESSOA eq {codigo_pessoa}'
    
    try:
        request = requests.get(url, headers=auth, timeout=10)
        if request.status_code == 200:
            data = request.json()
            if data['value']:
                cnpj = formatar_cnpj(data['value'][0])
                with cache_lock:
                    cnpj_cache[codigo_pessoa] = cnpj
                return cnpj
    except requests.exceptions.Timeout:
        print(f"Timeout ao buscar CNPJ para pessoa {codigo_pessoa}")
    
    return None

def formatar_cnpj(dados):
    """Função separada para formatação do CNPJ"""
    if not dados:
        return None
    
    est = dados.get('NUMERO_EST_CNPJ')
    fil = dados.get('NUMERO_FILIAL_CNPJ')
    dig = dados.get('DIGITO_CNPJ')
    
    if est is None or fil is None or dig is None:
        return None
    
    est_padded = str(est).zfill(8)
    fil_padded = str(fil).zfill(4)
    dig_padded = str(dig).zfill(2)
    
    return f"{est_padded[:2]}.{est_padded[2:5]}.{est_padded[5:8]}/{fil_padded}-{dig_padded}"


def processar_titulo_paralelo(titulo):
    """Processa um título em paralelo"""
    codigo_pessoa_sacado = titulo.get("PessoaSacado", {}).get("CODIGO_PESSOA")
    nome_pessoa_cedente = titulo.get("PessoaCedente", {}).get("NOME_PESSOA")
    
    # Buscar CNPJ e encargos em paralelo (dentro da mesma thread)
    cnpj = pessoaJuridica(codigo_pessoa_sacado)
    
    valor_encargos_total = titulo.get("VALOR_CORRIGIDO_VENCIDO", 0) - titulo.get("VALOR_ABERTO", 0)
    
    return {
        "VENCIMENTO": data_format(titulo.get("DATA_VENCIMENTO_REAL")),
        "CNPJ": cnpj,
        "CODIGO_PESSOA": codigo_pessoa_sacado,
        "NOME_SACADO": titulo.get("PessoaSacado", {}).get("NOME_PESSOA") if titulo.get("PessoaSacado") else None,
        "NOME_CEDENTE": nome_pessoa_cedente,
        "NUMERO_TITULO": titulo.get("NUMERO_TITULO"),
        "DESCRICAO_ROTULO_GRUPO": (titulo.get("Rotulo") and titulo["Rotulo"].get("RotuloGrupo", {}).get("DESCRICAO") or "DESCONTO"),
        "VALOR_FACE": titulo.get("VALOR_FACE"),
        "VALOR_BAIXADO": titulo.get("VALOR_BAIXADO"),
        "VALOR_DESCONTO": titulo.get("VALOR_DESCONTO"),
        "VALOR_CORRIGIDO_VENCIDO": titulo.get("VALOR_CORRIGIDO_VENCIDO"),
        "VALOR_ENCARGOS": valor_encargos_total,
        # "EMAIL_PESSOA_CEDENTE" : 0, #titulo.get("PessoaCedente", {}).get("EMAIL_PESSOA"),
        "PRESENTE_DEVIDO": titulo.get("VALOR_PRESENTE"),
        "SITUACAO_PROTESTO": titulo.get("SITUACAO_PROTESTO")
    }

def carregar_dados_odata(codigo_cedente):
    """Versão otimizada com processamento paralelo"""
    filters = [
        "CODIGO_EMPRESA eq 1",
        "CODIGO_SITUACAO_TITULO eq 1", 
        "TIPO_COBRANCA ne 2",
        "TIPO_COBRANCA ne 9",
        "VALOR_ABERTO gt 0",
        f"PessoaCedente/CODIGO_PESSOA eq {codigo_cedente}",
        "CODIGO_ESTAGIO_TITULO eq 6",
        f"DATA_VENCIMENTO_REAL le {data_d_menos_1()}",
    ]
    
    filter_query = " and ".join(filters)
    
    select_columns = [
        "NUMERO_TITULO",
        "VALOR_FACE", 
        "VALOR_BAIXADO",
        "VALOR_ABERTO",
        "VALOR_PRESENTE",
        "VALOR_DESCONTO",
        "VALOR_CORRIGIDO_VENCIDO",
        "DATA_VENCIMENTO_REAL",
        "SITUACAO_PROTESTO"   
    ]
    
    select_query = ",".join(select_columns)
    
    url = f"{base_url}/titulo?$select={select_query}&$filter={filter_query}&$expand=PessoaCedente($select=CODIGO_PESSOA,NOME_PESSOA,EMAIL_PESSOA),PessoaSacado($select=CODIGO_PESSOA,NOME_PESSOA),Rotulo($select=CODIGO_ROTULO;$expand=RotuloGrupo($select=CODIGO_GRUPO_ROTULO,DESCRICAO))"

    try:
        response = requests.get(url, headers=auth, timeout=30)
        if response.status_code != 200:
            print(f"Erro na requisição principal: {response.status_code}")
            return []
        
        data = response.json()
        
        if not data.get('value'):
            return []
        
        # Processar títulos em paralelo
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            titulos_processados = list(executor.map(processar_titulo_paralelo, data['value']))
        
        return titulos_processados
        
    except requests.exceptions.Timeout:
        print("Timeout na requisição principal")
        return []
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []
    
    
    
def gerar_html_tabela(dados_titulos):
    """Gera uma tabela HTML com os dados dos títulos"""
    
    def formatar_moeda(valor):
        if valor is None:
            return "0,00"
        return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    total_titulos = len(dados_titulos)
    valor_total = sum(titulo.get('VALOR_CORRIGIDO_VENCIDO', 0) or 0 for titulo in dados_titulos)
    
    linhas = []
    qtd_desc=0
    qtd_intercompany=0
    qtd_nc =0
    qtd_boletoEscrow = 0
    qtd_comisaria = 0
    
    for item in dados_titulos:
        valor_face = item.get('VALOR_FACE', 0) or 0
        valor_encargos = item.get('VALOR_ENCARGOS', 0) or 0
        desconto_abatido = item.get('VALOR_DESCONTO', 0) or 0
        v_baixa = item.get('VALOR_BAIXADO', 0) or 0
        corrigido = item.get('VALOR_CORRIGIDO_VENCIDO', 0) or 0
        v_devido = item.get('PRESENTE_DEVIDO')
        nome_cedente = item.get('NOME_CEDENTE')
        
        if item.get('DESCRICAO_ROTULO_GRUPO') == 'DESCONTO':
            qtd_desc += 1
        elif item.get('DESCRICAO_ROTULO_GRUPO') == 'NOTA COMERCIAL':
            qtd_nc += 1
        elif item.get('DESCRICAO_ROTULO_GRUPO') == 'COMISSÁRIA':
            qtd_comisaria += 1
        elif item.get('DESCRICAO_ROTULO_GRUPO') == 'INTERCOMPANY':
            qtd_intercompany += 1
        elif item.get('DESCRICAO_ROTULO_GRUPO') == 'BOLETO ESCROW':
            qtd_boletoEscrow += 1
        
        
        
        linha = f"""
        <tr>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0;">{item.get('VENCIMENTO', '-')}</td>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0; font-family: 'Courier New', monospace; font-size: 11px;">{item.get('CNPJ', '-')}</td>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0;">{item.get('NOME_SACADO', '-')}</td>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0;">{item.get('NUMERO_TITULO', '-')}</td>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0;">{item.get('DESCRICAO_ROTULO_GRUPO', '-')}</td>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0;">{item.get('SITUACAO_PROTESTO', '-') or ''}</td>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0;">{formatar_moeda(valor_face)}</td>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0;">{formatar_moeda(desconto_abatido)}</td>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0;">{formatar_moeda(v_baixa)}</td>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0;">{formatar_moeda(v_devido)}</td>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0;">{formatar_moeda(valor_encargos)}</td>
            <td style="padding: 8px 6px; border-bottom: 1px solid #e0e0e0; text-align: right; font-family: 'Courier New', monospace; font-weight: bold;">R$ {formatar_moeda(corrigido)}</td>
        </tr>
        """
        linhas.append(linha)
    
    # Definir conteúdo da tabela baseado se há dados ou não
    if not linhas:
        linhas_tabela = '<tr><td colspan="11" style="text-align: center; padding: 20px; color: #7f8c8d;">Nenhum título vencido encontrado</td></tr>'
        rodape_tabela = ''
    else:
        linhas_tabela = ''.join(linhas)
        # Rodapé com totais
        rodape_tabela = f"""
        <tfoot>
            <tr style="background-color: #f5e8e8 !important; font-weight: bold; border-top: 2px solid #f2a7a7;">
                <td colspan="11" style="padding: 12px 6px; border-bottom: 1px solid #e0e0e0;">
                    <strong>TOTAL GERAL ({total_titulos} títulos)</strong>
                </td>
                <td style="padding: 12px 6px; border-bottom: 1px solid #e0e0e0; text-align: right; font-family: 'Courier New', monospace; font-weight: bold;">
                    R$ {formatar_moeda(valor_total)}
                </td>
            </tr>
        </tfoot>
        """
    
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Relatório de Títulos Vencidos</title>
    </head>
    <body style="margin: 0; padding: 20px; background-color: #f5f5f5; font-family: Arial, sans-serif;">
        <div style="margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <!-- Cabeçalho -->
                       <div style="background: #080056; color: white; padding: 20px; text-align: center;">
                <h1 style="margin: 0; font-size: 20px; font-weight: bold;">Relatório de Títulos Vencidos</h1>
                
            </div>
     
            <!-- Informações gerais -->
      
        <div
          style="
            background-color: #f8f9fa;
            padding: 15px;
            border-left: 4px solid #3498db;
            margin: 15px;
            border-radius: 4px;
          "
        >
          <strong>Cedente:</strong> {nome_cedente}<br />
          <strong>Data do relatório:</strong> {dataForHtml()}<br />
          <strong>Total de títulos:</strong> {total_titulos} |
          <strong>Valor total:</strong> R$ {formatar_moeda(valor_total)} </br>
          {f'<strong>Quantidade de Descontos:</strong> {qtd_desc or ''} </br>' if qtd_desc != 0 or qtd_desc > 0 else ''}
          {f'<strong>Quantidade de Intercompany:</strong> {qtd_intercompany or ''} </br>' if qtd_intercompany != 0 or qtd_intercompany > 0 else ''}
          {f'<strong>Quantidade de Boletos Escrow:</strong> {qtd_boletoEscrow or ''} </br>' if qtd_boletoEscrow != 0 or qtd_boletoEscrow > 0 else ''}
          {f'<strong>Quantidade de Comissária:</strong> {qtd_comisaria or ''} </br>' if qtd_comisaria != 0 or qtd_comisaria > 0 else ''}
         { f'<strong>Quantidade de Notas Comerciais:</strong> {qtd_nc or ''} </br>' if qtd_nc != 0 or qtd_nc > 0 else ''}
          
        </div>
     
            
            <!-- Tabela -->
            <div style="padding: 0 15px 15px 15px;">
                <table style="width: 100%; border-collapse: collapse; font-size: 12px;">
                    <thead>
                        <tr>
                            <th style="background-color: #080056; color: white; padding: 10px 6px; text-align: left; font-weight: bold; border-bottom: 2px solid #2c3e50;">Vencimento</th>
                            <th style="background-color: #080056; color: white; padding: 10px 6px; text-align: left; font-weight: bold; border-bottom: 2px solid #2c3e50;">CNPJ</th>
                            <th style="background-color: #080056; color: white; padding: 10px 6px; text-align: left; font-weight: bold; border-bottom: 2px solid #2c3e50;">Sacado</th>
                            <th style="background-color: #080056; color: white; padding: 10px 6px; text-align: left; font-weight: bold; border-bottom: 2px solid #2c3e50;">Título</th>
                            <th style="background-color: #080056; color: white; padding: 10px 6px; text-align: left; font-weight: bold; border-bottom: 2px solid #2c3e50;">Rotulo</th>
                            <th style="background-color: #080056; color: white; padding: 10px 6px; text-align: left; font-weight: bold; border-bottom: 2px solid #2c3e50;">Sit. Prot</th>
                            <th style="background-color: #080056; color: white; padding: 10px 6px; text-align: left; font-weight: bold; border-bottom: 2px solid #2c3e50;">V. Face</th>
                            <th style="background-color: #080056; color: white; padding: 10px 6px; text-align: left; font-weight: bold; border-bottom: 2px solid #2c3e50;">Desc. Abat</th>
                            <th style="background-color: #080056; color: white; padding: 10px 6px; text-align: left; font-weight: bold; border-bottom: 2px solid #2c3e50;">V. Baixa</th>
                            <th style="background-color: #080056; color: white; padding: 10px 6px; text-align: left; font-weight: bold; border-bottom: 2px solid #2c3e50;">V. Devido</th>
                            <th style="background-color: #080056; color: white; padding: 10px 6px; text-align: left; font-weight: bold; border-bottom: 2px solid #2c3e50;">Encargos</th>
                            <th style="background-color: #ff0000a5; color: white; padding: 10px 6px; text-align: right; font-weight: bold; border-bottom: 2px solid #2c3e50;">Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        {linhas_tabela}
                    </tbody>
                    {rodape_tabela}
                </table>
            </div>
            
         
           
        </div>
    </body>
    </html>
    """
    
    return html

    
def salvar_html_local(html_content, nome_arquivo="relatorio_titulos.html"):
    """Salva o HTML na mesma pasta do script atual"""
    
    # Obter o diretório do script atual
    diretorio_atual = Path(__file__).parent
    
    # Caminho completo do arquivo
    caminho_arquivo = diretorio_atual / nome_arquivo
    
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Arquivo salvo com sucesso: {caminho_arquivo}")
        return True
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")
        return False
    
    
    
import requests
import json
from msal import ConfidentialClientApplication

def registrar_e_enviar_email(dados, nome_cedente):
    tenant_id =  os.getenv('TENANT_ID')  
    client_id = os.getenv('CLIENT_ID')  
    client_secret = os.getenv('CLIENT_SECRET')  # Certificates & secrets
    
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    
    # Criar aplicação
    
    app = ConfidentialClientApplication(
        client_id=client_id,
        client_credential=client_secret,
        authority=authority,
    )
    
    
    print("Obtendo token de acesso...")
    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    
    if "access_token" in result:
        access_token = result['access_token']
        print("✅ Token obtido com sucesso!")
        
        # Enviar email
        url = "https://graph.microsoft.com/v1.0/users/felipe.duarte@articocapital.com.br/sendMail"
        
        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json'
        }
        
        email_data = {
            "message": {
                "subject": f"RE: Vencidos {nome_cedente} x Ártico Capital ",
                "body": {
                    "contentType": "HTML",
                    "content": f"Prezados(as), bom dia! <br><br> Tudo bem? <br><br> Segue abaixo relatório de vencidos.<br><br> {gerar_html_tabela(dados)}"
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": "pedro.rogel@articocapital.com.br"
                        }
                    },
                    {
                        "emailAddress": {
                            "address": "felipe.duarte@articocapital.com.br"
                        }
                    }
                ]
            },
            "saveToSentItems": "true"
        }
        
        print("Enviando email...")
        response = requests.post(url, headers=headers, json=email_data)
        
        if response.status_code == 202:
            print("✅ Email enviado com sucesso via Graph API!")
        else:
            print(f"❌ Erro no envio: {response.status_code}")
            print(f"Detalhes: {response.text}")
    else:
        print(f"❌ Falha na autenticação: {result.get('error_description')}")
    

def mandar_email_cada_cedente():
    for i in cedentes_email:
        dados = carregar_dados_odata(i['codigo_pessoa'])
        if not dados:
            print(f"Sem titulos vencidos para a empresa {i['nome']}")
        else:
            salvar_html_local(gerar_html_tabela(dados))
            registrar_e_enviar_email(dados, i['nome'])
    
   



 
if __name__ == "__main__":
    dados = carregar_dados_odata(17122)
    mandar_email_cada_cedente()
    salvar_html_local(gerar_html_tabela(dados))
    # print(json.dumps(dados, indent=2))
   
    
    
    
