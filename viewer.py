from datetime import date


def html_table_row(r):
    row_head = "<tr>"
    for c in r:
        row_head += f"<td>{c}</td>"
    row_head += "</tr>"
    row_head += "\n"
    return row_head


def html_table(tb):
    table_head = "<tr>"
    cols = tb.columns.values.tolist()[0:]
    for c in cols:
        table_head += f"<th>{c}</th>"
    table_head += "</tr>"
    table_head += "\n"

    result = f"<table border=\"1\">"
    result += "\n"
    result = result + table_head

    for ind in tb.index:
        r = []
        for c in cols:
            r.append(tb[c][ind])
        result += html_table_row(r) + "\n"

    result += "</table>"
    result += "\n"

    return result


def css_table():
    css_style = """<style>
    table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        background: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 15px;
        color: #37474f;
    }
    
    th {
        background: #f8fafb;
        color: #546e7a;
        font-weight: 500;
        font-size: 14px;
        padding: 18px 20px;
        border-bottom: 1px solid #e3f2fd;
        border-right: 1px solid #f0f4f8;
        position: relative;
    }
    
    th:last-child {
        border-right: none;
    }
    
    th::after {
        content: '';
        position: absolute;
        bottom: -1px;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, #90caf9 50%, transparent 100%);
        opacity: 0.5;
    }
    
    td {
        padding: 15px 20px;
        border-bottom: 1px solid #f5f5f5;
        border-right: 1px solid #fafafa;
        max-width: 300px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    
    td:last-child {
        border-right: none;
    }
    
    td:hover {
        white-space: normal;
        word-wrap: break-word;
    }
    
    tr:nth-child(even) td {
        background-color: #fafbfc;
    }
    
    tr:nth-child(odd) td {
        background-color: #ffffff;
    }
    
    tbody tr:hover td {
        background: #f0f7ff;
        transform: translateX(2px);
        transition: all 0.2s ease;
    }
    
    tbody tr:last-child td {
        border-bottom: none;
    }
    </style>"""
    return css_style


def html(tb):
    table = html_table(tb)
    result = f"<!DOCTYPE html><html><head><title>news-{date.today()}</title>{css_table()}</head><body>{table}</body></html>"
    return result
