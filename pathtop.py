import os #importa o módulo os, que fornece uma maneira portátil de usar a funcionalidade dependente do sistema operacional, como ler ou escrever em um diretório.
import psutil #importa o módulo que permite acessar dados de uso de CPU e memória do processo
import subprocess #importa o módulo que permite a execução de comandos no teminal linux

def list_dirs(): #listar os diretórios em /proc
    #array que armazena os diretórios de /proc
    sysDirs = [f for f in os.listdir('/proc') if f.isdigit()] #função da biblioteca os que lista o diretorio do caminho que recebe em seu parâmetro

    dirs = []

    for pid in sysDirs:
        intPid = int(pid)
        if intPid > 1000: #Os PIDs de 1000 à baixo são relacionados ao sistem, as aplicações só se encontram acima disso
            dirs.append(pid)

    return dirs

def proc_stats(pid):
    process = psutil.Process(int(pid))

    # obter uso de CPU em porcentagem
    cpu_percent = process.cpu_percent(interval=1)

    # obter uso de memória RAM em bytes
    memory_info = process.memory_info()
    memory_usage = memory_info.rss
    print ('')
    print ("PID {}".format(pid))
    print(f"Uso de CPU: {cpu_percent:.2f}%")
    print(f"Uso de memória RAM: {memory_usage/1024/1024:.2f} MB")


def path_search(path): #procura os processos iniciados pelo binário em questão e exibe as métricas de cada um
    dirs = list_dirs() #obtém o array com os processos de interesse

    for pid in dirs: #estrutura para percorrer todo o array
        proc_path = f"/proc/{pid}/exe" #caminho para o arquivo que contém o caminho do binário que gerou o processo
        if os.path.exists(proc_path) and os.path.islink(proc_path): #se o caminho existir e o arquivo for um link simbólico
            bin_path = os.readlink(proc_path) #usa readlink para obter o caminho do binário a partir do link simbólico utilizando o comando 'readlink' do linux
            if bin_path == path: #compara a entrada do usuário com o caminho obtido
                proc_stats(pid) #chama a função que exibe as métricas do processo

path = str(input("Caminho do binário que gerou seu processo: "))
path_search(path)

