import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_category_model(self, category_factory):
        obj = category_factory(name="test_category")
        assert obj.__str__() == "test_category"


class TestBrandModel:
    def test_category_model(self, brand_factory):
        obj = brand_factory(name="test_brand")
        assert obj.__str__() == "test_brand"


class TestCarModel:
    def test_category_model(self, car_factory):
        obj = car_factory(model="BMW")
        assert obj.__str__() == "BMW"
