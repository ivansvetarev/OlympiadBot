import sqlite3

connect = sqlite3.connect("db/olympiads_info.db")
cursor = connect.cursor()

ols = []

for ol in cursor.execute("""SELECT * FROM olympiads"""):
    ol_s = ""
    cur = ol[1]
    for i in range(len(cur) - 1):
        ol_s += cur[i]
        if cur[i + 1] in ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']:
            ol_s += ", "
    if cur != "": 
        ol_s += cur[len(cur) - 1]
    ols.append([ol[0], ol_s])

    
for ol in ols:
    cursor.execute("""UPDATE olympiads SET subjects = ? WHERE olympiad_id = ?""", (ol[1], ol[0]))
connect.commit()

