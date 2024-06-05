# Noise Reduction App

Este repositório contém uma aplicação de redução de ruído em tempo real que pode ser utilizada com qualquer aplicação de áudio no Windows.

## Estrutura do Projeto

noise_reduction_project/
├── src/
│ ├── dist/
│ │ └── noise_reduction.exe
│ └── noise_reduction.py
├── installer/
│ └── setup.iss
└── README.md



## Funcionalidades

- Redução de ruído em tempo real utilizando a biblioteca `noisereduce`.
- Interface gráfica simples utilizando `tkinter`.
- Controle deslizante para ajustar o nível de redução de ruído.
- Seleção de dispositivos de entrada e saída de áudio.

## Pré-requisitos

- Python 3.6 ou superior
- `pip` para gerenciamento de pacotes
- [VB-CABLE](https://www.vb-audio.com/Cable/) para roteamento de áudio virtual
- [Inno Setup](https://jrsoftware.org/isinfo.php) para criar o instalador

## Instalação

### 1. Clone o Repositório

```sh
git clone https://github.com/seu-usuario/noise-reduction.git
cd noise-reduction


python -m venv venv
venv\Scripts\activate  # No Windows
# source venv/bin/activate  # No MacOS/Linux

pip install -r requirements.txt


cd src
pyinstaller --onefile noise_reduction.py


4. Criar o Instalador com Inno Setup
Abra o Inno Setup, carregue o script installer/setup.iss, e clique em "Compile".

5. Configurar o Dispositivo de Áudio
Instale o VB-CABLE.
Configure "CABLE Output (VB-Audio Virtual Cable)" como dispositivo de entrada padrão no Windows.
Configure seu microfone real para enviar áudio para "CABLE Output (VB-Audio Virtual Cable)".
Configure "CABLE Input (VB-Audio Virtual Cable)" como o microfone padrão no Windows.
Uso
Execute o instalador gerado pelo Inno Setup para instalar a aplicação.
Abra a aplicação "Noise Reduction App".
Use o controle deslizante para ajustar o nível de redução de ruído.
Selecione os dispositivos de entrada e saída apropriados.
Clique em "Start" para iniciar a redução de ruído em tempo real.
Contribuição
Contribuições são bem-vindas! Por favor, abra um problema (issue) ou envie uma solicitação de pull request.

Licença
Este projeto está licenciado sob os termos da licença MIT.



Aqui está um exemplo de README.md adequado para o GitHub:

markdown
Copiar código
# Noise Reduction App

Este repositório contém uma aplicação de redução de ruído em tempo real que pode ser utilizada com qualquer aplicação de áudio no Windows.

## Estrutura do Projeto

noise_reduction_project/
├── src/
│ ├── dist/
│ │ └── noise_reduction.exe
│ └── noise_reduction.py
├── installer/
│ └── setup.iss
└── README.md

markdown
Copiar código

## Funcionalidades

- Redução de ruído em tempo real utilizando a biblioteca `noisereduce`.
- Interface gráfica simples utilizando `tkinter`.
- Controle deslizante para ajustar o nível de redução de ruído.
- Seleção de dispositivos de entrada e saída de áudio.

## Pré-requisitos

- Python 3.6 ou superior
- `pip` para gerenciamento de pacotes
- [VB-CABLE](https://www.vb-audio.com/Cable/) para roteamento de áudio virtual
- [Inno Setup](https://jrsoftware.org/isinfo.php) para criar o instalador

## Instalação

### 1. Clone o Repositório

```sh
git clone https://github.com/seu-usuario/noise-reduction.git
cd noise-reduction
2. Crie um Ambiente Virtual e Instale Dependências
sh
Copiar código
python -m venv venv
venv\Scripts\activate  # No Windows
# source venv/bin/activate  # No MacOS/Linux

pip install -r requirements.txt
3. Criar o Executável com PyInstaller
Navegue até o diretório src/ e execute:

sh
Copiar código
cd src
pyinstaller --onefile noise_reduction.py
4. Criar o Instalador com Inno Setup
Abra o Inno Setup, carregue o script installer/setup.iss, e clique em "Compile".

5. Configurar o Dispositivo de Áudio
Instale o VB-CABLE.
Configure "CABLE Output (VB-Audio Virtual Cable)" como dispositivo de entrada padrão no Windows.
Configure seu microfone real para enviar áudio para "CABLE Output (VB-Audio Virtual Cable)".
Configure "CABLE Input (VB-Audio Virtual Cable)" como o microfone padrão no Windows.
Uso
Execute o instalador gerado pelo Inno Setup para instalar a aplicação.
Abra a aplicação "Noise Reduction App".
Use o controle deslizante para ajustar o nível de redução de ruído.
Selecione os dispositivos de entrada e saída apropriados.
Clique em "Start" para iniciar a redução de ruído em tempo real.
Contribuição
Contribuições são bem-vindas! Por favor, abra um problema (issue) ou envie uma solicitação de pull request.

Licença
Este projeto está licenciado sob os termos da licença MIT.

Feito com ❤️ por Maycon Pacheco
