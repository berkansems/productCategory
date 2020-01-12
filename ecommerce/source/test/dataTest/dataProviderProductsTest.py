from source.data.dataProviderProduct import DataProviderProduct
from source.domain.product import Product

dataProviderProduct = DataProviderProduct()

product=Product()

product.setId(2)
product.setName("ali")
product.setDescription("ec")
product.setPrice(3000)
product.setCategoryId("2")

#dataProviderProduct.insert(product)
dataProviderProduct.getList()
