from source.data.dataProviderCategory import DataProviderCategory
from source.domain.category import Category

dataProviderCategory = DataProviderCategory()

category = Category()
category.setId("3")
category.setName("bilgisayar")
category.setDescription("computer Description")

#dataProviderCategory.insert(category)
dataProviderCategory.getList()
