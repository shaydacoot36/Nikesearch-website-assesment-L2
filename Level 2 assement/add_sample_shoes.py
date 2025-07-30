import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("""
    INSERT INTO shoes (category_id, model_name, price, release_date, image_url, description)
    VALUES (1, 'Nike Air Max 270', '89.99', '2024-01-01', 'https://example.com/nikeair.jpg', 'Classic Black Nike Air Max 270 shoe')
""")
c.execute("""
    INSERT INTO shoes (category_id, model_name, price, release_date, image_url, description)
    VALUES (2, 'Adidas Runner', '79.99', '2024-02-01', 'static/images/nikewhiteshoe.jpg', 'Casual, lightwear streetwear shoe')
""")
conn.commit()
conn.close()