from ..models import Category


def add_categories_to_context(context):
    super_category = Category.objects.get(parent_category_id__isnull=True)
    categories = Category.objects.filter(parent_category_id=super_category.id).order_by('position')
    subcategories = [[{'id': subcategory.id,
                       'name': subcategory.name} for subcategory in category.subcategories.all()] for category in categories]

    context['categories'] = [{'id': category.id,
                              'name': category.name,
                              'subcategories': subcategories[i]} for i, category in enumerate(categories)]
