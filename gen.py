import csv


def main():
    rows_out = ""
    with open('tcs_out.csv') as f:
        rdr = csv.reader(f)
        for row in rdr:
            players = row[0].split('|')
            tourn = row[1]
            url = row[2]

            rows_out += "<tr>"
            rows_out += "<td>"
            rows_out += f"<a href=\"{url}\">"
            if len(players) == 2:
                rows_out += f"{players[0]}<br>vs<br>{players[1]}"
            else:
                rows_out += f"{players[0]}<br>{players[1]}<br>"
                rows_out += "vs<br>"
                rows_out += f"{players[2]}<br>{players[3]}<br>"
            rows_out += "</a></td>"

            rows_out += f"<td>{tourn}</td>"
            rows_out += "</tr>"

    with open('output.html', 'w') as fout:
        with open('template.html', 'r') as ftmpl:
            fout.write(ftmpl.read().replace('[[[TABLE_ROWS]]]', rows_out))


if __name__ == "__main__":
    main()
