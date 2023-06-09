# to populate otc database: from lib/db run => python3 seed_medications.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Otc

engine = create_engine('sqlite:///pharmacy.db')
Session = sessionmaker(bind=engine)

otc_list = [
    Otc(name="Tylenol", category="Pain Reliever", price=5.00),
    Otc(name="Advil", category="Pain Reliever", price=5.00),
    Otc(name="Aleve", category="Pain Reliever", price=5.00),
    Otc(name="Motrin", category="Pain Reliever", price=5.00),
    Otc(name="Excedrin", category="Pain Reliever", price=5.00),
    Otc(name="Benadryl", category="Allergy", price=5.00),
    Otc(name="Claritin", category="Allergy", price=5.00),
    Otc(name="Zyrtec", category="Allergy", price=5.00),
    Otc(name="Allegra", category="Allergy", price=5.00),
    Otc(name="Flonase", category="Allergy", price=5.00),
    Otc(name="Benadryl", category="Allergy", price=5.00),
    Otc(name="Mucinex", category="Cold & Flu", price=5.00),
    Otc(name="Nyquil", category="Cold & Flu", price=5.00),
    Otc(name="Dayquil", category="Cold & Flu", price=5.00),
    Otc(name="Robitussin", category="Cold & Flu", price=5.00),
    Otc(name="Theraflu", category="Cold & Flu", price=5.00),
    Otc(name="Imodium", category="Digestive Health", price=5.00),
    Otc(name="Pepto-Bismol", category="Digestive Health", price=5.00),
    Otc(name="Tums", category="Digestive Health", price=5.00),
    Otc(name="Gas-X", category="Digestive Health", price=5.00),
    Otc(name="Beano", category="Digestive Health", price=5.00),
    Otc(name="Prilosec", category="Digestive Health", price=5.00),
    Otc(name="Zantac", category="Digestive Health", price=5.00),
    Otc(name="Dramamine", category="Motion Sickness", price=5.00),
    Otc(name="Bonine", category="Motion Sickness", price=5.00),
    Otc(name="Sea-Band", category="Motion Sickness", price=5.00),
    Otc(name="Dramamine for Kids", category="Motion Sickness", price=5.00),
    Otc(name="Bonine for Kids", category="Motion Sickness", price=5.00),
    Otc(name="Sea-Band for Kids", category="Motion Sickness", price=5.00),
    Otc(name="Dramamine Less Drowsy", category="Motion Sickness", price=5.00),
    Otc(name="Bonine Less Drowsy", category="Motion Sickness", price=5.00),
    Otc(name="Sea-Band Less Drowsy", category="Motion Sickness", price=5.00),
    Otc(name="Dramamine Chewable", category="Motion Sickness", price=5.00),
    Otc(name="Bonine Chewable", category="Motion Sickness", price=5.00),
    Otc(name="Sea-Band Chewable", category="Motion Sickness", price=5.00),
    Otc(name="Dramamine Non-Drowsy Naturals", category="Motion Sickness", price=5.00),
    Otc(name="Bonine Non-Drowsy Naturals", category="Motion Sickness", price=5.00),
    Otc(name="Sea-Band Non-Drowsy Naturals", category="Motion Sickness", price=5.00),
    Otc(name="Dramamine Ginger", category="Motion Sickness", price=5.00),
    Otc(name="Bonine Ginger", category="Motion Sickness", price=5.00),
    Otc(name="Sea-Band Ginger", category="Motion Sickness", price=5.00),
    Otc(name="Band-Aid", category="First Aid", price=5.00),
    Otc(name="Neosporin", category="First Aid", price=5.00),
    Otc(name="Benadryl", category="First Aid", price=5.00),
    Otc(name="Cortizone-10", category="First Aid", price=5.00),
    Otc(name="Aveeno", category="First Aid", price=5.00),
    Otc(name="Tylenol", category="First Aid", price=5.00),
    Otc(name="Vitamin C", category="Vitamins", price=5.00),
    Otc(name="Vitamin D", category="Vitamins", price=5.00),
    Otc(name="Vitamin B12", category="Vitamins", price=5.00),
    Otc(name="Vitamin B6", category="Vitamins", price=5.00),
    Otc(name="Vitamin B1", category="Vitamins", price=5.00),
    Otc(name="Vitamin B2", category="Vitamins", price=5.00),
    Otc(name="Vitamin B3", category="Vitamins", price=5.00),
    Otc(name="Vitamin B5", category="Vitamins", price=5.00),
    Otc(name="Vitamin B9", category="Vitamins", price=5.00),
    Otc(name="Vitamin B7", category="Vitamins", price=5.00),
    Otc(name="Vitamin E", category="Vitamins", price=5.00),
    Otc(name="Vitamin K", category="Vitamins", price=5.00),
    Otc(name="Calcium", category="Vitamins", price=5.00),
    Otc(name="Iron", category="Vitamins", price=5.00),
    Otc(name="Magnesium", category="Vitamins", price=5.00),
    Otc(name="Zinc", category="Vitamins", price=5.00),
    Otc(name="Potassium", category="Vitamins", price=5.00),
    Otc(name="Fish Oil", category="Vitamins", price=5.00),
    Otc(name="Probiotics", category="Vitamins", price=5.00),
    Otc(name="Melatonin", category="Vitamins", price=5.00),
    Otc(name="CoQ10", category="Vitamins", price=5.00),
    Otc(name="Glucosamine", category="Vitamins", price=5.00),
    Otc(name="Chondroitin", category="Vitamins", price=5.00),
    Otc(name="Turmeric", category="Vitamins", price=5.00),
    Otc(name="Garlic", category="Vitamins", price=5.00),
    Otc(name="Green Tea", category="Vitamins", price=5.00),
    Otc(name="Ginger", category="Vitamins", price=5.00),
    Otc(name="St. Johns Wort", category="Vitamins", price=5.00),
    Otc(name="Valerian", category="Vitamins", price=5.00),
    Otc(name="Creatine", category="Vitamins", price=5.00),
    Otc(name="Glutamine", category="Vitamins", price=5.00),
    Otc(name="BCAAs", category="Vitamins", price=5.00),
    Otc(name="Arginine", category="Vitamins", price=5.00),
    Otc(name="BCAAs", category="Vitamins", price=5.00),
    Otc(name="Arginine", category="Vitamins", price=5.00),
    Otc(name="Jergens", category="Skin Care", price=5.00),
    Otc(name="Neutrogena", category="Skin Care", price=5.00),
    Otc(name="Olay", category="Skin Care", price=5.00),
    Otc(name="Vaseline", category="Skin Care", price=5.00),
    Otc(name="Gold Bond", category="Skin Care", price=5.00),
    Otc(name="Ace Bandage", category="First Aid", price=5.00),
    Otc(name="Vicks", category="Skin Care", price=5.00),
    Otc(name="Biotene",category="Oral Care",price=6.50),
    Otc(name="Cortizone-10",category="First Aid",price=7.00),
    Otc(name="Ace bandage",category="First Aid",price=7.50),
    Otc(name="Vickery",category="First Aid",price=8.00),
    Otc(name="Benadryl",category="First Aid",price=8.50),
    Otc(name="Corte azion",category="First Aid",price=9.00),
    Otc(name="Crest",category="Oral Care",price=9.50),
    Otc(name="Listeria",category="Oral Care",price=10.00),
    Otc(name="Sensodyne",category="Oral Care",price=10.50),
    Otc(name="Oral-B",category="Oral Care",price=11.00),
    Otc(name="Benadryl",category="First Aid",price=11.50),
    Otc(name="Tylenol",category="Pain Reliever",Price=4.50)
]


with Session() as session:
    session.bulk_save_objects(otc_list)
    session.commit()