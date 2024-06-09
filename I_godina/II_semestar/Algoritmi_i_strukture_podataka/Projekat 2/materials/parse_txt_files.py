import os


def read_results_from_files(root):
    filenames = os.listdir(root)
    result = {}
    for filename in filenames:
        content = read_results_from_file(os.path.join(root, filename)).decode('utf-8')
        try:
            page_number = int(content[:content.index('\n')].split()[-1])
        except:
            try:
                page_number = int(content[:content.index('\n')].split()[0])
            except:
                page_number = None
        index = filename.split(".")[0]
        result[index] = {'index': index,
                         'page_number': page_number,
                         'content': content}
    return result


def read_results_from_file(path):
    with open(path, 'rb') as file:
        return file.read()


def print_dict(dict):
    for key in dict:
        page = dict[key]
        print('Index: %s' % key)
        print('Page number: %s' % page['page_number'])
        print('Content:\n\n' + page['content'])
        print('\n\n\n')


if __name__ == '__main__':
    in_path = 'Data Structures and Algorithms in Python.pdf'
    out_path = 'Data Structures and Algorithms in Python'
    results = read_results_from_files(out_path)
    print_dict(results)
