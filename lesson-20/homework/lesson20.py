#Homework
import pandas as pd
import sqlite3

conn = sqlite3.connect("chinook.db")

invoices_df = pd.read_sql_query("SELECT CustomerId, Total FROM Invoice", conn)
customers_df = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM Customer", conn)

total_spent = invoices_df.groupby('CustomerId')['Total'].sum().reset_index()

customer_spending = pd.merge(total_spent, customers_df, on='CustomerId')

top_5_customers = customer_spending.sort_values(by='Total', ascending=False).head(5)

top_5_customers = top_5_customers[['CustomerId', 'FirstName', 'LastName', 'Total']]

print("Top 5 Customers by Total Purchase Amount:")
print(top_5_customers)

import pandas as pd
import sqlite3

conn = sqlite3.connect("chinook.db")

invoice_lines = pd.read_sql_query("SELECT InvoiceLineId, InvoiceId, TrackId FROM InvoiceLine", conn)
invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM Invoice", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track", conn)
customers = pd.read_sql_query("SELECT CustomerId FROM Customer", conn)

invoice_line_merged = invoice_lines.merge(invoices, on='InvoiceId') \
                                   .merge(tracks, on='TrackId')

album_tracks = tracks.groupby('AlbumId')['TrackId'].apply(set).reset_index()
album_tracks.columns = ['AlbumId', 'AllTracks']

customer_album_tracks = invoice_line_merged.groupby(['CustomerId', 'AlbumId'])['TrackId'].apply(set).reset_index()
customer_album_tracks.columns = ['CustomerId', 'AlbumId', 'PurchasedTracks']

merged = customer_album_tracks.merge(album_tracks, on='AlbumId')

merged['FullAlbum'] = merged.apply(lambda row: row['PurchasedTracks'] == row['AllTracks'], axis=1)

customers_with_full_album = merged[merged['FullAlbum']]['CustomerId'].unique()

all_customers = customers['CustomerId'].unique()

customers_with_individual_only = list(set(all_customers) - set(customers_with_full_album))

total_customers = len(all_customers)
pct_full_album = len(customers_with_full_album) / total_customers * 100
pct_individual_tracks = len(customers_with_individual_only) / total_customers * 100

print("Customer Album Purchase Preferences:")
print(f"Customers who purchased at least one full album: {pct_full_album:.2f}%")
print(f"Customers who only purchased individual tracks: {pct_individual_tracks:.2f}%")
