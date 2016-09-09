from ..models import Category


def add_categories_to_context(context):
    super_category = Category.objects.get(parent_category_id__isnull=True)
    categories = Category.objects.filter(parent_category_id=super_category.id).order_by('position')
    categories_ids_and_names = [{'id': category.id, 'name': category.name} for category in categories]
    context['categories'] = categories_ids_and_names
