def build_query(url, theme: str, range=None, page=1, per_page=100):

    theme = theme.replace(' ', '%20')
    search = f'&queryText=("All%20Metadata":{theme})'
    url += search

    if range:
        start_year = range[0]
        end_year = range[1]
        url += f'&ranges={start_year}_{end_year}_Year'

    if page:
        url += f'&rowsPerPage={per_page}&pageNumber={page}'
        
    print(url)
    return url