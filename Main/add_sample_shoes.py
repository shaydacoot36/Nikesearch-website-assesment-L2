import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("""
    INSERT INTO shoes (category_id, model_name, price, release_date, image_url, description)
    VALUES (1, 'Nike Air', '89.99', '2024-01-01', 'https://example.com/nikeair.jpg', 'Classic Nike Air shoe')
""")
c.execute("""
    INSERT INTO shoes (category_id, model_name, price, release_date, image_url, description)
    VALUES (2, 'Adidas Runner', '79.99', '2024-02-01', 'https://example.com/adidasrunner.jpg', 'Lightweight Adidas running shoe')
""")
conn.commit()
conn.close()