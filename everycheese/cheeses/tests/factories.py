from django.template.defaultfilters import slugify
from everycheese.users.tests.factories import UserFactory

import factory
import factory.fuzzy

from ..models import Cheese

def cheese():
    return CheeseFactory()

class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(
        lambda obj: slugify(obj.name))
    country_of_origin = factory.Faker('country_code')
    creator = factory.SubFactory(UserFactory)
    description = factory.Faker(
        'paragraph', nb_sentences=3,
        variable_nb_sentences=True
    )
    firmness = factory.fuzzy.FuzzyChoice(
        [x[0] for x in Cheese.Firmness.choices]
    )
    class Meta:
        model = Cheese
