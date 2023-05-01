# PathTop


Este é um script Python que permite a busca por processos iniciados por um determinado binário e exibe algumas métricas de uso de CPU e memória para cada processo encontrado.

O script utiliza os módulos os, psutil e subprocess do Python. O módulo os é usado para listar os diretórios em /proc, o módulo psutil é usado para acessar dados de uso de CPU e memória do processo.

A função list_dirs() lista os diretórios em /proc que contém apenas números (que correspondem aos PIDs dos processos) e retorna um array com os PIDs dos processos que são do interesse do usuário (ou seja, os PIDs dos processos iniciados pelo binário em questão).

A função proc_stats(pid) recebe como parâmetro um PID de um processo e usa o módulo psutil para obter o uso de CPU e de memória RAM do processo. As métricas são exibidas na saída padrão.

A função path_search(path) recebe como parâmetro o caminho do binário que gerou o processo e usa a função list_dirs() para obter os PIDs dos processos que foram iniciados por esse binário. Em seguida, o script usa o módulo os para acessar o arquivo que contém o caminho do binário que gerou cada processo e compara esse caminho com o caminho fornecido pelo usuário. Se os caminhos forem iguais, a função proc_stats(pid) é chamada para exibir as métricas do processo correspondente.

Além de ser útil para monitorar métricas de processos em desenvolvimento, este código pode ser usado para monitorar processos em produção, desde que se tenha acesso ao caminho do binário que gerou os processos que se deseja monitorar. Essa abordagem é conveniente, pois não é necessário instalar softwares adicionais ou configurar ambientes complexos para monitorar os processos.

Para executar o script, basta salvar o código em um arquivo com a extensão .py e executar o comando python nome_do_arquivo.py no terminal Linux.
