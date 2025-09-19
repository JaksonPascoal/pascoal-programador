# 🚀 Guia de Deploy - Pascoal Programador

## 📋 Opções de Deploy

### **Opção 1: Deploy Rápido (Recomendado)**
Use o arquivo `app_standalone.py` que contém todas as funções necessárias:

1. **Streamlit Cloud:**
   - Faça upload do repositório no GitHub
   - Conecte com Streamlit Cloud (share.streamlit.io)
   - Configure:
     - **Main file**: `app_standalone.py`
     - **Requirements**: `requirements_deploy.txt`

2. **Heroku:**
   ```bash
   # Procfile
   web: streamlit run app_standalone.py --server.port=$PORT --server.address=0.0.0.0
   ```

3. **Railway/Render:**
   - Use `app_standalone.py` como ponto de entrada
   - Configure variáveis de ambiente se necessário

### **Opção 2: Deploy com Pacote Instalado**
Se quiser usar o arquivo `app.py` original:

1. **Instalar o pacote no ambiente de deploy:**
   ```bash
   pip install -e .
   ```

2. **Ou modificar o PYTHONPATH:**
   ```bash
   export PYTHONPATH="${PYTHONPATH}:/app/src"
   streamlit run app.py
   ```

## ⚠️ Problemas Comuns e Soluções

### **ModuleNotFoundError: No module named 'pasqalib'**

**Solução 1 (Recomendada):** Use `app_standalone.py`
- ✅ Não depende de instalação de pacote
- ✅ Funciona em qualquer ambiente
- ✅ Mais confiável para deploy

**Solução 2:** Corrigir imports no `app.py`
```python
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)
```

### **Dependências Pesadas**
Se houver problemas com scipy/plotly no deploy:
- Use `requirements_deploy.txt` (versão mínima)
- Comente as dependências opcionais

### **Port/Address Issues**
Use as configurações em `.streamlit/config.toml`

## 📁 Arquivos para Deploy

### **Essenciais:**
- `app_standalone.py` (aplicação principal)
- `requirements_deploy.txt` (dependências)
- `.streamlit/config.toml` (configurações)

### **Opcionais:**
- `app.py` (versão com imports do pacote)
- `src/` (código fonte do pacote)
- `requirements.txt` (dependências completas)

## 🔧 Comandos Úteis

```bash
# Testar localmente
streamlit run app_standalone.py

# Verificar dependências
pip list

# Instalar requirements específicos
pip install -r requirements_deploy.txt

# Debug de imports
python -c "import sys; print(sys.path)"
```

## ✅ Checklist de Deploy

- [ ] Testado localmente com `app_standalone.py`
- [ ] Configurado arquivo de requirements adequado
- [ ] Verificado se todas as dependências estão disponíveis
- [ ] Testado upload de CSV (se aplicável)
- [ ] Configurado variables de ambiente (se necessário)
- [ ] Verificado logs de erro no deploy

## 🌐 Plataformas Testadas

- ✅ **Streamlit Cloud** (share.streamlit.io)
- ✅ **Heroku**
- ⚠️ **Railway** (verificar dependências)
- ⚠️ **Render** (verificar timeout)

---

💡 **Dica:** Para deploy rápido e sem problemas, sempre use `app_standalone.py` + `requirements_deploy.txt`