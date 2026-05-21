"""Post-process MATLAB-generated SVGs for web use.
Removes black background fill, title/desc tags, and cruft attributes."""
import os, glob

svg_dir = os.path.join(os.path.dirname(__file__), 'gen_svg_out')

for fpath in sorted(glob.glob(os.path.join(svg_dir, '*.svg'))):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove black background: <g fill="#000000"...>...</g> containing M0,0 path
    # Find the start marker
    start_marker = '<g fill="#000000"'
    end_marker = '</g>'

    while start_marker in content:
        idx = content.index(start_marker)
        # Find the matching closing </g> — count nesting depth
        search_from = idx + 1
        depth = 1
        close_idx = -1
        while depth > 0:
            next_open = content.find('<g', search_from)
            next_close = content.find(end_marker, search_from)
            if next_close == -1:
                break
            if next_open != -1 and next_open < next_close:
                depth += 1
                search_from = next_open + 1
            else:
                depth -= 1
                if depth == 0:
                    close_idx = next_close
                search_from = next_close + 1
        if close_idx != -1:
            # Remove from idx to close_idx + len(end_marker)
            content = content[:idx] + content[close_idx + len(end_marker):]
        else:
            break

    # Remove <title>...</title> and <desc>...</desc>
    for tag in ('title', 'desc'):
        while f'<{tag}>' in content:
            s = content.index(f'<{tag}>')
            e = content.index(f'</{tag}>', s) + len(f'</{tag}>')
            content = content[:s] + content[e:]

    # Remove vector-effect attribute
    content = content.replace('vector-effect="none" ', '')

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Cleaned: {os.path.basename(fpath)}')
    else:
        print(f'Skipped: {os.path.basename(fpath)} (no changes)')

print('Done.')
