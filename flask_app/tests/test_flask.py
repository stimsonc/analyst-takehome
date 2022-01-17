from flask_app.app import Pet, app, db

def test_new_pet():
    """
    Test creation of new Pet object and attributes.
    """
    pet = Pet('Fluffy', 'cat')
    assert pet.name == 'Fluffy'
    assert pet.breed == 'cat'

def test_landing_page():
    """
    Test correct rendering of landing page.
    """
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Add pet" in response.data
        assert b"Welcome to Carl's Pet Emporium" in response.data

def test_database():
    """
    Test database existence and insertion.
    """
    pet = Pet('Fluffinator', 'cat')
    db.session.add(pet)
    db.session.commit()
    query = Pet.query.filter_by(name='Fluffinator').first()
    db.session.delete(pet)
    db.session.commit()
    assert query.name == 'Fluffinator'
    assert query.breed == 'cat'
    