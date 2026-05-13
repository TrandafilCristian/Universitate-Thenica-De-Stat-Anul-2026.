import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


np.random.seed(42)
n_comenzi = 150


produse = {
    'Laptop ASUS': 15000,
    'Mouse Logitech': 450,
    'Monitor Samsung': 3500,
    'Tastatură RGB': 1200,
    'Căști JBL': 950,
    'Smartphone Xiaomi': 5500
}

nume_produse = list(produse.keys())

data = {
    'order_id': range(1000, 1000 + n_comenzi),
    'product_name': np.random.choice(nume_produse, n_comenzi),
    'category': np.random.choice(['IT & Mobile', 'Accesorii', 'Multimedia'], n_comenzi),
    'quantity': np.random.randint(1, 4, n_comenzi),
    'order_date': [datetime(2026, 1, 1) + timedelta(days=np.random.randint(0, 30)) for _ in range(n_comenzi)]
}

df = pd.DataFrame(data)


df['price'] = df['product_name'].map(produse)
df['revenue'] = df['price'] * df['quantity']
df['order_date'] = pd.to_datetime(df['order_date'])


total_revenue = df['revenue'].sum()
avg_order = df.groupby('order_id')['revenue'].sum().mean()
top_prod = df.groupby('product_name')['revenue'].sum().nlargest(3)


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
df.groupby('category')['revenue'].sum().plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Distribuție Vânzări pe Categorie')
plt.ylabel('')


plt.subplot(1, 2, 2)
daily_sales = df.groupby(df['order_date'].dt.date)['revenue'].sum()
daily_sales.plot(kind='line', marker='s', color='darkgreen', linewidth=2)
plt.title('Vânzări Zilnice (MDL)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


print("\n" + "="*45)
print("   DASHBOARD VÂNZĂRI MOLDOVA 2026")
print("="*45)
print(f" Venit Total:          {total_revenue:,.2f} MDL")
print(f" Valoare Medie Comandă: {avg_order:,.2f} MDL")
print("-" * 45)
xxprint(" TOP 3 PRODUSE DUPĂ VENIT:")
print(top_prod)
print("="*45)