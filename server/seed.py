#!/usr/bin/env python3

from app import app
from models import db, Bakery, BakedGood

with app.app_context():
    # Clear existing data
    BakedGood.query.delete()
    Bakery.query.delete()
    
    # Create bakeries
    bakery1 = Bakery(name='Delightful Donuts')
    bakery2 = Bakery(name='Incredible Crullers')

    db.session.add_all([bakery1, bakery2])
    db.session.commit()

    # Create baked goods
    baked_goods = [
        BakedGood(name='Chocolate Dipped Donut', price=2.75, bakery=bakery1),
        BakedGood(name='Apple-Spice Filled Donut', price=3.50, bakery=bakery1),
        BakedGood(name='Glazed Honey Cruller', price=3.25, bakery=bakery2),
        BakedGood(name='Chocolate Cruller', price=3.40, bakery=bakery2),
    ]

    db.session.add_all(baked_goods)
    db.session.commit()

    print("✅ Database seeded!")
