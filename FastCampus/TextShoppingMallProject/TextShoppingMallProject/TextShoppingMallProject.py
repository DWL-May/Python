
import sqlite3

## 데이터베이스를 연결하는 코드
conn = sqlite3.connect('C:\python\database.db', isolation_level=None)
c = conn.cursor()

## 상품과 주문 테이블을 생성하는 코드
c.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name text)")
c.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, product INTEGER, number INTEGER)")

## 상품 데이터를 추가하는 코드
productList = ((0, 'iPhone9'),
               (1, 'iPhone10'),
               (2, 'MacBook Pro'),
               (3, 'MacBook Air'),
               (4, 'iPad'))


#c.executemany("INSERT INTO products (id, name) VALUES (?,?)", productList) 

## 상품 목록을 표시하는 코드
for row in c.execute("SELECT * FROM products") :
    print(row)

print('')
print("구매하실 상품의 번호를 입력해주세요: ")
id = input()

## 상품 번호와 주문 수량을 입력받는 코드
print('')
print("구매할 수량을 입력해주세요: ")
number = input()

## 주문 데이터를 db에 추가하는 코드
c.execute("INSERT INTO orders (product, number) VALUES (?,?)", (id, number))

## 현재까지 주문 내역을 출력하는 코드
print('')
print("현재까지 구매한 내역 보기")
print('')
orders =  c.execute("SELECT * FROM orders").fetchall()
for row in orders :
    product = c.execute("SELECT name FROM products WHERE id = ?", (row[1],)).fetchone()
    print('상품 : %s 갯수 : %d' % (product[0], row[2]))
