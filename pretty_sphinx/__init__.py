import pandocfilters


def propagate_lang(lang):
    def run_on_node(key, value, fmt, meta):
        if key != 'CodeBlock':
            return None
        [[_, classes, _], content] = value
        classes += [lang]
        return pandocfilters.CodeBlock(*value)
    return run_on_node


def find_div_highlight(value):
    """Look for <div class=highlight-<LANG>> blocks and return LANG """
    [[_, classes, _], _] = value
    for x in classes:
        xs = x.split("-")
        if len(xs) == 2 and xs[0] == "highlight":
            return xs[1]


def filter_env(key, value, fmt, meta):
    if key != "Div":
        return

    lang = find_div_highlight(value)
    if lang is None:
        return

    [_, content] = value
    return pandocfilters.walk(content, propagate_lang(lang), fmt, meta)


def main():
    pandocfilters.toJSONFilters([filter_env])


if __name__ == '__main__':
    main()
