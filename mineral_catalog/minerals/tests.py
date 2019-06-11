from django.urls import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTest(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name= "Abelsonite",
            image_filename= "Abelsonite.jpg",
            image_caption= "Abelsonite from the Green River Formation, Uintah County, Utah, US",
            category= "Organic",
            formula= "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            strunz_classification= "10.CA.20",
            crystal_system= "Triclinic",
            unit_cell= "a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, \u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = 79.99\u00b0Z = 1",
            color= "Pink-purple, dark greyish purple, pale purplish red, reddish brown",
            crystal_symmetry= "Space group: P1 or P1Point group: 1 or 1",
            cleavage= "Probable on {111}",
            mohs_scale_hardness= "2\u20133",
            luster= "Adamantine, sub-metallic",
            streak= "Pink",
            diaphaneity= "Semitransparent",
            optical_properties= "Biaxial",
            group= "Organic Minerals"
        )
        rock_test = Mineral.objects.get(name = 'Abelsonite')
        self.assertEqual(rock_test.name, 'Abelsonite')


class MineralViewTest(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            name= "Zoisite",
            image_filename= "Zoisite.jpg",
            image_caption= "Yellow zoisite crystal (1.7 x 1 x 0.8 cm)",
            category= "Sorosilicate - epidote group",
            group= "Silicates"
        )
        self.mineral2 = Mineral.objects.create(
            name= "Zorite",
            image_filename= "Zorite.jpg",
            image_caption= "Zorite",
            category= "Inosilicate",
            group= "Silicates"
        )
        self.mineral3 = Mineral.objects.create(
            name= "Zunyite",
            image_filename= "Zunyite.jpg",
            image_caption= "Sharp, pyramids of brown-red zunyite from Silver City, Tintic District, East Tintic Mountains, Juab County, Utah, USA (size: 5.5 x 5 x 3.5 cm)",
            category= "Sorosilicates",
            formula= "Al<sub>13</sub>Si<sub>5</sub>O<sub>20</sub>(OH,F)<sub>18</sub>Cl",
            group= "Silicates"
        )

    def TestModelViews(self):
        response = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.course.name)
