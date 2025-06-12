from models import db, User, Post
from app import app

with app.app_context():

    print('seeding users...')

    cristina = User(first_name='Cristina', last_name='kamuthu', middle_name='pirece', username='cris')
    nevil = User(first_name='Nevil', last_name='oporo', middle_name='Lance', username='brandy')
    alice = User(first_name='Alice', last_name='Chelsea', middle_name='Megan', username='rihanna')

    db.session.add_all([cristina, nevil, alice])
    db.session.commit()

    print('seeding user process completed.')

    print('seeding posts...')

    p1 = Post(post_title='Adventure', post_content='I love adventure', user=alice)
    p2 = Post(post_title='Travelling', post_content='The Dubai trip was interesting', user=alice)
    p3 = Post(post_title='Banking', post_content='This sector is corrupt', user=nevil)
    p4 = Post(post_title='Education', post_content='Education is power', user=cristina)
    p5 = Post(post_title='Economy', post_content='Our economy is doing bad', user=nevil)

    db.session.add_all([p1, p2, p3, p4, p5])
    db.session.commit()

    print('seeding posts process completed.')
