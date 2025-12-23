def split_text(text: str, chunk_size: int = 500, overlap: int = 50):
    """Split into chunks with overlap"""
    sentences = text.replace("\n", " ").split('. ')
    chunks = []
    current_chunk = []
    current_size = 0

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        if not sentence.endswith('.'):
            sentence += '.'

        sentence_size = len(sentence.split())

        # agr chunk size exceed hua 
        if current_size + sentence_size > chunk_size and current_chunk:
            # current chunk ko save kr rhe h 
            chunk_text = " ".join(current_chunk)
            chunks.append(chunk_text)

            # handling overlap
            overlap_words = chunk_text.split()[-overlap:]
            # new chunk me overlap words add kr rhe h
            current_chunk = [" ".join(overlap_words), sentence]
            # cuurent size update kr rhe h
            current_size = len(overlap_words) + sentence_size

        else:
            # bache hue sentence ko current chunk me add kr rhe h
            current_chunk.append(sentence)
            current_size += sentence_size

    if current_chunk:
        # last chunk ko bhi add kr rhe h 
        chunks.append(' '.join(current_chunk))

    return chunks     
