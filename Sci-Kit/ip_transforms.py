'''
In machine learning (especially in graph neural networks), we need to convert the IP addresses into integers starting from 0. 
So we need a transformation that converts ips into integers and vice versa. Please note that an ip address should be mapped to the same integer, 
whether it is a source ip (src_ip) or a destination ip (dst_ip). 

To implement this transformation, we use Transformations from sklearn.preprocessing. Please complete the code in the 4 methods - __init__, fit, transform
and inverse_trasnform
The test cases in the end will verify if the transformation is giving the expected output. 
'''

import pandas as pd
from sklearn.base import TransformerMixin


# define a dataframe with source and destination ips
df = pd.DataFrame({
    'src_ip': ['1.1.1.1','2.2.2.2','3.3.3.3','1.1.1.1'],
    'dst_ip': ['5.5.5.5', '1.1.1.1','6.6.6.6','8.8.8.8']
})


# output expected after the forward transformation
df_transformed_expected = pd.DataFrame({
    'src_ip': [0, 1, 2, 0],
    'dst_ip': [3, 0, 4, 5]
})


class IpTransform(TransformerMixin):
  def __init__(self):
    #Call TransformerMixin init
    super().__init__()
    self.stack = [] #define a list to store all ip addresses for indexing
    self.src = [] #source ip list
    self.dest = []  #destinataion ip list
    
  def fit(self, df):
    df2 = df[:] #create a duplicate
    self.src = df2['src_ip'].tolist() #initialize source ip list
    self.dest = df2['dst_ip'].tolist() #initialize destination ip list

    #create unique list of ip addresses for both source and destination
    for ip in self.src:
      if ip not in self.stack:
        self.stack.append(ip)
    for ip in self.dest:
      if ip not in self.stack:
        self.stack.append(ip)
    return self

  
  def transform(self, df):
    df2 = df[:] #create a duplicate
    for i in range(len(self.src)):
      #create fitting values from the model
      self.src[i] = self.stack.index(self.src[i])
      self.dest[i] = self.stack.index(self.dest[i])

    #Transform the text data
    df2.src_ip = self.src
    df2.dst_ip = self.dest
    return df2

  def inverse_transform(self, df):
    df2 = df[:]
    inv_src = [self.stack[self.src[i]] for i in range(len(self.src))]
    inv_dest = [self.stack[self.dest[i]] for i in range(len(self.dest))]

    #inverse the test data
    df2.src_ip = inv_src
    df2.dst_ip = inv_dest
    return df2


# Define the transformation
ip_transform = IpTransform()

# do the forward transform
df_transformed_output = ip_transform.fit_transform(df)

# do the reverse transform
df_inverse_transformed = ip_transform.inverse_transform(df_transformed_output)

# Run these test cases to verify that the outputs of forward and reverse transform 
from pandas.testing import assert_frame_equal

assert_frame_equal(df_transformed_output, df_transformed_expected)
assert_frame_equal(df_inverse_transformed, df)
