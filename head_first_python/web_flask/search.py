def search(phrase: str, letters: str = 'aeiou') -> set:
    """在phrase中搜索letters,取两个参数的合集intersection"""
    return set(letters).intersection(set(phrase))

