def lines(text):
    return text.splitlines()


def unlines(elements):
    return '\n'.join(elements)


def words(text):
    return text.split()


def unwords(elements):
    return ' '.join(elements)


def tabs_to_spaces(str, one_tab_n_spaces):
    space_tab = ' ' * one_tab_n_spaces
    return space_tab.join(str.split('\t'))
