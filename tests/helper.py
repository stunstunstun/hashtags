
ICON = {
    'CHECK': '✔️',
    'SMILE': '😋',
    'FIRE': '🔥',
    'BOOK': '📖',
    'COOL': '👍',
    'STAR': '⭐️'
}


def attach_rank(index):
    print('attach_rank[{}]'.format(index))
    if index == 0:
        return ICON['CHECK']
    else:
        return str(index + 1) + '.'
