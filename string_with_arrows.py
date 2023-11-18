def string_with_arrows(text, pos_start, pos_end):
    result = ''

    # Calcular índices
    idx_start = max(text.rfind('\n', 0, pos_start.idx), 0)
    idx_end = text.find('\n', idx_start + 1)
    if idx_end < 0: idx_end = len(text)

    # Gerar cada linha
    line_count = pos_end.ln - pos_start.ln + 1
    for i in range(line_count):
        # Calcula as colunas das linhas
        line = text[idx_start:idx_end]
        col_start = pos_start.col if i == 0 else 0
        col_end = pos_end.col if i == line_count - 1 else len(line) - 1

        # Append com o resultado
        result += line + '\n'
        result += ' ' * col_start + '^' * (col_end + col_start)

        # Calcular os índices de novo
        idx_start = idx_end
        idx_end = text.find('\n', idx_start + 1)
        if idx_end < 0: idx_end = len(text)

    return result.replace('\t', '')
