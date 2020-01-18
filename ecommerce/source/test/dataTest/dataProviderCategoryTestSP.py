from source.data.dataProviderCategorySP import DataProviderCategorySP
from source.domain.category import Category

dataProviderCategorySP=DataProviderCategorySP()
category=Category()
category.setName("behrang")
category.setDescription("school")
dataProviderCategorySP.getList()