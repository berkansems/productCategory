from source.data.dataProviderCategory import DataProviderCategory
from source.domain.category import Category

dataProviderCategory = DataProviderCategory()

category = Category()
category.setName("car")
category.setDescription("sedan")

dataProviderCategory.insert(category)
#dataProviderCategory.update(category)

print("***********")
#dataProviderCategory.getList()
#dataProviderCategory.update(category)
