import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    path_files = [index["nome_do_arquivo"] for index in instance._data]

    if path_file not in path_files:
        file_lines = txt_importer(path_file)

        dict_files = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_lines),
            "linhas_do_arquivo": file_lines
        }

        instance.enqueue(dict_files)
        print(dict_files)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
