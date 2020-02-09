from source.data.dataProviderProduct import DataProviderProducts
from source.domain.product import Product

dataProviderProduct = DataProviderProducts()

product=Product()
product.setId(14)
product.setName("MSI")
product.setDescription("Core i7 8.generation")
product.setPrice(6050)
product.setCategory_Id("4")

#dataProviderProduct.insert(product)
#dataProviderProduct.Update(product)
#dataProviderProduct.getList()
#dataProviderProduct.getByCotegoryId(1)