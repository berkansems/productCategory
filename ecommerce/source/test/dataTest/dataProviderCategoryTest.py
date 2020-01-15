from source.data.dataProviderCategory import DataProviderCategory
from source.domain.category import Category

dataProviderCategory = DataProviderCategory()

category = Category()
category.setId(5)
category.setName("car")
category.setDescription("sedan")

#dataProviderCategory.insert(category)
#dataProviderCategory.update(category)
dataProviderCategory.delete(9)
print("***********")
#dataProviderCategory.getList()
#dataProviderCategory.update(category)
