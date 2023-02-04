from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    result = []

    for index in range(len(instance)):
        element = instance.search(index)

        list_file = [
            {"linha": index + 1}
            for index, line in enumerate(element["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]

        if list_file:
            result.append({
                "palavra": word,
                "arquivo": element["nome_do_arquivo"],
                "ocorrencias": list_file
            })

    return result


def search_by_word(word, instance: Queue):
    """Aqui irá sua implementação"""
