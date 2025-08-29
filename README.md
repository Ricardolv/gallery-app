# Galeria de Fotos e Vídeos Django

Uma aplicação web moderna para gerenciar e exibir fotos e vídeos com interface responsiva usando Django, Tailwind CSS v4 e DaisyUI.

## 🚀 Funcionalidades

- ✅ Upload e gerenciamento de fotos e vídeos
- ✅ Interface moderna e responsiva com Tailwind CSS v4 + DaisyUI
- ✅ Carrossel interativo para navegação
- ✅ Reprodução de vídeo com controles
- ✅ Sistema de thumbnails automático
- ✅ Painel administrativo Django
- ✅ Endpoint de API para consulta de dados
- ✅ Suporte a múltiplos formatos (JPG, PNG, GIF, MP4, AVI, MOV, WEBM)

## 📋 Pré-requisitos

- Python 3.8+
- Node.js 16+ (para Tailwind CSS)
- pip (gerenciador de pacotes Python)

## 🛠 Instalação

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd gallery-app
```

> **Nota**: Este projeto inclui um arquivo `requirements.txt` com todas as dependências necessárias.

### 2. Crie e ative o ambiente virtual
```bash
python -m venv .venv

# No macOS/Linux:
source .venv/bin/activate

# No Windows:
.venv\Scripts\activate
```

### 3. Instale as dependências Python
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 6. Instale e configure o Tailwind CSS
```bash
python manage.py tailwind install
python manage.py tailwind build
```

### 7. Colete arquivos estáticos
```bash
python manage.py collectstatic --noinput
```

## 🚀 Execução

### Desenvolvimento
```bash
python manage.py runserver
```

A aplicação estará disponível em: **http://127.0.0.1:8000/**

### Compilação do Tailwind CSS (modo watch)
Em um terminal separado, para desenvolvimento com auto-reload do CSS:
```bash
python manage.py tailwind start
```

## 📁 Estrutura do Projeto

```
gallery-app/
├── core/                 # Configurações principais do Django
│   ├── settings.py      # Configurações da aplicação
│   ├── urls.py          # URLs principais
│   └── wsgi.py          # Configuração WSGI
├── gallery/             # App principal da galeria
│   ├── models.py        # Modelos de dados
│   ├── views.py         # Views da aplicação
│   ├── urls.py          # URLs da galeria
│   ├── admin.py         # Configuração do admin
│   └── templates/       # Templates HTML
├── theme/               # App do Tailwind CSS
│   ├── static_src/      # Arquivos fonte do CSS
│   └── static/          # CSS compilado
├── media/               # Arquivos de mídia uploadados
├── static/              # Arquivos estáticos
└── manage.py            # Script de gerenciamento Django
```

## 🎯 Uso da Aplicação

### Acessando a Galeria
1. Acesse http://127.0.0.1:8000/ para ver a página inicial
2. Navegue para http://127.0.0.1:8000/gallery/ para ver a galeria completa

### Adicionando Mídia
1. Acesse o painel administrativo: http://127.0.0.1:8000/admin/
2. Faça login com suas credenciais de superusuário
3. Vá para "Itens de Mídia" e clique em "Adicionar"
4. Preencha os campos e faça upload do arquivo
5. Marque "Destaque" se quiser que apareça na seção em destaque

### API
A aplicação inclui um endpoint de API:
- `GET /api/media/` - Lista todos os itens de mídia em formato JSON

Exemplo de resposta:
```json
{
  "media_items": [
    {
      "id": 1,
      "title": "Título do item",
      "description": "Descrição",
      "media_type": "image",
      "file_url": "/media/gallery/2025/08/29/arquivo.jpg",
      "thumbnail_url": "/media/gallery/thumbnails/2025/08/29/thumb.jpg",
      "is_featured": true
    }
  ]
}
```

## 🎨 Personalização

### Modificando Estilos
1. Edite os arquivos em `theme/static_src/src/`
2. Execute `python manage.py tailwind build` para recompilar
3. Execute `python manage.py collectstatic` para atualizar os arquivos estáticos

### Configurações
Principais configurações em `core/settings.py`:
- `MEDIA_URL` e `MEDIA_ROOT` - Configuração de arquivos de mídia
- `STATIC_URL` e `STATIC_ROOT` - Configuração de arquivos estáticos
- `TAILWIND_APP_NAME` - Configuração do Tailwind CSS

## 🔧 Solução de Problemas

### CSS não está sendo aplicado
```bash
python manage.py tailwind build
python manage.py collectstatic --noinput
```

### Erro de thumbnail
Certifique-se de que o Pillow está instalado:
```bash
pip install pillow
```

### Problemas com arquivos de mídia
Verifique se as pastas `media/` e `static/` têm permissões de escrita.

## 📝 Tecnologias Utilizadas

- **Backend**: Django 4.x
- **Frontend**: HTML5, JavaScript, Tailwind CSS v4
- **UI Components**: DaisyUI
- **Database**: SQLite (desenvolvimento)
- **Media Processing**: Pillow
- **Icons**: Font Awesome

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas, abra uma issue no repositório do projeto.

---

**Desenvolvido com ❤️ usando Django e Tailwind CSS**