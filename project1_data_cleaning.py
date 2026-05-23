#import libraries
import pandas as pd

#load dataset
df=pd.read_csv("dataset data analytics.csv")

#check first 5 records
print(df.head())

#check rows and columns count
print(df.shape)


#check data summary
print(df.info())
print(df.dtypes)

# print(df.columns)
#standarize column name
df.rename(columns={
      'OrderID':'order_id',
      'Date':'date',
      'CustomerID':'customer_id',
      'Product':'product',
      'Quantity':'quantity',
      'UnitPrice':'unit_price',
      'ShippingAddress':'shipping_address',
      'PaymentMethod':'payment_method',
      'OrderStatus':'order_status',
      'TrackingNumber':'tracking_number',
      'ItemsInCart':'items_in_cart',
      'CouponCode':'coupon_code',
      'ReferralSource':'referral_source',
      'TotalPrice':'total_price'
}, inplace=True)
print(df.columns)


#check missing value count
print(df.isnull().sum().to_frame().T)
# print(df.isnull().mean()*100)

#handle missing values
df['coupon_code']=df['coupon_code'].fillna('No Coupon')

print(df.isnull().sum().to_frame().T)

#change datatype for date
df['date']=pd.to_datetime(df['date'])

print(df.duplicated().sum())


#check for incorrect data
print(df['product'].unique())
print(df['payment_method'].unique())

print(df.info())

df.to_csv("Cleaned_Dataset.csv", index=False)