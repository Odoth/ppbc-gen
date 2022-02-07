import re

def main():
    base_url = None
    tourn = None
    with open('tcs.txt', 'r') as f:
        lines = f.read().splitlines()

    with open('tcs_out.csv', 'w') as f:
        for line in lines:
            if line.strip() == '':
                base_url = None
                tourn = None
            elif base_url is None:
                base_url = line.strip()
            elif tourn is None:
                tourn = line.strip()
            else:
                m = re.match(r'(\S+) (.*) vs (.*)', line)
                tc = m.group(1)
                team1 = m.group(2)
                team2 = m.group(3)
                
                # * means no match split. full vid is a single match
                if tc == '*':
                    url = base_url
                else:
                    secs = 0
                    tcp = tc.split(':')
                    if len(tcp) == 3:
                        secs += 3600 * int(tcp[0])
                        secs += 60 * int(tcp[1])
                        secs += int(tcp[2])
                    elif len(tcp) == 2:
                        secs += 60 * int(tcp[0])
                        secs += int(tcp[1])
                    elif len(tcp) == 1:
                        secs += int(tcp[0])
                    else:
                        raise 'Weird number of tcp'
                    url = base_url + f'&t={secs}s'

                players = team1.split('/') + team2.split('/')
                f.write('|'.join(players) + ',')
                f.write(tourn + ',')
                f.write(url + '\n')


if __name__ == "__main__":
    main()